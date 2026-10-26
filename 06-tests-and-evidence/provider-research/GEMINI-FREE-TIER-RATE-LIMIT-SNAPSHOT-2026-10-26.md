# DJMRN Gemini API — Account Free-Tier Snapshot (2026-10-26)
Source: FIVE screenshots supplied by user from Google AI Studio > Rate Limit, project **Default Gemini Project**, time range **28 Days**, tier **Free**. These are user-account observations, not global guaranteed limits. No secrets included.

## Interpretation
RPM=requests/minute; TPM=input tokens/minute; RPD=requests/day. Each screenshot shows **used / allowed**. All visible usage numerators are 0. A limit 0 is **NOT** an available free quota. Unlimited shown in Live API is a rate-limit label, **not unlimited free billing/usage**. Model access, endpoint compatibility, and successful invocation remain untested. Screenshots are partial scroll captures; do not infer absent rows.

## Text and general agent models (visible account limits)
| Display name | RPM | TPM | RPD |
|---|---:|---:|---:|
| Gemini 2 Flash | 0 | 0 | 0 |
| Gemini 2 Flash Lite | 0 | 0 | 0 |
| Gemini 2.5 Flash | 5 | 250K | 20 |
| Gemini 2.5 Flash Lite | 10 | 250K | 20 |
| Gemini 2.5 Pro | 0 | 0 | 0 |
| Gemini 3 Flash | 5 | 250K | 20 |
| Gemini 3.1 Pro | 0 | 0 | 0 |
| Gemini 3.1 Flash Lite | 15 | 250K | 500 |
| Gemini 3.6 Flash | 5 | 250K | 20 |
| Gemini 3.5 Flash Lite | 15 | 250K | 500 |
| Gemini 3.8 Flash | 5 | 250K | 20 |
| Gemini 4 Argon | 0 | 0 | 0 |
| Gemma 4 26B | 30 | 16K | 14.4K |
| Gemma 4 31B | 30 | 16K | 14.4K |
| Antigravity (Agents) | 60 | 100K | 100 |
| Deep Research Pro Preview (Agents) | 0 | 0 | 0 |

## Embedding, robotics, speech, media (visible account limits)
| Display name | RPM | TPM | RPD |
|---|---:|---:|---:|
| Gemini Embedding 1 | 100 | 30K | 1K |
| Gemini Embedding 2 | 100 | 30K | 1K |
| Gemini Robotics ER 2 Preview | 5 | 250K | 20 |
| Gemini 2.5 Flash TTS | 3 | 10K | 10 |
| Gemini 3.1 Flash TTS | 3 | 10K | 10 |
| Gemini 3.8 Flash TTS | 3 | 10K | 10 |
| Gemini 3.8 Flash Lite TTS | 3 | 10K | 10 |
| Gemini 3.5 Transcribe (Live API) | 3 | 10K | 25 |
| Gemini 2.5 Flash Native Audio Dialog (Live API) | Unlimited | 1M | Unlimited |
| Gemini 3 Flash Live (Live API) | Unlimited | 65K | Unlimited |
| Gemini 3.5 Live Translate (Live API) | Unlimited | 20K | Unlimited |
| Gemini 3.5 Transcribe Live (Live API) | Unlimited | 20K | Unlimited |
| Gemini 3.8 Live (Live API) | Unlimited | 65K | Unlimited |
| Gemini 3.8 Live Extended Thinking (Live API) | Unlimited | 65K | Unlimited |
| Nano Banana (Gemini 2.5 Flash Preview Image) | 0 | 0 | 0 |
| Nano Banana Pro (Gemini 3 Pro Image) | 0 | 0 | 0 |
| Nano Banana 2 (Gemini 3.1 Flash Image) | 0 | 0 | 0 |
| Nano Banana 2 Lite (Gemini 3.1 Flash Lite Image) | 0 | 0 | 0 |
| Gemini Nano Banana 2.1 | 0 | 0 | 0 |
| Gemini Omni 1.1 Flash | 0 | 0 | 0 |
| Lyria 3 Clip | 0 | 0 | 0 |
| Lyria 3 Pro | 0 | 0 | 0 |
| Veo 3 Fast Generate | 0 | - | 0 |
| Veo 3 Generate | 0 | - | 0 |
| Veo 3 Lite Generate | 0 | - | 0 |
| Computer Use Preview | 0 | 0 | 0 |

## Tools (separate from generation model quota)
Visible map grounding rows for Deep Research Pro Preview, Gemini 2 Flash, Computer Use Preview, Gemini 2.5 Flash, Gemini 2.5 Flash Lite, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Lite, Gemini 3.1 Flash TTS, Gemini 3.6 Flash, Gemini 3.5 Flash Lite, Gemini 3.5 Transcribe, Gemini 3.8 Flash, Gemini 4 Argon, Gemini Robotics ER 2 Preview: RPD=0 (RPM and TPM shown as dash).
Search grounding: Gemini 2: RPD 1.5K; Gemini 2.5: RPD 1.5K; Gemini 3 and newer: RPD 0; Default: RPD 1.5K. These are **tool quota rows**; do not interpret as ability to call disabled base models or automatically free search usage.

## Architecture decisions / next tests
- Candidate main shared pool: Gemini 3.1 Flash Lite, Gemini 3.5 Flash Lite, Gemini 3.8 Flash, Gemini 3.6 Flash, Gemini 3 Flash, Gemini 2.5 Flash, Gemini 2.5 Flash Lite; Gemma 4 26B/31B separately due to 16K TPM; embeddings as separate vector/RAG service. Avoid zero-limit models.
- Do NOT add daily request quotas together as a guaranteed independent global budget: project/model-specific constraints and shared upstream quotas may exist. Verify with real responses.
- No fixed quota assigned to Agno agents; use task capability tiers, weighted/random choice within eligible model set, 429/backoff/failover, health checks and rate-limit awareness; protect non-idempotent tool actions from duplicate execution.
- Obtain exact API model IDs from official models.list and map display names; never guess IDs from screenshot alone. Check OmniRoute provider/model compatibility, 429 behavior, reset state, and whether Live API/agent endpoints need dedicated integration.
- Preserve free-only posture: billing not enabled without explicit approval. Store keys locally, never in GitHub.
- Refresh snapshot when dashboard limits change; official documentation says project-level limits, not per API key, and RPD resets midnight Pacific.

## Official references (external; not screenshot evidence)
- https://ai.google.dev/gemini-api/docs/rate-limits
- https://ai.google.dev/gemini-api/docs/models
- https://ai.google.dev/api/models
- https://ai.google.dev/gemini-api/docs/billing
