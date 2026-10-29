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

## 2026-10-30 — Cross-provider operational model roster: OpenRouter Nemotron Ultra added

**Operator update:** User explicitly confirmed the new OpenRouter model has been **activated and made operational in the installed OmniRoute UI**. Add this to the *same saved working-model inventory* alongside the eight Gemini baseline models above and the existing six-model Groq validation tracker. This is a roster/documentation update only; no local application mutation or API call was performed by the GitHub assistant.

### Existing operational-model evidence, unchanged

| Provider | Confirmed prepared / tested inventory | Best verified level | Source of truth |
|---|---:|---|---|
| Gemini | 6 chat models + 2 embeddings = **8** | Individual Gemini Gateway tests recorded in this document and linked test receipts; individual modality qualifications vary | Six chat and two embedding tables **above** |
| Groq | **6** (five built-in cards UI-green, one Prompt Guard 22M real Gateway PASS) | UI-green for five, actual Gateway completion for Prompt Guard 22M; modality-specific testing still pending for other entries | [Groq validation tracker](DJMRN-GROQ-MODEL-VALIDATION-TRACKER.md) |

### Newly added — OpenRouter operational model #1

| Field | Verified / recorded value |
|---|---|
| Provider | `OpenRouter` (existing connected provider, **do not create duplicate**) |
| Upstream model ID | `nvidia/nemotron-3-ultra-550b-a55b:free` |
| Full OmniRoute card / route ID | `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` |
| Intended role | **Advanced / heavy reasoning**, architecture analysis and difficult multi-step tasks (proposed use; not quality-benchmarked) |
| User-reported operational state | **ACTIVE AND OPERATIONAL — USER CONFIRMED** (2026-10-30) |
| UI evidence | Screenshot: **1/1 active**, **CUSTOM**, **chat**, **Manual**, **Free**, and green check indicator |
| Live direct OpenRouter inference | **PASS**, HTTP 200, model returned correctly, 17 × 23 = **391**, finish_reason `stop` |
| OmniRoute provider connection | **PASS**, management `valid=True`, `diagnosis.type=ok` after key-scoped HTTP proxy `127.0.0.1:20809` |
| End-to-end OmniRoute Gateway inference | **Not independently evidenced by a user-posted Gateway completion receipt**; do not claim an observed Gateway HTTP 200 solely from UI operational confirmation |
| Account free inventory | 16 observed `:free` zero-price variants of 420 catalog models at audit time; **50 shared free requests/day**, remaining 50 at inventory time, not 50 per model |
| Cost guard | Must retain exact suffix `:free`; UI **Free** badge is metadata, not a payment/billing block |
| Combo/family membership | **Not yet independently confirmed**; don't silently add it to `DJMRN-PM-Standard` or any Combo |

**Operational roster accounting (evidence-labeled):** existing 8 user-confirmed Gemini baseline + 6 Groq tracker-confirmed test entries + **1 new user-confirmed active OpenRouter model** = **15 entries in the cross-provider working/validated inventory**. This is *not* 15 independent accounts, 15 equivalent chat LLMs or 15 end-to-end tested Combo routes. Specialist classifier, embeddings and modality differences remain clearly distinguished.

**Persistence/provenance:** direct OpenRouter API receipt, screenshot UI card and connection recovery are also documented under the 2026-10-30 OpenRouter Nemotron Ultra heading in [CURRENT-STATUS.md](../CURRENT-STATUS.md). Continue updating **this existing roster** instead of creating a parallel operational-model list. Do not alter Gemini/Groq historical statuses or report a Gateway call not observed.


## 2026-10-30 — Mistral Ministral 3 14B added to operational roster

**User-requested update to the established cross-provider working-model inventory.** The user reported that the newly registered Custom model `mistral/ministral-14b-2512` **passed the model test in OmniRoute** (`اوکی بود`). The preceding Mistral built-in `mistral/mistral-small-latest` and subsequent Custom `mistral/mistral-small-2603` had **failed/been reported blocked**; do not count them as operational. No claim is made about their underlying root causes.

| Field | State and evidence |
|---|---|
| Provider | Mistral, using the existing user-created Mistral account/connection (do not duplicate) |
| Upstream model ID | `ministral-14b-2512` |
| OmniRoute full model route | `mistral/ministral-14b-2512` |
| Format | Custom model; Chat Completions / Default (auto); Chat; Vision-capable proposed (vision has **not** been individually tested); Free badge OFF |
| Status | **OPERATIONAL UI TEST PASS — USER CONFIRMED**, 2026-10-30 |
| Intended usage | DJMRN Opportunity Hunter: analyzing job listings, assessing suitability/risks, drafting multilingual outreach/proposals, assistant decision-making alongside independent browser extraction |
| Live Gateway HTTP 200 transcript | **Not yet provided**; user-confirmed OmniRoute model test success must remain distinct from a direct `POST /v1/chat/completions` receipt and from actual autonomous Web Use/send workflows |
| Combo/group membership | User said they were going to add it to a group; **group membership not independently confirmed**, do not claim it was added or select a group by guess |
| Account finance context | Mistral Studio Free snapshot dated 2026-10-26 showed an included $10/month API/Studio allowance, no payment method and pay-as-you-go not enabled. This model has token-based list pricing and is **not** intrinsically free; do not represent UI Free badge as spending protection, or infer current remaining allowance without new readback |
| Recorded account throttling | Historical screenshot limits for `ministral-14b-2512`: **937,500 tokens/min**, **0.50 requests/sec**; limits are account screenshot ceilings, not promised throughput or entitlement |

**Running cross-provider inventory, evidence-qualified:** Gemini **8** (six chat + two embedding), Groq **6** previously confirmed in Groq tracker, OpenRouter **1** (Nemotron Ultra direct API pass + OmniRoute UI green and user-affirmed operational), Mistral **1** (Ministral 14B user-affirmed OmniRoute UI model test pass). **Total: 16 working/validated entries across providers**, not 16 independently live Gateway-inferenced text-chat models. Preserve prior Gemini, Groq and OpenRouter test evidence. The total excludes failed Mistral Small 4 and other unticked built-ins. This is a documentation-only GitHub change; no local router, model, Combo, billing or credentials were changed.


## 2026-10-30 — Cloudflare Workers AI: GLM 4.7 Flash and Gemma 4 26B added

**User-requested registration in existing operational-model inventory.** After the Cloudflare provider had previously shown an OmniRoute `502` error `Cloudflare Workers AI requires an Account ID`, the user entered the missing Cloudflare Account ID and explicitly reported `اوکی شد` (connection problem resolved). The user subsequently requested the **two earlier-selected models** to be counted among DJMRN's operational engines. Capture that **operator-reported operational status** without inventing unprovided HTTP response logs, OmniRoute UI green screenshots for either model, or their group membership.

| Item | GLM primary | Gemma secondary |
|---|---|---|
| Provider | Cloudflare Workers AI (existing connection `DJMRN-Cloudflare-AI`, alias `cf`) | Same Cloudflare account |
| Upstream model ID | `@cf/zai-org/glm-4.7-flash` | `@cf/google/gemma-4-26b-a4b-it` |
| Full OmniRoute route ID | `cf/@cf/zai-org/glm-4.7-flash` | `cf/@cf/google/gemma-4-26b-a4b-it` |
| Intended role | Primary for free-first text-based analysis of job listings, classification, project suitability, tool-assisted research (tool calling not end-to-end verified) | Secondary fallback for text; separate visual/screenshots analysis candidate (vision endpoint not independently verified) |
| Operator state | **USER-REPORTED OPERATIONAL / REQUESTED FOR WORKING ROSTER**, 2026-10-30 | **USER-REPORTED OPERATIONAL / REQUESTED FOR WORKING ROSTER**, 2026-10-30 |
| Individual API/OmniRoute model test receipt | **Not furnished in this conversation**; do not claim independently observed Gateway `HTTP 200` | **Not furnished in this conversation**; do not claim independently observed Gateway `HTTP 200` |
| Suggested model metadata | `Chat Completions`, `Chat=ON`, `Vision=OFF`, `Free badge=ON` | `Chat Completions`, `Chat=ON`, `Vision-capable=ON` (capability proposed; test pending), `Free badge=ON` |
| Combo membership | **Not confirmed**; proposed `DJMRN-CF-WebUse-Fallback` with Priority strategy has not been shown created or tested | **Not confirmed**; fallback only a plan until Combo/failover test |

**Common configuration and cost context:** Existing Cloudflare Workers AI token appeared `Valid` in user screenshot and the Cloudflare provider had displayed a missing Account ID error. User later stated adding Account ID fixed the connection. The separate orange `Account Analytics: Read` permission warning blocks dashboard **Neuron usage analytics**, not necessarily model inference; do not conflate it with a 502 error or claim the permission was added. Prior user-confirmed account was **Workers Free** with no payment method, Workers Paid inactive. Public Free allocation **10,000 shared Neurons per UTC day**, **not** 10,000 requests and **not per-model**. Both model IDs were identified in the earlier official Cloudflare Free-compatible documentation review (see `06-tests-and-evidence/provider-research/CLOUDFLARE-WORKERS-AI-CATALOG-AND-FREE-TIER-AUDIT-2026-10-26.md`). Never assume UI `Free` badge alone enforces billing or proves real account-specific inference.

**Accounting:** Gemini **8** + Groq **6** + OpenRouter **1** + Mistral **1** + Cloudflare **2** = **18 entries** in the evidence-qualified *working/prepared roster*, with distinct verification grades and modalities. Previous total of 16 (before these Cloudflare entries) remains a historical milestone. This does **not** establish 18 verified direct/Gateway HTTP 200 completions or a functioning Cloudflare automatic fallback. Earlier 9 Cloudflare Built-in `Assumed` cards are **not** all counted. Other Cloudflare models (Qwen Coder, QwQ, DeepSeek Distill, Kimi etc.) remain excluded pending successful tests and account eligibility.

**Suggested next acceptance checks (not performed by this documentation update):** One low-token `POST /v1/chat/completions` via OmniRoute Gateway for each exact full route, separately test Gemma vision if planned, then create the proposed Priority Combo and actually demonstrate fallback on a recoverable model failure. Both share one Cloudflare account and allocation; exhausted daily Neurons cannot be bypassed through intra-provider fallback. No OmniRoute configuration, API token, account permissions, billing or Combo was modified here.
