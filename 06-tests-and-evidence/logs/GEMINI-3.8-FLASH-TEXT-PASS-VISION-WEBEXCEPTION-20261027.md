# DJMRN OmniRoute — Gemini 3.8 Flash text PASS, vision WebException (2026-10-27)

**Source:** Actual Windows PowerShell script and terminal output shared by user. Only this model was tested in this execution; no new Custom model or provider was installed.

## Scope
- Existing Gemini model route: `gemini/gemini-3.8-flash`, OmniRoute v3.8.52, loopback Gateway `http://127.0.0.1:20128/v1/chat/completions`.
- Authentication: existing Gateway API key entered via SecureString; no key contents shared.
- Request type: OpenAI-compatible chat completions, `stream=false`, `max_tokens=512`.

## Verified results
1. **Text PASS:** `HTTP_STATUS=200`, `SECONDS=3.91`, `RESPONSE=READY`, `TEXT_TEST=PASS` for `Reply with exactly READY.`.
2. **Vision image preflight PASS:** public Wikimedia Commons cat JPEG downloaded, 279603 bytes, JPEG header validated, sent as inline `data:image/jpeg;base64,...` in `messages[].content[].image_url.url`, CAT/OTHER request.
3. **Vision NOT VERIFIED:** `FAILED_STAGE=VISION`; `HTTP_STATUS=UNKNOWN`; `ERROR_REASON=WebException`; `MODEL_STATUS=NOT_FULLY_VERIFIED`. Existing script did not print WebException.Status, inner exception, elapsed time at failure, or actual HTTP error body, so this is **not evidence of any particular Google HTTP status**. No valid Vision response was observed.

## Interpretive constraints
- The Gateway's successful text result cannot establish the Vision route is operational. Unknown status may mean timeout, connection interruption, other transport failure, or issue not surfaced by the existing script. **Root cause unknown.**
- Prior five models individually passed minimal text and inline-JPEG Vision: Gemma 4 26B A4B, Gemma 4 31B, Gemini 3.5 Flash-Lite, Gemini 3.6 Flash, Gemini 3.1 Flash-Lite.
- No proof of long-term stability, arbitrary image formats, zero billing, model quality, Combo / Agno group readiness, or paid-feature restrictions.

## Next diagnostic
- Before another inference call, retrieve read-only latest matching OmniRoute management call logs for `gemini-3.8-flash`; print only sanitized timestamps, statuses, durations and error classes. Inspect whether the previous vision attempt was logged and whether Gateway saw any HTTP upstream status.
- If logs insufficient, conduct just **one** retry on same model with controlled deadline and a catch printing `WebException.Status`, safe inner-exception type, elapsed seconds and sanitized upstream HTTP status; do not disclose keys, raw image Base64 or full private logs.
- Keep model under `TEXT_PASS; VISION_PENDING_DIAGNOSIS` and do not advance to another model until chosen. No provider, model, proxy, settings, billing or credentials should be modified speculatively.

Record is a factual receipt of the user's terminal output; NO fresh local inference was executed by GitHub logging.

## FOLLOWUP-CALL-LOGS-20261027: management call-log evidence supplied by user (read-only)

Authenticated `GET /api/usage/call-logs?model=gemini-3.8-flash&limit=12` on local OmniRoute returned `LOG_MATCHES=5` and `DIAGNOSIS=LOG_READ_COMPLETE`. The user did NOT make any new inference call in this diagnostics step.

| Timestamp UTC | Provider/model | Status | Duration ms | Sanitized error |
| --- | --- | ---: | ---: | --- |
| 2026-10-26T22:40:57.225Z | gemini / gemini-3.8-flash | 499 | 87248 | Request aborted |
| 2026-10-26T22:39:26.998Z | gemini / gemini-3.8-flash | 502 | 59783 | [502]: Proxy request failed: fetch failed (cause ECONNRESET) |
| 2026-10-26T22:38:26.210Z | gemini / gemini-3.8-flash | 200 | 3837 | none |
| 2026-10-26T22:37:30.258Z | gemini / gemini-3.8-flash | 499 | 144784 | Request aborted |
| 2026-10-26T22:35:03.395Z | gemini / gemini-3.8-flash | 503 | 3176 | [503]: This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later. |

**Diagnostic synthesis:** This is affirmative evidence of (a) upstream Google model congestion on at least one prior attempt (HTTP 503), (b) one failed proxy transport connection (HTTP 502, ECONNRESET), (c) aborted requests (499), and (d) a successful request (200; consistent with previous text PASS). This does **not** prove which individual error was responsible for the current image attempt because the log list lacks request modality and correlation ID in the shared sanitized output. In particular, 499 does not establish that the model explicitly rejected image input; `HTTP_STATUS=UNKNOWN` in the user's client refers to no HTTP response exposed by that client catch.

**Next user-run action (PENDING):** Before sending another vision inference, perform a read-only TCP listening check of the currently configured local proxy if reachable; then perform at most ONE follow-up Vision retry for this exact model with the same previously accepted JPEG inline Base64 format. Capture elapsed time, `WebException.Status`, nested socket error class, actual HTTP status when present, and a redacted error class. Do not print API credentials, request body, Base64 image, or full raw logs. On success mark `VISION_PASS`; on repeat transport failure classify `VISION_UNVERIFIED / NETWORK_OR_UPSTREAM_UNSTABLE`, avoid repeated calls or broad proxy changes. No other model is to be tested until continued user direction.

This record documents user-observed outputs only; neither a configuration change nor an actual retry occurred during recording.

## VISION-RETEST-TIMEOUT-110S-USER-TEXT-ONLY-20261027: retry of same JPEG timed out, user requests no more images

**User-supplied real Windows PowerShell terminal output on Oct 27, 2026:** One retry of inline JPEG Vision for the **same** `gemini/gemini-3.8-flash` model, with `-TimeoutSec 110`. Local previous HTTP proxy listener at `127.0.0.1:20809` was up: `PREVIOUS_PROXY_PORT_LISTENING=True`. Download succeeded: `IMAGE_BYTES=279603`. The POST to OmniRoute Gateway did **not** expose an HTTP response: `FAILED_STAGE=VISION`, `HTTP_STATUS=NO_HTTP_RESPONSE`, `WEB_EXCEPTION_STATUS=Timeout`, `SOCKET_ERROR=NONE`, `ERROR_TYPE=WebException`, `ERROR_REASON=NO_STRUCTURED_ERROR`, `SECONDS=110.02`, `VISION_TEST=FAILED`.

**Assessment:** Actual client request deadline expired after 110.02 sec. No direct evidence in this output that Google returned a model-capability rejection or any particular HTTP response. Proxy TCP port LISTENING is not proof of healthy upstream proxy end-to-end. Prior local model logs showed HTTP 499 aborted, 502 proxy ECONNRESET, and 503 high-demand, all preserved above. **Vision remains UNVERIFIED.** Prior text test **PASS**: `HTTP_STATUS=200`, `SECONDS=3.91`, `RESPONSE=READY`.

**User's explicit instruction now:** `بدون عکس امتحان کن` ("test without image"). Therefore **do not retry or send any images**. Provide a single small **text-only** PowerShell Gateway test of `gemini/gemini-3.8-flash`, input one short text message and no image, using privately entered Gateway API key; timeout <= 40 sec and print actual status/time/answer safely. A new text result has **not** yet been supplied. Do not declare Vision operational, do not change the working proxy, and do not switch to another model automatically.


## TEXT-ONLY-RETEST-TIMEOUT-40S-20261027: second text-only run also timed out

**Verified user terminal result:** A new **text-only** Gateway request targeting `gemini/gemini-3.8-flash`, no image attached (`IMAGE_ATTACHED=False`), body with `Reply with exactly READY.`, `max_tokens=128`, `stream=false`, and `-TimeoutSec 40` failed without an HTTP response.
- `HTTP_STATUS=NO_HTTP_RESPONSE`
- `NETWORK_STATUS=Timeout`
- `ERROR_TYPE=WebException`
- `SECONDS=40.05`
- `TEXT_TEST=FAILED`

**Cumulative state:** The first text-only run of this model returned HTTP 200 with `READY` in 3.91 seconds. This later text-only timeout, alongside the previous 110.02-second Vision timeout and management logs with 499 aborted, 502 proxy ECONNRESET and 503 Google high demand, demonstrates unstable or unavailable inference service through the current route. **Do not mark the model reliably operational for agents**. This user test did not obtain a Google HTTP response or diagnose the definitive root cause, and no settings were changed.

**DJMRN operational disposition:** `gemini/gemini-3.8-flash` = `TEXT_EVER_PASS / CURRENT_TEXT_TIMEOUT / VISION_NOT_VERIFIED / DEFERRED_UNSTABLE_ROUTE`; exclude from automatic routing / Combo until a later evidence-backed controlled retest. Keep five other previously validated routes unchanged. Do not run repeated 3.8 Flash calls or new image trials now. If resuming troubleshooting later, first check local connection-scoped proxy, fresh per-call logs and upstream status; compare direct official API vs Gateway on the *same model* only when useful and within free-use constraints. Record any new evidence before promoting.

**Scope:** Recording a new result in GitHub; no direct user-system access, provider/key/model changes, paid plans, downloads, or deployments.


## NEXT-PLAN-GEMINI-2.5-FLASH-LITE-TEXT-ONLY-20261027: next admission candidate (not yet tested)
- Gemini 3.8 Flash is **deferred** for unstable Gateway response, not deleted. Existing five working text+inline-JPEG models retain prior smoke-test PASS statuses; no model groups updated.
- Next one-by-one model proposed: `gemini/gemini-2.5-flash-lite`, **already in the OmniRoute built-in Gemini provider registry** (`cheaper-inference/OmniRoute`, release v3.8.52); no duplicate Custom installation. User's prior Google AI Studio Free Tier screenshot recorded 10 RPM / 250K input TPM / 20 RPD for Gemini 2.5 Flash Lite, which is an old account observation, not an account-level billing gate.
- Google model documentation checked 2026-10-27: `https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite` validates the exact ID, supports text+image input, and warns that the 2.5 models are now restricted to projects with historical usage; access for this user's project must be empirically verified. Google free-tier Standard text usage is listed on `https://ai.google.dev/gemini-api/docs/pricing`, but account-specific no-charge protection is unverified.
- **Current user instruction: text-only, no images** in the ongoing testing sequence. Proposed test is a SINGLE small text-only Gateway Chat Completions request for `gemini/gemini-2.5-flash-lite`, max_tokens=128 and client timeout approximately 30–40s. Print real HTTP status, answer, time, network exception class only; do not make further calls automatically and do not record it as PASS prior to user output.
- Do not modify the Gemini connection/proxy, add the model to a Combo, change billing or store credentials. Continue to preserve chronological tests and errors.
