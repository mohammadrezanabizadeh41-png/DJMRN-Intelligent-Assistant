"""Run: python -m unittest -v test_p2.py in this directory.
Each test uses a fresh SQLite fixture and FAKE model backends (no network).
"""
import concurrent.futures
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from mock_policy import SharedQuota, Provider, Request, FakeBackend, RouterMock

class RouterP2Mock(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'quota.db'
        self.db=SharedQuota(self.path)
        self.fake=FakeBackend()
    def model(self,name,tier,account,caps=('chat','persian'),**opts):
        return Provider(name=name,model='fake-'+name,tier=tier,account=account,capabilities=frozenset(caps),**opts)
    def router(self,*models):return RouterMock(models,self.db,self.fake)
    def test_R01_lite_does_not_consume_reasoning(self):
        self.db.set_account('L',2);self.db.set_account('R',2,reserve=1)
        r=self.router(self.model('light','lite','L'),self.model('strong','reasoning','R'))
        result=r.route(Request('persian-chat','lite'))
        self.assertEqual((result.ok,result.served_by,self.db.snapshot('R')[1]),(True,'light',0))
    def test_R02_minute_429_falls_back_standard(self):
        self.db.set_account('A',2);self.db.set_account('B',2)
        self.fake.responses={'first':['429_minute'],'second':['ok']}
        r=self.router(self.model('first','standard','A'),self.model('second','standard','B'))
        a=r.route(Request('persian-chat','standard'))
        self.assertTrue(a.ok);self.assertEqual(a.served_by,'second');self.assertEqual(r._health['first'],160)
    def test_R03_reasoning_day_429_same_tier_only(self):
        for a in ['A','B','L']:self.db.set_account(a,2)
        self.fake.responses={'high1':['429_day'],'high2':['ok']}
        r=self.router(self.model('high1','reasoning','A'),self.model('high2','reasoning','B'),self.model('lite','lite','L'))
        out=r.route(Request('persian-chat','reasoning'))
        self.assertEqual(out.served_by,'high2');self.assertNotIn(('lite','persian-chat'),self.fake.calls)
    def test_R04_high_tier_exhaustion_no_paid_trial_or_downgrade(self):
        self.db.set_account('A',0);self.db.set_account('P',10);self.db.set_account('L',10)
        r=self.router(self.model('R','reasoning','A'),self.model('pay','reasoning','P',price=0.01),self.model('trial','reasoning','P',kind='trial'),self.model('lite','lite','L'))
        out=r.route(Request('persian-chat','reasoning',allow_downgrade=True))
        self.assertEqual(out.status,'FREE_POOL_EXHAUSTED');self.assertEqual(self.fake.calls,[])
    def test_R05_auth_billing_promo_fail_closed(self):
        for status in ('401','403','402'):
            with self.subTest(status=status):
                self.db.set_account('A',2);self.db.set_account('P',2)
                self.fake.calls.clear();self.fake.responses={'first':[status]}
                r=self.router(self.model('first','lite','A'),self.model('promo','lite','P',kind='expired_promo'))
                out=r.route(Request('persian-chat','lite'))
                self.assertFalse(out.ok);self.assertEqual(out.status,'FREE_POOL_EXHAUSTED');self.assertEqual([x[0] for x in self.fake.calls],['first'])
    def test_R06_two_clients_atomic_one_shared_slot(self):
        self.db.set_account('A',1)
        r=self.router(self.model('same','lite','A'))
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
            two=list(ex.map(r.route,[Request('persian-chat','lite'),Request('second-app','lite')]))
        self.assertEqual(sum(x.ok for x in two),1);self.assertEqual(self.db.snapshot('A')[1:3],(1,0))
        self.assertEqual(SharedQuota(self.path).snapshot('A')[1],1)
    def test_R07_tools_require_capability(self):
        self.db.set_account('A',1)
        r=self.router(self.model('text-only','standard','A'))
        out=r.route(Request('coding-agent','standard',capabilities=frozenset({'chat','persian','tools'})))
        self.assertEqual(out.status,'NO_COMPATIBLE_FREE_MODEL');self.assertEqual(r.exec_tool_count,0)
    def test_R08_partial_stream_fail_must_not_claim_ok(self):
        self.db.set_account('A',2);self.db.set_account('B',2)
        self.fake.responses={'first':['partial_503'],'second':['ok']}
        r=self.router(self.model('first','standard','A'),self.model('second','standard','B'))
        out=r.route(Request('persian-chat','standard',streaming=True))
        self.assertEqual(out.status,'STREAM_INTERRUPTED');self.assertFalse(out.ok);self.assertEqual([x[0] for x in self.fake.calls],['first'])
    def test_R09_untrusted_identity_or_tier_override_ignored(self):
        self.db.set_account('A',1);self.db.set_account('R',1)
        r=self.router(self.model('one','lite','A'),self.model('power','reasoning','R'))
        out=r.route(Request('indexer','lite',claimed_client_id='coding-agent',claimed_tier='reasoning'))
        self.assertTrue(out.ok);self.assertEqual(out.served_by,'one');self.assertEqual(self.db.snapshot('R')[1],0)
        self.assertEqual(r.route(Request('unknown','reasoning')).status,'AUTH_REQUIRED')
    def test_R10_classifier_down_fails_closed(self):
        self.db.set_account('A',1);r=self.router(self.model('one','standard','A'))
        out=r.route(Request('persian-chat','auto'),classify=lambda _:None)
        self.assertEqual(out.status,'CLASSIFIER_UNAVAILABLE');self.assertEqual(self.fake.calls,[])
    def test_R11_reset_requires_explicit_authority_and_no_pending(self):
        self.db.set_account('A',1,reset_at=100)
        first=self.db.reserve('A','lite');self.assertIsNotNone(first)
        self.assertFalse(self.db.authoritative_reset('A',200))
        self.db.settle(first,True)
        self.assertFalse(self.db.authoritative_reset('A',99))
        self.assertEqual(SharedQuota(self.path).snapshot('A')[1],1)
        self.assertTrue(self.db.authoritative_reset('A',200))
        self.assertEqual(self.db.snapshot('A')[1],0)
    def test_R12_model_variants_share_same_quota_group(self):
        self.db.set_account('SHARED',1)
        r=self.router(self.model('alpha','standard','SHARED'),self.model('beta','standard','SHARED'))
        x=r.route(Request('persian-chat','standard'));y=r.route(Request('second-app','standard'))
        self.assertTrue(x.ok);self.assertFalse(y.ok);self.assertEqual(self.db.snapshot('SHARED')[1],1)
    def test_R13_fallback_logs_route_only_not_payload(self):
        self.db.set_account('A',1);self.db.set_account('B',1)
        self.fake.responses={'first':['503'],'second':['ok']}
        r=self.router(self.model('first','lite','A'),self.model('second','lite','B'))
        out=r.route(Request('persian-chat','lite'))
        self.assertTrue(out.fallback);self.assertEqual(out.served_by,'second');self.assertEqual(r.logs[0],{'route':'second','status':'success','fallback':True})
    def test_R14_cloud_unavailable_cannot_open_file_guard(self):
        self.db.set_account('A',0)
        r=self.router(self.model('first','lite','A'))
        out=r.route(Request('persian-chat','lite',external_tool_approved=False))
        self.assertEqual(out.status,'FREE_POOL_EXHAUSTED');self.assertEqual(r.exec_tool_count,0)
    def test_extra_reasoning_reserve_blocks_lower_task(self):
        self.db.set_account('A',2,reserve=1)
        r=self.router(self.model('one','lite','A'))
        self.assertTrue(r.route(Request('persian-chat','lite')).ok)
        self.assertFalse(r.route(Request('persian-chat','lite')).ok)
        self.assertEqual(self.db.snapshot('A')[1],1)
    def test_extra_unknown_price_or_unmeasured_model_denied(self):
        self.db.set_account('A',10)
        r=self.router(self.model('unknown','lite','A',price=None))
        self.assertEqual(r.route(Request('persian-chat','lite')).status,'NO_COMPATIBLE_FREE_MODEL')

if __name__ == '__main__':unittest.main()
