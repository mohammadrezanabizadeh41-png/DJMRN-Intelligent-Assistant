# ROUTER-P002B — real loopback HTTP MOCK tests PASS; actual Bifrost execution BLOCKED
**2026-10-23 | evidence class:** independently executed off-device synthetic HTTP transport mock (not Bifrost). **Status:** MOCK FIXTURES 8/8 PASS; ACTUAL OSS MAXIM BIFROST NOT_RUN/BLOCKED; WINDOWS NOT_RUN; ALL REAL PROVIDERS NOT_RUN.
**User:** "اوکی انجام بدیم" authorized advancing the formerly gated P2B **in isolated execution environment using solely fictitious HTTP providers**. No real service key, bank data, account, license bypass or paid calls.

## Reproducibility and exact assets (identical bytes to executed local files)
- [fake_upstream.py](../pilots/ROUTER-P002B-20261023/fake_upstream.py): 5,324 bytes, SHA256 `2fc3ff9fbf2ad73a113d8871973f2e05848604a40078a17d28d445fba4b4bf6f`, Git blob `5c9b8077abc06458f5a90229bf3ffbd465b1cb45`.
- [test_fake_upstream.py](../pilots/ROUTER-P002B-20261023/test_fake_upstream.py): 3,852 bytes, SHA256 `62ee2729cf0261bc1cee4a6892c7d317a0cd0af6ea596818072ea2c33e1f5660`, Git blob `e221547b31fcf365699c3cc501d48c10fe4ac7ce`.
- Both Git blobs independently fetched from `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` **main**, and exactly matched the tested local bytes.
- Environment: assistant isolated **Linux x86_64, Python 3.13.5**, `http.server.ThreadingHTTPServer`, `urllib.request`, JSON. All fake servers were dynamically bound only to `127.0.0.1`, cleaned up by `shutdown/server_close/join`; no external HTTP requests in tests, no extra packages/install. Command `python -W error::ResourceWarning -m unittest -v test_fake_upstream.py`. Final observed `Ran 8 tests in 6.533s\n\nOK`, no test failures/skips/resource warnings.
- One initial **SyntaxError** from missing parenthesis in `test_05` prevented first draft from running; corrected before GitHub commit. Final 8 tests passed.

## Eight executed fixture scenarios (NOT Bifrost integration)
| ID | Tested actual socket behavior | Observed |
|---|---|---|
| HTTP-01 | Two independent loopback servers and `/health` | PASS; both 200 from distinct ephemeral 127.0.0.1 ports |
| HTTP-02 | A responds HTTP 429 with `Retry-After: 5`; client explicitly requests B | PASS; A 429, B 200 with fake OpenAI ChatCompletion JSON. **The test client, NOT Bifrost, invoked B** |
| HTTP-03 | A replies 401, 402, 403, 503 in scripted sequence | PASS; real HTTP statuses, B untouched |
| HTTP-04 | successful `text/event-stream` with `data: [DONE]` | PASS; valid mock SSE termination |
| HTTP-05 | partial SSE then connection close with no terminal `[DONE]` | PASS; fixture produced missing marker and consumer detected truncation |
| HTTP-06 | synthetic auth header and prompt not stored in mock observation | PASS; only model identifier + boolean auth presence |
| HTTP-07 | invalid route `/v1/invalid` | PASS; HTTP 404 |
| HTTP-08 | missing Authorization request to intentionally permissive fake provider | PASS; observed `auth_present:false`, demonstrating **fake server does not provide gateway authorization** |

## Why actual Bifrost P2B stopped before runtime
- Original planned target: `maximhq/bifrost` public annotated tag `transports/v2.3.2`, source commit `a05ea20e68bf116a35e9f05b1a3d749624b3935e`, official NPX transport binary URL pattern `https://downloads.getmaxim.ai/bifrost/v2.3.2/linux/amd64/bifrost-http`. The release tag metadata has zero GitHub downloadable assets. Code source/release identity was researched in [P1](../../03-architecture-and-tools/BIFROST-OSS-WINDOWS-P1-SOURCE-PREFLIGHT-20261023.md).
- In isolated Linux container, attempts `curl -I -L --max-time 12` for both Linux and Windows transport binaries returned **`curl: (6) Could not resolve host: downloads.getmaxim.ai`, HTTP 000**. Container-based sanctioned download also refused because the source could not be viewed/verified. A web open returned inaccessible/cache miss. Go runtime exists, but Bifrost full source/module dependencies and binary are **not cached**. No unverifiable substitute downloaded/executed, no unsafe unpinned `npx -y latest` attempt.
- **Therefore Bifrost service process never started.** No authenticated proxy test, Bifrost CEL, virtual key, built-in beta complexity, actual 429 failover, model-id translation, interface memory, signed artifact/hash, Windows compatibility or real provider daily allowance was observed.
- The HTTP fixture success IS reusable for the next true Bifrost run but is **not proof** that Bifrost handles 429/stream/auth. Do NOT promote P2B to PASS, and do NOT confuse separate P2A policy 16/16 with P2B integration result.

## Safe continuation when binary acquisition possible
1. With an environment that can reach the vendor's **exact pinned transport v2.3.2** artifact, retrieve over HTTPS, capture SHA256/size/signature/publisher and verify exact architecture and source/release mapping; no blind self-update. If unavailable/opaque -> BLOCKED, no execution.
2. Only in an isolated test namespace, start Bifrost bound to `127.0.0.1` with preplanned setup-token/admin+inference auth, scoped VK/provider/model allowlist and **no real provider secrets**. Never use default publicly exposed unauthenticated dashboard.
3. Run two fixture endpoints above and send real client->Bifrost->A->B requests; verify 429, 503, forbidden 401/402, 200 fallback route metadata, authentication failures, allowed models, CEL routes, partial SSE behavior, shared quota holds and exact failure cases. The next test must be separately recorded as real Bifrost/integration only on actual evidence.
4. No changes to user's Windows laptop or CAP-006/G3B closed safety guard; P3 real free API/model/provider remains independently gated. `D-016` technical preference, `D-005` broader architecture OPEN.
