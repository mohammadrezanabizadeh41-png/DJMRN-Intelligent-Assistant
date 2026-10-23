"""Unit/source tests for the future manual real Bifrost CI workflow.

These tests do NOT start Bifrost, Docker or connect to any remote endpoint.
"""
from pathlib import Path
from http.server import ThreadingHTTPServer
from threading import Thread
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import os
import subprocess
import sys
import unittest
import mock_provider

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT/'config.json').read_text())

class StaticAdmission(unittest.TestCase):
    def test_01_synthetic_only_providers(self):
        self.assertEqual(set(CONFIG['providers']), {'djmrn-fake-a','djmrn-fake-b'})
        for p in CONFIG['providers'].values():
            self.assertTrue(p['network_config']['base_url'].startswith('http://djmrn-mock-'))
            self.assertEqual(p['keys'][0]['value'], 'env.DJMRN_FAKE_PROVIDER_TOKEN')
    def test_02_auth_and_model_whitelist(self):
        self.assertTrue(CONFIG['client']['enforce_auth_on_inference'])
        self.assertTrue(CONFIG['governance']['auth_config']['is_enabled'])
        self.assertTrue(CONFIG['governance']['auth_config']['setup_token'].startswith('env.'))
        for p in CONFIG['governance']['virtual_keys'][0]['provider_configs']:
            self.assertTrue(p['allowed_models'])
            self.assertNotIn('*',p['allowed_models'])
            self.assertTrue(all(m.startswith('fixture-') for m in p['allowed_models']))
    def test_03_manual_workflow_source_only(self):
        text=(ROOT/'djmrn-p2c-manual.yml').read_text()
        self.assertIn('workflow_dispatch:', text)
        self.assertNotIn('schedule:',text)
        self.assertNotIn('push:',text)
        self.assertIn('billing_guard_confirmed:', text)
        self.assertIn('timeout-minutes: 8',text)
        self.assertIn('permissions:',text)
    def test_04_safety_runner_shell_guards(self):
        script=(ROOT/'run_ci.sh').read_text()
        for literal in ('--internal','127.0.0.1:18080:8080','--cap-drop ALL', 'DJMRN_APPROVED_FREE_ACTIONS_MINUTES', 'sha256:d53775fd4b1d444c350443d2487ceb8aa8c0bab722cd5dc7b0001a7fa88ecd7f'):
            self.assertIn(literal, script)
    def test_05_no_approval_refuses_before_docker(self):
        env=dict(os.environ);env.pop('DJMRN_APPROVED_FREE_ACTIONS_MINUTES',None)
        p=subprocess.run(['bash',str(ROOT/'run_ci.sh')],env=env,capture_output=True,text=True,timeout=3)
        self.assertEqual(p.returncode,90)
        self.assertIn('STOP',p.stdout)
    def test_06_direct_http_mock_A_is_not_falsely_gateway_auth(self):
        mock_provider.NAME='A'
        srv=ThreadingHTTPServer(('127.0.0.1',0),mock_provider.Handler)
        srv.daemon_threads=True
        th=Thread(target=srv.serve_forever,daemon=True);th.start()
        try:
            base=f'http://127.0.0.1:{srv.server_port}'
            with urlopen(base+'/health',timeout=2) as r:self.assertEqual(r.status,200)
            req=Request(base+'/v1/chat/completions',data=json.dumps({'model':'fixture-rate429','messages':[]}).encode(),headers={'Content-Type':'application/json'})
            with self.assertRaises(HTTPError) as got:urlopen(req,timeout=2)
            try:self.assertEqual(got.exception.code,429)
            finally:got.exception.close()
        finally:
            srv.shutdown();srv.server_close();th.join(timeout=3)
    def test_07_probe_calls_gateway_not_fakes(self):
        src=(ROOT/'probe_gateway.py').read_text()
        self.assertIn('http://127.0.0.1:18080/v1/chat/completions',src)
        self.assertNotIn('http://djmrn-mock-',src)
        self.assertIn('unauthenticated_denied',src)
        self.assertIn('bifrost_429_fallback',src)

if __name__=='__main__':unittest.main()
