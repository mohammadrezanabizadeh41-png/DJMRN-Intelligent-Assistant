"""DJMRN P2 offline mock policy prototype. No network, credentials, OS tools, or Bifrost binary.

This is deliberately NOT a Bifrost integration/adapter. Test the required invariants
without granting a model any capability beyond fake response selection.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from contextlib import contextmanager
from pathlib import Path
import sqlite3
import threading
from typing import Callable, Iterable

TIERS = frozenset({'lite', 'standard', 'reasoning'})
ISSUES = frozenset({'AUTH_REQUIRED','BILLING_BLOCKED','RATE_LIMITED','UPSTREAM_FAILURE','STREAM_INTERRUPTED'})

@dataclass(frozen=True)
class Request:
    client_id: str
    task_class: str
    capabilities: frozenset[str] = frozenset({'chat', 'persian'})
    claimed_client_id: str | None = None  # untrusted; intentionally ignored
    claimed_tier: str | None = None  # untrusted; intentionally ignored
    allow_downgrade: bool = False  # overridden by policy
    streaming: bool = False
    external_tool_approved: bool = False

@dataclass(frozen=True)
class Provider:
    name: str
    model: str
    tier: str
    account: str
    capabilities: frozenset[str]
    kind: str = 'renewable_free'
    price: float | None = 0.0
    reset_at: int = 0
    available: bool = True
    privileged_tools: bool = False

@dataclass(frozen=True)
class Reply:
    ok: bool
    status: str
    served_by: str | None = None
    fallback: bool = False
    public_detail: str = ''
    _events: tuple[tuple[str,str], ...] = ()

class SharedQuota:
    """Transactional admission, keyed by shared provider ACCOUNT, not model/client.

    A quota 'used' is settled on admitted successful fake result. A held reservation
    is counted immediately, so concurrent clients cannot both take the last slot.
    The reset method is an explicit authority signal for tests only, NEVER a timer guess.
    """
    def __init__(self, path: Path):
        self.path = str(path)
        self._lock = threading.RLock()
        with self._db() as db:
            db.execute('CREATE TABLE IF NOT EXISTS quota (account TEXT PRIMARY KEY, cap INTEGER NOT NULL, used INTEGER NOT NULL DEFAULT 0, held INTEGER NOT NULL DEFAULT 0, protected INTEGER NOT NULL DEFAULT 0, reset_at INTEGER NOT NULL DEFAULT 0)')
            db.execute('CREATE TABLE IF NOT EXISTS holds (id INTEGER PRIMARY KEY AUTOINCREMENT, account TEXT NOT NULL, state TEXT NOT NULL)')
    @contextmanager
    def _db(self):
        db = sqlite3.connect(self.path, timeout=15, isolation_level=None)
        try:
            yield db
        finally:
            db.close()
    def set_account(self, account: str, cap: int, reserve: int = 0, reset_at: int = 0) -> None:
        assert cap >= 0 and 0 <= reserve <= cap
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('INSERT OR REPLACE INTO quota(account,cap,used,held,protected,reset_at) VALUES (?,?,?,?,?,?)', (account, cap, 0, 0, reserve, reset_at))
            db.execute('DELETE FROM holds WHERE account=?',(account,))
            db.commit()
    def snapshot(self, account: str):
        with self._db() as db:
            return db.execute('SELECT cap,used,held,protected,reset_at FROM quota WHERE account=?',(account,)).fetchone()
    def reserve(self, account: str, task_tier: str) -> int | None:
        with self._db() as db:
            try:
                db.execute('BEGIN IMMEDIATE')
                row=db.execute('SELECT cap,used,held,protected FROM quota WHERE account=?',(account,)).fetchone()
                if not row:
                    db.rollback(); return None
                cap, used, held, protect = row
                # Don't touch protected advanced pool for any lower-task tier.
                accessible = cap - (protect if task_tier != 'reasoning' else 0)
                if used + held >= accessible:
                    db.rollback();return None
                db.execute('UPDATE quota SET held=held+1 WHERE account=?',(account,))
                hid=db.execute("INSERT INTO holds(account,state) VALUES (?, 'held')",(account,)).lastrowid
                db.commit();return hid
            except BaseException:
                db.rollback();raise
    def settle(self, hid: int, consumed: bool) -> None:
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            row=db.execute('SELECT account,state FROM holds WHERE id=?',(hid,)).fetchone()
            if not row or row[1]!='held':
                db.rollback();raise RuntimeError('unknown or settled hold')
            a=row[0]
            db.execute('UPDATE quota SET held=held-1,used=used+? WHERE account=?',(1 if consumed else 0,a))
            db.execute("UPDATE holds SET state=? WHERE id=?",('consumed' if consumed else 'released',hid))
            db.commit()
    def authoritative_reset(self, account:str, reset_at:int):
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            old=db.execute('SELECT reset_at, held FROM quota WHERE account=?',(account,)).fetchone()
            if not old or reset_at<=old[0] or old[1]!=0:
                db.rollback();return False
            db.execute('UPDATE quota SET used=0,reset_at=? WHERE account=?',(reset_at,account))
            db.commit();return True

# Fake provider behavior is purely in-memory, never HTTP or real inference.
@dataclass
class FakeBackend:
    responses: dict[str, list[str]] = field(default_factory=dict)
    calls: list[tuple[str,str]] = field(default_factory=list)
    def call(self, provider:Provider, req:Request) -> str:
        self.calls.append((provider.name, req.client_id))
        values=self.responses.get(provider.name,['ok'])
        return values.pop(0) if values else 'ok'

class RouterMock:
    def __init__(self, pools: Iterable[Provider], ledger:SharedQuota, fake:FakeBackend):
        self.pools=tuple(pools)
        self.ledger=ledger
        self.fake=fake
        self.allowed_clients={'persian-chat':frozenset(TIERS), 'coding-agent':frozenset({'standard','reasoning'}), 'indexer':frozenset({'lite'}), 'second-app':frozenset(TIERS)}
        self._health={}
        self.clock=100
        self.max_attempts=3
        self.exec_tool_count=0
        self.logs=[]
    def route(self, req:Request, classify:Callable[[Request],str|None]|None=None)->Reply:
        # Trusted identity comes from auth layer, NOT from arbitrary request header.
        if req.client_id not in self.allowed_clients:
            return Reply(False,'AUTH_REQUIRED')
        if req.task_class=='auto':
            tier=classify(req) if classify else None
            if tier is None: return Reply(False,'CLASSIFIER_UNAVAILABLE')
        else: tier=req.task_class
        if tier not in TIERS or tier not in self.allowed_clients[req.client_id]:
            return Reply(False,'POLICY_DENIED')
        need=req.capabilities
        candidates=[p for p in self.pools if p.tier==tier and p.available and p.kind=='renewable_free' and p.price==0.0 and need.issubset(p.capabilities) and self._health.get(p.name,0)<=self.clock]
        if not candidates:
            return Reply(False,'NO_COMPATIBLE_FREE_MODEL')
        events=[]
        denied=False
        for i,p in enumerate(candidates[:self.max_attempts]):
            hold=self.ledger.reserve(p.account,tier)
            if hold is None:
                denied=True
                continue
            result='no_result'
            try:
                result=self.fake.call(p,req)
            finally:
                # Fake request failure does not imply free quota successfully used.
                self.ledger.settle(hold,consumed=(result=='ok' or result=='partial_503'))
            events.append((p.name,result))
            if result=='ok':
                self.logs.append({'route':p.name,'status':'success','fallback':i>0})
                return Reply(True,'OK',served_by=p.name,fallback=i>0,_events=tuple(events))
            if result=='429_minute':
                self._health[p.name]=self.clock+60
            elif result=='429_day':
                self._health[p.name]=self.clock+86400
            elif result in ('401','403'):
                # Credential failures don't imply a route is healthy: hold this route.
                self._health[p.name]=self.clock+86400
            elif result=='402':
                self._health[p.name]=self.clock+86400
            elif result=='partial_503':
                return Reply(False,'STREAM_INTERRUPTED',served_by=p.name,_events=tuple(events))
            elif result=='400':
                return Reply(False,'NO_COMPATIBLE_FREE_MODEL',served_by=p.name,_events=tuple(events))
            elif result!='503':
                return Reply(False,'UPSTREAM_FAILURE',served_by=p.name,_events=tuple(events))
        return Reply(False,'FREE_POOL_EXHAUSTED' if denied or events else 'NO_COMPATIBLE_FREE_MODEL',_events=tuple(events))
