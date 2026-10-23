"""Real gateway P2B probe. Must run only against a pinned isolated Bifrost container.

Never uses real provider models, Windows file access, paid keys or non-loopback HTTP.
Failure is reported rather than silently switching to a test-client fallback.
"""
import base64
import json
import os
import time
import urllib.error
import urllib.request

URL = os.environ.get('DJMRN_GATEWAY_TEST_URL', 'http://127.0.0.1:18080/v1/chat/completions')
assert URL in ('http://127.0.0.1:18080/v1/chat/completions', 'http://djmrn-bifrost-p2c:8080/v1/chat/completions'), 'Refuse any non-test endpoint'
ADMIN = os.environ['BIFROST_ADMIN_USERNAME']
PASSWORD = os.environ['BIFROST_ADMIN_PASSWORD']
VK = os.environ['BIFROST_TEST_VIRTUAL_KEY']
assert PASSWORD and VK.startswith('sk-bf-')


def wait_for_gateway(timeout_seconds=35):
    health = URL.rsplit('/v1/chat/completions',1)[0] + '/health'
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(health, timeout=2) as response:
                if response.status == 200:
                    print('GATEWAY_HEALTH_ENDPOINT_PASS')
                    return
        except (OSError, urllib.error.URLError):
            pass
        time.sleep(1)
    raise RuntimeError('Bifrost health check timeout; NOT READY')


def post(model, fallbacks=(), *, authorized=True, with_vk=True, stream=False):
    payload = {
        'model': model,
        'messages': [{'role': 'user', 'content': 'Synthetic fixture. No private data.'}],
        'stream': stream,
        'max_tokens': 16,
    }
    if fallbacks:
        payload['fallbacks'] = list(fallbacks)
    headers = {'Content-Type': 'application/json'}
    if authorized:
        pair = base64.b64encode(f'{ADMIN}:{PASSWORD}'.encode()).decode()
        headers['Authorization'] = 'Basic ' + pair
    if with_vk:
        headers['x-bf-vk'] = VK
    request = urllib.request.Request(URL, json.dumps(payload).encode(), headers)
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return response.status, response.read().decode(errors='replace')
    except urllib.error.HTTPError as error:
        try:
            return error.code, error.read().decode(errors='replace')
        finally:
            error.close()


def check(name, test):
    try:
        status, body = test()
        print(json.dumps({'probe': name, 'http_status': status, 'pass': bool(body)}, ensure_ascii=False))
        assert body, f'{name}: observed status {status}'
    except Exception as exc:
        print(json.dumps({'probe': name, 'pass': False, 'reason_type': type(exc).__name__}))
        raise


def require_status(status, body, acceptable, content=None):
    if status not in acceptable:
        # Safe fixture-only diagnostic, not a request-body dump or external payload.
        try:
            data=json.loads(body)
            description=str(data.get('error', data))[:220]
        except (ValueError, AttributeError):
            description='non-JSON gateway error'
        for secret in (PASSWORD,VK):
            description=description.replace(secret,'[REDACTED]')
        print(json.dumps({'probe_failure_status':status,'gateway_error':description}))
        raise AssertionError(f'status={status}; wanted {acceptable}')
    if content is not None:
        assert content in body, 'expected fixture content not observed'
    return status, True


def main():
    wait_for_gateway()
    # 1. Fail before allowing any successful inference if auth/vk is bypassed.
    check('unauthenticated_denied', lambda: require_status(*post('djmrn-fake-a/fixture-ok',authorized=False,with_vk=False), {401,403}))
    check('missing_virtual_key_denied', lambda: require_status(*post('djmrn-fake-a/fixture-ok',with_vk=False), {401,403}))
    check('explicit_nonallowlisted_model_denied', lambda: require_status(*post('djmrn-fake-a/fixture-paid'),{400,401,403,404,422}))

    # 2. From here all calls pass through the real Bifrost HTTP endpoint.
    check('normal_genuine_gateway_route',lambda: require_status(*post('djmrn-fake-a/fixture-ok'), {200},'synthetic A'))
    check('bifrost_429_fallback', lambda: require_status(*post('djmrn-fake-a/fixture-rate429',['djmrn-fake-b/fixture-rate429']), {200}, 'synthetic B'))
    check('bifrost_503_fallback', lambda: require_status(*post('djmrn-fake-a/fixture-down503',['djmrn-fake-b/fixture-down503']), {200}, 'synthetic B'))
    check('valid_gateway_stream', lambda: require_status(*post('djmrn-fake-b/fixture-ok',stream=True),{200},'[DONE]'))

    # 3. For partial SSE, classify observed outcome, never claim seamless fallback.
    status, body = post('djmrn-fake-a/fixture-no-done',stream=True)
    incomplete = (status != 200 or '[DONE]' not in body)
    print(json.dumps({'probe': 'partial_stream_observed', 'http_status': status, 'has_done_marker': '[DONE]' in body, 'incomplete_or_rejected': incomplete}))
    if not incomplete:
        # A gateway may normalize the stream; correctness would need a deeper chunk trace.
        # Do not label a normalized 200/[DONE] as a tested interruption guarantee.
        print('PARTIAL_STREAM_DIAGNOSTIC: Gateway emitted [DONE]; needs manual semantics review')

    print('DJMRN_P2B_REAL_GATEWAY_CORE_PROBES_PASS: 7, plus 1 diagnostic; NOT a free-quota validation')

if __name__ == '__main__':
    main()
