"""P1 Hub tests use real sibling CAP-006 whenever checked out in the main repo.
These tests perform no network or model calls and use only generated synthetic files.
"""
import hashlib
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4

from hub_p1 import Hub, ContractError, CAPABILITY, example_request


class HubPilotTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "alpha.md").write_text("کتاب اول درباره تحقیق است.\nمتن مثال ساختگی است.\n", encoding="utf-8")
        (self.root / "beta.md").write_text("كتاب دوم درباره مدیریت دانش است.\n", encoding="utf-8")
        self.path = self.root / "hub.sqlite3"
        self.allowlist = {"fixture.alpha": "alpha.md", "fixture.beta": "beta.md"}
        self.h = Hub(self.path, self.root, self.allowlist)

    def tearDown(self):
        self.h.close()
        self.tmp.cleanup()

    def request(self):
        r = example_request()
        r["request_id"] = "req-" + uuid4().hex
        r["idempotency_key"] = "key-" + uuid4().hex
        return r

    def test_persian_success_and_source_hash(self):
        task = self.h.submit(self.request(), query="كتاب", principal="trusted-local")
        self.assertEqual(task["status"], "QUEUED")
        finished = self.h.run(task["task_id"])
        self.assertEqual(finished["status"], "SUCCEEDED")
        self.assertNotEqual(task["task_id"], finished["legacy_cap006_fingerprint_task_id"])
        found = self.h.get_result(task["task_id"])
        self.assertEqual(len(found["searched"]), 2)
        self.assertGreaterEqual(found["match_count_returned"], 2)
        for item in found["searched"]:
            actual = hashlib.sha256((self.root / item["file"]).read_bytes()).hexdigest()
            self.assertEqual(item["sha256"], actual)
        self.assertTrue(any(x["event_type"] == "RESULT_PERSISTED" for x in self.h.events(task["task_id"])))

    def test_duplicate_submission_same_task(self):
        req = self.request()
        first = self.h.submit(req, query="كتاب", principal="local")
        second = self.h.submit(req, query="كتاب", principal="local")
        self.assertEqual(first["task_id"], second["task_id"])
        self.assertEqual(self.h.db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0], 1)

    def test_idempotency_conflict(self):
        req = self.request()
        self.h.submit(req, query="كتاب", principal="local")
        with self.assertRaisesRegex(ContractError, "IDEMPOTENCY_KEY_CONFLICT"):
            self.h.submit(req, query="دیگر", principal="local")

    def test_unknown_resource_is_denied(self):
        req = self.request()
        req["input_refs"] = ["fixture.alpha", "third-file"]
        t = self.h.submit(req, query="كتاب", principal="local")
        self.assertEqual(t["status"], "DENIED")
        self.assertEqual(t["error_code"], "RESOURCE_SCOPE_DENIED")

    def test_direct_web_forbidden(self):
        req = self.request()
        req["capability_id"] = "research.web"
        t = self.h.submit(req, query="خبر", principal="local")
        self.assertEqual(t["status"], "DENIED")
        self.assertEqual(t["error_code"], "CAPABILITY_NOT_ACTIVE")

    def test_wrong_version_and_extra_fields_rejected(self):
        req = self.request()
        req["contract_version"] = "djmrn.coord.v2"
        with self.assertRaises(ContractError):
            self.h.submit(req, query="كتاب", principal="local")
        req["contract_version"] = "djmrn.coord.v1"
        req["claimed_principal"] = "admin"
        with self.assertRaises(ContractError):
            self.h.submit(req, query="كتاب", principal="local")

    def test_nonqueued_may_not_run_twice(self):
        t = self.h.submit(self.request(), query="كتاب", principal="local")
        self.h.run(t["task_id"])
        with self.assertRaisesRegex(ContractError, "TASK_NOT_QUEUED"):
            self.h.run(t["task_id"])

    def test_restart_persistence(self):
        t = self.h.submit(self.request(), query="كتاب", principal="local")
        done = self.h.run(t["task_id"])
        self.h.close()
        self.h = Hub(self.path, self.root, self.allowlist)
        again = self.h.get(t["task_id"])
        self.assertEqual(again["status"], "SUCCEEDED")
        self.assertEqual(done["result_refs"], again["result_refs"])
        self.assertIsNotNone(self.h.get_result(t["task_id"]))
        self.assertGreaterEqual(len(self.h.events(t["task_id"])), 6)

    def test_bounded_recovery_for_readonly_only(self):
        t = self.h.submit(self.request(), query="كتاب", principal="local")
        with self.h.db:
            self.h._state(t["task_id"], "QUEUED", "DISPATCHED")
            self.h._state(t["task_id"], "DISPATCHED", "RUNNING")
            self.h.db.execute("UPDATE tasks SET attempts=1 WHERE task_id=?", (t["task_id"],))
        self.assertEqual(self.h.reconcile_readonly(), [t["task_id"]])
        self.assertEqual(self.h.get(t["task_id"])["status"], "QUEUED")
        self.assertEqual(self.h.run(t["task_id"])["status"], "SUCCEEDED")

    def test_recovery_limit_fails_closed(self):
        t = self.h.submit(self.request(), query="كتاب", principal="local")
        with self.h.db:
            self.h._state(t["task_id"], "QUEUED", "DISPATCHED")
            self.h._state(t["task_id"], "DISPATCHED", "RUNNING")
            self.h.db.execute("UPDATE tasks SET attempts=2 WHERE task_id=?", (t["task_id"],))
        self.h.reconcile_readonly()
        done = self.h.get(t["task_id"])
        self.assertEqual(done["status"], "FAILED")
        self.assertEqual(done["error_code"], "RETRY_LIMIT")

    def test_deleted_file_is_failure_not_success(self):
        t = self.h.submit(self.request(), query="كتاب", principal="local")
        (self.root / "beta.md").unlink()
        done = self.h.run(t["task_id"])
        self.assertEqual(done["status"], "FAILED")
        self.assertIsNone(self.h.get_result(t["task_id"]))


if __name__ == "__main__":
    unittest.main()