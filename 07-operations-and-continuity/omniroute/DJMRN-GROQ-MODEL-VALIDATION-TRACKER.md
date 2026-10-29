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
