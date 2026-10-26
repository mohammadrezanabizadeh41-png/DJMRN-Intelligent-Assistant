# DJMRN | Gemini 3.5 Flash-Lite — Gateway text + vision PASS
Date: 2026-10-27
Status: VERIFIED_SINGLE_MODEL_SMOKE_PASS
Evidence: User pasted actual Windows PowerShell test output (not a simulation).

## Test target
- Model: `gemini/gemini-3.5-flash-lite`
- Environment: existing OmniRoute v3.8.52 gateway at `http://127.0.0.1:20128/v1/chat/completions`
- Authentication: private Gateway API key entered locally; not recorded or modified.
- Existing Custom model was documented earlier as `chat-completions`, `supportedEndpoints=chat`, `isFree=True`, `supportsVision=True`. Flags are metadata only; actual routing/billing must be verified separately.

## Observed execution
1. Text test: OpenAI-compatible Chat Completions `POST`, prompt `Reply with exactly READY.`, `max_tokens=384`, `stream=false`.
   - `HTTP_STATUS=200`
   - `SECONDS=1.11`
   - `RESPONSE=READY`
   - `TEXT_TEST=PASS`
2. Vision test: same Gateway model with public cat JPEG fetched from Wikimedia Commons, checked as JPEG, included as `image_url.url=data:image/jpeg;base64,...`, prompt requested CAT/OTHER.
   - `HTTP_STATUS=200`
   - `SECONDS=6.41`
   - `RESPONSE=CAT`
   - `VISION_TEST=PASS`
   - `MODEL_STATUS=TEXT_AND_VISION_OPERATIONAL`

## Scope and implications
- Working in a minimal smoke test: text chat + single-image understanding through the existing Gemini provider in OmniRoute. No local model install or duplicate registration was necessary.
- The image path tested is **inline JPEG Base64**. Remote image URL handling, other modalities, uptime, throughput, quota availability, and guaranteed zero-cost usage are NOT confirmed.
- No local provider model settings, proxy, Windows settings, group/Combo, Agno integration, or credentials were changed by this test.
- Prior verified models: `gemini/gemma-4-26b-a4b-it` and `gemini/gemma-4-31b-it`; both independently passed text + inline-image Vision. Do not equate historical Gemma 31B 500s with current Gemini 3.5 results.

## Next (not yet executed)
- Move **one at a time** to the next existing Custom candidate `gemini/gemini-3.6-flash`, with a minimal real gateway text test first, then (only after text success) inline JPEG vision.
- Prior inventory lists `gemini-3.6-flash` as chat-completions/chat and `isFree=True`, `supportsVision=True`. Prior account screenshot documented positive free daily RPD; old quotas can change. No actual inference result for this model yet.
- Do not claim deployment, billing enforcement or a group-ready quality SLA from these two minimal tests.
