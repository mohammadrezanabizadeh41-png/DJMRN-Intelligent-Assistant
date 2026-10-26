# DJMRN — Free Cloud API Provider Onboarding Queue
Date: 2026-10-26
Status: Research queue; no keys stored; not proof of account creation or OmniRoute connection.

## Objective
Shared dynamic pool of free cloud models behind OmniRoute, usable by Agno agents without per-agent token rationing. Capability-based model selection, account/provider quota awareness, random/weighted distribution among suitable models, automatic failover for 429/outage, and zero unexpected paid usage. Permissions per agent concern model/tool/data access, not fixed token allotments.

## Provider onboarding queue (one by one)
1. Google Gemini API — existing keys reportedly available; verify models and project-level free quotas; do not create duplicate keys unnecessarily. https://aistudio.google.com/api-keys
2. GroqCloud — create key; verify free-model catalog and account limits. https://console.groq.com/keys
3. OpenRouter — create key; filter :free models; limits shared across free models/account. https://openrouter.ai/settings/keys
4. Mistral AI Studio — free mode; verify available models and current org limits. https://console.mistral.ai/
5. Cloudflare Workers AI — daily free Neurons; verify account/token and eligible models. https://dash.cloudflare.com/
6. NVIDIA API Catalog — developer/prototyping access; check model quotas and commercial-use conditions. https://build.nvidia.com/explore/discover
7. Cohere — trial key; verify limits and commercial-use eligibility. https://dashboard.cohere.com/api-keys
8. Hugging Face — investigate current inference credits; not assumed to provide recurring free production inference. https://huggingface.co/settings/tokens

## DeepSeek and related candidates
DeepSeek is a MODEL DEVELOPER and API provider. Official DeepSeek API pricing is token-billed, not verified as a recurring free API tier; large concurrency or context is not free daily token allowance. Official: https://api-docs.deepseek.com/quick_start/pricing/ and https://api-docs.deepseek.com/quick_start/rate_limit/ . Investigate DeepSeek models hosted on free-tier third-party APIs (e.g. OpenRouter :free, NVIDIA NIM trial, others), checking current exact model ID, limits, terms and production permission. Additional candidate providers to audit separately: Z.AI/GLM, SambaNova, Cerebras (trial vs recurring), SiliconFlow, AMD Radeon Cloud, LLM7; do not treat third-party quota claims as verified until official docs and account dashboards confirm.

## Operational rules
For each provider: create account/key manually, store secrets only locally in OmniRoute/approved secret store; record key status without secret value; confirm free eligible model IDs, quota units and reset time, whether quota is account/project-level, billing/overage behavior, privacy/commercial terms, OpenAI-compatible endpoint, test request, 429 failover and routing policies. Do not auto-register, pay, or activate billable features. No keys in GitHub.
