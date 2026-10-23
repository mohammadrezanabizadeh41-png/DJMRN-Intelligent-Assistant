# ROUTER-P002B — Genuine HTTP mock upstream fixture (Bifrost binary pending)
**2026-10-23 | RESULT: 8/8 synthetic loopback HTTP test cases PASS in assistant Linux Python 3.13.5 | REAL BIFROST GATEWAY NOT RUN / BLOCKED-BINARY-ACQUISITION**

These two files are a test **fixture** awaiting the real `maximhq/bifrost` transport v2.3.2 (tag `transports/v2.3.2`, source commit `a05ea20e68bf116a35e9f05b1a3d749624b3935e`). The `ThreadingHTTPServer` mock creates two ephemeral servers bound to **127.0.0.1 only**, exposing `GET /health` and `POST /v1/chat/completions`. Responses are manually scripted to return synthetic 200, 429, 401, 402, 403, 503 and valid/partial SSE. **No real model, provider, key, billing, cloud traffic, Jan, CAP-006 or Windows process.**

### Reproduction (Python 3.11+ standard library only)
```bash
cd 06-tests-and-evidence/pilots/ROUTER-P002B-20261023
python -W error::ResourceWarning -m unittest -v test_fake_upstream.py
```
The successful run reports `Ran 8 tests in 6.533s / OK` on isolated Linux Python 3.13.5. The first draft had a **test-file syntax typo** and did not run; it was corrected **before GitHub source registration**, then all 8 passed without warnings. For hashes/limits, see [receipt](../../logs/ROUTER-P002B-SYNTHETIC-HTTP-AND-BINARY-BLOCKER-20261023.md).

### Critical boundaries
1. Fake HTTP servers ran. **Bifrost did not**. The test's client invokes A and then B explicitly; it does **not** demonstrate automatic Bifrost failover on 429 or 503. A fake header-presence check does **not** validate gateway admin or inference authentication.
2. Successful SSE completion and deliberately truncated response were **produced by the mocks**, not forwarded by Bifrost. The test recognizes missing `data: [DONE]` but did not test actual provider stream recovery, tool schemas, or Bifrost CEL.
3. Mock responses are intentionally permissive for fixture purposes; never expose beyond loopback or treat as real security.
4. No downloads/installs in user's Windows. The isolated container lacked DNS to `downloads.getmaxim.ai`; downloading the exact Bifrost binary and verifying it is the **unresolved P2B execution blocker**. The path from official source is `https://downloads.getmaxim.ai/bifrost/v2.3.2/linux/amd64/bifrost-http`, not a verified signed artifact.
5. **NEXT**: trusted offline/manual delivery of a checksum-attested matching artifact to a fresh isolated execution environment, validate release identity and security startup, run actual Bifrost with mock upstreams and verify authenticated client->Bifrost->A->B requests, model allowlists, CEL, 429 and SSE. This requires additional permitted executable and security setup, and real provider API accounts remain an independently gated P3.

Read [P0 contract](../../../03-architecture-and-tools/DJMRN-CLOUD-ROUTER-P0-REQUEST-POLICY-CONTRACT-20261023.md) and [P1 preflight](../../../03-architecture-and-tools/BIFROST-OSS-WINDOWS-P1-SOURCE-PREFLIGHT-20261023.md) first.
