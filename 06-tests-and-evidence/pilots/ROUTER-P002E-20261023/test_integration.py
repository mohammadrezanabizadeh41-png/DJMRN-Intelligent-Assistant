"""No Docker/network required: verify the P2E adapter's admission-before-HTTP path."""
import tempfile
from pathlib import Path
import unittest
from admission import Denied, QuotaLedger
from integration import AdmissionGateway, fake_route, synthetic_request, verified_fixture, real_gateway_transport, GATEWAY_URL

class P2EOffline(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.ledger=QuotaLedger(str(Path(self.tmp.name)/'quota.db'))
        self.a=fake_route('djmrn-fake-a',limit=1)
        self.b=fake_route('djmrn-fake-b',limit=1,priority=2)
        self.sent=[]
        self.day='2026-10-23'
    def tearDown(self):self.tmp.cleanup()
    def sender(self,model,*,stream=False):
        self.sent.append(model)
        return 200,'synthetic '+model.split('/')[0][-1]+(' [DONE]' if stream else '')
    def app(self,routes=None,sender=None):
        return AdmissionGateway(self.ledger,tuple(routes or (self.a,self.b)),sender or self.sender,self.day)
    def test_01_not_sent_if_untrusted(self):
        with self.assertRaises(Denied):self.app().handle(synthetic_request('a',trusted=False))
        self.assertEqual(self.sent,[])
    def test_02_unknown_price_denied_before_send(self):
        from dataclasses import replace
        with self.assertRaises(Denied):self.app([replace(self.a,price_per_token=None)]).handle(synthetic_request('a'))
        self.assertEqual(self.sent,[])
    def test_03_paid_route_denied(self):
        from dataclasses import replace
        with self.assertRaises(Denied):self.app([replace(self.a,price_per_token=.01)]).handle(synthetic_request('a'))
        self.assertEqual(self.sent,[])
    def test_04_only_fixture_providers(self):
        from dataclasses import replace
        self.assertFalse(verified_fixture(replace(self.a,provider='groq')))
        with self.assertRaises(Denied):self.app([replace(self.a,provider='groq')])
    def test_05_actual_model_exact_match(self):
        from dataclasses import replace
        with self.assertRaises(Denied):self.app([replace(self.a,route_id='djmrn-fake-a/gpt-4')])
    def test_06_first_A_second_B(self):
        self.assertIn('synthetic a',self.app().handle(synthetic_request('first')).body)
        self.assertIn('synthetic b',self.app().handle(synthetic_request('second')).body)
        self.assertEqual(len(self.sent),2)
    def test_07_exhaustion_never_sent(self):
        self.app().handle(synthetic_request('first')); self.app().handle(synthetic_request('second'))
        with self.assertRaises(Denied) as c:self.app().handle(synthetic_request('third'))
        self.assertEqual(c.exception.code,'FREE_POOL_EXHAUSTED')
        self.assertEqual(len(self.sent),2)
    def test_08_metered_429_then_B(self):
        def trans(model,*,stream=False):
            self.sent.append(model)
            return (429,'fake 429') if model.startswith('djmrn-fake-a/') else (200,'synthetic B')
        result=self.app(sender=trans).handle(synthetic_request('rate'))
        self.assertEqual(result.status,200)
        self.assertEqual(len(result.used_routes),2)
        self.assertEqual(len(self.sent),2)
    def test_09_metered_503_then_B(self):
        def trans(model,*,stream=False):
            self.sent.append(model)
            return (503,'fake 503') if model.startswith('djmrn-fake-a/') else (200,'synthetic B')
        result=self.app(sender=trans).handle(synthetic_request('down'))
        self.assertEqual(result.status,200)
        self.assertEqual(len(self.sent),2)
    def test_10_no_retry_after_partial_sse(self):
        def trans(model,*,stream=False):
            self.sent.append(model);return 200,'data: {"synthetic":"partial"}\n\n'
        result=self.app(sender=trans).handle(synthetic_request('sse'),stream=True)
        self.assertEqual(result.decision,'STOP_PARTIAL_STREAM')
        self.assertEqual(self.sent,[self.a.route_id])
    def test_11_billing_error_stops_without_B(self):
        def trans(model,*,stream=False):
            self.sent.append(model);return 402,'mock payment required'
        r=self.app(sender=trans).handle(synthetic_request('billing'))
        self.assertEqual(r.decision,'STOP_AUTH_OR_BILLING')
        self.assertEqual(len(self.sent),1)
    def test_12_repeated_request_denied(self):
        app=self.app();app.handle(synthetic_request('dupe'))
        with self.assertRaises(Denied):app.handle(synthetic_request('dupe'))
        self.assertEqual(len(self.sent),1)
    def test_13_no_model_downgrade(self):
        with self.assertRaises(Denied):self.app().handle(synthetic_request('hard',tier='reasoning'))
        self.assertFalse(self.sent)
    def test_14_at_most_two_attempts(self):
        def trans(model,*,stream=False):
            self.sent.append(model);return 429,'mock rate'
        with self.assertRaises(Denied) as c:self.app(sender=trans).handle(synthetic_request('rate'))
        self.assertEqual(c.exception.code,'ATTEMPTS_EXHAUSTED')
        self.assertEqual(len(self.sent),2)
    def test_15_literal_url_lock_and_no_gateway_fallbacks(self):
        self.assertEqual(GATEWAY_URL,'http://djmrn-bifrost-p2c:8080/v1/chat/completions')
        from inspect import getsource
        code=getsource(real_gateway_transport)
        self.assertIn("'fallbacks' not in payload",code)
        self.assertNotIn('api.openai.com',code)

if __name__=='__main__':unittest.main()
