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
