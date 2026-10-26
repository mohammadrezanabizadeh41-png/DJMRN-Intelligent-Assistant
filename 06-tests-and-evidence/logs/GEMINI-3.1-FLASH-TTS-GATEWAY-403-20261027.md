# DJMRN Model 12 — Gemini 3.1 Flash TTS initial speech test FAILED HTTP 403

Date: 2026-10-27. Evidence: original Windows PowerShell code and actual console output provided by the user; no assistant inference run.

## Request
- Existing OmniRoute local Gateway: POST `http://127.0.0.1:20128/v1/audio/speech`.
- Requested TTS model: `google/gemini-3.1-flash-tts-preview`.
- Text input: `Hello from DJMRN. This is a short audio connection test.`
- Voice: `Kore`.
- Existing OmniRoute **Gateway API key** entered privately using SecureString; no secret printed or stored.
- PowerShell output target: `$env:USERPROFILE/Downloads/DJMRN-TTS31-<random GUID>.wav`, or TEMP if Downloads missing. Exact path was *not* printed because request failed before successful output.

## Observed terminal output
```text
MODEL=google/gemini-3.1-flash-tts-preview
ENDPOINT=/v1/audio/speech
INPUT_TYPE=TEXT
OUTPUT_TYPE=AUDIO
HTTP_STATUS=403
NETWORK_STATUS=ProtocolError
ERROR_TYPE=WebException
SECONDS=0.56
TTS_TEST=FAILED
```

## Outcome
- TTS generation **NOT VERIFIED**, no playable WAV retained. The PowerShell `finally` block deletes `$file` when `$success` remains false (which it did), including any possible incomplete download.
- An HTTP 403 occurred, but the script did not expose the error body. Cannot reliably conclude whether denied by OmniRoute speech routing, upstream Google account/preview-model eligibility, or network proxy HTML error. The route remains TTS_UNVERIFIED / HTTP_403.
- No provider, model, voice, proxy, authentication, quota, registry, billing, Agno, or database configuration was changed in this test.
- Next useful step (not yet executed): use existing OmniRoute Management Token for read-only call-log lookup of the 3.1 Flash TTS preview model (or recent logs if model filter not captured); print sanitized HTTP/status/provider/error. Do not retry TTS inference until reason examined. Existing working Chat/Embedding routes unaffected. Do not claim the 403 produced an audio file.


## AUDIO-403-SOURCE-AUDIT-NETWORK-DIAGNOSTIC-PLAN-20261027 — read-only upstream adapter audit, NOT a completed diagnostic

Inspected source in `cheaper-inference/OmniRoute` branch `release/v3.8.52`:
- `open-sse/config/audioRegistry.ts`: the `AUDIO_SPEECH_PROVIDERS.google` record uses `credentialProviderId: "gemini"`, `format: "gemini-tts"`, Google models API base URL, and includes exact model `gemini-3.1-flash-tts-preview`; hence `google/gemini-3.1-flash-tts-preview` is the source-defined audio route.
- `open-sse/handlers/audioSpeech.ts`: `handleSpeech` dispatches `gemini-tts` to `handleGeminiTtsSpeech` and checks existing credentials.
- `open-sse/executors/geminiTts.ts`: native `fetch("https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent")` with `x-goog-api-key`, JSON `responseModalities:["AUDIO"]` and configured voice. **No explicit per-provider proxy configuration is passed to the fetch in this executor.** This alone does NOT prove that global/OS-level proxies are unused.
- `open-sse/utils/audioResponse.ts`: non-JSON upstream error body is masked as `Upstream error (status)` in client output. Therefore old `HTTP 403` without body cannot distinguish provider access restriction vs proxy HTML/403.
- Proposed **read-only** diagnostic: inspect call-log entries (may be absent for speech; no absence-based conclusion), then compare official Google model metadata GET with existing Gemini API key on default network route versus explicit HTTP proxy `127.0.0.1:20809`; print status/response type/structural error class only, never key, raw HTML or response body. GET metadata does not perform TTS inference. The source audits and call-log evidence are compatible with a network discrepancy but NO cause has been established. User run/results pending.
- No edits of OmniRoute, provider connections, proxies, billing, agent model groups, or API secrets authorized by this plan.
