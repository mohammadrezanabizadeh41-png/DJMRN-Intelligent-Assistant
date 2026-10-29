# DJMRN — OmniRoute Model Baseline and Next-Phase Continuation
Date: 2026-10-29
Status: USER-CONFIRMED BASELINE / BOTH INITIAL COMBOS CREATED IN UI; WEB VISION PROPOSED
Repository: DJMRN-Intelligent-Assistant

## User decision — authoritative for next phase
The user confirms **six chat-capable models already prepared in OmniRoute** and **two operational embedding routes** (eight selected models total). Treat these as the current working inventory, not a request to repeat Google AI Studio onboarding. The sixth chat model, Gemini 3 Flash Preview, is INCLUDED despite having only a text smoke-test; do not silently exclude it because its image route was not tested. The two embedding routes are reserved for a dedicated future semantic retrieval/memory family and need not be used immediately. TTS, robotics and other specialized or failed/deferred models remain OUT OF SCOPE until separately requested.

## Six chat models — exact recorded gateway IDs
| Model route | Recorded evidence (2026-10-27) | Vision qualification |
|---|---|---|
| `gemini/gemma-4-26b-a4b-it` | text and inline JPEG vision PASS, referenced by subsequent receipts | one-off image PASS |
| `gemini/gemma-4-31b-it` | text and inline JPEG vision PASS | one-off image PASS |
| `gemini/gemini-3.5-flash-lite` | text and inline JPEG vision PASS | one-off image PASS |
| `gemini/gemini-3.6-flash` | text and inline JPEG vision PASS | one-off image PASS |
| `gemini/gemini-3.1-flash-lite` | text and inline JPEG vision PASS | one-off image PASS |
| `gemini/gemini-3-flash-preview` | text PASS HTTP 200, 2.11 s | vision NOT TESTED |

The user says all six are already prepared in OmniRoute. On 2026-10-29 a subsequent user screenshot confirms **DJMRN-PM-Standard** Combo exists with PRIORITY strategy, shows three individual model IDs and '+3 more'; the remaining three expected IDs are from user-confirmed baseline, not separately expanded in that screenshot. **Combo inference and failover are not yet tested.** See the later UI receipt linked below. Earlier `DJMRN-Persian-L1` AI Horde Combo is a distinct historical pilot, not the six-model final inventory.

## Two embedding models — exact gateway IDs
| Model route | Endpoint | Recorded smoke evidence |
|---|---|---|
| `gemini/gemini-embedding-2` | `POST /v1/embeddings` | HTTP 200, 0.71s, 3072-dimensional output |
| `gemini/gemini-embedding-001` | `POST /v1/embeddings` | HTTP 200, 0.77s, 3072-dimensional output |

These are two distinct vector spaces; do not combine their vectors in the same index without explicit versioning and re-embedding. **Actually created in OmniRoute UI on 2026-10-29:** `DJMRN-Semantic-Memory` (PRIORITY); screenshot visibly shows both embedding routes with the existing Gemini account. The earlier working name `DJMRN-EMBEDDING-RETRIEVAL` was superseded. Creating/listing a Combo in UI is NOT evidence that `POST /v1/embeddings` with Combo ID works, nor that cross-model fallback can be used with one persisted vector index. Keep the family reserved until a separate acceptance test.

## Next work: role-specific model families and free API expansion
1. Reuse six existing chat models. Evaluate `VISION-BROWSER` using existing five image-tested candidates first; sixth chat model remains eligible for text and may receive one image test only when needed and approved.
2. For web monitoring, use DOM/structured extraction first when sufficient; invoke screenshot vision for visual-only/complex UI; browser actions require a separate authorized controller. A successful CAT/OTHER image smoke test is not proof of UI grounding, OCR accuracy, tool calling or browser control.
3. Compare models on actual task-specific quality, latency, stability, free account quota, function calling/structured output and gateway compatibility before choosing primary/fallback.
4. Keep embedding family prepared as a future plan, without connecting it to a vector DB or claiming semantic search is deployed.
5. Expand API providers one by one, verify official free tier and user-account limits, zero unapproved charges, geographic eligibility, model IDs, actual OmniRoute inference, then record receipts. Do not repeat successful Google onboarding by default.
6. Maintain provider/model/family registry, separate USER-CONFIRMED, SMOKE-VERIFIED, FAMILY-PLANNED and END-TO-END-VERIFIED statuses. No API keys or private credentials in GitHub.

## Evidence references
- `06-tests-and-evidence/logs/GEMINI-3-FLASH-PREVIEW-TEXT-PASS-20261027.md`
- `06-tests-and-evidence/logs/GEMINI-3.1-FLASH-LITE-GATEWAY-VERIFIED-20261027.md`
- `06-tests-and-evidence/logs/GEMINI-3.5-FLASH-LITE-GATEWAY-VERIFIED-20261027.md`
- `06-tests-and-evidence/logs/GEMINI-3.6-FLASH-GATEWAY-VERIFIED-20261027.md`
- `06-tests-and-evidence/logs/GEMMA4-31B-GATEWAY-VERIFIED-20261027.md`
- `06-tests-and-evidence/logs/GEMINI-EMBEDDING-001-GATEWAY-PASS-20261027.md`
- `06-tests-and-evidence/logs/GEMINI-EMBEDDING-2-GATEWAY-PASS-20261027.md`
- `06-tests-and-evidence/logs/GEMINI-3.8-FLASH-TEXT-PASS-VISION-WEBEXCEPTION-20261027.md` (deferred, NOT among selected six)
- `07-operations-and-continuity/CURRENT-STATUS.md` (historical evidence; not overwritten)

## Change boundaries
Documentation only. No local OmniRoute settings, Combo, model/provider, API key, AGNT integration, database or billing changes were performed by this commit.
## 2026-10-29 continuity update — source-of-truth cross-references

- **User-created OmniRoute UI Combos:** `DJMRN-PM-Standard` (six chat models by user report; screenshot shows three names and +3 more) and `DJMRN-Semantic-Memory` (both embedding models individually visible), both with PRIORITY badges and apparently ON toggles. See [`DJMRN-OMNIROUTE-TWO-COMBOS-UI-CONFIRMED-20261029.md`](./DJMRN-OMNIROUTE-TWO-COMBOS-UI-CONFIRMED-20261029.md). No claim that endpoints via Combo have been smoke-tested.
- **Next family planned but NOT yet created:** `DJMRN-Web-Vision` with five locally image-tested models, initial priority suggestion `gemini-3.6-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemma-4-26b-a4b-it`, `gemma-4-31b-it`; the sixth selected chat route `gemini-3-flash-preview` remains PM-Standard-only for now until local image test. See [`DJMRN-WEB-SEARCH-VISION-COMBO-RESEARCH-AND-SETUP-20261029.md`](./DJMRN-WEB-SEARCH-VISION-COMBO-RESEARCH-AND-SETUP-20261029.md).
- Existing Combo membership is **reused, not moved**; do not delete original models or provider credentials. All five models use the same Gemini provider account, so failures can correlate and quotas are not independent.
