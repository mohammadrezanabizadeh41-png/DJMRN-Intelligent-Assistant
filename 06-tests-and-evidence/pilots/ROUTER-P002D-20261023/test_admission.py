"""Synthetic-only P2D tests; no network, provider API, credentials, or billing."""
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import os
import tempfile
import unittest
from admission import QuotaLedger, Route, Request, Denied, next_step

A = Route('mock-lite-a','fake-a','fixture-lite','shared-a','lite',frozenset({'chat','persian'}),4096,3,0,True,True,True,protected_daily_reserve=0,priority=1)
B = Route('mock-lite-b','fake-b','fixture-lite','shared-b','lite',frozenset({'chat','persian'}),4096,3,0,True,True,True,priority=2)
H = Route('mock-reason','fake-h','fixture-reason','shared-h','reasoning',frozenset({'chat','persian','coding'}),32768,4,0,True,True,True,protected_daily_reserve=2)
DAY='2026-10-23'

class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.d=tempfile.TemporaryDirectory(); self.ledger=QuotaLedger(os.path.join(self.d.name,'q.db'))
    def tearDown(self):self.d.cleanup()
    def req(self,n='r',**changes):return replace(Request(n,'lite',frozenset({'chat','persian'}),100),**changes)
    def deny(self,code,req,routes,attempted=()):
        with self.assertRaises(Denied) as c:self.ledger.reserve(req,routes,DAY,attempted)
        self.assertEqual(c.exception.code,code)
    def test_01_cheapest_adequate_tier(self):self.assertEqual(self.ledger.reserve(self.req(),(H,B,A),DAY),'mock-lite-a')
    def test_02_unknown_price_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(),(replace(A,price_per_token=None),))
    def test_03_positive_price_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(),(replace(A,price_per_token=.01),))
    def test_04_unverified_free_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(),(replace(A,confirmed_free_api=False),))
    def test_05_billing_enabled_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(),(replace(A,billing_disabled=False),))
    def test_06_unknown_quota_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(),(replace(A,daily_limit=None),))
    def test_07_explicit_paid_fallback_deny(self):self.deny('POLICY_DENIED',self.req(allow_paid_fallback=True),(A,))
    def test_08_untrusted_deny(self):self.deny('POLICY_DENIED',self.req(trusted=False),(A,))
    def test_09_sensitive_deny(self):self.deny('POLICY_DENIED',self.req(privacy_class='sensitive'),(A,))
    def test_10_missing_capability_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(capabilities=frozenset({'vision'})),(A,B,H))
    def test_11_insufficient_context_deny(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(context_tokens=9000),(A,B))
    def test_12_no_downgrade(self):self.deny('NO_COMPATIBLE_FREE_MODEL',self.req(tier='reasoning'),(A,B))
    def test_13_reasoning_reserve_kept(self):
        for i in range(2):self.assertEqual(self.ledger.reserve(self.req(str(i)),(H,),DAY),'mock-reason')
        self.deny('FREE_POOL_EXHAUSTED',self.req('third'),(H,))
        self.assertEqual(self.ledger.reserve(self.req('reason',tier='reasoning',capabilities=frozenset({'coding'})),(H,),DAY),'mock-reason')
    def test_14_shared_quota_across_models(self):
        v=replace(A,route_id='mock-a-2',model='fixture-alt')
        for i in range(3):self.ledger.reserve(self.req(str(i)),(A,v),DAY)
        self.deny('FREE_POOL_EXHAUSTED',self.req('fourth'),(v,),())
    def test_15_conflicting_quota_deny(self):self.deny('CONFLICTING_SHARED_QUOTA',self.req(),(A,replace(A,route_id='b',daily_limit=7)))
    def test_16_idempotent_same_request_deny(self):
        self.ledger.reserve(self.req('x'),(A,),DAY)
        self.deny('REQUEST_HISTORY_MISMATCH',self.req('x'),(A,),())
    def test_17_two_attempts_only(self):
        self.ledger.reserve(self.req('x'),(A,B),DAY)
        self.assertEqual(self.ledger.reserve(self.req('x'),(A,B),DAY,('mock-lite-a',)),'mock-lite-b')
        self.deny('ATTEMPTS_EXHAUSTED',self.req('x'),(A,B),('mock-lite-a','mock-lite-b'))
    def test_18_429_503_fallback_only(self):
        self.assertEqual(next_step(429),'TRY_ELIGIBLE_FREE_FALLBACK');self.assertEqual(next_step(503),'TRY_ELIGIBLE_FREE_FALLBACK')
    def test_19_402_401_stop(self):self.assertEqual(next_step(402),'STOP_AUTH_OR_BILLING');self.assertEqual(next_step(401),'STOP_AUTH_OR_BILLING')
    def test_20_partial_stream_stop(self):self.assertEqual(next_step(503,stream_started=True),'STOP_PARTIAL_STREAM')
    def test_21_atomic_concurrent_quota(self):
        def work(i):
            try:self.ledger.reserve(self.req(str(i)),(A,),DAY);return True
            except Denied as e:
                self.assertEqual(e.code,'FREE_POOL_EXHAUSTED');return False
        with ThreadPoolExecutor(max_workers=12) as pool:items=list(pool.map(work,range(24)))
        self.assertEqual(sum(items),3)
    def test_22_utc_day_is_explicit(self):
        with self.assertRaises(Denied) as e:self.ledger.reserve(self.req(),(A,),'2026-99-99')
        self.assertEqual(e.exception.code,'INVALID_DAY')
    def test_23_distinct_reset_day(self):
        for i in range(3):self.ledger.reserve(self.req(str(i)),(A,),DAY)
        self.assertEqual(self.ledger.reserve(self.req('next'),(A,),'2026-10-24'),'mock-lite-a')
    def test_24_conflicting_reserves_deny(self):
        self.deny('CONFLICTING_SHARED_QUOTA',self.req(),(H,replace(H,route_id='other',protected_daily_reserve=1)))
    def test_25_unsupported_error_no_fallback(self):self.assertEqual(next_step(422),'STOP_UNSUPPORTED_ERROR')

if __name__ == '__main__':unittest.main()
