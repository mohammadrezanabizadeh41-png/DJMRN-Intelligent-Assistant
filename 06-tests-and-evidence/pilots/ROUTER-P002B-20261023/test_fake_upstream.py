"""Real socket transport tests of MOCK upstreams, NOT a Bifrost integration test."""
import json
from collections import deque
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen, Request
from fake_upstream import Script, pair


class FakeUpstreamLoopbackTests(unittest.TestCase):
    def post(self, url, stream=False, model="fake-model", auth="Bearer SYNTHETIC"):
        body=json.dumps({"model": model,"messages":[{"role":"user","content":"SYNTHETIC"}],"stream":stream}).encode()
        headers={"Content-Type":"application/json"}
        if auth is not None:headers["Authorization"]=auth
        req=Request(url+"/v1/chat/completions", data=body, headers=headers)
        try:
            with urlopen(req, timeout=4) as res:
                return res.status, dict(res.headers), res.read()
        except HTTPError as e:
            try:return e.code, dict(e.headers), e.read()
            finally:e.close()

    def test_01_both_mock_servers_live_and_local(self):
        with pair(Script(),Script()) as urls:
            self.assertTrue(all(u.startswith("http://127.0.0.1:") for u in urls))
            self.assertNotEqual(urls[0],urls[1])
            for u in urls:
                with urlopen(u+"/health",timeout=4) as r:
                    self.assertEqual(r.status,200)

    def test_02_primary_429_secondary_200_observed(self):
        a=Script(deque(["status:429"]));b=Script(deque(["ok"]))
        with pair(a,b) as (u1,u2):
            status,head,_=self.post(u1)
            self.assertEqual(status,429)
            self.assertEqual(head.get("Retry-After"),"5")
            status,_,body=self.post(u2)
            self.assertEqual(status,200)
            self.assertEqual(json.loads(body)["choices"][0]["message"]["content"],"synthetic B")
        self.assertEqual(len(a.seen),1);self.assertEqual(len(b.seen),1)

    def test_03_error_codes_distinct_from_quota(self):
        a=Script(deque(["status:401","status:402","status:403","status:503"]));b=Script()
        with pair(a,b) as (u1,_):
            self.assertEqual([self.post(u1)[0] for _ in range(4)],[401,402,403,503])
        self.assertEqual(len(b.seen),0)

    def test_04_valid_sse_has_done(self):
        with pair(Script(deque(["ok"])),Script()) as (u1,_):
            code,head,body=self.post(u1,stream=True)
        self.assertEqual(code,200)
        self.assertIn("text/event-stream",head["Content-Type"])
        self.assertIn(b"data: [DONE]",body)

    def test_05_broken_sse_missing_done(self):
        with pair(Script(deque(["partial_stream"])),Script()) as (u1,_):
            code,_,body=self.post(u1,stream=True)
        self.assertEqual(code,200)
        self.assertIn(b"partial",body)
        self.assertNotIn(b"data: [DONE]",body)

    def test_06_no_raw_request_payload_or_auth_in_mock_events(self):
        a=Script(deque(["ok"]))
        with pair(a,Script()) as (u1,_):
            code,_,_=self.post(u1,model="fake-model",auth="Bearer SYNTHETIC-NOT-SECRET")
        self.assertEqual(code,200)
        self.assertEqual(a.seen,[{"model":"fake-model","auth_present":True}])
        self.assertNotIn("SYNTHETIC-NOT-SECRET",repr(a.seen))

    def test_07_invalid_endpoint_returns_404(self):
        with pair(Script(),Script()) as (u1,_):
            req=Request(u1+"/v1/invalid",data=b"{}")
            with self.assertRaises(HTTPError) as caught:urlopen(req,timeout=4)
            self.assertEqual(caught.exception.code,404)

    def test_08_absent_key_still_recorded_as_absent(self):
        a=Script(deque(["ok"]))
        with pair(a,Script()) as (u1,_):
            self.assertEqual(self.post(u1,auth=None)[0],200)
        self.assertEqual(a.seen,[{"model":"fake-model","auth_present":False}])
        # Intentionally: mock upstream DOES NOT enforce gateway inference auth.

if __name__=='__main__':unittest.main()
