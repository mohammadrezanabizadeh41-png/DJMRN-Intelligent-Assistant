# DJMRN OmniRoute — Two Combos created, UI evidence (2026-10-29)

**Evidence level:** USER-SUPPLIED-SCREENSHOT (OmniRoute desktop UI, screenshot filename `image(20261029-173714).png`, received in the ChatGPT conversation). **No direct read/write access to the local OmniRoute instance was exercised by this GitHub commit.** Local installation: OmniRoute v3.8.52 according to prior screenshots; screenshot itself does not show a version label.

## Confirmed visible Combo entries

1. **`DJMRN-PM-Standard`** — `PRIORITY` strategy badge, six chat models reported by user to be included and prepared. The UI lists:
   - `gemini/gemma-4-26b-a4b-it`
   - `gemini/gemma-4-31b-it`
   - `gemini/gemini-3.1-flash-lite`
   - `+3 more` (not expanded in the provided screenshot). Per user confirmation and preexisting individual test receipts, the remaining expected selected members are `gemini/gemini-3.5-flash-lite`, `gemini/gemini-3.6-flash`, `gemini/gemini-3-flash-preview`. **Those three are expected from user-reported baseline; not visually individually verified in the current Combo screenshot.**
   - Account labels shown with visible models: `DJMRN-OmniRoute-Gemini`.
   - UI toggle appears in the ON position. Do not conflate toggle/UI creation with actual Combo inference or failover validation.

2. **`DJMRN-Semantic-Memory`** — `PRIORITY` strategy badge, screenshot visibly lists both embedding entries:
   - `gemini/gemini-embedding-001` — `DJMRN-OmniRoute-Gemini`
   - `gemini/gemini-embedding-2` — `DJMRN-OmniRoute-Gemini`
   - UI toggle appears ON. Current screenshot confirms the Combo was **created and is listed**, NOT that `POST /v1/embeddings` accepts this Combo as its `model` nor that its first model falls back successfully.

## Separate prior verified individual-model evidence

- `gemini/gemini-embedding-001` — direct Gateway `/v1/embeddings` smoke PASS HTTP 200, 3072 dimensions.
- `gemini/gemini-embedding-2` — direct Gateway `/v1/embeddings` smoke PASS HTTP 200, 3072 dimensions.
- Five selected chat models passed one small text + inline-JPEG recognition test; `gemini/gemini-3-flash-preview` passed text-only (vision not checked).
- Individual model PASS does not imply each Combo, downstream browser automation, fallback, billing enforcement, or vision on real web screenshots has passed.

## Architecture cautions / current next work

- Embedding 001 and Embedding 2 have distinct vector spaces. Although both generated 3072-dimensional outputs, they must **not silently fail over within one stored index**. In future use pin one embedding model ID and version the index; no vector DB or semantic-search integration was installed or shown.
- `DJMRN-Semantic-Memory` is a reserved future family and need not run now.
- **Next planned:** design separate dedicated Web Search / web-page visual-analysis Combo using suitable models from existing six, without altering `DJMRN-PM-Standard`. Rate limit, true vision support, structured outputs, tool-calling, actual website screenshot test and costs should be verified; DOM-first extraction preferred. Research proposal must be labeled separately from user-created Combo.
- Model route `gemini/gemini-3.8-flash` was deferred due to repeated instability; do not add it to new production routing.
- TTS, Robotics and other specialist models remain deferred.
- Preserve API secrets; never commit them.

## Repo provenance
- Baseline: `07-operations-and-continuity/omniroute/DJMRN-OMNIROUTE-EIGHT-MODEL-BASELINE-AND-FAMILIES-20261029.md`.
- Screenshot-derived OmniRoute navigation: `08-project-knowledge-base/tools/omniroute/WORKING-WITH-OMNIROUTE-v3.8.52-20261024.md`.
- Model tests: `06-tests-and-evidence/logs/GEMINI-*-20261027.md` and `GEMMA4-31B-GATEWAY-VERIFIED-20261027.md`.
