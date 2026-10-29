# DJMRN Groq — Existing Provider Connection Created, Auto-Test Error (2026-10-29)

Status: GROQ_PROXY_RECOVERED / FIVE_UI_GREEN_BUILTINS / TWO_PROMPT_GUARD_DIRECT_HTTP200 / INVENTORY_RECONCILIATION_PENDING
Evidence: Actual full Windows PowerShell execution stdout supplied by the user. No upstream or local test was executed by the assistant.

## Exact observed output (secrets excluded)
```text
MANAGEMENT_API=PASS
EXISTING_GROQ_CONNECTIONS=0
GROQ_API=PASS
MODEL_COUNT=11
GPT_OSS_20B_AVAILABLE=True
REGISTER_HTTP=201
REGISTER_RESULT=CREATED
READBACK=FOUND
CONNECTION_ACTIVE=False
TEST_STATUS=error
```

## Observed inputs and actions
- OmniRoute Desktop v3.8.52 local management endpoint: `http://127.0.0.1:20128/api/providers`.
- Authenticated management `GET /api/providers?provider=groq` returned no prior Groq connection.
- Direct, authenticated upstream `GET https://api.groq.com/openai/v1/models` succeeded on user's Windows PowerShell network (eleven listed models; `openai/gpt-oss-20b` among them). This independently establishes that user's private Groq credential authenticated to the official catalog at that time.
- Management `POST /api/providers` submitted `provider=groq`, `name=DJMRN-Groq-Free`, `defaultModel=openai/gpt-oss-20b`, `priority=1`; returned HTTP 201, and read-back found the record.
- After an observed six-second delay, `isActive=False` and `testStatus=error`. No successful chat/inference response or imported model claim. No second Groq connection should be created.

## Exact-version source audit and interpretation
- `cheaper-inference/OmniRoute` branch `release/v3.8.52` `src/app/api/providers/route.ts`: a newly created connection is initially `isActive:false`. A subsequent background `testSingleConnection` auto-test may activate it on success; HTTP 201 alone is not proof of activation.
- `src/app/api/providers/[id]/test/route.ts` contains the connection test logic and stores status and error diagnostic fields.
- `src/lib/providers/validation.ts` dispatches to OpenAI-style provider validation, which may call the model catalog through its own networking/proxy path. The recorded error does **not** prove an invalid API key, because the same key succeeded against Groq's authenticated catalog directly.
- Distinguish PowerShell's network/proxy path from OmniRoute's Node/Electron provider-specific proxy configuration; error might be different proxies, DNS, timeout, TLS, provider validator behavior, or a non-key failure. Root cause is NOT YET KNOWN.

## Immediate next step (read-only, no inference quota)
Authenticated `GET /api/providers?provider=groq` through local OmniRoute management, select only `name,provider,isActive,testStatus,lastError,lastErrorType,lastErrorSource,errorCode,lastTested,proxyEnabled,perKeyProxyEnabled`. Sanitize any token-like substrings in error string before pasting. Do not echo raw JSON or provider account fields that could include keys. If results still lack diagnostic detail, inspect the provider-specific connection test status/known proxy settings and local logs **without blindly re-running tests**. Check direct Groq API success vs internal OmniRoute proxy separately. Only after identifying issue, repair the existing connection ID, do not POST another account.

## Security/continuity
Groq upstream API key, OmniRoute Management token, Gateway key, and dashboard password are distinct secrets. None are captured in GitHub. No provider upgrades or paid-model admission authorized.

## References
- `06-tests-and-evidence/provider-research/GROQ-FREE-TIER-MODEL-REVIEW-20261029.md`
- `06-tests-and-evidence/provider-research/GROQ-ACCOUNT-AND-MODEL-ONBOARDING-2026-10-26.md`
- `07-operations-and-continuity/CURRENT-STATUS.md` for earlier Gemini's similar UI validation issues.

## Follow-up 2026-10-29 — Windows proxy ON, Groq has no effective resolved proxy

**Actual user Windows PowerShell read-only output:**

```text
WINDOWS_PROXY_ENABLED=1
WINDOWS_PROXY_SERVER=127.0.0.1:20809
GROQ_CONNECTIONS=1
CONNECTION=DJMRN-Groq-Free
ACTIVE=False
TEST_STATUS=active
PROXY_ENABLED=True
RESOLVED_PROXY_TYPE=
RESOLVED_PROXY_HOST=
RESOLVED_PROXY_PORT=
```

**Important correction to previous status:** The connection's `testStatus` changed from `error` to `active`, while `isActive` remained `False`. These are distinct fields. The effective proxy GET `GET /api/settings/proxy?resolve=<connectionId>` yielded no proxy type/host/port with the user's extraction script. Exact OmniRoute v3.8.52 route implementation returns a top-level `proxy` field, so the result supports `NO_EFFECTIVE_CONNECTION_PROXY`. It does not prove the validator must fail, or that the upstream key is invalid.

**Close historical comparison:** `07-operations-and-continuity/CURRENT-STATUS.md`, section `OMNIROUTE-GEMINI-403-HTML-PROXY-RECOVERY-20261027`, records that the existing Gemini connection had `proxyEnabled=True` but no resolved proxy. Its connection-only `PUT /api/settings/proxy` assignment with `level=key` and the then-active Windows HTTP proxy `127.0.0.1:20809` followed by a gateway HTTP 200 fixed Gemini chat. This is corroborating history, not proof the same fix will cure Groq.

**Next plan, not yet executed:** First check proxy listener and whether the Groq connection carries an explicit operator-disable marker. Only if safe, assign the observed HTTP proxy to the **existing Groq connection ID only** by management `PUT /api/settings/proxy` with `{level:"key",id:existingId,proxy:{type:"http",host:"127.0.0.1",port:20809}}`, then GET resolved proxy and one `POST /api/providers/<id>/test`. Log true status and `isActive` read-back. Do not touch Gemini, global proxy, account credentials or billing; do not create a second Groq connection.

**User-visible action pending.** No management writes, inference tests or gateway activation have been observed for Groq during this note.

## Verified recovery (2026-10-29): connection-level proxy and successful credential check

**Evidence:** User-supplied Windows PowerShell stdout from the previously proposed bounded recovery script; not remotely executed by this assistant:

```text
ACCOUNT=DJMRN-Groq-Free
INITIAL_ACTIVE=False
INITIAL_TEST_STATUS=active
PROXY_TCP=True
PROXY_ASSIGNMENT=SUBMITTED
PROXY_LEVEL=key
PROXY_TYPE=http
PROXY_HOST=127.0.0.1
PROXY_PORT=20809
CONNECTION_TEST_VALID=True
CONNECTION_TEST_HTTP=
CONNECTION_TEST_MS=441
DIAGNOSIS_TYPE=ok
FINAL_ACTIVE=True
FINAL_TEST_STATUS=active
FINAL_ERROR_TYPE=
FINAL_ERROR_CODE=
RESULT=GROQ_CONNECTION_ACTIVE
```

**Technical conclusion:** The existing Groq account connection has now been configured with a *key/connection-scoped* HTTP proxy `127.0.0.1:20809`, the effective settings read back correctly, an explicit OmniRoute management connection test returned `valid=True` in 441 ms with diagnosis `ok`, and the subsequent provider GET confirmed `isActive=True`, `testStatus=active`, and no final error type/code. This recovers the account credential-validation/activation stage. The exact cached auto-test failure root cause was not conclusively identified, but proxy-path mismatch is supported by analogous Gemini incident and successful post-change probe. No HTTP status was printed for the connection test itself (`CONNECTION_TEST_HTTP=`); **do not invent 200** from an empty field.

**Important separation:** Groq authenticated direct API catalog `GET /models` and OmniRoute's now successful credential test do **NOT** prove a routed chat completion worked, model-level output, token limits, 429 handling, Combo failover or free-only safety. The next planned single model is existing Free-account candidate `openai/gpt-oss-20b` sent as `groq/openai/gpt-oss-20b` through the local OmniRoute **Gateway** (not Groq upstream, and not Management API). Model prefix from `cheaper-inference/OmniRoute` `release/v3.8.52` provider registry: `open-sse/config/providers/registry/groq/index.ts` declares `id:"groq"` and `models:[{id:"openai/gpt-oss-20b"}]`. Gateway route must be verified by actual user test. Ask for privately entered **OmniRoute Gateway API Key**, not Groq upstream key and not Management token. Use one minimal non-streaming text request and record actual status, safe answer and seconds only.

**Affected scope:** only existing Groq connection proxy assignment and one validation probe. Gemini accounts, provider credentials, other Combos, Windows proxy, global proxy, API keys, billing and user-installed software unchanged. This is a verified user-run recovery, not an assistant-executed local action.

**Next:** One bounded real Groq GPT-OSS 20B Gateway smoke test. If fails, diagnose exact sanitized status rather than adding another Groq account or flipping activation by hand.

## 2026-10-29 — User-completed OmniRoute model checks: five green model cards

**New screenshot and user statement:** From Groq provider page in OmniRoute Desktop v3.8.52, user confirms they have just tested the following FIVE BUILT-IN models and each card shows a green checkmark: `groq/allam-2-7b`, `groq/openai/gpt-oss-120b`, `groq/openai/gpt-oss-20b`, `groq/qwen/qwen3.8-27b`, `groq/openai/gpt-oss-safeguard-20b`. User calls all five `connected/tested`. **Evidence class:** USER-REPORTED_TESTED + GREEN_UI_INDICATOR. No raw HTTP status, model reply content, exact test modality, structured-output quality or screenshots of usage were supplied; therefore do not misclassify as captured text/vision Gateway HTTP 200 or screenshot recognition PASS. These are **not Custom models** and must not be duplicated.

**Other previously displayed Built-ins**: `groq/groq/compound` and `groq/qwen/qwen3.6-27b` were present in seven-item default OmniRoute catalog, but Groq official deprecations list shutdowns 2026-09-21 and 2026-09-14 respectively; exclude from active future Combos, despite lingering catalog cards. Official source https://console.groq.com/docs/deprecations .

**Free text quota reconciliation**: official Groq https://console.groq.com/docs/rate-limits lists four existing general/specialist Groq models `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `qwen/qwen3.8-27b`, `openai/gpt-oss-safeguard-20b`, and two missing free-rate-limit rows: `meta-llama/llama-prompt-guard-2-22m`, `meta-llama/llama-prompt-guard-2-86m`, both 30 RPM / 14400 RPD / 15000 TPM / 500000 TPD. Also account's earlier screenshot had `allam-2-7b` at 30 RPM / 7000 RPD / 6000 TPM / 500000 TPD and user currently has a green indicator for ALLaM; no official current aggregate free-tier row, so maintain as USER-TESTED/CURRENT-FREE-QUOTA-UNVERIFIED.

**Decision:** Add ONLY missing two Prompt Guard models as Groq Custom model metadata if absent, not as separate provider connections. Exact upstream Model IDs `meta-llama/llama-prompt-guard-2-22m` and `meta-llama/llama-prompt-guard-2-86m`. Suggested OmniRoute fields: `API Format=Chat Completions`, `Supported endpoints=Chat`, `Target Format=Default (auto)`, `Vision capable=OFF`, `FREE metadata=ON` only if Free organization Limits still shows them. No extra Groq key; current key-scoped proxy `127.0.0.1:20809` must be preserved. Groq supports them via OpenAI chat completions, but their task is prompt-attack classification, NOT ordinary multi-turn chat or visual document understanding; context 512 tokens per official catalog. Do not add to general fallback Combo until purpose-specific Gateway classification smoke proves them useful.

**Next screenshot requested:** The "Custom Models" add form under existing Groq provider, one new model at a time. Creation not yet confirmed; new models are RECOMMENDED, NOT CREATED. If importing `/models` rather than manual Custom creation, first review whole catalog because it includes specialty audio and varying free eligibility; do not blindly import all or enable paid routes.

**Later nontext modalities** (not part of "all text models"): Whisper V3/Turbo speech-to-text; Orpheus English/Arabic audio-speech. These require correct specialized endpoint and separate free/gateway tests; do not force Chat Completions Custom.

**Free pricing disclaimer:** UI "Free" badge is metadata and official model catalog's Developer pricing is not Free plan billing. Confirm per-account Free tier, no unexpected paid use; no use of model merely because a catalog row exists.

## 2026-10-29 — User reports BOTH Prompt Guard 2 variants BLOCKED

- User reports both `meta-llama/llama-prompt-guard-2-22m` and `meta-llama/llama-prompt-guard-2-86m` are **blocked** in their current setup. Evidence level: USER-REPORTED BLOCKED. No exact HTTP code, Groq upstream error, screenshot of block reason, or model creation receipt was included in this statement. Do not infer geographical denial or a provider-wide shutdown.
- **Correction to earlier provisional onboarding recommendation:** Groq's public docs still list these two model IDs as preview/content-moderation and the rate-limit table lists nominal Free request budgets. Public catalog presence or rate-limit rows **do not establish user-specific entitlement/access**. Treat both as **NOT USABLE / BLOCKED IN USER ENVIRONMENT** pending explicit contrary evidence, and **exclude them from activation, general chat Combos, or automated fallback**. Do not advise re-creating Custom entries or repeated tests as a prerequisite for proceeding.
- Five previously screenshot-green built-ins remain the available user-tested inventory: `groq/allam-2-7b`, `groq/openai/gpt-oss-120b`, `groq/openai/gpt-oss-20b`, `groq/qwen/qwen3.8-27b`, and `groq/openai/gpt-oss-safeguard-20b`. Their green UI indicators are not a benchmark of text, vision or structured extraction.
- If diagnostic access is later desired, check one existing sanitized error log and `GET /models` membership, without multiple speculative retries; proceed with already working models now.
- Sources (public docs): https://console.groq.com/docs/models ; https://console.groq.com/docs/rate-limits ; https://console.groq.com/docs/content-moderation .

## 2026-10-29 — Decisive correction: both Prompt Guard models DIRECT-GROQ HTTP 200

**New actual user PowerShell stdout** from direct upstream requests to `https://api.groq.com/openai/v1` with their own private Groq API key via local HTTP proxy `127.0.0.1:20809`, bypassing OmniRoute:

```text
CATALOG=PASS
MODEL_COUNT=11
CATALOG_HAS[meta-llama/llama-prompt-guard-2-22m]=True
CATALOG_HAS[meta-llama/llama-prompt-guard-2-86m]=True
MODEL=meta-llama/llama-prompt-guard-2-22m
HTTP_STATUS=200
SECONDS=0.45
RESPONSE=0.9990056157112122
DIRECT_TEST=PASS
MODEL=meta-llama/llama-prompt-guard-2-86m
HTTP_STATUS=200
SECONDS=0.48
RESPONSE=0.9995385408401489
DIRECT_TEST=PASS
```

**Correction:** This overrides the preceding USER-REPORTED BLOCKED status **for upstream Groq access**. The two Prompt Guard models are directly accessible to the tested key and returned valid classification scores to a short injected-instruction test (values near 1, not normal chat text). **Their actual routing through OmniRoute remains unverified / prior UI block discrepancy unresolved**. Do not mark blocked at Groq; do not conflate `model text reply` with probability-classifier output. No new model metadata creation was reported.

**User's next goal:** obtain the exact live 11-row upstream model list again and compare with current OmniRoute native + Custom inventory and documented Groq Free base RPD/RPM/TPM/TPD; install only actual missing, compatible models without duplicates or paid routing. The Groq public Free table currently lists 10 models (six chat/classifiers and four voice); `allam-2-7b` came from user Oct 26 account Limits screenshot (7000 RPD, 500000 TPD), but current public Free table omits it; account-specific daily cap and continued free entitlement must be independently confirmed in console. Historical 11 model IDs cannot be inferred from just the count, so produce full ID inventory via fresh user-local GET /models.

**OmniRoute v3.8.52 exact native audio-registry source:** `open-sse/config/audioRegistry.ts` already includes `groq/whisper-large-v3` and `groq/whisper-large-v3-turbo` at `/v1/audio/transcriptions`. Audio transcribe is not Chat and does not need duplicate Chat Custom rows. Same audio registry currently has **no Groq TTS `AUDIO_SPEECH_PROVIDERS.groq`**. Orpheus may need a dedicated adapter/compatible provider node rather than an incorrectly typed Chat Custom row. Both are future specialist tests; do not claim operational proof from catalog-only listing.

**Public sources:** https://console.groq.com/docs/rate-limits (Free table of 10 rows), https://console.groq.com/docs/models, https://console.groq.com/docs/deprecations (native built-in `groq/compound` and `qwen/qwen3.6-27b` already retired), https://console.groq.com/docs/speech-to-text, https://console.groq.com/docs/text-to-speech/orpheus.

Next outcome PENDING: user executes one read-only, key-safe PowerShell inventory to print all upstream IDs and identify only missing entries; neither software installation nor model/provider config mutation performed here.

## 2026-10-29 — COMPLETE LIVE GROQ CATALOG reconciled with OmniRoute Custom entries (user PowerShell evidence)

**Command result:**
```text
CATALOG=PASS
LIVE_MODEL_COUNT=11
CUSTOM_MODEL_COUNT=2
LIVE_MODEL=allam-2-7b
LIVE_MODEL=canopylabs/orpheus-arabic-saudi
LIVE_MODEL=canopylabs/orpheus-v1-english
LIVE_MODEL=meta-llama/llama-prompt-guard-2-22m
LIVE_MODEL=meta-llama/llama-prompt-guard-2-86m
LIVE_MODEL=openai/gpt-oss-120b
LIVE_MODEL=openai/gpt-oss-20b
LIVE_MODEL=openai/gpt-oss-safeguard-20b
LIVE_MODEL=qwen/qwen3.8-27b
LIVE_MODEL=whisper-large-v3
LIVE_MODEL=whisper-large-v3-turbo
RESULT=INVENTORY_COMPLETE_READ_ONLY
```

**Per-model comparison from actual script:**
| Model ID | Model modality | User's live account | OmniRoute status | Public free RPD/TPD (nominal) |
|---|---|---|---|---|
| `allam-2-7b` | Chat | TRUE | KEEP_BUILTIN | historic user account limit 7000/500000; currently absent from public Free list, verify |
| `openai/gpt-oss-20b` | Chat | TRUE | KEEP_BUILTIN | 1000/200000 |
| `openai/gpt-oss-120b` | Chat | TRUE | KEEP_BUILTIN | 1000/200000 |
| `qwen/qwen3.8-27b` | Chat + Vision | TRUE | KEEP_BUILTIN | 1000/200000 |
| `openai/gpt-oss-safeguard-20b` | Chat + safety | TRUE | KEEP_BUILTIN | 1000/200000 |
| `meta-llama/llama-prompt-guard-2-22m` | Classifier | TRUE | KEEP_CUSTOM | 14400/500000 |
| `meta-llama/llama-prompt-guard-2-86m` | Classifier | TRUE | KEEP_CUSTOM | 14400/500000 |
| `whisper-large-v3` | Audio transcriptions | TRUE | NATIVE_AUDIO_ROUTE | 2000 RPD / 28800 audio seconds daily |
| `whisper-large-v3-turbo` | Audio transcriptions | TRUE | NATIVE_AUDIO_ROUTE | 2000 RPD / 28800 audio seconds daily |
| `canopylabs/orpheus-v1-english` | Audio speech | TRUE | REVIEW_TTS_ADAPTER | 100/3600 |
| `canopylabs/orpheus-arabic-saudi` | Audio speech | TRUE | REVIEW_TTS_ADAPTER | 100/3600 |

There were **no OTHER LIVE MODELS NOT IN REVIEWED TABLE**, so the authenticated catalog is exhaustively accounted for by these 11 rows. `CUSTOM_MODEL_COUNT=2` plus both Prompt Guard rows marked `KEEP_CUSTOM` confirm they are already registered as Groq Custom metadata. **NO MISSING TEXT/SAFETY Custom models**, and none should be duplicated.

**Crucial capability boundary:** Account's `GET /models` shows upstream availability, not routed model inference or voice endpoint support inside OmniRoute. Native Groq Whisper transcription adapters are present in v3.8.52 `open-sse/config/audioRegistry.ts` but still require a real authorized audio test. Groq Orpheus official endpoint `POST https://api.groq.com/openai/v1/audio/speech` exists (https://console.groq.com/docs/text-to-speech), whereas the same OmniRoute registry does not include `AUDIO_SPEECH_PROVIDERS.groq`, so existing Groq provider's TTS routing is NOT established. Need a dedicated OpenAI-compatible speech provider node or adapter assessment, not Chat Custom or a duplicate Groq API-key provider registration.

**Official public rate limits verified 2026-10-29**: https://console.groq.com/docs/rate-limits (ten Free model rows, ALLaM not in public Free table). `Free Plan Limits` refer organization-wide base limits, not real-time remaining quotas or per-key fresh allowances; no actual authenticated account Limits-page scrape was performed.

**Next operational checkpoints:** (1) one bounded and key-safe Gateways test for both already-existing Custom Prompt Guards (`groq/meta-llama/llama-prompt-guard-2-22m`, `groq/meta-llama/llama-prompt-guard-2-86m`), distinguishing numeric score from ordinary assistant prose; (2) Groq Whisper input-audio transcribe smoke via native audio route, (3) resolve Orpheus TTS compatible adapter and optionally test upstream direct speech. No blind creation of additional models, no family assembly yet. Preserve existing Gemini provider, existing Groq scoped proxy, keys and free-only policy.
