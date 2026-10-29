# DJMRN Groq — Existing Provider Connection Created, Auto-Test Error (2026-10-29)

Status: PROVIDER_CONNECTION_CREATED_IN_OMNIROUTE / AUTO_TEST_ERROR / INACTIVE
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
