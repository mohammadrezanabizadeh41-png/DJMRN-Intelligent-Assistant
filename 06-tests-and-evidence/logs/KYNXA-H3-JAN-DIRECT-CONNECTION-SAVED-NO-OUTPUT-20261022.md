# KYNXA H3 — User confirms Jan localhost connection saved but no generated response visible

**Date:** 2026-10-22. **Evidence:** two direct user screenshots (KYNXA v1.7 UI), user says "انجام دادم اما چیزی بالا نیامد". Coordinator has not accessed Jan/KYNXA/Windows.

## User-visible facts
- KYNXA Models > My connections has **one saved connection** named **DJMRN - Jan Local**, shows **Models: 1**, selected provider **Custom service**, Service URL **http://127.0.0.1:1337/v1**, API key shown blank, Context window **32K**, and Saved status. Thus **the connection record and model selection succeeded**; nothing yet proves Jan server is healthy or generated a reply.
- KYNXA main UI is now **Chat** (not Work). The composer selected model **gemma-3-1b-it-qat-Q4_0.gguf** (Jan connection candidate, different from KYNXA internal import-id). Earlier "سلام" appears with **Generation stopped** and no visible text. A second "سلام" is at **Replying... Generating**, elapsed **3 seconds**, without output yet, and has blue Stop button. Screenshot after three seconds alone does not establish an indefinite hang; user report says no output materialized. Expanded usage shows tokens not yet counted and Model calls 10, Complete usage 0, which is not proof of ten completed inference calls.
- Provider label **Custom service**, despite earlier request to select **Local API (direct)**. Both may be OpenAI-compatible if configured correctly; do not assume provider label alone causes failed response. No visible API error code/HTTP status, and server-side Jan logs not provided.
- Earlier KYNXA **native** Gemma3 1B GGUF engine had waited for native resource admission under low RAM; **this current provider is the Jan localhost API** and its failure cannot be attributed to KYNXA's native model resource admission without fresh evidence.

## Independent official documentation grounding
- Current official Jan Local API Server docs https://docs.jan.ai/desktop/api-server : Jan Settings > Local API Server must have Server Status Running; base URL default 127.0.0.1:1337/v1; GET /v1/models lists models; POST /v1/chat/completions performs actual inference; default model must actually load before the server runs; if API key is configured, Authorization: Bearer is required; 401 when missing; 404 for incorrect model ID or API prefix; 127.0.0.1 binds localhost only. Important: **model listing and saving KYNXA connection alone do not prove generation**.
- KYNXA v1.7.0 official tagged ModelPresets https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Services/Models/ModelPresets.cs includes an OpenAI-compatible Custom service and Local API direct provider; current screenshot has Custom service on loopback Jan endpoint.
- Jan API server Execute Tools on Server should remain OFF, no external tools/accounts given.

## Shortest bounded next check; NOT RUN
Perform one user-local, single-shot probe of Jan API *directly* from Windows PowerShell:
1. GET http://127.0.0.1:1337/v1/models read-only, verify server/model list; 401 indicates Jan API key was configured; never paste secret into conversation.
2. If Gemma3 1B listed, POST a **single tiny non-sensitive chat completion** to 127.0.0.1:1337/v1/chat/completions with exactly that returned model id, 12 max tokens, streaming false, timeout ~25s. No tools or files. Return just success text or a redacted error category (HTTP code and type). This is an intentional user-approved local inference test, not a no-side-effect GET; it will load/use model compute. Do not loop or retry automatically.
3. Jan API direct success => KYNXA custom connection/provider integration or UI context is next target if user elects; Jan direct 401/404/connection refused/timeout => fix Jan server/API key/model id or stop experiments. If Jan alone unresponsive, **park KYNXA and go back to main DJMRN** per user preference.

**Current status:** KYNXA external Jan connection SAVED; Chat model selected; generation success NOT_OBSERVED; root cause still unknown. Proposed Jan one-shot smoke NOT_RUN; D-005 stack adoption OPEN; G3B file guard CLOSED. No KYNXA/Windows settings changed by coordinator.
