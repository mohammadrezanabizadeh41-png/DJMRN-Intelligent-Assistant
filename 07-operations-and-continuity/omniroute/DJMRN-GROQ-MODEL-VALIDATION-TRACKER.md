# DJMRN — Groq Model Validation Tracker

Reference date: 2026-10-29
Purpose: One stable, append/update-in-place roster for the user's **Groq provider** `DJMRN-Groq-Free` under OmniRoute Desktop v3.8.52. Add to the confirmed list only when user evidence shows an OmniRoute green test indicator or a real Gateway HTTP 200 with valid output; distinguish UI-green from Gateway-real verification and from direct upstream calls. Never silently mark a model validated based solely on the upstream catalog or an imported Custom row. Do not create duplicate models or provider connections.

## Summary
- Groq account authenticated upstream GET `https://api.groq.com/openai/v1/models`: **11 live IDs**, evidenced by user PowerShell output on 2026-10-29.
- **Five Groq Built-in models visibly have green test indicators in OmniRoute** (user screenshot). This confirms the UI test result only; not all endpoints, multimodal or sustained inference.
- **Both Prompt Guard Custom models are already registered**, and both had previously passed direct Groq HTTP 200. **Prompt Guard 22M is NOW GATEWAY REAL PASS** with user-supplied HTTP 200, 0.83s, numeric score 0.9990056157112122; Prompt Guard 86M remains Gateway PENDING.
- **Two Whisper speech-to-text models** occur in upstream account and the bundled native `groq` transcription adapter; actual routed audio-transcription test not yet observed.
- **Two Orpheus TTS models** occur in upstream account; native `groq` speech adapter not present in release/v3.8.52; routed TTS pending adapter evaluation.
- **6/11 confirmed models** in total: five native Built-ins from user screenshot green tests + one Prompt Guard 22M Custom with actual OmniRoute Gateway HTTP 200 and valid numeric classifier score. Do not claim all other modalities verified.
- Two other built-in catalog-only models `groq/compound` and `qwen/qwen3.6-27b` are retired upstream; exclude them from the 11 current live and from candidates.

## CONFIRMED — five OmniRoute UI-green Built-ins + one Gateway-real Custom (six)

| # | OmniRoute gateway model ID | Source | Verification evidence | Application idea (future, not yet grouped) |
|---|---|---|---|---|
| 1 | `groq/allam-2-7b` | Built-in | UI GREEN (user screenshot) | Arabic text |
| 2 | `groq/openai/gpt-oss-120b` | Built-in | UI GREEN (user screenshot) | Deeper text reasoning/coding |
| 3 | `groq/openai/gpt-oss-20b` | Built-in | UI GREEN (user screenshot) | General/light text |
| 4 | `groq/qwen/qwen3.8-27b` | Built-in | UI GREEN (user screenshot) | Text, potential vision (vision modality test not yet proved) |
| 5 | `groq/openai/gpt-oss-safeguard-20b` | Built-in | UI GREEN (user screenshot) | Safety and moderation |
| 6 | `groq/meta-llama/llama-prompt-guard-2-22m` | Existing Custom | **REAL GATEWAY PASS**: HTTP 200, 0.83 s, score `0.9990056157112122`, test `PASS_REAL_GATEWAY` (user PowerShell 2026-10-29); prior direct Groq HTTP 200 / 0.45 s | Prompt injection classifier (numeric risk score, not chat text) |

## STILL PENDING — five models awaiting actual OmniRoute modality-specific validation

| # | Upstream model ID | OmniRoute registration/route status | Evidence and pending check |
|---|---|---|---|
| 7 | `meta-llama/llama-prompt-guard-2-86m` | Existing Custom model, Groq | Direct Groq HTTP 200 / 0.48s / score 0.9995385408401489, but OmniRoute test/route GREEN not confirmed |
| 8 | `whisper-large-v3` | Native Groq STT route in OmniRoute source | Actual audio through `/v1/audio/transcriptions` pending |
| 9 | `whisper-large-v3-turbo` | Native Groq STT route in OmniRoute source | Actual audio through `/v1/audio/transcriptions` pending |
| 10 | `canopylabs/orpheus-v1-english` | Native Groq TTS route not found in OmniRoute 3.8.52 | Groq direct speech and/or dedicated compatible TTS adapter pending |
| 11 | `canopylabs/orpheus-arabic-saudi` | Native Groq TTS route not found in OmniRoute 3.8.52 | Groq direct speech and/or dedicated compatible TTS adapter pending |

## Evidence and update rules

1. Add to GREEN only on new **actual OmniRoute test success** (user screenshot with recognizable model + green indicator, or user PowerShell Gateway HTTP 200 with response) and record which kind of test it passed. A direct upstream-only success is separate, not a Green OmniRoute result.
2. For a request that fails, retain the model as pending and record the HTTP status and safe error class. Do not mark as categorically blocked without separating provider limitations from gateway, model metadata and network proxy.
3. Do not duplicate two Prompt Guard Custom rows; do not re-create the five native Built-ins. Every model is under existing `DJMRN-Groq-Free` account, with its connection-scoped HTTP proxy.
4. The account’s public Free quotas are **plan-level nominal**, not an actual per-key guaranteed daily balance or paid-use safety control. Avoid automatic spillover or model batch tests without the user's request.
5. Source receipt with full model inventory, Groq proxy recovery and direct two-classifier HTTP 200 tests: `06-tests-and-evidence/logs/GROQ-OMNIROUTE-PROVIDER-CREATED-TEST-ERROR-20261029.md`. Limits study: `06-tests-and-evidence/provider-research/GROQ-FREE-TIER-MODEL-REVIEW-20261029.md`.
6. This file is the single canonical **Groq model test progress tracker**. When a new model succeeds, update this same file instead of creating multiple unrelated lists. Current accepted count: **6 of 11 VERIFIED**, comprising 5 user screenshot UI GREEN and 1 real Gateway HTTP 200.

## Next
User chooses the next Groq model to test. Next: `groq/meta-llama/llama-prompt-guard-2-86m` one real Gateway classifier call using the private Gateway API Key. Then STT using a sample audio clip, then Orpheus TTS adapter research. Keep 22M result and the 5 UI-green records unchanged. There is no active Combo grouping request yet.


## Receipt — 2026-10-29 — model #6 Prompt Guard 22M confirmed through REAL OmniRoute Gateway

User ran a single local PowerShell `POST http://127.0.0.1:20128/v1/chat/completions` with `model=groq/meta-llama/llama-prompt-guard-2-22m`, `stream=false`, `max_tokens=32`, and a test prompt resembling a prompt-injection instruction. Exact safe stdout:

```text
MODEL=groq/meta-llama/llama-prompt-guard-2-22m
HTTP_STATUS=200
DURATION_SECONDS=0.83
ANSWER=0.9990056157112122
CLASSIFICATION_SCORE=0.999005615711212
RESULT=PASS_REAL_GATEWAY
```

**Conclusion:** User-confirmed Gateway chat request and numeric classifier output are real and valid for this specific model. It moves from pending to CONFIRMED (#6 of 11), without requiring a new Custom entry or changing any connection/proxy. The earlier reported red “Blacklist” UI action does not by itself negate this runtime success. All other model states remain unchanged; classification quality, real adversarial robustness, and free-cost enforcement remain untested.


## Standing operator rule — after each successful test, provide exact OmniRoute UI registration settings

User explicitly requires: after a successful *actual PowerShell model test*, the assistant must immediately give copy/paste-ready UI settings to add **or review/adjust** that model in OmniRoute's **Groq provider → Custom Models**, and only then move to the next model. Distinguish an API model test success from a UI model registration or green icon; only mark a UI registration completed after user evidence.

**Two Prompt Guard entries are already stored**: user management `GET /api/provider-models?provider=groq` returned `CUSTOM_MODEL_COUNT=2`, plus both rows were `KEEP_CUSTOM`. Therefore **do not click + Add for either again**. If they are absent from the broader `Models & Combos` page, use Groq provider → Custom Models (existing row), refresh, clear model filters / show hidden, and review/Edit the existing row; do not infer missing DB row from missing global card. OmniRoute v3.8.52 source `src/app/(dashboard)/dashboard/providers/[id]/ProviderDetailPageClient.tsx` merges `modelMeta.customModels` into the provider's Available Models listing, and `CustomModelsSection.tsx` supports editing rather than duplicate insertion.

**Current tested 22M settings** (`modelId` must be upstream ID without `groq/` prefix): `meta-llama/llama-prompt-guard-2-22m`; display `DJMRN Groq Prompt Guard 22M`; `API Format=Chat Completions`; `Target Format=Default (auto)`; `Supported Endpoints=[Chat]` only; `Vision capable=OFF`; `FREE=ON` (documentation Free tier; metadata only, not a spending guard); context/output overrides leave blank; expected full gateway model `groq/meta-llama/llama-prompt-guard-2-22m`. Real Gateway HTTP200 / 0.83s / numeric score pass already user-confirmed.

**86M pending Gateway test settings** likewise: upstream ID `meta-llama/llama-prompt-guard-2-86m`; display `DJMRN Groq Prompt Guard 86M`; same Chat Completions / Default / Chat only / no Vision / Free tag; expected full route `groq/meta-llama/llama-prompt-guard-2-86m`. Already present as a Custom row; no duplicate. Only mark gateway confirmed after user test.

**Non-chat modalities:** For Groq Whisper 3/Turbo, OmniRoute 3.8.52 already includes native `AUDIO_TRANSCRIPTION_PROVIDERS.groq`; use Audio Transcriptions endpoint and a real audio sample, not Chat Custom. Orpheus English and Arabic in the actual upstream catalog lack built-in Groq `AUDIO_SPEECH_PROVIDERS.groq` in this version, so after verifying direct API speech propose compatible audio-speech adapter configuration; do not pretend merely setting Custom `API Format=Audio Speech` activates the missing executor. Preserve one Groq provider connection and key-scoped proxy.

**Next after 22M registration review:** 86M PowerShell real OmniRoute Gateway test, then check its existing Custom settings and make it visible where applicable, then Whisper and Orpheus one by one. Five UI-green Built-ins remain unchanged.


## 2026-10-29 — Research diagnosis: Groq Prompt Guard Gateway 200 but OmniRoute model-card TEST shows red "Blacklist"

**Evidence known:** Model 22M successfully returned genuine numeric classifier output on a user-run OmniRoute Gateway non-streaming chat request (HTTP 200, 0.83s). In a prior screenshot the model's card displayed a red error icon and the red `Blacklist` action; **`Blacklist` is an action to hide a model after an unsuccessful built-in test**, not proof of Groq upstream restriction or proof that an operator actually clicked blacklist.

**Source-verified in `cheaper-inference/OmniRoute` `release/v3.8.52`:**
- `src/app/(dashboard)/dashboard/providers/[id]/hooks/useModelVisibilityHandlers.ts`: the UI test button POSTs `/api/models/test` with `providerId`, full model ID and selected `connectionId`; it shows red on `status!="ok"`. `ModelRow.tsx` shows `Blacklist` only for `testStatus === "error"` and clicking it sets `isHidden=true`.
- `src/app/api/models/test/route.ts`: model-card test uses `streamChat:true`, and if `hidePaidModels=true` it checks only `isFreeModel(providerId, { id: modelId })` against shipped catalog/heuristics (does **not** read Custom `isFree` flag) and returns HTTP403 `Paid model blocked while hidePaidModels is enabled` before any upstream dispatch. This is a **plausible** cause; need actual setting and UI-test error to establish.
- `open-sse/config/freeModelCatalog.data.ts` on that release lists four/five Groq general chat rows but no `meta-llama/llama-prompt-guard-2-22m` / `86m`. Yet Groq's official `https://console.groq.com/docs/rate-limits` lists these two under public Free limits, and direct Groq and 22M OmniRoute Gateway requests passed.
- `src/lib/api/modelTestRunner.ts` default `streamChat=true` for UI tests with test-body builder in `src/lib/combos/testHealth.ts` using `Reply with exactly: pong`; tested user Gateway route instead used `stream=false` and an adversarial sample, returning a numeric classifier score. Difference is also a possible cause (no proof that Groq streaming fails until actual UI-test result).

**No changes recommended yet:** Do not delete/re-add models, turn off global free/paid safeguards, or label as upstream banned. Next bounded diagnostic: use management token to GET only `/api/settings` `hidePaidModels` and `/api/provider-models?provider=groq` fields for exact 22M existing Custom (id, format, endpoints, free flag, hidden flag), then invoke exactly one user-approved `POST /api/models/test` with same model and connection ID and show sanitized status/error. If it's 403 `Paid model blocked...`, investigate specific model free-tag recognition without disabling no-paid policy. If other error, check streaming/probe output before changing settings.

**Status:** Root cause pending, existing 22M Gateway REAL PASS is preserved. Model 86M Gateway remains pending and should not be marked failed because of card UI alone.


## 2026-10-29 — Newly isolated UI mismatch: Custom model ID is almost certainly double-prefixed (readback confirmation pending)

User ran management read-only diagnostic for the already Gateway-passed 22M and obtained:
```text
HIDE_PAID_MODELS=False
MODEL_RECORDS=0
RESULT=MODEL_RECORD_NEEDS_REVIEW
```
The probe looked for the exact proper upstream Custom row ID `meta-llama/llama-prompt-guard-2-22m`. Earlier the same account's management `GET /api/provider-models?provider=groq` returned `CUSTOM_MODEL_COUNT=2` and classified BOTH Prompt Guard models as `KEEP_CUSTOM`, where `KEEP_CUSTOM` accepted either `<raw-id>` or `groq/<raw-id>`. Thus combined evidence implies 22M was stored with a **mistaken `groq/` prefix in Custom model ID**, and 86M very likely likewise; list actual IDs before edits to prove exact content.

Exact OmniRoute `release/v3.8.52` implementation `CustomModelsSection.tsx` computes `fullModel = `${providerAlias}/${model.id}`` unconditionally. So a stored ID `groq/meta-llama/...` would become incorrect `groq/groq/meta-llama/...` in UI. Editing Custom metadata (format/endpoints/Free) does not edit its `id`, and the user has observed UI error despite real Gateway 22M PASS. The UI test `/api/models/test` was NOT executed by the user's last diagnostic script because it returned early on the missing exact record; **do not claim a 403 or test-status from this run**. `hidePaidModels=False` excludes that specific global paid-only test-block branch currently.

**Next bounded step:** read-only GET Custom model rows, print only stored `id`, computed provider-prefixed route, Chat/Free/Hidden fields, and classify DOUBLE_PREFIX. If proven, create a correctly identified Custom row `meta-llama/...` with `apiFormat=chat-completions, supportedEndpoints=[chat], isFree=true` (FREE is metadata only); verify readback before deleting only the specifically identified malformed row (if user authorizes cleanup), one model at a time. Preserve existing provider and proxy; do not blindly re-register credentials. Maintain 6/11 confirmed model runtime count (this is UI registration defect, not a new Gateway failure).


## 2026-10-29 — Source-confirmed root mechanism; safe staged repair proposed (NOT YET EXECUTED ON USER WINDOWS)

After user reports two Prompt Guard Custom models do not appear/work as desired in OmniRoute Models page, inspected exact `cheaper-inference/OmniRoute` `release/v3.8.52`:
- `src/lib/db/models.ts`: `addCustomModel(providerId, modelId,...)` persists the operator-provided `modelId` **unchanged**; dedup is exact-ID only.
- `src/app/(dashboard)/dashboard/providers/[id]/components/CustomModelsSection.tsx`: builds `fullModel = `${providerAlias}/${model.id}`` for displayed model route. Therefore storing `groq/meta-llama/...` under `provider=groq` would present the wrong `groq/groq/meta-llama/...`. The required Custom ID is the unprefixed upstream ID `meta-llama/...`.
- `src/shared/validation/schemas/provider.ts` supports POST fields `provider`, `modelId`, `modelName`, `apiFormat=chat-completions`, `supportedEndpoints=["chat"]`, `supportsVision=false`, `isFree=true` and `targetFormat` omitted for auto.
- `src/app/api/provider-models/route.ts` supports management-key GET and POST. A correctly created Custom row is merged into provider Available Models page by `ProviderDetailPageClient.tsx`.
- User's last diagnostic: `HIDE_PAID_MODELS=False`, `MODEL_RECORDS=0` for correct bare 22M ID; prior `CUSTOM_MODEL_COUNT=2` and both `KEEP_CUSTOM` (comparison matched bare or `groq/`-prefixed). Strong double-prefix hypothesis but **still pending inspection of stored raw IDs**.
- Pending user action: Execute a guarded PowerShell migration against localhost management API: GET and print the two stored raw Custom IDs; only if both exact prefix-wrong variants exist (or one exact correct + other prefix-wrong) add **missing corrected bare IDs**, verify readback; leave old rows in place until successful UI check. Never blindly delete, never change API keys/proxies, don't confuse display repair with Gateway inference (22M was already Gateway PASS). If unexpected existing ID set is observed, fail closed and report actual IDs instead of guessing.
- The UI test button's probe is **not equivalent** to the successful non-streaming classification request: source `src/app/api/models/test/route.ts` calls `runSingleModelTest(streamChat=true)`; `src/lib/combos/testHealth.ts` injects a `Reply with exactly: pong` prompt. Even after correcting a prefix mismatch, a classifier may fail UI's generic streaming/prose probe; capture `status`/`error` separately before claiming end-to-end UI green. This is not an upstream model access limitation.
- No migration or new model registration was performed by ChatGPT in the user's local OmniRoute; wait for user-run audit/repair receipt before marking UI resolution.
