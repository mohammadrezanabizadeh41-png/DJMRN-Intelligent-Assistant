# DJMRN | Gemini 3.6 Flash — Gateway text and vision verified
Date: 2026-10-27
Status: USER-OBSERVED-SMOKE-PASS
Model: `gemini/gemini-3.6-flash`
Environment: existing OmniRoute v3.8.52 `http://127.0.0.1:20128/v1/chat/completions`

## Actual Windows PowerShell outcomes
- Text request: Chat Completions, `Reply with exactly READY.`, `max_tokens=384`, `stream=false`.
  - `HTTP_STATUS=200`, `SECONDS=3.07`, `RESPONSE=READY`, `TEXT_TEST=PASS`.
- Image-understanding request: same model, public Wikimedia Commons cat JPEG downloaded and checked as JPEG, passed inline as `image_url.url=data:image/jpeg;base64,...`; classification prompt CAT / OTHER.
  - `HTTP_STATUS=200`, `SECONDS=9.35`, `RESPONSE=CAT`, `VISION_TEST=PASS`, `MODEL_STATUS=TEXT_AND_VISION_OPERATIONAL`.

## Interpretation and boundaries
Fourth model to pass both text and single-inline-JPEG vision via OmniRoute, after `gemini/gemma-4-26b-a4b-it`, `gemini/gemma-4-31b-it`, and `gemini/gemini-3.5-flash-lite`. These are distinct observed one-off smoke tests, not benchmark guarantees.
No provider, Custom entry, route, local model, group/Combo, proxy, Windows setting, or API key was changed. No credentials retained. Existing catalog free tag does not enforce zero charge; rate limits and billing conditions remain separate checks.
User's standing DJMRN instruction: each actual action and failure/success must have a verifiable repository receipt.

## Pending next stage
Existing remaining Custom models include specialist TTS (`gemini-3.8-flash-lite-tts`, `gemini-3.8-flash-tts`), embeddings (`gemini-embedding-001`, `gemini-embedding-2`), and robotics (`gemini-robotics-er-2-preview`). Those MUST be validated on matching modality routes and only one at a time; do not treat a Chat endpoint as proof of a non-chat modality. Previously observed TTS/embedding Custom metadata mismatch `apiFormat=chat-completions` with specialized supportedEndpoints requires careful in-place correction after verifying supported adapters. No fifth model tested by this receipt.
