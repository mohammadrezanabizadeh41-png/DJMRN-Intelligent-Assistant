"""DJMRN P2D. Synthetic-only deterministic free-first admission.

No network, accounts, credentials, timers, providers, Bifrost calls or Windows access.
SQLite reservations count against budget even on upstream failures (conservative).
Never put model-generated or HTTP-untrusted fields directly into Request.
"""
from dataclasses import dataclass
from contextlib import closing
from datetime import date
import sqlite3
from typing import FrozenSet

TIERS = {'lite': 0, 'standard': 1, 'reasoning': 2}


@dataclass(frozen=True)
class Route:
    route_id: str
    provider: str
    model: str
    account_group: str
    tier: str
    capabilities: FrozenSet[str]
    context_limit: int
    daily_limit: int | None
    price_per_token: float | None
    confirmed_free_api: bool
    billing_disabled: bool
    enabled: bool
    protected_daily_reserve: int = 0
    priority: int = 100


@dataclass(frozen=True)
class Request:
    request_id: str
    tier: str
    capabilities: FrozenSet[str]
    context_tokens: int
    free_only: bool = True
    allow_paid_fallback: bool = False
    allow_tier_downgrade: bool = False
    max_attempts: int = 2
    trusted: bool = True
    privacy_class: str = 'normal'


class Denied(ValueError):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


class QuotaLedger:
    """Single SQLite DB shared across clients, BEGIN IMMEDIATE reservations.

    Distinct registered models can share one account quota group. No automatic
    quota reset inference from HTTP 429; caller supplies UTC day explicitly.
    """
    def __init__(self, path: str):
        self.path = path
        with closing(self._connect()) as db:
            db.execute('CREATE TABLE IF NOT EXISTS usage (day TEXT NOT NULL, grp TEXT NOT NULL, used INTEGER NOT NULL, lim INTEGER NOT NULL, PRIMARY KEY(day,grp))')
            db.execute('CREATE TABLE IF NOT EXISTS reservations (request_id TEXT NOT NULL, attempt INTEGER NOT NULL, day TEXT NOT NULL, grp TEXT NOT NULL, route TEXT NOT NULL, PRIMARY KEY(request_id, attempt))')

    def _connect(self):
        db = sqlite3.connect(self.path, timeout=5, isolation_level=None)
        db.execute('PRAGMA busy_timeout=5000')
        return db

    @staticmethod
    def _eligible(req: Request, route: Route) -> bool:
        if not route.enabled or not route.confirmed_free_api or not route.billing_disabled:
            return False
        if route.price_per_token is None or route.price_per_token != 0 or route.daily_limit is None:
            return False
        if route.daily_limit < 1 or route.protected_daily_reserve < 0 or route.protected_daily_reserve >= route.daily_limit:
            return False
        if not route.account_group or not route.route_id or not route.model or not route.provider:
            return False
        if route.tier not in TIERS or req.tier not in TIERS:
            return False
        if TIERS[route.tier] < TIERS[req.tier]:
            return False
        if not route.capabilities.issuperset(req.capabilities):
            return False
        if req.context_tokens < 1 or route.context_limit < req.context_tokens:
            return False
        return True

    def reserve(self, req: Request, routes: tuple[Route, ...], utc_day: str, attempted: tuple[str, ...] = ()):
        if not req.trusted or req.privacy_class != 'normal' or not req.free_only or req.allow_paid_fallback or req.allow_tier_downgrade:
            raise Denied('POLICY_DENIED')
        if req.tier not in TIERS or req.context_tokens < 1 or req.max_attempts not in (1, 2) or not req.request_id:
            raise Denied('INVALID_REQUEST')
        if len(set(attempted)) != len(attempted) or len(attempted) >= req.max_attempts:
            raise Denied('ATTEMPTS_EXHAUSTED')
        try:
            if date.fromisoformat(utc_day).isoformat() != utc_day:
                raise ValueError('noncanonical UTC day')
        except (TypeError, ValueError):
            raise Denied('INVALID_DAY') from None
        route_ids = [r.route_id for r in routes]
        if len(set(route_ids)) != len(route_ids):
            raise Denied('INVALID_REGISTRY')
        # Static registry never silently merges conflicting quota assumptions.
        group_limits = {}
        for r in routes:
            if r.daily_limit is not None:
                if r.account_group in group_limits and group_limits[r.account_group] != (r.daily_limit, r.protected_daily_reserve):
                    raise Denied('CONFLICTING_SHARED_QUOTA')
                group_limits[r.account_group] = (r.daily_limit, r.protected_daily_reserve)
        compatible = sorted((r for r in routes if r.route_id not in attempted and self._eligible(req,r)), key=lambda r:(TIERS[r.tier],r.priority,r.route_id))
        if not compatible:
            raise Denied('NO_COMPATIBLE_FREE_MODEL')
        with closing(self._connect()) as db:
            db.execute('BEGIN IMMEDIATE')
            previous = db.execute('SELECT 1 FROM reservations WHERE request_id=?', (req.request_id,)).fetchall()
            if len(previous) != len(attempted):
                db.execute('ROLLBACK')
                raise Denied('REQUEST_HISTORY_MISMATCH')
            seen = [x[0] for x in db.execute('SELECT route FROM reservations WHERE request_id=? ORDER BY attempt',(req.request_id,)).fetchall()]
            if tuple(seen) != attempted:
                db.execute('ROLLBACK')
                raise Denied('REQUEST_HISTORY_MISMATCH')
            for r in compatible:
                row=db.execute('SELECT used,lim FROM usage WHERE day=? AND grp=?', (utc_day,r.account_group)).fetchone()
                used, limit = row if row else (0,r.daily_limit)
                if limit != r.daily_limit:
                    db.execute('ROLLBACK')
                    raise Denied('CONFLICTING_SHARED_QUOTA')
                reserve = r.protected_daily_reserve if req.tier != 'reasoning' else 0
                if used >= limit-reserve:
                    continue
                db.execute('INSERT INTO usage(day,grp,used,lim) VALUES(?,?,1,?) ON CONFLICT(day,grp) DO UPDATE SET used=used+1',(utc_day,r.account_group,r.daily_limit))
                db.execute('INSERT INTO reservations(request_id,attempt,day,grp,route) VALUES(?,?,?,?,?)',(req.request_id,len(attempted),utc_day,r.account_group,r.route_id))
                db.execute('COMMIT')
                return r.route_id
            db.execute('ROLLBACK')
        raise Denied('FREE_POOL_EXHAUSTED')


def next_step(http_status: int, *, stream_started: bool = False) -> str:
    if stream_started:
        return 'STOP_PARTIAL_STREAM'
    if http_status in (401, 402, 403):
        return 'STOP_AUTH_OR_BILLING'
    if http_status in (429,500,502,503,504):
        return 'TRY_ELIGIBLE_FREE_FALLBACK'
    if 200 <= http_status < 300:
        return 'COMPLETE'
    return 'STOP_UNSUPPORTED_ERROR'
