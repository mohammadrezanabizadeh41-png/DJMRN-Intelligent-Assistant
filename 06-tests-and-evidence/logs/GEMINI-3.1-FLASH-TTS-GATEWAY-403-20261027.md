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
