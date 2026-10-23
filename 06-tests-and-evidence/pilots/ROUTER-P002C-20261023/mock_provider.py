"""Synthetic OpenAI-shaped provider. Runs ONLY in a private Docker test network.

No public bind/published port, no third-party model/API, no prompt or secret logging.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NAME = os.environ.get('DJMRN_MOCK_NAME', 'A')
assert NAME in ('A', 'B')
MODELS = ('fixture-ok', 'fixture-rate429', 'fixture-down503', 'fixture-no-done')

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        return

    def write_json(self, code, obj, headers=None):
        b = json.dumps(obj).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(b)))
        for key, val in (headers or {}).items():
            self.send_header(key, val)
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path == '/health':
            return self.write_json(200, {'ok': True, 'provider': NAME})
        if self.path in ('/v1/models', '/models'):
            return self.write_json(200, {'object': 'list', 'data': [{'id': m, 'object': 'model'} for m in MODELS]})
        return self.write_json(404, {'error': {'message': 'missing'}})

    def do_POST(self):
        if self.path not in ('/v1/chat/completions', '/chat/completions'):
            return self.write_json(404, {'error': {'message': 'missing'}})
        try:
            n = int(self.headers.get('Content-Length', '-1'))
            if n < 0 or n > 32768:
                return self.write_json(413, {'error': {'message': 'invalid length'}})
            payload = json.loads(self.rfile.read(n))
            model = payload['model'].split('/')[-1]
            if model not in MODELS or not isinstance(payload.get('messages'), list):
                return self.write_json(400, {'error': {'message': 'invalid model/request'}})
        except (ValueError, KeyError, TypeError):
            return self.write_json(400, {'error': {'message': 'bad JSON'}})
        # Only primary fake A simulates rejection; secondary B is always available.
        if NAME == 'A' and model in ('fixture-rate429', 'fixture-down503'):
            status = 429 if model == 'fixture-rate429' else 503
            headers = {'Retry-After': '1'} if status == 429 else {}
            return self.write_json(status, {'error': {'type': 'rate_limit_error' if status == 429 else 'server_error', 'message': f'synthetic {status}'}}, headers)
        if NAME == 'A' and model == 'fixture-no-done' and payload.get('stream'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(b'data: {"choices":[{"delta":{"content":"synthetic partial"}}]}\n\n')
            self.wfile.flush()
            self.close_connection = True
            return
        if payload.get('stream'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Connection', 'close')
            self.end_headers()
            b = json.dumps({'id': 'fake', 'object':'chat.completion.chunk','model':model, 'choices':[{'index':0,'delta':{'content':f'synthetic {NAME}'},'finish_reason':None}]}).encode()
            self.wfile.write(b'data: '+b+b'\n\ndata: [DONE]\n\n')
            self.close_connection = True
            return
        self.write_json(200, {'id':'fake','object':'chat.completion','model':model,'choices':[{'index':0,'message':{'role':'assistant','content':f'synthetic {NAME}'},'finish_reason':'stop'}],'usage':{'prompt_tokens':0,'completion_tokens':0,'total_tokens':0}})

if __name__ == '__main__':
    # 0.0.0.0 is inside a named Docker network marked --internal, no host port published.
    ThreadingHTTPServer(('0.0.0.0', 8081), Handler).serve_forever()
