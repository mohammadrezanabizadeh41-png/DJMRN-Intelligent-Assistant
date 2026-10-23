"""DJMRN P2E: isolated synthetic-only, quota-admitted REAL Bifrost gateway requests.

Not production middleware. Only two named dummy providers and four fixture models.
P2D admission reserves *each* attempt before Bifrost HTTP; Bifrost fallbacks
are explicitly omitted so hidden downstream attempts cannot bypass quota ledger.
"""
import base64
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.error
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ROUTER-P002D-20261023'))
from admission import Denied, QuotaLedger, Request, Route, next_step

GATEWAY_URL = 'http://djmrn-bifrost-p2c:8080/v1/chat/completions'
PROVIDERS = ('djmrn-fake-a', 'djmrn-fake-b')
MODELS = ('fixture-ok', 'fixture-rate429', 'fixture-down503', 'fixture-no-done')


def verified_fixture(route):
    return (route.provider in PROVIDERS and route.model in MODELS
            and route.route_id == route.provider + '/' + route.model
            and route.account_group in ('quota-fake-a', 'quota-fake-b')
            and route.account_group == 'quota-fake-' + route.provider[-1])


def fake_route(provider, model='fixture-ok', *, limit=2, price=0, verified=True,
               billed=False, tier='lite', priority=1):
    assert provider in PROVIDERS and model in MODELS
    return Route(provider + '/' + model, provider, model,
                 'quota-fake-' + provider[-1], tier, frozenset({'chat','persian'}),
                 4096, limit, price, verified, not billed, True, priority=priority)


def synthetic_request(id, *, trusted=True, tier='lite', capabilities=frozenset({'chat', 'persian'})):
    # Trusted metadata here is fixed *test harness input*, never an HTTP user flag.
    return Request(id, tier, capabilities, 32, trusted=trusted)


def real_gateway_transport(model, *, stream=False):
    """Exactly one HTTP request, no client retry, and crucially NO Bifrost fallbacks."""
    assert model.split('/',1)[0] in PROVIDERS
    assert model.split('/',1)[1] in MODELS
    assert os.environ.get('DJMRN_GATEWAY_TEST_URL') == GATEWAY_URL, 'test-only endpoint gate'
    admin = os.environ['BIFROST_ADMIN_USERNAME']
    password = os.environ['BIFROST_ADMIN_PASSWORD']
    vk = os.environ['BIFROST_TEST_VIRTUAL_KEY']
    assert password and vk.startswith('sk-bf-')
    token = base64.b64encode((admin+':'+password).encode()).decode()
    payload={'model':model,'messages':[{'role':'user','content':'P2E synthetic-only fixture'}],
             'max_tokens':16,'stream':stream}
    assert 'fallbacks' not in payload
    req=urllib.request.Request(GATEWAY_URL,json.dumps(payload).encode(),
         {'Content-Type':'application/json','Authorization':'Basic '+token,'x-bf-vk':vk})
    try:
        with urllib.request.urlopen(req,timeout=12) as response:
            return response.status,response.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as ex:
        try: return ex.code,ex.read().decode('utf-8',errors='replace')
        finally: ex.close()


@dataclass(frozen=True)
class Outcome:
    status: int
    body: str
    used_routes: tuple[str, ...]
    decision: str


class AdmissionGateway:
    """Test-only pre-router, *not* a public endpoint or native Bifrost plugin."""
    def __init__(self, ledger, routes, sender, utc_day):
        self.ledger=ledger
        self.routes=tuple(routes)
        self.sender=sender
        self.utc_day=utc_day
        if not self.routes or not all(verified_fixture(r) for r in self.routes):
            raise Denied('ONLY_SYNTHETIC_FIXTURES_ALLOWED')
        self.sent=0

    def handle(self, request, *, stream=False):
        attempted=()
        while True:
            route_id=self.ledger.reserve(request,self.routes,self.utc_day,attempted)
            if route_id not in {r.route_id for r in self.routes}:
                raise Denied('NONFIXTURE_ROUTE')
            self.sent+=1
            status,body=self.sender(route_id,stream=stream)
            if stream and (status == 200 and '[DONE]' not in body):
                return Outcome(status,body,attempted+(route_id,),next_step(status,stream_started=True))
            decision=next_step(status)
            used=attempted+(route_id,)
            if decision != 'TRY_ELIGIBLE_FREE_FALLBACK':
                return Outcome(status,body,used,decision)
            attempted=used
            # The next P2D atomic reservation MUST happen before a second HTTP attempt.


def assert_live(condition, label):
    if not condition:
        raise AssertionError(label)
    print('P2E_LIVE_PASS: '+label)


def run_live():
    if os.environ.get('DJMRN_P2E_SYNTHETIC_ONLY') != 'yes':
        raise RuntimeError('STOP: synthetic-only gate missing')
    assert os.environ.get('DJMRN_GATEWAY_TEST_URL') == GATEWAY_URL
    day=datetime.now(timezone.utc).date().isoformat()
    with tempfile.TemporaryDirectory(prefix='djmrn-p2e-') as directory:
        ledger=QuotaLedger(str(Path(directory)/'quota.db'))
        a=fake_route('djmrn-fake-a',limit=1,priority=1)
        b=fake_route('djmrn-fake-b',limit=1,priority=2)
        app=AdmissionGateway(ledger,(a,b),real_gateway_transport,day)
        for name, req, routes in (
            ('untrusted_denied',synthetic_request('deny-trust',trusted=False),(a,b)),
            ('unknown_price_denied',synthetic_request('deny-price'),(fake_route('djmrn-fake-a',price=None),)),
            ('paid_route_denied',synthetic_request('deny-paid'),(fake_route('djmrn-fake-a',price=0.001),)),
            ('tier_downgrade_denied',synthetic_request('deny-tier',tier='reasoning'),(a,b)),
        ):
            trial=AdmissionGateway(ledger,routes,real_gateway_transport,day)
            try:
                trial.handle(req)
                raise AssertionError('Failed to deny: '+name)
            except Denied:
                assert_live(trial.sent == 0,name+'_before_http')
        first=app.handle(synthetic_request('quota-a'))
        assert_live(first.status == 200 and 'synthetic A' in first.body and first.used_routes==(a.route_id,),'admitted_A_through_real_Bifrost')
        second=app.handle(synthetic_request('quota-b'))
        assert_live(second.status == 200 and 'synthetic B' in second.body and second.used_routes==(b.route_id,),'shared_quota_exhaustion_routes_to_B')
        try:
            app.handle(synthetic_request('quota-overflow'))
            raise AssertionError('Over-quota HTTP allowed')
        except Denied as ex:
            assert_live(ex.code == 'FREE_POOL_EXHAUSTED' and app.sent == 2,'exhausted_fails_closed_before_http')
        # Independent groups for each error kind; each attempted upstream reserved once.
        for model, expected in (('fixture-rate429','429'),('fixture-down503','503')):
            tmp=QuotaLedger(str(Path(directory)/('err-'+expected+'.db')))
            x=fake_route('djmrn-fake-a',model,limit=1,priority=1)
            y=fake_route('djmrn-fake-b',model,limit=1,priority=2)
            client=AdmissionGateway(tmp,(x,y),real_gateway_transport,day)
            out=client.handle(synthetic_request('error-'+expected))
            assert_live(out.status==200 and 'synthetic B' in out.body and
                        out.used_routes==(x.route_id,y.route_id) and client.sent==2,
                        'admission_metered_'+expected+'_fallback_via_Bifrost')
        tmp=QuotaLedger(str(Path(directory)/'partial.db'))
        x=fake_route('djmrn-fake-a','fixture-no-done',limit=1,priority=1)
        y=fake_route('djmrn-fake-b','fixture-no-done',limit=1,priority=2)
        client=AdmissionGateway(tmp,(x,y),real_gateway_transport,day)
        out=client.handle(synthetic_request('partial'),stream=True)
        assert_live(out.decision=='STOP_PARTIAL_STREAM' and client.sent==1 and
                    out.used_routes==(x.route_id,),'partial_stream_no_retry')
    print('P2E_GENUINE_BIFROST_ADMISSION_SYNTHETIC_PASS: 8 guarded groups; NOT a real provider/quota proof')


if __name__ == '__main__':
    run_live()
