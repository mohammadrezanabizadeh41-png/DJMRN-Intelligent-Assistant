# ROUTER-P002 — OFF-DEVICE Python SQLite fake-provider policy test receipt (2026-10-23)
**Classification:** INDEPENDENT TEST / ISOLATED ASSISTANT CONTAINER / **16 UNIT TEST METHODS PASS** / REAL MAXIM BIFROST INTEGRATION **NOT RUN** / Windows 11 **NOT RUN** / external LLM APIs **NOT CALLED**.
**User approval context:** After P0/P1 documentation in current conversation and user message "ادامه بده", coordinator advanced narrowly to a **synthetic mock-only** simulation in the isolated assistant Linux container; no software change to user device, no real endpoint/accounts/secrets.
**Canonical project:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, branch `main`; base HEAD before write `50c53e22392e9627db1642867d5a209049c10a1d`; under [P0 contract](../../03-architecture-and-tools/DJMRN-CLOUD-ROUTER-P0-REQUEST-POLICY-CONTRACT-20261023.md), [P1 source audit](../../03-architecture-and-tools/BIFROST-OSS-WINDOWS-P1-SOURCE-PREFLIGHT-20261023.md), D-016 scoped choice.

## Exact audited/committed input
Files in [ROUTER-P002 pilot](../pilots/ROUTER-P002-20261023/README.md):
- `mock_policy.py`: **8,905 bytes**, SHA256 `14eb579cac11af6a8a2a5a1f73d2716c075065200db4008233d6242fffe276a5`, **Git blob `42b9c6257ffff5d18c1ed118c394af8478d30bcc`** — independently fetched from GitHub main and matches exact executed container bytes.
- `test_p2.py`: **7,867 bytes**, SHA256 `49862ca95c62996275014b87102a8d65ea5cb3aa79e819d8a1f988ac4321a143`, **Git blob `b52aa36dfdcd861b887b18d4ce893f7861766941`** — independently fetched from GitHub main and matches exact executed container bytes.
- README: reproducer and negative scope; its GitHub blob must be read at current HEAD, not claimed as original container hash.
**Execution environment:** isolated Linux Python **3.13.5**, Python standard library only (`unittest`, `sqlite3`, `threading`, `concurrent.futures`, `tempfile`), no `pip`, no network/HTTP socket, no Bifrost binary or Windows APIs.
**Exact command:** `python -W error::ResourceWarning -m unittest -v test_p2.py` inside the pilot directory.
**Observed terminal receipt:** `Ran 16 tests in 0.159s\n\nOK` with 16 named `ok` results, no failures/skips, no ResourceWarning after correcting the earlier SQLite connection-close warning. This measures only test duration in this isolated container; it is NOT inference latency/RAM or Windows performance.

## Individual R01–R14 contract observations
| Test | Scenario | Off-device synthetic result |
|---|---|---|
| R01 | lite request, protected strong reasoning account | **PASS**: lite route succeeds; strong account unchanged |
| R02 | standard primary returns fake minute-window 429 | **PASS**: switch to approved standard B; fake cooldown 60 |
| R03 | reasoning primary returns fake day-window 429 | **PASS**: same-tier reasoning B; no lite downgrade |
| R04 | no eligible strong free allowance; paid/trial/lite variants exist | **PASS**: stop `FREE_POOL_EXHAUSTED`, zero fake paid calls |
| R05 | fake 401/403/402; promotion-expired route | **PASS**: rejected failure path, no promotion alternate |
| R06 | two caller identities, a single shared account allowance | **PASS**: one success only; SQLite used=1 and restart readback; race coverage **limited**, threads may not overlap at reserve |
| R07 | tools required but only text model | **PASS**: `NO_COMPATIBLE_FREE_MODEL`, mock tool count 0 |
| R08 | fake partial streamed reply then upstream 503 | **PASS**: `STREAM_INTERRUPTED`, no silently successful replay |
| R09 | untrusted requested client ID / tier fields | **PASS**: fields ignored, caller access policy enforced; **NOT live HTTP authentication test** |
| R10 | classifier returns no class | **PASS**: explicit `CLASSIFIER_UNAVAILABLE`, no provider call |
| R11 | reset requires explicit increasing reset marker and no holds | **PASS**: prior/pending reset rejected; persisted used count; explicit synthetic reset permitted |
| R12 | two models under one provider account | **PASS**: one shared free slot never counted separately per model |
| R13 | fake 503 fallback successful | **PASS**: route metadata only in mock log, no prompt/secret content |
| R14 | free cloud route unavailable, CAP-006 action unapproved | **PASS**: no tool execution in mock; **not a test of real CAP-006 security guard** |
| Extra-01 | protected quota for reasoning on shared account | **PASS**: second lite request refused, reserve preserved |
| Extra-02 | provider cost UNKNOWN | **PASS**: fails closed, no routing |

## IMPORTANT limitations / findings for next phase
- **This is a deterministic simulated POLICY/router library, not Maxim Bifrost**. Provider results are an in-memory `FakeBackend`, not a Bifrost process, HTTP server, SSE stream, MCP or compatible provider transport; calls are not observed on a real Bifrost gateway. No claims about `maximhq/bifrost` actual Windows, auth, virtual keys, CEL, native complexity classification, adapter, retry or reset behavior.
- SQLite `BEGIN IMMEDIATE` gives transaction serialization in this fixture, but production crash recovery/unknown upstream billing/slot reservation TTL, multi-process races, failure after debit, reset, and provider authoritative grants are **NOT PROVEN**. The toy ledger counts fake successful responses, while real 429/error requests can still count toward token/rate limits; must read real response headers and provider terms. `set_account` uses destructive `INSERT OR REPLACE` for test setup and must never be carried over as production quota update. Fake time `100` and synthetic reset `200` are NOT provider reset evidence.
- No verified identity/auth middleware; `client_id` is trusted by construction in unit test. Partial streaming is a fake string, not a real HTTP chunk. Failover model quality, contextual compatibility, tool side-effect dedup, actual private data egress and anti-prompt-injection **NOT PROVEN**.
- User's 8GiB RAM / OS-visible 5.88GiB laptop was never accessed. **No Windows install or rollback needed** from this run. Project local file-access G3B CLOSED.
- **NEXT P2B bounded gate:** IF separately approved, obtain/verify an actual pinned OSS Bifrost binary, configure secure loopback+setup token+authenticated inference, use two synthetic HTTP upstreams, enforce per-tier/price allowlist and test status propagation+fallback+inference auth. Only after actual Bifrost process tests can Bifrost integration be promoted; further provider account/API calls require separate approval.
**Overall verdict:** **ROUTER-P002 MOCK-ONLY 16/16 PASS** / **BIFROST-INTEGRATION NOT_RUN** / **WINDOWS NOT_RUN** / **EXTERNAL PROVIDER NOT_RUN**; D-016 evaluation preference unchanged, D-005 broad system OPEN, no CAP-006/G3B expansion.
