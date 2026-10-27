"""DJMRN P1: offline, single-user, language-neutral record shape, Python reference.

No listener, OAuth, LLM, Docker, Gmail, web or secrets. NOT a security boundary for
untrusted local users or adversarial filesystem races. Host must supply trusted scope.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sqlite3
import sys
from datetime import datetime, timezone
from uuid import uuid4

VERSION = "djmrn.coord.v1"
CAPABILITY = "documents.search.v0"
MAX_ATTEMPTS = 2
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def wire_json(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


class ContractError(ValueError):
    pass


class Hub:
    """Hub-owned durable task/dispatch/audit ledger; CAP-006 remains a worker.

    root, allowlisted resource IDs and principal are TRUSTED HOST CONFIG, not
    user/agent-submitted claims. This P1 class has no network interface or auth.
    """

    def __init__(self, db_file: str | Path, root: str | Path, allowlist: dict[str, str]):
        self.root = Path(root).resolve(strict=True)
        if not self.root.is_dir():
            raise ContractError("TRUSTED_ROOT_NOT_DIRECTORY")
        if not allowlist or len(allowlist) > 2 or any(
            not isinstance(k, str) or not isinstance(v, str) or not k or not v
            for k, v in allowlist.items()
        ):
            raise ContractError("TRUSTED_ALLOWLIST_INVALID")
        self.allowlist = dict(allowlist)
        self.db_file = Path(db_file)
        self.db_file.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(self.db_file), timeout=5)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA busy_timeout=5000")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY, principal TEXT NOT NULL,
                request_id TEXT NOT NULL, idempotency_key TEXT NOT NULL,
                payload_digest TEXT NOT NULL, intent TEXT NOT NULL,
                query TEXT NOT NULL, resource_ids TEXT NOT NULL,
                capability_id TEXT NOT NULL, status TEXT NOT NULL,
                attempts INTEGER NOT NULL DEFAULT 0,
                result_json TEXT, worker_fingerprint TEXT, error_code TEXT,
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
                UNIQUE(principal, idempotency_key)
            );
            CREATE TABLE IF NOT EXISTS dispatches (
                dispatch_id TEXT PRIMARY KEY, task_id TEXT NOT NULL,
                target_role TEXT NOT NULL, capability_id TEXT NOT NULL,
                attempt INTEGER NOT NULL, status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(task_id) REFERENCES tasks(task_id)
            );
            CREATE TABLE IF NOT EXISTS audit (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT NOT NULL, event_type TEXT NOT NULL,
                actor TEXT NOT NULL, detail TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(task_id) REFERENCES tasks(task_id)
            );
        """)
        self.db.commit()
        cap_path = Path(__file__).resolve().parents[1] / "document_search_v0" / "docsearch_v0.py"
        if not cap_path.is_file():
            raise RuntimeError("CAP006_NOT_FOUND_IN_REPO_LAYOUT")
        spec = importlib.util.spec_from_file_location("djmrn_p1_cap006", cap_path)
        cap = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cap)
        self.cap006 = cap

    def close(self):
        self.db.close()

    def _event(self, task_id, kind, actor, detail):
        self.db.execute(
            "INSERT INTO audit(task_id,event_type,actor,detail,created_at) VALUES(?,?,?,?,?)",
            (task_id, kind, actor, wire_json(detail), timestamp()))

    def _state(self, task_id, expect, state, *, error=None):
        sql = "UPDATE tasks SET status=?,updated_at=?,error_code=? WHERE task_id=? AND status=?"
        cur = self.db.execute(sql, (state, timestamp(), error, task_id, expect))
        if cur.rowcount != 1:
            raise ContractError("INVALID_STATE_TRANSITION")
        self._event(task_id, "STATE_CHANGED", "hub", {"from": expect, "to": state})

    @staticmethod
    def _validated_submission(req):
        if not isinstance(req, dict) or set(req) != {
            "kind", "contract_version", "request_id", "idempotency_key",
            "locale", "capability_id", "intent", "input_refs"
        }:
            raise ContractError("INVALID_SUBMISSION_FIELDS")
        if req["kind"] != "TASK_SUBMISSION" or req["contract_version"] != VERSION or req["locale"] != "fa-IR":
            raise ContractError("INVALID_SUBMISSION_VERSION_OR_LOCALE")
        for field, maximum in [("request_id", 128), ("idempotency_key", 128),
                               ("intent", 2048), ("capability_id", 128)]:
            value = req[field]
            if not isinstance(value, str) or not value.strip() or len(value) > maximum:
                raise ContractError("INVALID_" + field.upper())
        refs = req["input_refs"]
        if not isinstance(refs, list) or not 1 <= len(refs) <= 2 or any(
            not isinstance(r, str) or not 1 <= len(r) <= 128 for r in refs
        ) or len(set(refs)) != len(refs):
            raise ContractError("INVALID_RESOURCE_IDS")
        if any(0xD800 <= ord(c) <= 0xDFFF for c in wire_json(req)):
            raise ContractError("INVALID_UNICODE")

    def submit(self, req: dict, *, query: str, principal: str):
        """Trusted host establishes principal. Duplicate key returns same task.

        A different request with same (principal, idempotency key) is conflict.
        """
        self._validated_submission(req)
        if not isinstance(query, str) or not query.strip() or len(query) > 512:
            raise ContractError("INVALID_CAPABILITY_QUERY")
        if not isinstance(principal, str) or not principal or len(principal) > 128:
            raise ContractError("INVALID_TRUSTED_PRINCIPAL")
        digest = hashlib.sha256(wire_json({"submission": req, "capability_input": {"query": query}}).encode("utf-8")).hexdigest()
        with self.db:
            previous = self.db.execute(
                "SELECT task_id,payload_digest FROM tasks WHERE principal=? AND idempotency_key=?",
                (principal, req["idempotency_key"])).fetchone()
            if previous:
                if previous["payload_digest"] != digest:
                    raise ContractError("IDEMPOTENCY_KEY_CONFLICT")
                return self.get(previous["task_id"])
            tid = str(uuid4())
            now = timestamp()
            self.db.execute("""INSERT INTO tasks
                (task_id,principal,request_id,idempotency_key,payload_digest,intent,
                 query,resource_ids,capability_id,status,created_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                (tid,principal,req["request_id"],req["idempotency_key"],digest,
                 req["intent"],query,wire_json(req["input_refs"]),
                 req["capability_id"],"RECEIVED",now,now))
            self._event(tid,"SUBMITTED",principal,{"capability_id":req["capability_id"]})
            if req["capability_id"] != CAPABILITY:
                self._state(tid,"RECEIVED","DENIED",error="CAPABILITY_NOT_ACTIVE")
            elif not all(r in self.allowlist for r in req["input_refs"]):
                self._state(tid,"RECEIVED","DENIED",error="RESOURCE_SCOPE_DENIED")
            else:
                self._state(tid,"RECEIVED","VALIDATED")
                self._state(tid,"VALIDATED","QUEUED")
        return self.get(tid)

    def get(self, task_id):
        row = self.db.execute("SELECT * FROM tasks WHERE task_id=?", (task_id,)).fetchone()
        if row is None:
            raise ContractError("TASK_NOT_FOUND")
        return {
            "kind":"TASK_RECORD", "contract_version":VERSION,
            "task_id":row["task_id"],"request_id":row["request_id"],
            "owner_principal":row["principal"],"capability_id":row["capability_id"],
            "status":row["status"], "attempts":row["attempts"],
            "error_code":row["error_code"],
            "legacy_cap006_fingerprint_task_id":row["worker_fingerprint"],
            "result":json.loads(row["result_json"]) if row["result_json"] else None,
            "created_at":row["created_at"],"updated_at":row["updated_at"]
        }

    def events(self, task_id):
        return [dict(r) for r in self.db.execute(
            "SELECT event_id,task_id,event_type,actor,detail,created_at FROM audit "
            "WHERE task_id=? ORDER BY event_id",(task_id,))]

    def run(self, task_id):
        """Synchronous read-only worker, no automatic external retries.

        Do not call this concurrently for the same Hub connection. The
        conditional UPDATE below prevents double-dispatch across connections.
        """
        row = self.db.execute("SELECT * FROM tasks WHERE task_id=?",(task_id,)).fetchone()
        if row is None:
            raise ContractError("TASK_NOT_FOUND")
        if row["status"] != "QUEUED":
            raise ContractError("TASK_NOT_QUEUED")
        refs = json.loads(row["resource_ids"])
        if row["capability_id"] != CAPABILITY or not all(r in self.allowlist for r in refs):
            raise ContractError("TRUSTED_SCOPE_CHANGED")
        selected = [self.allowlist[r] for r in refs]
        with self.db:
            self._state(task_id,"QUEUED","DISPATCHED")
            self.db.execute("UPDATE tasks SET attempts=attempts+1 WHERE task_id=?",(task_id,))
            self.db.execute("""INSERT INTO dispatches
                (dispatch_id,task_id,target_role,capability_id,attempt,status,created_at)
                VALUES(?,?,?,?,?,?,?)""",
                (str(uuid4()),task_id,"cap006_adapter",CAPABILITY,
                 int(row["attempts"])+1,"ISSUED",timestamp()))
            self._event(task_id,"DISPATCHED","hub",{"to":"cap006_adapter"})
        with self.db:
            self._state(task_id,"DISPATCHED","RUNNING")
        try:
            # The sole capability operation; CAP-006 enforces relative path,
            # size, syntax and symlink restrictions again at worker boundary.
            output = self.cap006.search(self.root,selected,row["query"],limit=8)
            if not isinstance(output, dict) or output.get("status") != "succeeded" or \
                    output.get("contract_version") != "djmrn.document-search.v0":
                raise ContractError("INVALID_WORKER_RECEIPT")
            searched = output.get("searched")
            matches = output.get("matches")
            if not isinstance(searched, list) or len(searched) != len(selected) or \
                    not isinstance(matches, list) or len(matches) > 8 or \
                    output.get("match_count_returned") != len(matches):
                raise ContractError("INVALID_WORKER_RECEIPT")
            digest_by_file = {}
            for f in searched:
                if not isinstance(f, dict) or not isinstance(f.get("file"), str) or \
                        f["file"] in digest_by_file or not isinstance(f.get("sha256"), str) or \
                        not SHA256.fullmatch(f["sha256"]) or \
                        not isinstance(f.get("bytes"), int) or f["bytes"] > 1024 * 1024:
                    raise ContractError("INVALID_WORKER_RECEIPT")
                digest_by_file[f["file"]] = f["sha256"]
            if set(digest_by_file) != set(selected) or any(
                not isinstance(m, dict) or m.get("file") not in digest_by_file or
                m.get("source_sha256") != digest_by_file.get(m.get("file")) or
                not isinstance(m.get("line"), int) or m["line"] < 1
                for m in matches
            ):
                raise ContractError("INVALID_WORKER_RECEIPT")
        except (Exception) as exc:
            # Pilot has no autonomous repair; special errors are classified
            # for later specialist-owned workflow retry. Never retry denied scope.
            name = "WORKER_INPUT_REJECTED" if isinstance(exc,self.cap006.InputRejected) else "WORKER_FAILED"
            with self.db:
                self._state(task_id,"RUNNING","FAILED",error=name)
                self._event(task_id,"WORKER_ERROR","cap006_adapter",{"type":type(exc).__name__})
            return self.get(task_id)
        with self.db:
            # Result and SUCCEEDED are atomic, unlike a streaming UI message.
            self.db.execute("UPDATE tasks SET result_json=?,worker_fingerprint=? WHERE task_id=?",
                            (wire_json(output),output["task_id"],task_id))
            self._state(task_id,"RUNNING","SUCCEEDED")
            self._event(task_id,"RESULT_PERSISTED","hub",{"count":output["match_count_returned"],
                                                              "evidence_digests":[f["sha256"] for f in output["searched"]]})
        return self.get(task_id)

    def reconcile_readonly(self):
        """After an interrupted process, queue bounded read-only work only.

        Requires explicitly calling run() afterward. No emails/side-effects.
        """
        recovered=[]
        with self.db:
            rows=self.db.execute("SELECT task_id,status,attempts,capability_id FROM tasks WHERE status IN ('DISPATCHED','RUNNING')").fetchall()
            for r in rows:
                if r["capability_id"] != CAPABILITY:
                    continue
                if r["attempts"] >= MAX_ATTEMPTS:
                    self._state(r["task_id"],r["status"],"FAILED",error="RETRY_LIMIT")
                else:
                    self._state(r["task_id"],r["status"],"RETRY_WAIT")
                    self._state(r["task_id"],"RETRY_WAIT","QUEUED")
                recovered.append(r["task_id"])
        return recovered


def example_request():
    return {"kind":"TASK_SUBMISSION","contract_version":VERSION,
            "request_id":"sample-request-001","idempotency_key":"sample-once-001",
            "locale":"fa-IR","capability_id":CAPABILITY,
            "intent":"در دو سند مجاز درباره کتاب جست‌وجو کن",
            "input_refs":["fixture.alpha","fixture.beta"]}


def demo(db_path: str):
    fixture_dir = Path(__file__).resolve().parents[1] / "document_search_v0" / "fixtures"
    h=Hub(db_path,fixture_dir,{"fixture.alpha":"sample_alpha.txt","fixture.beta":"sample_beta.md"})
    try:
        req=example_request()
        existing=h.db.execute("SELECT task_id FROM tasks WHERE principal=? AND idempotency_key=?",
                              ("local-demo",req["idempotency_key"])).fetchone()
        r=h.submit(req,query="كتاب",principal="local-demo")
        if r["status"] == "QUEUED": r=h.run(r["task_id"])
        print(json.dumps(r,ensure_ascii=False,indent=2))
        print("READBACK_EVIDENCE=",len(h.events(r["task_id"])))
        return 0 if r["status"]=="SUCCEEDED" else 1
    finally:
        h.close()


if __name__ == "__main__":
    if len(sys.argv)==3 and sys.argv[1]=="demo":
        sys.exit(demo(sys.argv[2]))
    print("Use: python hub_p1.py demo <local-pilot.sqlite3>",file=sys.stderr)
    sys.exit(2)