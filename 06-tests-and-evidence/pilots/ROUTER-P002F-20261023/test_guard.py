"""P2F offline regression: fail closed on restart and adversarial client metadata."""
from contextlib import closing
from pathlib import Path
from unittest.mock import patch
import os,sqlite3,tempfile,unittest
import server
from admission import Denied
class TestP2F(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.root=Path(self.t.name)
        self.env={'DJMRN_P2F_SYNTHETIC_ONLY':'yes','DJMRN_GATEWAY_TEST_URL':'http://djmrn-bifrost-p2c:8080/v1/chat/completions','DJMRN_P2F_LEDGER_DIR':'/ledger'}
    def tearDown(self):self.t.cleanup()
    def check(self,bootstrap):
        with patch.object(server,'LEDGER_DIR',self.root),patch.object(server,'TOKEN','x'*36),patch.dict(os.environ,{**self.env,'DJMRN_P2F_ALLOW_BOOTSTRAP':bootstrap},clear=True):
            return server.check_bootstrap()
    def test_01_extra_model_denied(self):
        with self.assertRaises(Denied):server.validate({'request_id':'x','scenario':'ok','model':'paid'})
    def test_02_unknown_scene_denied(self):
        with self.assertRaises(Denied):server.validate({'request_id':'x','scenario':'real'})
    def test_03_scene_is_finite(self):
        self.assertEqual(set(server.SCENARIOS),{'ok','rate429','down503','partial','paid','unknown','reason'})
    def test_04_invalid_replay_ids(self):
        for key in ('UPPER','../../', '', 'z'*64, 12):
            with self.assertRaises(Denied):server.validate({'request_id':key,'scenario':'ok'})
    def test_05_offline_paid_deny(self):
        a=server.app_for(server.QuotaLedger(str(self.root/'q.db')),'paid')
        with self.assertRaises(Denied):a.handle(server.synthetic_request('paid'))
    def test_06_offline_unknown_price_deny(self):
        a=server.app_for(server.QuotaLedger(str(self.root/'q.db')),'unknown')
        with self.assertRaises(Denied):a.handle(server.synthetic_request('unknown'))
    def test_07_no_automatic_bootstrap(self):
        with self.assertRaisesRegex(RuntimeError,'STOP'):self.check('no')
    def test_08_explicit_first_boot(self):
        self.check('yes')
        self.assertEqual((self.root/'initialized.marker').read_text(),'p2f-synthetic-v1\n')
        self.assertTrue((self.root/'usage.sqlite').is_file())
    def test_09_missing_db_failclosed(self):
        self.check('yes')
        (self.root/'usage.sqlite').unlink()
        with self.assertRaisesRegex(RuntimeError,'STOP'):self.check('no')
    def test_10_corrupt_marker_failclosed(self):
        self.check('yes')
        (self.root/'initialized.marker').write_text('corrupt')
        with self.assertRaisesRegex(RuntimeError,'STOP'):self.check('no')
    def test_11_quota_persists_restart(self):
        a=self.check('yes')
        from integration import fake_route,synthetic_request
        a.reserve(synthetic_request('first'),(fake_route('djmrn-fake-a',limit=4),),'2026-10-23')
        q=self.check('no')
        with closing(sqlite3.connect(q.path)) as db:
            self.assertEqual(db.execute('SELECT used FROM usage').fetchone()[0],1)
    def test_12_untrusted_metadata_default_deny(self):
        from admission import Request
        self.assertFalse(Request('r','lite',frozenset({'chat'}),32).trusted)
    def test_13_no_hidden_Bifrost_fallback(self):
        p=Path(__file__).resolve().parents[1]/'ROUTER-P002E-20261023'/'integration.py'
        self.assertIn("assert 'fallbacks' not in payload",p.read_text())
    def test_14_front_checks_direct_network_bypass(self):
        s=Path(__file__).with_name('front_probe.py').read_text()
        self.assertIn("check_direct_bypass()",s)
        self.assertIn("djmrn-bifrost-p2c:8080",s)
    def test_15_sidecar_has_no_real_provider_hostname(self):
        s=Path(__file__).with_name('server.py').read_text()
        self.assertNotIn('api.openai.com',s);self.assertNotIn('api.groq.com',s)
    def test_16_server_request_body_is_bounded(self):
        s=Path(__file__).with_name('server.py').read_text()
        self.assertIn('1<=n<=1024',s)
        self.assertIn('hmac.compare_digest',s)
        self.assertIn('def log_message(self,*_):return',s)
if __name__=='__main__':unittest.main()
