# Groq Free Tier Model Review — 2026-10-29

Status: public documentation checked; the user's account Free-plan and Limits screenshots were recorded on 2026-10-26; local Groq-to-OmniRoute integration has not been tested.

## Main candidates

| Model | RPM | RPD | TPM | TPD | Task |
|---|---:|---:|---:|---:|---|
| openai/gpt-oss-20b | 30 | 1000 | 8000 | 200000 | fast text triage and structured extraction |
| openai/gpt-oss-120b | 30 | 1000 | 8000 | 200000 | reasoning, coding, detailed review |
| qwen/qwen3.8-27b | 30 | 1000 | 8000 | 200000 | multimodal image and OCR |
| openai/gpt-oss-safeguard-20b | 3 | 1000 | 2000 | 200000 | policy review only |
| meta-llama/llama-prompt-guard-2-22m | 30 | 14400 | 15000 | 500000 | prompt safety |
| meta-llama/llama-prompt-guard-2-86m | 30 | 14400 | 15000 | 500000 | prompt safety |

Historic allam-2-7b had 30 RPM, 7000 RPD, 6000 TPM, 500000 TPD in the account screenshot, but is absent from the current official aggregate Free limits list; its current account availability is unknown.

Whisper Large V3 and Whisper Large V3 Turbo each had 20 RPM, 2000 RPD, 7200 audio seconds per hour and 28800 per day. TTS models are deferred.

## Quota rules

The provider's rate limits are defined at organization level; project-level caps may restrict further but cannot increase organization limits. Limits are not per individual access credential. Every request is constrained simultaneously by request-per-minute, request-per-day, token-per-minute and token-per-day limits. Distinct model rows should not be conflated with independent organizations or duplicated quotas. Paid Developer prices and RPM from the model catalog are not Free-plan allowances.

## Feature research

Qwen 3.8 27B official vision documentation: image, OCR, JSON and tools; up to three images/request, max 20 MB image input. GPT-OSS 20B and 120B support optional Groq built-in browser_search. Its Free eligibility and routing through local OmniRoute remain unverified. Browser Search is separate from automated account login/website control. Older built-in browser_automation is retired. Qwen preview stability warrants caution.

## Next steps

Read current console Organization and Project Limits, verify the account is still on Free, validate available model IDs, connect Groq to OmniRoute without altering Gemini setup, then smoke test GPT-OSS 20B, GPT-OSS 120B and Qwen 3.8 27B one at a time. Use evidence-based admission to future specialist model families. Do not record untested models as active.

## Sources

https://console.groq.com/docs/rate-limits
https://console.groq.com/docs/models
https://console.groq.com/docs/vision
https://console.groq.com/docs/projects
https://console.groq.com/docs/tool-use/built-in-tools/browser-search
https://console.groq.com/docs/deprecations

Previous evidence files: GROQ-ACCOUNT-AND-MODEL-ONBOARDING-2026-10-26.md, GROQ-BILLING-FREE-PLAN-SNAPSHOT-2026-10-26.md, GROQ-ORGANIZATION-LIMITS-SNAPSHOT-2026-10-26.md, GROQ-MODEL-CATALOG-SNAPSHOT-2026-10-26.md.

## 2026-10-29 — Screenshot of working Groq provider page, exact built-ins and current official deprecations

**Actual user's OmniRoute v3.8.52 screenshot:** provider Groq shows one connection `DJMRN-Groq-Free` as green connected, Protected, enabled; proxy label `127.0.0.1`. Available Models reports **7/7 active** BUILT-IN card entries. This is *local model visibility*, not proof all models can be successfully used with current Groq API:
- `groq/groq/compound`
- `groq/allam-2-7b`
- `groq/openai/gpt-oss-120b`
- `groq/openai/gpt-oss-20b`
- `groq/qwen/qwen3.6-27b`
- `groq/qwen/qwen3.8-27b`
- `groq/openai/gpt-oss-safeguard-20b`

**Critical research correction** from official Groq deprecation page (retrieved 2026-10-29): `groq/compound` was retired on **2026-09-21**; `qwen/qwen3.6-27b` was retired for Free and Developer accounts on **2026-09-14**, superseded by `qwen/qwen3.8-27b`. They remain BUILT-IN in OmniRoute v3.8.52 yet should **NOT** enter operative Combos or new duplicate Custom records. The presence of the older IDs in a local static built-in catalog is NOT evidence of upstream availability.

**Official Groq current Free rate-limits table plus user Oct-26 account quotas:** exactly six fully documented Free-tier text-input models:
1. `openai/gpt-oss-20b` — 30 RPM, 1,000 RPD, 8,000 TPM, 200,000 TPD; Built-in present.
2. `openai/gpt-oss-120b` — same; Built-in present.
3. `qwen/qwen3.8-27b` — same; Built-in present, text plus vision.
4. `openai/gpt-oss-safeguard-20b` — 3 RPM, 1,000 RPD, 2,000 TPM, 200,000 TPD; Built-in present, specialist safety.
5. `meta-llama/llama-prompt-guard-2-22m` — 30 RPM, 14,400 RPD, 15,000 TPM, 500,000 TPD; NOT among 7 visible built-ins, candidate manual Custom after live account listing.
6. `meta-llama/llama-prompt-guard-2-86m` — same; NOT among 7 built-ins, candidate manual Custom after live account listing.

**`allam-2-7b`:** present as local built-in and historical user Oct-26 Limits row at 30 RPM / 7K RPD / 6K TPM / 500K TPD, still has an official Groq model card at https://console.groq.com/docs/model/allam-2-7b but **not listed in the current Groq consolidated Free rate limits table**; model card pricing says Pending. User-account current authenticated `GET /models` confirmation and Free entitlement require further check. No inference run or promotion yet.

**The prior live Groq account `GET /models` returned 11 models total but user did not print the 11 IDs**; cannot infer the overlap with static 7 built-ins or the exact 11 model types. Follow-up: read-only authenticated Groq `GET https://api.groq.com/openai/v1/models` from user's own PowerShell using previously saved Groq key and print only IDs, not credentials. Classify against six official Free text IDs and two deprecated IDs; keep other media separate.

**Why NOT click "Import from /models" yet:** direct code audit `cheaper-inference/OmniRoute` release/v3.8.52 `src/app/(dashboard)/dashboard/providers/[id]/hooks/useModelImportHandlers.ts` finds `handleImportModels` fetches `/api/providers/<connectionId>/models?refresh=true` then loops all returned **new** models and creates each via `POST /api/provider-models`. This importer does not provide a per-model selection stage and its UI Free-only filtering must not be assumed to be a hard spend guard; bulk import can pull in audio and other inventory rows that the user did not request. Prefer targeted manual Custom creation for the two missing text specialists only **after live catalog verification**, and avoid Custom duplicates of existing Built-ins. Autocomplete/auto-fetch and auto-sync may change inventory and have not been enabled by user.

**Next desired phase:** user wants **all currently eligible free text models** in OmniRoute, one-by-one safe admission; first compare live 11-model API catalog IDs, then preserve the existing 4 eligible built-ins, create only 2 missing Prompt Guard entries if account actually exposes them, and check ALLaM individually if current free access verifiable. Test functional Gateway inference individually; keep specialist safety models out of normal chat and Web Vision Combos until needed. Separate connection-level PASS vs actual model Gateway completion PASS.

## Official source checks on 2026-10-29
- https://console.groq.com/docs/deprecations (compound shutdown 2026-09-21, Qwen 3.6 shutdown 2026-09-14)
- https://console.groq.com/docs/rate-limits (six free-tier text-input model rows, plus audio/tts)
- https://console.groq.com/docs/models (hosted model IDs and modalities, and enterprise restrictions)
- https://console.groq.com/docs/model/allam-2-7b (model card present, pricing Pending, Free availability uncertain)
- https://console.groq.com/docs/content-moderation (three text safety specialists)
