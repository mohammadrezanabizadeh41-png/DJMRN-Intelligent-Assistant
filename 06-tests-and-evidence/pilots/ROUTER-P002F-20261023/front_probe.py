"""P2F: front-only independent probe, never has Bifrost gateway credentials."""
import json,os,time,urllib.error,urllib.request
URL='http://djmrn-p2f-admission:8090'
TOKEN=os.environ['P2F_CLIENT_TOKEN']
PHASE=os.environ['P2F_PHASE']
def call(scene,ident,token=TOKEN,extra=None):
    payload={'request_id':ident,'scenario':scene}
    if extra:payload.update(extra)
    hdr={'Content-Type':'application/json'}
    if token:hdr['x-djmrn-client-token']=token
    req=urllib.request.Request(URL+'/v1/chat/completions',json.dumps(payload).encode(),hdr)
    try:
        with urllib.request.urlopen(req,timeout=14) as resp:return resp.status,json.loads(resp.read())
    except urllib.error.HTTPError as e:
        with e:return e.code,json.loads(e.read())
def expect(label,scene,ident,status,code,served=None,attempts=None,**kw):
    actual,body=call(scene,ident,**kw)
    assert actual==status and body['code']==code,(label,actual,body)
    if served is not None:assert body.get('fixture_provider')==served,(label,body)
    if attempts is not None:assert body.get('attempts')==attempts,(label,body)
    print('P2F_LIVE_PASS: '+label,flush=True)
def healthy():
    stop=time.monotonic()+35
    while time.monotonic()<stop:
        try:
            with urllib.request.urlopen(URL+'/health',timeout=2) as r:
                if r.status==200:return
        except (OSError,urllib.error.URLError):pass
        time.sleep(1)
    raise RuntimeError('front adapter not ready')
def check_direct_bypass():
    for target in ('djmrn-bifrost-p2c:8080','djmrn-mock-a:8081','djmrn-mock-b:8081'):
        try:
            with urllib.request.urlopen('http://'+target+'/health',timeout=2) as resp:
                raise AssertionError('BACKEND BYPASS: '+target)
        except urllib.error.HTTPError:
            raise AssertionError('BACKEND HOST REACHABLE: '+target)
        except (OSError,urllib.error.URLError):
            print('P2F_LIVE_PASS: frontend_cannot_reach_'+target.split(':')[0],flush=True)
def run():
    healthy();check_direct_bypass()
    if PHASE=='first':
        expect('missing_token_deny','ok','unauth',401,'UNAUTHORIZED',token='')
        expect('injected_provider_field_deny','ok','forged',400,'INVALID_REQUEST',extra={'model':'some-paid-model'})
        expect('paid_route_never_called','paid','paid',403,'NO_COMPATIBLE_FREE_MODEL')
        expect('unknown_price_never_called','unknown','unknown',403,'NO_COMPATIBLE_FREE_MODEL')
        expect('reasoning_downgrade_denied','reason','reason',403,'NO_COMPATIBLE_FREE_MODEL')
        expect('metered_429_to_B','rate429','f429',200,'OK',served='B',attempts=2)
        expect('metered_503_to_B','down503','f503',200,'OK',served='B',attempts=2)
        expect('partial_sse_stopped','partial','partial',502,'STOP_PARTIAL_STREAM',attempts=1)
        expect('admitted_A','ok','first-ok',200,'OK',served='A',attempts=1)
        expect('admitted_B_after_A_exhausted','ok','second-ok',200,'OK',served='B',attempts=1)
        print('P2F_PHASE1_PASS',flush=True)
    elif PHASE=='second':
        expect('quota_persisted_after_restart','ok','third-ok',200,'OK',served='B',attempts=1)
        expect('quota_fully_exhausted','ok','overflow',429,'FREE_POOL_EXHAUSTED')
        expect('replay_denied','ok','first-ok',409,'REQUEST_HISTORY_MISMATCH')
        print('P2F_PHASE2_RESTART_PASS',flush=True)
    else:raise RuntimeError('invalid probe phase')
if __name__=='__main__':run()
