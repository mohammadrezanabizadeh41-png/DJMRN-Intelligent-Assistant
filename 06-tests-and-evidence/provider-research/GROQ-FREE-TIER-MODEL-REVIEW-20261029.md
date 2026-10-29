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
