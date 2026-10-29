# DJMRN — Groq Model Validation Tracker

Reference date: 2026-10-29
Purpose: One stable, append/update-in-place roster for the user's **Groq provider** `DJMRN-Groq-Free` under OmniRoute Desktop v3.8.52. Append each model to **UI GREEN** only when the user presents a fresh green OmniRoute test result; separate routing, text and voice verification evidence. Never silently mark a model validated based solely on the upstream catalog or an imported Custom row. Do not create duplicate models or provider connections.

## Summary
- Groq account authenticated upstream GET `https://api.groq.com/openai/v1/models`: **11 live IDs**, evidenced by user PowerShell output on 2026-10-29.
- **Five Groq Built-in models visibly have green test indicators in OmniRoute** (user screenshot). This confirms the UI test result only; not all endpoints, multimodal or sustained inference.
- **Two additional Prompt Guard models** are already present as **two Custom entries** (user's GET OmniRoute model inventory), and both have independently passed **direct Groq chat HTTP 200** returning numeric prompt-injection classifier scores. Their OmniRoute model test status remains **PENDING/NOT CONFIRMED GREEN**.
- **Two Whisper speech-to-text models** occur in upstream account and the bundled native `groq` transcription adapter; actual routed audio-transcription test not yet observed.
- **Two Orpheus TTS models** occur in upstream account; native `groq` speech adapter not present in release/v3.8.52; routed TTS pending adapter evaluation.
- Five **UI GREEN** is a user-confirmed operational shortlist; do not claim complete Gateway text/vision/transcription/speech HTTP 200 for each without real evidence.
- Two other built-in catalog-only models `groq/compound` and `qwen/qwen3.6-27b` are retired upstream; exclude them from the 11 current live and from candidates.

## GREEN — confirmed user screenshot of OmniRoute model test (five)

| # | OmniRoute gateway model ID | Source | UI status | Application idea (future, not yet grouped) |
|---|---|---|---|---|
| 1 | `groq/allam-2-7b` | Built-in | GREEN (user screenshot) | Arabic text |
| 2 | `groq/openai/gpt-oss-120b` | Built-in | GREEN (user screenshot) | Deeper text reasoning/coding |
| 3 | `groq/openai/gpt-oss-20b` | Built-in | GREEN (user screenshot) | General/light text |
| 4 | `groq/qwen/qwen3.8-27b` | Built-in | GREEN (user screenshot) | Text, potential vision (vision modality test not yet proved) |
| 5 | `groq/openai/gpt-oss-safeguard-20b` | Built-in | GREEN (user screenshot) | Safety and moderation |

## NOT YET GREEN — pending OmniRoute modality-specific validation

| # | Upstream model ID | OmniRoute registration/route status | Evidence and pending check |
|---|---|---|---|
| 6 | `meta-llama/llama-prompt-guard-2-22m` | Existing Custom model, Groq | Direct Groq HTTP 200 / 0.45s / score 0.9990056157112122, but OmniRoute test/route GREEN not confirmed |
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
6. This file is the single canonical **Groq model test progress tracker**. When a new model succeeds, update this same file instead of creating multiple unrelated lists. Current accepted count: **5 of 11 GREEN in OmniRoute**.

## Next
User chooses the next Groq model to test. Recommended: `groq/meta-llama/llama-prompt-guard-2-22m` then 86M, with a single low-cost Gateway text request each; afterwards test STT using a sample audio clip; then resolve the TTS adapter for Orpheus. There is no active Combo grouping request yet.
