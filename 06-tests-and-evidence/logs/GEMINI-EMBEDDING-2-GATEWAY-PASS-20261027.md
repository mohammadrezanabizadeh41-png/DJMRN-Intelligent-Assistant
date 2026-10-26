# DJMRN | Model 10: Gemini Embedding 2 — text embedding PASS

Date: 2026-10-27
Evidence class: USER_EXECUTED_WINDOWS_POWERSHELL — full source code and actual printed terminal output provided. Not an assistant-run inference.
Exact model ID: `gemini/gemini-embedding-2`
Existing OmniRoute v3.8.52 Gateway: `http://127.0.0.1:20128/v1/embeddings`

## Actual request

The user entered their existing OmniRoute **Gateway API key** securely with `Read-Host -AsSecureString` (not logged). The following short request was sent to the correct **Embeddings** endpoint, NOT Chat Completions:

```json
{"model":"gemini/gemini-embedding-2","input":"DJMRN embedding connection test"}
```

Request: single small text string; **IMAGE_ATTACHED=False**, no new model registration, no provider/proxy edits, no new local model download, no database changes.

## Verified stdout

```text
MODEL=gemini/gemini-embedding-2
ENDPOINT=/v1/embeddings
IMAGE_ATTACHED=False
HTTP_STATUS=200
SECONDS=0.71
VECTOR_DIMENSIONS=3072
EMBEDDING_TEST=PASS
```

## Evidence-based outcome

- Gateway correctly returned the OpenAI-compatible embedding format `data[0].embedding`, with **3072 numeric-coordinate positions** by the script's array-length check. The script printed no embedding contents, just length.
- VERIFIED: ONE text input => ONE recognized 3072-dimension vector through the current local OmniRoute gateway.
- NOT YET VERIFIED: input normalization/distance behavior, dimensions option, batch throughput, cross-provider compatibility, retrieval precision, mixed modalities, sustained stability, quotas, hard billing prevention, database persistence or search. Model is **not connected to DJMRN Neon/Postgres or any Agno vector store** by this test.
- Keep model family isolated. Embedding 2 and Embedding 001 are separate vector spaces; do not store/mix them in one index and assume cosine-score comparability. If switching existing stored vectors, plan explicit re-embedding and versioned namespace.
- OmniRoute source release v3.8.52 `open-sse/config/embeddingRegistry.ts` has native Gemini embedding model entries; route `/v1/embeddings` is used. Earlier `apiFormat=chat-completions` labels on independently registered Custom embedding entries do not prove Chat endpoint correctness. No metadata correction needed to establish native Gateway success.
- Google official pricing/free-tier and historical account quota snapshots do not constitute zero-charge enforcement; no paid action was authorized.

## Next model (pending user-run result)

Model 11: `gemini/gemini-embedding-001` tested ONCE with small TEXT input via the same `POST /v1/embeddings` route, without image, installation, or modifications. OmniRoute source lists this model as an available Gemini embedding model. Its apparent dimension entry in source is 768; **do not assert output dimensions until observed**, and do not compare vector coordinates to Embedding 2. Capture only `HTTP_STATUS`, `SECONDS`, `VECTOR_DIMENSIONS`, `EMBEDDING_TEST` and sanitized transport class. As usual, only one model at a time.
