# DJMRN — Model 11: Gemini Embedding 001 — actual Gateway success

**Date:** 2026-10-27
**Evidence:** User-executed Windows PowerShell script and terminal output, provided directly in chat. No independent assistant inference was performed.
**Model:** `gemini/gemini-embedding-001`
**Gateway:** `POST http://127.0.0.1:20128/v1/embeddings` (OmniRoute v3.8.52), using existing Gateway API key entered privately as a SecureString.

## Exact request and observed result
Request data: `{"model":"gemini/gemini-embedding-001","input":"DJMRN semantic memory connection test"}`. No image or batch inputs, no model installation/configuration changes, no database writes.

```text
MODEL=gemini/gemini-embedding-001
ENDPOINT=/v1/embeddings
IMAGE_ATTACHED=False
HTTP_STATUS=200
SECONDS=0.77
VECTOR_DIMENSIONS=3072
EMBEDDING_TEST=PASS
MODEL_STATUS=TEXT_EMBEDDING_OPERATIONAL
```

**Interpretation:** Gateway responded 200 and the local script found `data[0].embedding` with 3072 elements. This verifies a **single text-to-embedding smoke-test** only; numeric validity/distribution, provider-reported model metadata, embedding accuracy, indexing, persistence, long-term stability, cost and quota enforcement were not tested. Do not claim hard billing-free guarantee.

**Critical architecture observation:** Earlier built-in `embeddingRegistry.ts` release v3.8.52 lists `gemini-embedding-001` with 768 dimensions, but the **actual observed response was 3072**. Preserve this observed discrepancy, do not overwrite the output with registry expectation, and do not silently assume the route is wrong. For future investigation, review response `model` field and adapter settings read-only if exact upstream identity is required.

**Separate family:** Gemini Embedding 2 independently passed on model 10 with HTTP 200, 0.71s, 3072 elements. Equal dimension count does **not** establish semantic-vector compatibility; never mix/migrate cross-model embeddings into one vector index without a versioned re-embedding strategy and testing.

**Next stage:** Two embedding routes have independent initial success. TTS models must use dedicated audio output route `POST /v1/audio/speech`, not Chat nor Embeddings. Before any TTS test, verify exact provider prefix and model ID from matching OmniRoute source/official catalog; test ONE small text-to-audio output, validate audio header and byte count, do not claim TTS working without evidence. Preserve strict free-tier review and no unapproved configuration changes. No Agno Combo, Neon/Postgres data persistence or Google billing changes were made here.


## TTS-ADAPTER-GATE-RESEARCH-20261027 — preparation only, no live TTS call yet

Reviewed OmniRoute source branch `release/v3.8.52` in `cheaper-inference/OmniRoute`:
- `open-sse/config/audioRegistry.ts` registers the native audio **speech** provider ID `google`, credentials bound to existing `gemini` provider, with model `gemini-3.1-flash-tts-preview`.
- `open-sse/handlers/audioSpeech.ts` supports `POST /v1/audio/speech` and dispatches provider format `gemini-tts` to `handleGeminiTtsSpeech`.
- `open-sse/executors/geminiTts.ts` converts upstream Gemini inline PCM to `audio/wav` with a WAV header and uses the requested voice or default `Kore`.
- For this adapter, the exact **speech endpoint model ID** is `google/gemini-3.1-flash-tts-preview`. This is intentional, different from Chat/Embeddings prefix `gemini/` and requires NO second Gemini key or Custom model registration.
- Google's official model page `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview` labels the model as **legacy preview**, recommends newer 3.8 Flash TTS / Flash-Lite TTS for new production workloads. `https://ai.google.dev/gemini-api/docs/pricing` lists Standard Free Tier input/output free for this legacy TTS model; account-specific billing protection NOT independently verified.
- **Old-vs-new schema caution:** Google TTS guide `https://ai.google.dev/gemini-api/docs/speech-generation` documents different 3.8 TTS request structure. OmniRoute legacy `geminiTts.ts` uses generateContent/speechConfig; do NOT assume compatibility with `gemini-3.8-flash-tts` or `gemini-3.8-flash-lite-tts` without a specific schema audit/test.
- Proposed next single small TTS smoke test (user execution PENDING): `POST http://127.0.0.1:20128/v1/audio/speech` with `model=google/gemini-3.1-flash-tts-preview`, tiny English input, `voice=Kore`, existing Gateway API key. Verify HTTP 200 plus actual WAV RIFF/WAVE header and nontrivial byte count; do not mark success until tested. Save generated file locally only at a uniquely named output path and report it to user. No media input from user, no image, no provider changes.
