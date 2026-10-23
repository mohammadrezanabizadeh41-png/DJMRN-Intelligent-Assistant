"""P2B offline fixture: two loopback OpenAI-shaped fake upstreams.

NOT Maxim Bifrost and NOT a real cloud provider. No external traffic, accounts,
credentials, payment, Windows tools or user files. Logs only test metadata.
"""
from __future__ import annotations

from collections import deque
from contextlib import contextmanager
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread, Lock
import json


@dataclass
class Script:
    outcomes: deque[str] = field(default_factory=lambda: deque(["ok"]))
    seen: list[dict] = field(default_factory=list)
    lock: Lock = field(default_factory=Lock)

    def next_outcome(self, model: str, auth_present: bool) -> str:
        with self.lock:
            self.seen.append({"model": model, "auth_present": auth_present})
            return self.outcomes.popleft() if self.outcomes else "ok"


def build_handler(script: Script, name: str):
    class FakeProvider(BaseHTTPRequestHandler):
        server_version = "DJMRNMock/0.1"
        sys_version = ""

        def log_message(self, *args):
            # Do not log authorization or prompt/payloads.
            return

        def do_GET(self):
            if self.path != "/health":
                return self._json(404, {"error": {"message": "not found"}})
            return self._json(200, {"ok": True, "server": name})

        def do_POST(self):
            if self.path != "/v1/chat/completions":
                return self._json(404, {"error": {"message": "not found"}})
            try:
                n = int(self.headers.get("Content-Length", "-1"))
                if n < 0 or n > 8_192:
                    return self._json(413, {"error": {"message": "invalid fixture length"}})
                payload = json.loads(self.rfile.read(n))
                model = payload["model"]
                if not isinstance(model, str) or not isinstance(payload["messages"], list):
                    raise ValueError("bad shape")
            except (ValueError, KeyError, TypeError, json.JSONDecodeError):
                return self._json(400, {"error": {"message": "invalid fixture request"}})

            # No prompt/messages retained. A fake key may be present; never log it.
            outcome = script.next_outcome(model, bool(self.headers.get("Authorization")))
            if outcome.startswith("status:"):
                status = int(outcome.split(":", 1)[1])
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                if status == 429:
                    self.send_header("Retry-After", "5")
                data = json.dumps({"error": {"type": "fake_upstream", "message": f"FAKE {status}"}}).encode()
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return

            if outcome == "partial_stream":
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write(b'data: {"choices":[{"delta":{"content":"partial"}}]}\n\n')
                self.wfile.flush()
                self.close_connection = True  # purposely no terminal [DONE]
                return

            if payload.get("stream"):
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write((
                    'data: '+json.dumps({"id":"fake-1","choices":[{"index":0,"delta":{"content":f"synthetic {name}"}}]})+'\n\n'
                    'data: [DONE]\n\n'
                ).encode())
                self.close_connection = True
                return
            return self._json(200, {
                "id": "fake-1", "object": "chat.completion", "model": model,
                "choices": [{"index": 0, "message": {"role": "assistant", "content": f"synthetic {name}"}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
            })

        def _json(self, status: int, obj: dict):
            data = json.dumps(obj).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return FakeProvider


@contextmanager
def pair(a: Script, b: Script):
    servers = []
    threads = []
    try:
        for script, name in ((a, "A"), (b, "B")):
            srv = ThreadingHTTPServer(("127.0.0.1", 0), build_handler(script, name))
            srv.daemon_threads = True
            thread = Thread(target=srv.serve_forever, daemon=True)
            thread.start()
            servers.append(srv)
            threads.append(thread)
        yield tuple(f"http://127.0.0.1:{srv.server_port}" for srv in servers)
    finally:
        for srv in servers:
            srv.shutdown()
            srv.server_close()
        for thread in threads:
            thread.join(timeout=3)
