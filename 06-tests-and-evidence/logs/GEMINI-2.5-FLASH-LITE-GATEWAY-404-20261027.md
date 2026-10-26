# DJMRN — Gemini 2.5 Flash-Lite gateway HTTP 404
Date: 2026-10-27
Verification: REAL USER-RUN PowerShell test. Model 7; text-only; no image.

## Exact execution
- Target existing built-in OmniRoute v3.8.52 Gemini route: `gemini/gemini-2.5-flash-lite`.
- Gateway endpoint: POST `http://127.0.0.1:20128/v1/chat/completions`.
- Body: `messages=[{role:user,content:"Reply with exactly READY."}]`, `max_tokens=128`, `stream=false`.
- User locally supplied existing OmniRoute Gateway API key via SecureString; no credential recorded, no provider/model registration or configuration changes.

## Observed output
```text
MODEL=gemini/gemini-2.5-flash-lite
IMAGE_ATTACHED=False
HTTP_STATUS=404
NETWORK_STATUS=ProtocolError
ERROR_CLASS=UNKNOWN
ERROR_TYPE=WebException
SECONDS=0.67
TEXT_TEST=FAILED
```

## Interpretation and caution
- HTTP 404 is a real error response on the gateway path, as opposed to a client Timeout; however the script did NOT capture upstream body or a detailed internal error classification. The root cause remains UNKNOWN: routing/model ID vs upstream Google availability/permissions cannot be discriminated from this stdout alone.
- Official Google model page https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite confirms exact resource ID `gemini-2.5-flash-lite` but explicitly restricts API access to projects with past usage of 2.5 models; Google considers the model not deprecated. Account-specific eligibility remains UNVERIFIED.
- Official Gemini API error definitions https://ai.google.dev/gemini-api/docs/api-errors classify both `not_found` and `model_not_found` as HTTP 404; the existing client omitted the structured body that would distinguish them. Do NOT claim permanent model retirement, free eligibility, 404 caused by a specific entity, or an auto-fix.
- Previous user project records showed a 2.5 Flash Lite Google AI Studio account rate-limit row (10 RPM / 250K input TPM / 20 RPD), but it is a historical screenshot and DOES NOT prove current model access or guaranteed zero-billing.

## Next one-model diagnostic (NOT YET EXECUTED)
1. Read-only OmniRoute management GET `/api/usage/call-logs?model=gemini-2.5-flash-lite&limit=8`, with private Management Token; print only sanitized error/status/duration. If this shows actionable `model_not_found` or upstream error, preserve it.
2. If needed, privately authenticated **Google direct metadata GET** `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite` (no inference) to inspect exact resource and `supportedGenerationMethods`, understanding metadata access does not guarantee inference eligibility. Do not perform a paid-tier upgrade or repeated generation calls; require user-provided output to record actual results.
3. Keep `MODEL7_TEXT_GATEWAY_404`, `MODEL7_VISION_NOT_TESTED`, `MODEL7_NOT_OPERATIONAL` until verified. Do not alter working shared Gemini connection, proxy, other five working models, model registry or billing. User requested **text only**; do not send images.

Prior model 6 `gemini/gemini-3.8-flash` was deferred for instability after repeated Vision and text Timeouts; historical text PASS is not proof of current reliability. Current 5 stable smoke-tested routes unchanged.


## MODEL7-ACCOUNT-NEW-USER-RESTRICTION-CONFIRMED-20261027: direct upstream error from OmniRoute logs + official docs

**New actual user-run diagnostics:**
- Read-only GET `http://127.0.0.1:20128/api/usage/call-logs?model=gemini-2.5-flash-lite&limit=8` authenticated with privately entered OmniRoute Management Token returned `LOG_MATCHES=6`.
- Most recent relevant row `LOG_STATUS=404`, `LOG_DURATION_MS=541`, `LOG_ERROR=[404]: This model models/gemini-2.5-flash-lite is no longer available to new users. Please update your code to use models/gemini-3.5-flash-lite for the latest features and improvements. We recommend y` — truncated at 200 characters by local script. **Do not reconstruct or invent omitted portion.**
- Three additional shown rows: `LOG_STATUS=403` at `25002`, `562`, `525` ms with `<!DOCTYPE html>` indicators, corresponding to earlier HTML errors; no confident attribution of their exact cause.
- Separately, upstream Google authenticated **metadata GET**, `/v1beta/models/gemini-2.5-flash-lite`: `GOOGLE_HTTP_STATUS=400`, `GOOGLE_ERROR_CLASS=UNKNOWN`, `METADATA_CHECK=FAILED`. Request made no generation call. Structured 400 reason was not exposed.
- Neither of the user's diagnostics changed OmniRoute provider settings, model registration, proxies, billing, Combo, or Gateway credentials. No model generation was done during log/metadata GET.

**Verified interpretation:** In this account/project's observed inference route the specific Google 404 unambiguously says **no longer available to new users**, and recommends migrating to `gemini-3.5-flash-lite` (already independently passed text and inline-JPEG Vision in the same OmniRoute setup). Previous client `HTTP_STATUS=404`, `NETWORK_STATUS=ProtocolError`, `SECONDS=0.67` was thus from a genuine provider-level eligibility rejection surfaced by the gateway; **do not debug the shared Gemini proxy or guess wrong model ID**.

**Do not mislabel globally retired/deprecated:** Google's current official docs `https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite` and `https://ai.google.dev/gemini-api/docs/deprecations`, checked 2026-10-27, explicitly say 2.5 models are **NOT deprecated** and still served for prior active users; `gemini-2.5-flash-lite` has **no shutdown date announced**. The old preview `gemini-2.5-flash-lite-preview-09-2025` *is* shut down and should not be conflated with stable. Upstream provider access to new users is restricted, not universal retirement.

**Operational disposition:** `gemini/gemini-2.5-flash-lite` = `RESTRICTED_FOR_NEW_USERS / CURRENT_ACCOUNT_UNAVAILABLE / NOT_ADMITTED_TO_AGENT_ROUTING`. Preserve catalog/history for reference and possible later eligibility change; do not repeatedly retry, remove working infrastructure, or use in automatic Combos. Suggested substitution is working `gemini/gemini-3.5-flash-lite`. User prefers text-only tests for further onboarding. Specialist models require their own endpoints/adapters, not Chat automatically.

