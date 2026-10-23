"""P2F: synthetic-only front-facing quota gate; not a production API."""
import hmac,json,os,re,sqlite3,sys
from contextlib import closing
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
sys.path.insert(0,'/opt/ROUTER-P002E-20261023')
sys.path.insert(0,'/opt/ROUTER-P002D-20261023')
from integration import AdmissionGateway,fake_route,real_gateway_transport,synthetic_request
from admission import Denied,QuotaLedger
PORT=8090
SCENARIOS={'ok':'fixture-ok','rate429':'fixture-rate429','down503':'fixture-down503','partial':'fixture-no-done','paid':'fixture-ok','unknown':'fixture-ok','reason':'fixture-ok'}
KEY_RE=re.compile(r'^[a-z0-9][a-z0-9_-]{0,47}$')
TOKEN=os.getenv('P2F_CLIENT_TOKEN','')
LEDGER_DIR=Path(os.getenv('DJMRN_P2F_LEDGER_DIR','/ledger'))
FIXTURE_DAY='2026-10-23'
LEDGER=None
def check_bootstrap():
    if os.getenv('DJMRN_P2F_SYNTHETIC_ONLY')!='yes' or os.getenv('DJMRN_GATEWAY_TEST_URL')!='http://djmrn-bifrost-p2c:8080/v1/chat/completions':
        raise RuntimeError('STOP: non-synthetic endpoint')
    if not TOKEN or len(TOKEN)<32 or os.getenv('DJMRN_P2F_LEDGER_DIR')!='/ledger':
        raise RuntimeError('STOP: missing trusted client or ledger')
    if not LEDGER_DIR.is_dir() or LEDGER_DIR.is_symlink():
        raise RuntimeError('STOP: unsafe ledger mount')
    marker=LEDGER_DIR/'initialized.marker'
    db=LEDGER_DIR/'usage.sqlite'
    if marker.exists():
        if not db.is_file() or db.is_symlink():
            raise RuntimeError('STOP: missing saved database')
    elif os.getenv('DJMRN_P2F_ALLOW_BOOTSTRAP')=='yes' and not db.exists():
        QuotaLedger(str(db))
        fd=os.open(marker,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(fd,'w') as f:f.write('p2f-synthetic-v1\n')
    else:raise RuntimeError('STOP: state lost; explicit bootstrap only')
    if marker.read_text()!='p2f-synthetic-v1\n':
        raise RuntimeError('STOP: wrong state identity')
    with closing(sqlite3.connect(db)) as c:
        if c.execute('PRAGMA integrity_check').fetchone()[0]!='ok':
            raise RuntimeError('STOP: corrupt quota database')
    return QuotaLedger(str(db))
def validate(obj):
    if not isinstance(obj,dict) or set(obj)!={'request_id','scenario'}:
        raise Denied('INVALID_REQUEST')
    ident=obj['request_id'];scene=obj['scenario']
    if not isinstance(ident,str) or not KEY_RE.fullmatch(ident) or not isinstance(scene,str) or scene not in SCENARIOS:
        raise Denied('INVALID_REQUEST')
    return ident,scene
def app_for(ledger,scene):
    model=SCENARIOS[scene]
    kw={'price':.002} if scene=='paid' else ({'price':None} if scene=='unknown' else {})
    routes=(fake_route('djmrn-fake-a',model,limit=4,priority=1,**kw),
            fake_route('djmrn-fake-b',model,limit=4,priority=2,**kw))
    return AdmissionGateway(ledger,routes,real_gateway_transport,FIXTURE_DAY)
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*_):return
    def reply(self,status,value):
        out=json.dumps(value,separators=(',',':')).encode()
        self.send_response(status)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(out)))
        self.send_header('Cache-Control','no-store')
        self.end_headers()
        self.wfile.write(out)
    def do_GET(self):
        if self.path=='/health':return self.reply(200,{'status':'ready','type':'synthetic'})
        return self.reply(404,{'code':'NOT_FOUND'})
    def do_POST(self):
        if self.path!='/v1/chat/completions':return self.reply(404,{'code':'NOT_FOUND'})
        if not hmac.compare_digest(self.headers.get('x-djmrn-client-token',''),TOKEN):
            return self.reply(401,{'code':'UNAUTHORIZED'})
        try:n=int(self.headers.get('Content-Length','-1'))
        except ValueError:return self.reply(400,{'code':'INVALID_LENGTH'})
        if not 1<=n<=1024:return self.reply(413,{'code':'INVALID_LENGTH'})
        try:ident,scene=validate(json.loads(self.rfile.read(n)))
        except (ValueError,UnicodeDecodeError,Denied):return self.reply(400,{'code':'INVALID_REQUEST'})
        try:
            app=app_for(LEDGER,scene)
            req=synthetic_request('p2f-'+ident,tier='reasoning' if scene=='reason' else 'lite')
            result=app.handle(req,stream=scene=='partial')
            if result.decision=='STOP_PARTIAL_STREAM':
                return self.reply(502,{'code':'STOP_PARTIAL_STREAM','attempts':len(result.used_routes)})
            if result.decision!='COMPLETE' or result.status!=200:
                return self.reply(502,{'code':'UPSTREAM_STOP','attempts':len(result.used_routes)})
            served='B' if 'synthetic B' in result.body else ('A' if 'synthetic A' in result.body else 'unknown')
            if served=='unknown':return self.reply(502,{'code':'INVALID_FIXTURE_RESPONSE'})
            return self.reply(200,{'code':'OK','fixture_provider':served,'attempts':len(result.used_routes)})
        except Denied as e:
            statuses={'FREE_POOL_EXHAUSTED':429,'ATTEMPTS_EXHAUSTED':429,'REQUEST_HISTORY_MISMATCH':409,'NO_COMPATIBLE_FREE_MODEL':403,'POLICY_DENIED':403}
            return self.reply(statuses.get(e.code,403),{'code':e.code})
        except Exception:
            return self.reply(502,{'code':'UNCERTAIN_DELIVERY_STOP'})
def main():
    global LEDGER
    LEDGER=check_bootstrap()
    print('P2F_SYNTHETIC_ADMISSION_READY',flush=True)
    ThreadingHTTPServer(('0.0.0.0',PORT),Handler).serve_forever()
if __name__=='__main__':main()
