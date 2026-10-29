# Hugging Face — DJMRN Account, API Token and Inference Providers / OmniRoute Handoff

## 2026-10-30 — HUGGINGFACE-FUTURE-PAID-OPTION-DEFERRED-20261030 — user decision to retain Hugging Face for future paid use

**Explicit user instruction (2026-10-30):** Preserve Hugging Face as an **optional, potentially economical paid Inference Providers gateway for a future DJMRN phase**, not a currently free production engine. Defer model onboarding, bulk import, any paid call, PRO subscription, purchased credits, custom provider billing, automatic recharge, or credit-card setup. Reassess vendor/provider model prices and ROI when the user actually approves a future paid budget. Keep existing no-spend, free-first routing as the current priority. **This is a documentation-only decision.**

### Status and evidence boundaries
- User's new screenshot from the installed OmniRoute v3.8.52 **Add HuggingFace API Key** modal showed a **masked** key and UI **Valid**. This proves a local key validation indicator, **not** that the user pressed Save, that the provider connection is persisted/active, or that any routed Gateway completion succeeded. User later requested that Hugging Face be 'saved for future use'; treat that as **research/project-decision persistence**, not permission to activate billing or inference.
- Suggested label `DJMRN-HuggingFace-Free` was an assistant proposal; actual OmniRoute saved connection name and ID **NOT OBSERVED**. Original user browser token label was `DJMRN-OmniRoute-HuggingFace` (existing historical screenshot); token value must never be stored. `Import only free models` checkbox was OFF in screenshot, and the assistant recommended turning it ON; save/toggle results unverified.
- Previous 2026-10-26 public hosted-chat snapshot was **132 model IDs across 267 model-provider routes**, **none** had confirmed `is_free=true` or both input/output prices 0. This is a **dated snapshot**, not a permanent guarantee that no free cloud API models exist. Downloading open-source model weights from the Hugging Face Hub is different from hosted/pay-as-you-go inference.
- **Updated official billing documentation checked 2026-10-30**: `https://huggingface.co/docs/inference-providers/pricing` and the corresponding official GitHub `huggingface/hub-docs:docs/inference-providers/pricing.md` state **Free Users: None** under included monthly credits; PRO and Team/Enterprise: $2 monthly (different eligibility). Thus supersede the earlier 2026-10-26 **$0.10/month HF Free inference credits** assumption: it is **outdated / not a verified current entitlement**. Free user has **no guaranteed monthly included hosted inference calls**. A `Valid` HF token is not free access evidence.
- HF-routed models are charged at upstream provider rates **without an additional Hugging Face markup** per current official policy. **Potential future economic value is a hypothesis**: compare exact current model+provider pricing, achievable throughput/latency, tool/vision quality, direct provider API pricing, payment/availability restrictions and runtime cost per task before choosing.
- Previous browser `Inference Providers > Settings` showed an editable **$300 monthly spending limit**. This is a risk indicator, **not a free allowance** or a verified hard $0 stop; whether it was saved is unconfirmed. Payment method status is **UNKNOWN**, and previous browser Billing overview showed usage $0 as of 2026-10-26 only.
- For future paid usage require **explicit owner approval** of a budget, verify current pricing, actual billing eligibility, payment method, account limits, spending cap behavior and account-specific remaining credits, configure fail-closed cost control and separate the paid family from free-only models. `Free` badge, `Import only free models` switch, and model open-source license **do not enforce zero cost**; custom provider key routes are billed by provider outside the HF routed monthly cap. Until then **no HF automatic production routing**.
- Candidate low-cost research examples from previous 2026-10-26 price snapshot: `Qwen/Qwen3-4B-Instruct-2507` (nscale), `Qwen/Qwen2.5-Coder-3B-Instruct` (nscale), `openai/gpt-oss-20b` (deepinfra), `google/gemma-4-26B-A4B-it` (deepinfra). **Do not treat those prior prices or availability as current**, and don't claim the candidates are free.
- Cross-provider working/validated model roster **remains 18**; Hugging Face contributes **zero verified operational model completions** so far. Distinguish provider account/token from live model route.

**Retrieval instruction for future DJMRN assistants:** Reopen this dossier, inspect actual OmniRoute Hugging Face connection status, read current `https://huggingface.co/docs/inference-providers/pricing`, current catalog/price data and billing controls, and obtain user approval **before** any cost-incurring experiment. Preserve the earlier Oct 26 screenshots/analysis as historical evidence rather than silently rewriting it.

---

## 2026-10-26 — VERIFIED BROWSER INFERENCE SETTINGS (USER SCREENSHOTS; PRIORITY ACCOUNT WARNING)

**Source:** Two user-submitted screenshots of their signed-in browser at `Settings → Inference Providers → Settings`, 2026-10-26. The current account's technical Free status/credit information comes from the other screenshots and vendor policy; no inference call performed.

### Billing/spending admission (CRITICAL for OmniRoute)
- The editable **Monthly spending limit for Inference Providers** field visibly displays **`$300`**, with a `Save` button. **This is a configured/visible spending cap**, **NOT** free credit, user balance, actual spending, remaining quota or a charge by itself. Whether it is a saved value rather than a prefilled/editable default is not independently proven beyond what the page displays; there is no Save action evidence for this conversation.
- On-screen vendor description (paraphrased): when total inference spending would exceed this limit, requests fail with error; **does NOT apply to providers with a custom key**.
- The same screen says HF-routed requests *without a custom provider key* are billed to the user's Hugging Face account, with a registered credit card required for metered billing; actual browser account's **Payment Information tab was not inspected** and no card-on-file is confirmed.
- An explicitly upsell banner offers PRO with **$2/month included credits** (paid subscription), which is NOT the current Free user's documented **$0.10/month** included promotional allowance. Do not confuse the two.
- **Immediate action requirement:** treat `$300` as **UNSAFE FOR DJMRN FREE-ONLY AUTOMATION**. Prior to a single call or adding a provider key, inspect `Billing → Payment Information` and determine whether a lower cap can be saved and which charges count (trial credit vs paid usage). No guaranteed `$0`/ `$0.10` setting behavior has been tested. Do not assert an untested zero-spend guarantee. Never purchase credits, add a card, activate PRO, or enable automatic recharge without explicit user approval.
- For future protected HF-only experimentation, consider requesting the user to set the lowest accepted restrictive spending cap **after** understanding whether it includes existing free credits. If $0 disables even promotional free inference, classify as `FREE_API_TEST_BLOCKED_BY_ZERO_CAP`, not a broken token. A $0.10 cap is not equivalent to no paid charges if the granted allowance is exhausted or the interpretation of cap changes. No cap was changed here.

### Provider routing settings, NOT evidence of free provider entitlements
- **18 UI provider rows visible** with blue enabled switches: `groq`, `novita`, `cerebras`, `nscale`, `fal`, `together-ai`, `fireworks-ai`, `featherless-ai`, `zai`, `replicate`, `cohere`, `scaleway`, `publicai`, `baseten`, `ovhcloud`, `deepinfra`, `wavespeed`, `hf-inference`. Slugs are normalized research labels for matching current HF routing API; actual internal API names/IDs need exact confirmation from live model catalog and HF UI. **Blue enable switches signal provider availability/allowance in user preferences, NOT free billing, upstream credentials, independent monthly allowance, price certainty or successful API request.**
- `Together AI` and `Fireworks` rows carry **`BILLING DISABLED`** banners in the screenshot, even though enabled switches are blue. These routes are explicitly **not confirmed usable** until billing/routing is independently resolved.
- `Last Used` in visible rows is `-`; no actual usage proven. The routing preference can be rearranged by dragging; HF model-page widgets favor the first compatible provider by default. Do not reorder blindly; dynamic default provider may pick paid-priced endpoints. **The API catalog snapshot in the preceding section** reflects 12 providers currently serving listed Chat models; the **18 settings toggles cover broader tasks/provider integrations** and must NOT be treated as 18 live Chat providers in our 267-route audit.
- In the custom-key setting, entering a `Groq`, `Cohere` or other upstream key means that provider may charge its own account, **outside the HF monthly spending cap and $0.10 HF credit**. DJMRN already has distinct upstream account API keys; connect them directly to installed **OmniRoute** instead of creating duplicate HF-mediated billing paths without a separate reason.
- **Policy outcome:** `HF_MODEL_CATALOG_PUBLIC_SNAPSHOT_ARCHIVED`; `BROWSER_TOKEN_CREATED_CONFIRMED`; `SPEND_LIMIT_VISIBLE_300_USD`; `PAYMENT_METHOD_UNKNOWN`; `CUSTOM_PROVIDER_KEYS_NOT_CONFIRMED`; `OMNIROUTE_INTEGRATION_PENDING`; `NO_AUTOMATIC_HF_PAID_ROUTES`.

### Next minimal user-side verification, not executed
1. Browser `Billing → Payment Information` — screenshot showing whether a payment method exists (obscure sensitive fields).
2. Browser `Billing → Subscriptions` — check actual Free vs PRO, paid features; the “Get PRO” upsell does not by itself substitute for this.
3. Revisit `Inference Providers → Settings` and agree on a safe cap behavior; do not experiment with dozens of paid-priced provider/model calls just to prove the cap. Record any user-saved change and live error semantics separately.
4. Then decide whether HF Free $0.10 credit can be spent for one tiny controlled **development-only** call without exposing user to paid usage; account eligibility and per-model prices require this user-bound test. User's broader goal is OmniRoute free-only automatic routing, not maximization of aggregate allowed paid spending.

**Source hierarchy:** screenshots establish UI state; https://huggingface.co/docs/inference-providers/pricing and https://huggingface.co/docs/inference-providers/hub-integration establish distinct HF routed/custom-key billing; https://huggingface.co/docs/hub/billing distinguishes credit, PRO, credit-card and pay-as-you-go.


## 2026-10-26 — LIVE FULL CHAT INFERENCE PROVIDERS MODEL/PRICE SNAPSHOT (LATEST, ACCOUNT-UNTESTED)

**What was really fetched:** Fresh unauthenticated public official `GET https://router.huggingface.co/v1/models`, via a web extraction proxy on 2026-10-26; parsed JSON, not a Google search snippet or a screenshot. **Data rows:** 132 distinct Chat-compatible model IDs, **267** model–provider listings across **12** provider names (`baseten`, `cerebras`, `cohere`, `deepinfra`, `featherless-ai`, `groq`, `novita`, `nscale`, `ovhcloud`, `publicai`, `scaleway`, `zai-org`); 267 with public status `live`; 171 live routes have numeric input **and** output rates; 96 live routes lack one/both rates.

**Critical free-status result:** **0 live listings with `is_free=true`**, **0 live listings with public input & output pricing both 0**. For the 267 live route listings in this specific capture, `is_free=false`=267, null/omitted=0. Thus **NO provider/model route independently confirmed zero-charge in this API snapshot**. This is a time-bound public API claim, **NOT** proof free trials of individual underlying vendors are unavailable. The HF Free account's **$0.10/month included Inference Providers credit (official policy, not account-specific remaining balance)** can offset token charges while it lasts; it is **NOT** free recurring per-model RPD or RPM. An HF account may use some paid-priced routes with its included credit. This is **not zero-priced inference**; keep separate flags:
- `HOSTED_CHAT=PUBLIC_LISTED` if in below table;
- `IS_FREE_PROVIDER_FLAG` exactly as returned, never derived from open-source weights or $0.10 promotional credits;
- `PRICED_USD_PER_1M_IN_TOKENS`, `PRICED_USD_PER_1M_OUT_TOKENS` (missing -> `UNKNOWN`, **not $0**);
- `ACCOUNT_TRIAL_ELIGIBLE=UNVERIFIED`, `ACCOUNT_MONTHLY_CREDIT_REMAINING=UNKNOWN`, `ACCOUNT_USABLE=NOT_TESTED`, `AUTOROUTE_FREE_ONLY=DENY` until enforced spending controls and actual tests.

**Verified browser-account status (user-supplied screenshots, separate from public API):** Browser HF personal account logged in; named `DJMRN-OmniRoute-HuggingFace` `FINEGRAINED` token has been **created** (previous screen showed `Inference` preset with `Make calls to Inference Providers` + `Make calls to Inference Endpoints`). Masked token shown, **no actual secret stored**. Token list says last used `-` as of snapshot. Billing Overview Oct 26: `Credits $0.00` (purchased credit balance), `Automatic Recharge -` (not a confirmed explicit setting), `Inference Usage $0.00`, current period ends Nov 1; Inference Providers Overview reports `No usage`. Account's **$0.10 free monthly credit is a public policy**, not a separately visible cash balance in these screenshots; don't infer absent from the purchased-credit $0.00 label. The Billing page shows PRO upsell but Subscriptions and Payment Information **not yet inspected**. The detailed usage panels in another screenshot said `Fetching usage...`, no totals from those panels established.

**No inference or OmniRoute call is claimed.** Models, provider attachment, scopes/quality, HTTP 200, support for particular paid credit, quota/429, cost-stop and commercial access require later user-side verification. The linked Hugging Face ChatGPT plugin is a different account than the browser; NEVER use plugin account metadata to assert user's browser entitlement.

### Working low-cost CANDIDATES FOR LATER TESTING, not free-marked

All prices below are from the **same public snapshot**, in **USD per 1 million input and output tokens**, and are paid-priced; the model/provider may exhaust free included credit. Only select if compatible, user-approved and a hard free-credit/purchase guard is actually verified. `Role` is a research hypothesis; no model quality benchmark was run.

| Exact model | Current provider | Input $/1M | Output $/1M | Context | Tool calls | Practical DJMRN candidate |
|---|---|---:|---:|---:|---:|---|
| `Qwen/Qwen3-4B-Instruct-2507` | `nscale` | 0.01 | 0.03 | 262144 | YES | Low-cost text candidate |
| `Qwen/Qwen3-4B-Thinking-2507` | `nscale` | 0.01 | 0.03 | 262144 | YES | Reasoning |
| `Qwen/Qwen2.5-Coder-3B-Instruct` | `nscale` | 0.01 | 0.03 | 32768 | NO | Coding |
| `Qwen/Qwen2.5-Coder-7B-Instruct` | `nscale` | 0.01 | 0.03 | 131072 | NO | Coding |
| `meta-llama/Llama-3.1-8B-Instruct` | `novita` | 0.02 | 0.05 | 16384 | NO | Low-cost text candidate |
| `google/gemma-3-4b-it` | `deepinfra` | 0.05 | 0.1 | 131072 | YES | Text/vision |
| `Qwen/Qwen3.5-9B` | `deepinfra` | 0.1 | 0.15 | 262144 | YES | Low-cost text candidate |
| `openai/gpt-oss-20b` | `deepinfra` | 0.03 | 0.14 | 131072 | YES | General tool-capable |
| `google/gemma-3-12b-it` | `deepinfra` | 0.05 | 0.15 | 131072 | YES | Text/vision |
| `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` | `nscale` | 0.05 | 0.05 | 131072 | NO | Reasoning |
| `CohereLabs/tiny-aya-earth` | `cohere` | UNKNOWN | UNKNOWN | UNKNOWN | NO | Persian multilingual |

**Price example only, not a promise of actual free call counts:** Qwen/Qwen3-4B-Instruct-2507 @ `nscale`, public `$0.01 / $0.03` per 1M in/out tokens, hypothetical one request of 1,000 input + 100 output tokens costs approximately `$0.000013` at listed text-token rate. HF $0.10 included would theoretically cover about 7,692 such identical requests *if* no other cost, identical tokenization, no billing minimum/surcharge, unchanged rates and account/provider entitlement. **This is math, not a verified quota, not account entitlement, and NOT authorization to spend or automate thousands of calls**. Need actual user-side rate-limit and billing screen.

### Full public `/v1/models` roster — exact model × provider rows (all 267 saved)

Schema: `input` and `output` = USD per **1 million tokens**, `context` in tokens, `tools/structured` are advertised support when known; unknown fields left UNKNOWN; `free` is the **provider's own `is_free` flag** and is NOT inferred from Free user signup. `modes` = declared input modalities. **No runtime API test or account model filter was run.**

| # | Exact model ID | Provider slug | is_free | $/1M input | $/1M output | Context | Tools | Structured output | Input modes | API status |
|---:|---|---|:---:|---:|---:|---:|:---:|:---:|---|---|
| 1 | `aisingapore/Nemotron-SEA-LION-v4.8-120B-A12B` | `publicai` | NO | 0.5 | 2 | 262144 | YES | NO | text | live |
| 2 | `alpindale/WizardLM-2-8x22B` | `novita` | NO | 0.62 | 0.62 | 65535 | NO | NO | text | live |
| 3 | `BSC-LT/ALIA-40b-instruct-2606` | `publicai` | NO | 0.3 | 0.6 | 65536 | YES | YES | text | live |
| 4 | `CohereLabs/aya-expanse-32b` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO | text | live |
| 5 | `CohereLabs/aya-vision-32b` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO | text+image | live |
| 6 | `CohereLabs/c4ai-command-a-03-2025` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 7 | `CohereLabs/c4ai-command-r-08-2024` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 8 | `CohereLabs/c4ai-command-r7b-12-2024` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 9 | `CohereLabs/c4ai-command-r7b-arabic-02-2025` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 10 | `CohereLabs/command-a-reasoning-08-2025` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 11 | `CohereLabs/command-a-translate-08-2025` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 12 | `CohereLabs/command-a-vision-07-2025` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | YES | text+image | live |
| 13 | `CohereLabs/tiny-aya-earth` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO | text | live |
| 14 | `CohereLabs/tiny-aya-fire` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO | text | live |
| 15 | `CohereLabs/tiny-aya-global` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO | text | live |
| 16 | `CohereLabs/tiny-aya-water` | `cohere` | NO | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO | text | live |
| 17 | `deepseek-ai/DeepSeek-R1` | `novita` | NO | 0.7 | 2.5 | 64000 | YES | YES | text | live |
| 18 | `deepseek-ai/DeepSeek-R1-0528` | `deepinfra` | NO | 0.5 | 2.15 | 163840 | YES | YES | text | live |
| 19 | `deepseek-ai/DeepSeek-R1-0528` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 20 | `deepseek-ai/DeepSeek-R1-0528` | `novita` | NO | 0.7 | 2.5 | 163840 | YES | YES | text | live |
| 21 | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 22 | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` | `nscale` | NO | 0.05 | 0.05 | 131072 | NO | YES | text | live |
| 23 | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 24 | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B` | `nscale` | NO | 0.2 | 0.2 | 131072 | NO | YES | text | live |
| 25 | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 26 | `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` | `nscale` | NO | 0.15 | 0.15 | 131072 | NO | NO | text | live |
| 27 | `deepseek-ai/DeepSeek-V3` | `deepinfra` | NO | 0.32 | 0.89 | 163840 | YES | YES | text | live |
| 28 | `deepseek-ai/DeepSeek-V3-0324` | `deepinfra` | NO | 0.24 | 0.9 | 163840 | YES | YES | text | live |
| 29 | `deepseek-ai/DeepSeek-V3-0324` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 30 | `deepseek-ai/DeepSeek-V3.1` | `deepinfra` | NO | 0.25 | 0.95 | 163840 | YES | YES | text | live |
| 31 | `deepseek-ai/DeepSeek-V3.1` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 32 | `deepseek-ai/DeepSeek-V3.1-Terminus` | `deepinfra` | NO | 0.27 | 0.95 | 163840 | YES | YES | text | live |
| 33 | `deepseek-ai/DeepSeek-V3.1-Terminus` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 34 | `deepseek-ai/DeepSeek-V3.2` | `deepinfra` | NO | 0.26 | 0.38 | 163840 | YES | YES | text | live |
| 35 | `deepseek-ai/DeepSeek-V4-Flash` | `deepinfra` | NO | 0.09 | 0.18 | 1048576 | YES | YES | text | live |
| 36 | `deepseek-ai/DeepSeek-V4-Flash` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 37 | `deepseek-ai/DeepSeek-V4-Flash-0731` | `baseten` | NO | 0.13 | 0.26 | 1048576 | YES | YES | text | live |
| 38 | `deepseek-ai/DeepSeek-V4-Flash-0731` | `deepinfra` | NO | 0.06 | 0.18 | 1048576 | YES | YES | text | live |
| 39 | `deepseek-ai/DeepSeek-V4-Flash-0731` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 40 | `deepseek-ai/DeepSeek-V4-Flash-0731` | `novita` | NO | 0.44 | 1.32 | 1048576 | YES | NO | text | live |
| 41 | `deepseek-ai/DeepSeek-V4-Flash-0731` | `scaleway` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 42 | `deepseek-ai/DeepSeek-V4-Flash-Vision-Exp` | `deepinfra` | NO | 0.44 | 1.32 | 1048576 | YES | YES | text+image | live |
| 43 | `deepseek-ai/DeepSeek-V4-Pro` | `deepinfra` | NO | 1.3 | 2.6 | 1048576 | YES | YES | text | live |
| 44 | `deepseek-ai/DeepSeek-V4-Pro` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 45 | `deepseek-ai/DeepSeek-V4-Pro` | `novita` | NO | 1.6 | 3.2 | 1048576 | YES | NO | text | live |
| 46 | `deepseek-ai/DeepSeek-V4-Pro-0813` | `baseten` | NO | 1.32 | 3.96 | 1048576 | YES | NO | text | live |
| 47 | `deepseek-ai/DeepSeek-V4-Pro-0813` | `deepinfra` | NO | 1.3 | 2.6 | 1048576 | YES | YES | text | live |
| 48 | `deepseek-ai/DeepSeek-V4-Pro-0813` | `novita` | NO | 1.32 | 3.96 | 1048576 | YES | NO | text | live |
| 49 | `deepseek-ai/DeepSeek-V4.1-Flash` | `baseten` | NO | 0.3 | 1.2 | 1048576 | YES | YES | text+image | live |
| 50 | `deepseek-ai/DeepSeek-V4.1-Flash` | `deepinfra` | NO | 0.2 | 0.6 | 1048576 | YES | YES | text+image | live |
| 51 | `deepseek-ai/DeepSeek-V4.1-Flash` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 52 | `deepseek-ai/DeepSeek-V4.1-Flash` | `novita` | NO | 0.3 | 1.2 | 1048576 | YES | NO | text+image | live |
| 53 | `deepseek-ai/DeepSeek-V4.1-Flash-1017` | `baseten` | NO | 0.3 | 1.2 | 1048576 | YES | YES | text+image | live |
| 54 | `deepseek-ai/DeepSeek-V4.1-Flash-1017` | `novita` | NO | 0.3 | 1.2 | 1048576 | YES | NO | text+image | live |
| 55 | `google/gemma-3-12b-it` | `deepinfra` | NO | 0.05 | 0.15 | 131072 | YES | YES | text+image | live |
| 56 | `google/gemma-3-12b-it` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 57 | `google/gemma-3-27b-it` | `deepinfra` | NO | 0.08 | 0.16 | 131072 | YES | YES | text+image | live |
| 58 | `google/gemma-3-27b-it` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 59 | `google/gemma-3-4b-it` | `deepinfra` | NO | 0.05 | 0.1 | 131072 | YES | YES | text+image | live |
| 60 | `google/gemma-3-4b-it` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 61 | `google/gemma-4-26B-A4B-it` | `deepinfra` | NO | 0.07 | 0.34 | 262144 | YES | YES | text+image | live |
| 62 | `google/gemma-4-26B-A4B-it` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 63 | `google/gemma-4-26B-A4B-it` | `novita` | NO | 0.13 | 0.4 | 262144 | YES | NO | text+image | live |
| 64 | `google/gemma-4-26B-A4B-it` | `scaleway` | NO | 0.285 | 0.57 | UNKNOWN | YES | YES | text+image | live |
| 65 | `google/gemma-4-31B-it` | `deepinfra` | NO | 0.2 | 0.4 | 262144 | YES | YES | text+image | live |
| 66 | `google/gemma-4-31B-it` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 67 | `google/gemma-4-31B-it` | `novita` | NO | 0.14 | 0.4 | 262144 | YES | YES | text+image | live |
| 68 | `ibm-granite/granite-4.2-30b` | `deepinfra` | NO | 0.16 | 0.65 | 131072 | YES | NO | text | live |
| 69 | `ibm-granite/granite-4.2-3b` | `deepinfra` | NO | 0.03 | 0.12 | 131072 | YES | NO | text | live |
| 70 | `ibm-granite/granite-4.2-8b` | `deepinfra` | NO | 0.06 | 0.25 | 131072 | YES | NO | text | live |
| 71 | `inclusionAI/Ling-3.0-flash` | `novita` | NO | 0.06 | 0.18 | 262144 | YES | NO | text | live |
| 72 | `inclusionAI/Ling-3.0-flash-Fin` | `novita` | NO | 0.075 | 0.22 | 262144 | YES | NO | text | live |
| 73 | `inclusionAI/Ling-3.0-flash-VL` | `novita` | NO | 0.075 | 0.22 | 262144 | YES | NO | text+image | live |
| 74 | `inclusionAI/Ling-3.1-flash` | `novita` | NO | 0.3 | 0.9 | 262144 | YES | NO | text | live |
| 75 | `meta-llama/Llama-3.1-8B-Instruct` | `deepinfra` | NO | 0.02 | 0.05 | 131072 | YES | NO | text | live |
| 76 | `meta-llama/Llama-3.1-8B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 77 | `meta-llama/Llama-3.1-8B-Instruct` | `novita` | NO | 0.02 | 0.05 | 16384 | NO | NO | text | live |
| 78 | `meta-llama/Llama-3.1-8B-Instruct` | `nscale` | NO | 0.06 | 0.06 | 131072 | NO | YES | text | live |
| 79 | `meta-llama/Llama-3.3-70B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 80 | `meta-llama/Llama-3.3-70B-Instruct` | `novita` | NO | 0.135 | 0.4 | 12288 | YES | NO | text | live |
| 81 | `meta-llama/Llama-3.3-70B-Instruct` | `ovhcloud` | NO | 0.74 | 0.74 | 131072 | YES | YES | text | live |
| 82 | `meta-llama/Llama-3.3-70B-Instruct` | `scaleway` | NO | 1.026 | 1.026 | UNKNOWN | YES | YES | text | live |
| 83 | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | `novita` | NO | 0.27 | 0.85 | 1048576 | NO | YES | text+image | live |
| 84 | `meta-llama/Llama-4-Scout-17B-16E-Instruct` | `nscale` | NO | 0.09 | 0.29 | 890000 | YES | YES | text+image | live |
| 85 | `meta-llama/Llama-Guard-4-12B` | `deepinfra` | NO | 0.18 | 0.18 | 163840 | NO | NO | text+image | live |
| 86 | `meta-models/Muse-Glimmer-30B` | `deepinfra` | NO | 0.3 | 1.2 | 131072 | YES | YES | text+image | live |
| 87 | `meta-models/Muse-Glimmer-30B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 88 | `meta-models/Muse-Spark-Open-816B-A42B` | `baseten` | NO | 1.25 | 4.25 | 1048576 | YES | NO | text+image | live |
| 89 | `microsoft/phi-4` | `deepinfra` | NO | 0.07 | 0.14 | 16384 | NO | YES | text | live |
| 90 | `microsoft/phi-4` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 91 | `MiniMaxAI/MiniMax-M1-80k` | `novita` | NO | 0.55 | 2.2 | 1000000 | YES | NO | text | live |
| 92 | `MiniMaxAI/MiniMax-M2.5` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 93 | `MiniMaxAI/MiniMax-M2.5` | `novita` | NO | 0.3 | 1.2 | 204800 | YES | NO | text | live |
| 94 | `MiniMaxAI/MiniMax-M2.7` | `deepinfra` | NO | 0.25 | 1 | 196608 | YES | YES | text | live |
| 95 | `MiniMaxAI/MiniMax-M2.7` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 96 | `MiniMaxAI/MiniMax-M2.7` | `novita` | NO | 0.3 | 1.2 | 204800 | YES | NO | text | live |
| 97 | `MiniMaxAI/MiniMax-M3` | `deepinfra` | NO | 0.28 | 1.1 | 524288 | YES | YES | text+image | live |
| 98 | `MiniMaxAI/MiniMax-M3` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 99 | `MiniMaxAI/MiniMax-M3` | `novita` | NO | 0.3 | 1.2 | 1000000 | YES | NO | text+image | live |
| 100 | `MiniMaxAI/MiniMax-M3.1-Flash` | `novita` | NO | 0.15 | 0.6 | 1000000 | YES | NO | text+image | live |
| 101 | `moonshotai/Kimi-K2-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 102 | `moonshotai/Kimi-K2-Instruct` | `novita` | NO | 0.57 | 2.3 | 131072 | YES | NO | text | live |
| 103 | `moonshotai/Kimi-K2-Instruct-0905` | `novita` | NO | 0.6 | 2.5 | 262144 | YES | YES | text | live |
| 104 | `moonshotai/Kimi-K2.5` | `deepinfra` | NO | 0.45 | 2.25 | 262144 | YES | YES | text+image | live |
| 105 | `moonshotai/Kimi-K2.5` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 106 | `moonshotai/Kimi-K2.5` | `novita` | NO | 0.6 | 3 | 262144 | YES | YES | text+image | live |
| 107 | `moonshotai/Kimi-K2.6` | `deepinfra` | NO | 0.75 | 3.5 | 262144 | YES | YES | text+image | live |
| 108 | `moonshotai/Kimi-K2.6` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 109 | `moonshotai/Kimi-K2.6` | `novita` | NO | 0.8 | 3.4 | 262144 | YES | NO | text+image | live |
| 110 | `moonshotai/Kimi-K2.7-Code` | `deepinfra` | NO | 0.68 | 3.4 | 262144 | YES | YES | text+image | live |
| 111 | `moonshotai/Kimi-K2.7-Code` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 112 | `moonshotai/Kimi-K2.7-Code` | `novita` | NO | 0.95 | 4 | 262144 | YES | YES | text+image | live |
| 113 | `moonshotai/Kimi-K3` | `baseten` | NO | 3 | 15 | 1048576 | YES | YES | text+image | live |
| 114 | `moonshotai/Kimi-K3` | `deepinfra` | NO | 2.85 | 14.25 | 1048576 | YES | YES | text+image | live |
| 115 | `moonshotai/Kimi-K3` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 116 | `NousResearch/Hermes-3-Llama-3.1-70B` | `deepinfra` | NO | 0.7 | 0.7 | 131072 | NO | YES | text | live |
| 117 | `NousResearch/Hermes-3-Llama-3.1-70B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 118 | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16` | `deepinfra` | NO | 1 | 5 | 262144 | YES | YES | text | live |
| 119 | `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4` | `baseten` | NO | 0.2 | 0.5 | 1048576 | YES | YES | text+image | live |
| 120 | `openai/gpt-oss-120b` | `baseten` | NO | 0.1 | 0.5 | 128072 | YES | YES | text | live |
| 121 | `openai/gpt-oss-120b` | `cerebras` | NO | 0.35 | 0.75 | 131072 | YES | YES | text | live |
| 122 | `openai/gpt-oss-120b` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 123 | `openai/gpt-oss-120b` | `groq` | NO | 0.15 | 0.75 | 131072 | YES | YES | text | live |
| 124 | `openai/gpt-oss-120b` | `novita` | NO | 0.05 | 0.25 | 131072 | YES | YES | text | live |
| 125 | `openai/gpt-oss-120b` | `nscale` | NO | 0.1 | 0.4 | 131072 | YES | YES | text | live |
| 126 | `openai/gpt-oss-120b` | `ovhcloud` | NO | 0.09 | 0.47 | 131072 | YES | YES | text | live |
| 127 | `openai/gpt-oss-120b` | `scaleway` | NO | 0.171 | 0.684 | UNKNOWN | YES | YES | text | live |
| 128 | `openai/gpt-oss-20b` | `deepinfra` | NO | 0.03 | 0.14 | 131072 | YES | YES | text | live |
| 129 | `openai/gpt-oss-20b` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 130 | `openai/gpt-oss-20b` | `groq` | NO | 0.1 | 0.5 | 131072 | YES | YES | text | live |
| 131 | `openai/gpt-oss-20b` | `nscale` | NO | 0.05 | 0.2 | 131072 | YES | YES | text | live |
| 132 | `openai/gpt-oss-20b` | `ovhcloud` | NO | 0.05 | 0.18 | 131072 | YES | NO | text | live |
| 133 | `openai/gpt-oss-safeguard-20b` | `groq` | NO | UNKNOWN | UNKNOWN | 131072 | YES | YES | text | live |
| 134 | `Qwen/Qwen2.5-72B-Instruct` | `deepinfra` | NO | 0.36 | 0.4 | 32768 | YES | YES | text | live |
| 135 | `Qwen/Qwen2.5-72B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 136 | `Qwen/Qwen2.5-Coder-32B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 137 | `Qwen/Qwen2.5-Coder-32B-Instruct` | `nscale` | NO | 0.06 | 0.2 | 131072 | NO | YES | text | live |
| 138 | `Qwen/Qwen2.5-Coder-3B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 139 | `Qwen/Qwen2.5-Coder-3B-Instruct` | `nscale` | NO | 0.01 | 0.03 | 32768 | NO | YES | text | live |
| 140 | `Qwen/Qwen2.5-Coder-7B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 141 | `Qwen/Qwen2.5-Coder-7B-Instruct` | `nscale` | NO | 0.01 | 0.03 | 131072 | NO | YES | text | live |
| 142 | `Qwen/Qwen2.5-VL-72B-Instruct` | `ovhcloud` | NO | 1.01 | 1.01 | 32768 | NO | YES | text+image | live |
| 143 | `Qwen/Qwen3-14B` | `deepinfra` | NO | 0.12 | 0.24 | 40960 | YES | YES | text | live |
| 144 | `Qwen/Qwen3-14B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 145 | `Qwen/Qwen3-14B` | `nscale` | NO | 0.07 | 0.2 | 40960 | YES | YES | text | live |
| 146 | `Qwen/Qwen3-235B-A22B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 147 | `Qwen/Qwen3-235B-A22B` | `nscale` | NO | 0.2 | 0.6 | 32000 | YES | YES | text | live |
| 148 | `Qwen/Qwen3-235B-A22B-Instruct-2507` | `deepinfra` | NO | 0.09 | 0.55 | 262144 | YES | YES | text | live |
| 149 | `Qwen/Qwen3-235B-A22B-Instruct-2507` | `nscale` | NO | 0.2 | 0.6 | 32768 | YES | YES | text | live |
| 150 | `Qwen/Qwen3-235B-A22B-Instruct-2507` | `scaleway` | NO | 0.855 | 2.565 | UNKNOWN | YES | YES | text | live |
| 151 | `Qwen/Qwen3-235B-A22B-Thinking-2507` | `deepinfra` | NO | 0.23 | 2.3 | 262144 | YES | YES | text | live |
| 152 | `Qwen/Qwen3-235B-A22B-Thinking-2507` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 153 | `Qwen/Qwen3-30B-A3B` | `deepinfra` | NO | 0.12 | 0.5 | 40960 | YES | YES | text | live |
| 154 | `Qwen/Qwen3-32B` | `deepinfra` | NO | 0.08 | 0.28 | 40960 | YES | YES | text | live |
| 155 | `Qwen/Qwen3-32B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 156 | `Qwen/Qwen3-32B` | `nscale` | NO | 0.08 | 0.25 | 40960 | YES | YES | text | live |
| 157 | `Qwen/Qwen3-4B-Instruct-2507` | `nscale` | NO | 0.01 | 0.03 | 262144 | YES | YES | text | live |
| 158 | `Qwen/Qwen3-4B-Thinking-2507` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 159 | `Qwen/Qwen3-4B-Thinking-2507` | `nscale` | NO | 0.01 | 0.03 | 262144 | YES | YES | text | live |
| 160 | `Qwen/Qwen3-8B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 161 | `Qwen/Qwen3-8B` | `nscale` | NO | 0.07 | 0.18 | 40960 | YES | YES | text | live |
| 162 | `Qwen/Qwen3-Next-80B-A3B-Instruct` | `deepinfra` | NO | 0.09 | 1.1 | 262144 | YES | YES | text | live |
| 163 | `Qwen/Qwen3-Next-80B-A3B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 164 | `Qwen/Qwen3-VL-235B-A22B-Instruct` | `deepinfra` | NO | 0.2 | 0.88 | 262144 | YES | YES | text+image | live |
| 165 | `Qwen/Qwen3-VL-30B-A3B-Instruct` | `deepinfra` | NO | 0.15 | 0.6 | 262144 | YES | YES | text+image | live |
| 166 | `Qwen/Qwen3-VL-30B-A3B-Instruct` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 167 | `Qwen/Qwen3-VL-30B-A3B-Instruct` | `novita` | NO | 0.2 | 0.7 | 131072 | YES | YES | text+image | live |
| 168 | `Qwen/Qwen3.5-122B-A10B` | `deepinfra` | NO | 0.29 | 2.4 | 262144 | YES | YES | text+image | live |
| 169 | `Qwen/Qwen3.5-122B-A10B` | `novita` | NO | 0.4 | 3.2 | 262144 | YES | NO | text+image | live |
| 170 | `Qwen/Qwen3.5-27B` | `deepinfra` | NO | 0.26 | 2.6 | 262144 | YES | YES | text+image | live |
| 171 | `Qwen/Qwen3.5-27B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 172 | `Qwen/Qwen3.5-27B` | `novita` | NO | 0.3 | 2.4 | 262144 | YES | NO | text+image | live |
| 173 | `Qwen/Qwen3.5-35B-A3B` | `deepinfra` | NO | 0.14 | 1 | 262144 | YES | YES | text+image | live |
| 174 | `Qwen/Qwen3.5-35B-A3B` | `novita` | NO | 0.25 | 2 | 262144 | YES | NO | text+image | live |
| 175 | `Qwen/Qwen3.5-397B-A17B` | `deepinfra` | NO | 0.45 | 3 | 262144 | YES | YES | text+image | live |
| 176 | `Qwen/Qwen3.5-397B-A17B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 177 | `Qwen/Qwen3.5-397B-A17B` | `novita` | NO | 0.6 | 3.6 | 262144 | YES | NO | text+image | live |
| 178 | `Qwen/Qwen3.5-397B-A17B` | `ovhcloud` | NO | 0.71 | 4.25 | 262144 | YES | YES | text+image | live |
| 179 | `Qwen/Qwen3.5-397B-A17B` | `scaleway` | NO | 0.684 | 4.104 | UNKNOWN | YES | YES | text+image | live |
| 180 | `Qwen/Qwen3.5-9B` | `deepinfra` | NO | 0.1 | 0.15 | 262144 | YES | YES | text+image | live |
| 181 | `Qwen/Qwen3.5-9B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 182 | `Qwen/Qwen3.5-9B` | `ovhcloud` | NO | 0.12 | 0.18 | 262144 | YES | YES | text+image | live |
| 183 | `Qwen/Qwen3.6-27B` | `deepinfra` | NO | 0.32 | 3.2 | 262144 | YES | YES | text+image | live |
| 184 | `Qwen/Qwen3.6-27B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 185 | `Qwen/Qwen3.6-27B` | `ovhcloud` | NO | 0.47 | 3.19 | 262144 | YES | YES | text+image | live |
| 186 | `Qwen/Qwen3.6-35B-A3B` | `deepinfra` | NO | 0.1 | 0.95 | 262144 | YES | YES | text+image | live |
| 187 | `Qwen/Qwen3.6-35B-A3B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 188 | `Qwen/Qwen3.6-35B-A3B` | `scaleway` | NO | 0.285 | 1.71 | UNKNOWN | YES | YES | text+image | live |
| 189 | `Qwen/Qwen3.8-2.4T-A95B` | `deepinfra` | NO | 2 | 6 | 262144 | YES | YES | text | live |
| 190 | `Qwen/Qwen3.8-2.4T-A95B` | `novita` | NO | 2 | 6 | 1000000 | YES | NO | text | live |
| 191 | `Qwen/Qwen3.8-27B` | `cerebras` | NO | 0.99 | 1.49 | 65536 | YES | YES | text+image | live |
| 192 | `Qwen/Qwen3.8-27B` | `deepinfra` | NO | 0.2 | 2.5 | 262144 | YES | YES | text+image | live |
| 193 | `Qwen/Qwen3.8-27B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 194 | `Qwen/Qwen3.8-27B` | `novita` | NO | 0.42 | 3 | 1000000 | YES | YES | text+image | live |
| 195 | `Qwen/Qwen3.8-27B` | `ovhcloud` | NO | 0.47 | 3.19 | 262144 | YES | NO | text+image | live |
| 196 | `reflection/Beam-1.0-501B-A23B` | `baseten` | NO | 0.4 | 1.2 | 1048576 | YES | YES | text | live |
| 197 | `Sao10K/L3-8B-Stheno-v3.2` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 198 | `Sao10K/L3-8B-Stheno-v3.2` | `novita` | NO | 0.05 | 0.05 | 8192 | NO | NO | text | live |
| 199 | `speakleash/Bielik-11B-v3.0-Instruct` | `publicai` | NO | 0.4 | 0.4 | UNKNOWN | YES | NO | text | live |
| 200 | `stepfun-ai/Step-3.5-Flash` | `deepinfra` | NO | 0.1 | 0.3 | 262144 | YES | YES | text | live |
| 201 | `stepfun-ai/Step-3.5-Flash` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 202 | `stepfun-ai/Step-3.7-Flash` | `deepinfra` | NO | 0.2 | 1.15 | 262144 | YES | YES | text+image | live |
| 203 | `stepfun-ai/Step-3.7-Flash` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 204 | `swiss-ai/Apertus-70B-Instruct-2509` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 205 | `swiss-ai/Apertus-70B-Instruct-2509` | `publicai` | NO | 0.82 | 2.92 | UNKNOWN | YES | YES | text | live |
| 206 | `swiss-ai/Apertus-8B-Instruct-2509` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 207 | `swiss-ai/Apertus-8B-Instruct-2509` | `publicai` | NO | 0.1 | 0.2 | UNKNOWN | NO | YES | text | live |
| 208 | `swiss-ai/Apertus-v1.5-70B` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 209 | `swiss-ai/Apertus-v1.5-70B` | `publicai` | NO | 0.82 | 2.92 | UNKNOWN | YES | YES | text+image | live |
| 210 | `tencent/Hy3` | `deepinfra` | NO | 0.13 | 0.53 | 262144 | YES | YES | text | live |
| 211 | `tencent/Hy3` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 212 | `tencent/Hy4-preview` | `deepinfra` | NO | 0.834 | 2.501 | 1048576 | YES | YES | text | live |
| 213 | `tencent/Hy4-preview` | `novita` | NO | 0.834 | 2.501 | 1000000 | YES | YES | text | live |
| 214 | `thinkingmachines/Inkling` | `deepinfra` | NO | 0.95 | 4.05 | 524288 | YES | YES | text+image | live |
| 215 | `thinkingmachines/Inkling-Small` | `deepinfra` | NO | 0.45 | 1.2 | 524288 | YES | YES | text+image | live |
| 216 | `XiaomiMiMo/MiMo-V2.5` | `deepinfra` | NO | 0.14 | 0.28 | 262144 | YES | YES | text | live |
| 217 | `XiaomiMiMo/MiMo-V2.5-Pro` | `deepinfra` | NO | 1 | 3 | 1048576 | YES | YES | text | live |
| 218 | `XiaomiMiMo/MiMo-V2.6-Flash-RL` | `novita` | NO | 0.14 | 0.28 | 1048576 | YES | NO | text | live |
| 219 | `XiaomiMiMo/MiMo-V2.6-Pro-RL` | `novita` | NO | 0.435 | 0.87 | 1048576 | YES | NO | text | live |
| 220 | `zai-org/AutoGLM-Phone-9B-Multilingual` | `novita` | NO | 0.035 | 0.138 | 65536 | NO | NO | text+image | live |
| 221 | `zai-org/GLM-4.5-Air` | `novita` | NO | 0.13 | 0.85 | 131072 | YES | NO | text | live |
| 222 | `zai-org/GLM-4.5-Air` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 223 | `zai-org/GLM-4.5V` | `novita` | NO | 0.6 | 1.8 | 65536 | YES | NO | text+image | live |
| 224 | `zai-org/GLM-4.5V` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text+image | live |
| 225 | `zai-org/GLM-4.5V-FP8` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text+image | live |
| 226 | `zai-org/GLM-4.6` | `deepinfra` | NO | 0.5 | 2 | 202752 | YES | YES | text | live |
| 227 | `zai-org/GLM-4.6` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 228 | `zai-org/GLM-4.6` | `novita` | NO | 0.55 | 2.2 | 204800 | YES | NO | text | live |
| 229 | `zai-org/GLM-4.6` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 230 | `zai-org/GLM-4.6V` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text+image | live |
| 231 | `zai-org/GLM-4.6V-Flash` | `novita` | NO | 0.3 | 0.9 | 131072 | YES | NO | text+image | live |
| 232 | `zai-org/GLM-4.6V-Flash` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text+image | live |
| 233 | `zai-org/GLM-4.6V-FP8` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text+image | live |
| 234 | `zai-org/GLM-4.7` | `deepinfra` | NO | 0.4 | 1.75 | 202752 | YES | YES | text | live |
| 235 | `zai-org/GLM-4.7` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 236 | `zai-org/GLM-4.7` | `novita` | NO | 0.6 | 2.2 | 204800 | YES | NO | text | live |
| 237 | `zai-org/GLM-4.7-Flash` | `deepinfra` | NO | 0.06 | 0.4 | 202752 | YES | YES | text | live |
| 238 | `zai-org/GLM-4.7-Flash` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 239 | `zai-org/GLM-4.7-Flash` | `novita` | NO | 0.07 | 0.4 | 200000 | YES | NO | text | live |
| 240 | `zai-org/GLM-4.7-Flash` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 241 | `zai-org/GLM-4.7-FP8` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 242 | `zai-org/GLM-5` | `deepinfra` | NO | 0.6 | 2.08 | 202752 | YES | YES | text | live |
| 243 | `zai-org/GLM-5` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 244 | `zai-org/GLM-5` | `novita` | NO | 1 | 3.2 | 202800 | YES | NO | text | live |
| 245 | `zai-org/GLM-5` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 246 | `zai-org/GLM-5.1` | `deepinfra` | NO | 1.05 | 3.5 | 202752 | YES | YES | text | live |
| 247 | `zai-org/GLM-5.1` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 248 | `zai-org/GLM-5.1-FP8` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 249 | `zai-org/GLM-5.2` | `baseten` | NO | 1.4 | 4.4 | 1048576 | YES | YES | text | live |
| 250 | `zai-org/GLM-5.2` | `deepinfra` | NO | 0.75 | 2.4 | 1048576 | YES | YES | text | live |
| 251 | `zai-org/GLM-5.2` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 252 | `zai-org/GLM-5.2` | `novita` | NO | 1.4 | 4.4 | 1048576 | YES | YES | text | live |
| 253 | `zai-org/GLM-5.2` | `scaleway` | NO | 2.052 | 6.27 | UNKNOWN | YES | YES | text | live |
| 254 | `zai-org/GLM-5.2` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 255 | `zai-org/GLM-5.2-FP8` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | NO | text | live |
| 256 | `zai-org/GLM-5.3` | `baseten` | NO | 1.4 | 4.4 | 1048576 | YES | YES | text | live |
| 257 | `zai-org/GLM-5.3` | `deepinfra` | NO | 0.9 | 4 | 1048576 | YES | YES | text | live |
| 258 | `zai-org/GLM-5.3` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text | live |
| 259 | `zai-org/GLM-5.3` | `novita` | NO | 1.4 | 4.4 | 1048576 | YES | YES | text | live |
| 260 | `zai-org/GLM-5.3` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 261 | `zai-org/GLM-5.3-BF16` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text | live |
| 262 | `zai-org/GLM-5.3-Flash` | `baseten` | NO | 0.15 | 0.5 | 1048576 | YES | YES | text+image | live |
| 263 | `zai-org/GLM-5.3-Flash` | `deepinfra` | NO | 0.15 | 0.5 | 1048576 | YES | NO | text+image | live |
| 264 | `zai-org/GLM-5.3-Flash` | `featherless-ai` | NO | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | text+image | live |
| 265 | `zai-org/GLM-5.3-Flash` | `novita` | NO | 0.15 | 0.5 | 1048576 | YES | YES | text+image | live |
| 266 | `zai-org/GLM-5.3-Flash` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text+image | live |
| 267 | `zai-org/GLM-5.3-Flash-BF16` | `zai-org` | NO | UNKNOWN | UNKNOWN | UNKNOWN | YES | YES | text+image | live |

### OmniRoute import and routing safeguards

1. **Use only exact model IDs in this table** as research labels. When configuring HF Inference Providers, OpenAI-compatible API base is `https://router.huggingface.co/v1` and for chat `/chat/completions`, authenticated with the user-owned private HF token. Never commit or ask the user to paste a full token. Provider suffix syntax in official docs supports `model:provider` for pinning providers; confirm exact spelling against the live model metadata before saving in OmniRoute. Do not use `:fastest` or `:cheapest` blindly: cheapest can still incur paid usage, fastest can route to expensive upstream.
2. **Keep the 12 providers separate logically for price analysis; their model routes are NOT 12 independent included free-credit grants.** All HF-routed requests debit the same HF account monthly included balance; "custom provider key" mode instead charges the upstream account according to its terms. This is important because some of the same upstream vendors (Groq/Cohere) also have direct DJMRN keys.
3. Since **0 confirmed zero-charge routes** exist in this public snapshot, an unrestricted OmniRoute `FREE_ONLY` Combo should **not** automatically include these HF paths based on this snapshot. Trial usage through included $0.10 must be treated as **CREDIT-LIMITED_EVALUATION / HUMAN-APPROVED** and only if cap/stop controls are demonstrably safe.
4. To refresh later without spending inference tokens, use `GET https://router.huggingface.co/v1/models` for current provider flags/costs, and `GET https://huggingface.co/api/models?inference_provider=all` for non-chat model discovery. **The latter is not covered by the 132-Chat count** (image/audio/embedding tasks require their own catalog, adapters, distinct price/quota checks).
5. First user-side check upon returning to OmniRoute: browser `Inference Providers → Settings` and `Billing → Payment Information / Subscriptions`, then native provider add of existing token (private), one tiny non-sensitive test only with user approval, verify billed usage/remaining credit, retry/429 behavior and cost stop. Keep exact prior `DJMRN-Persian-L1` AI Horde Combo and Agno state intact.

**Independent authoritative source documents:** HF [List OpenAI-compatible hosted models with optional provider flags](https://huggingface.co/docs/inference-providers/hub-api), [Price and free monthly credit](https://huggingface.co/docs/inference-providers/pricing), [HF OpenAI-compatible Chat and provider pinning](https://huggingface.co/docs/inference-providers/index), [Hosted Hub model discovery](https://huggingface.co/docs/inference-providers/hub-integration). Public live API capture date: 2026-10-26. **No Pay/PRO/Add Credits action requested or performed.**


**Recorded 2026-10-26; source:** user-provided authenticated browser dashboard screenshot; current official Hugging Face docs linked below.  
**Provider queue position:** #8 (last of the currently planned onboarding phase), after Cohere; NVIDIA remains blocked pending support/manual phone-verification.  
**Current state (2026-10-26):** `BROWSER_ACCOUNT_LOGGED_IN / TOKEN_CREATE_PENDING / TOKEN_NAME_PROPOSED / MODEL_CATALOG_PUBLIC_DOCS_VERIFIED / ACCOUNT_FREE_CREDITS_NOT_SCREENSHOT_CONFIRMED / PAID_FEATURES_NOT_APPROVED / API_INFERENCE_NOT_TESTED / OMNIROUTE_NOT_CONNECTED`.
**Scope:** User requested a provider-specific file in the main **implementation project** GitHub repository alongside existing provider onboarding dossiers. This is the sole provider-specific record for Hugging Face; do not duplicate in Freelance or Research Bridge. No HF credentials, OTPs, email addresses, personal profile URL, access token prefixes, secret suffixes or screenshots with tokens.

## 1. Browser-account evidence and progress

- On 2026-10-26, user submitted screenshot of a **signed-in Hugging Face home/feed**, including sidebar `Profile`, `Inbox`, `Settings`, `Billing`, `Get PRO`. Account login **verified by screenshot**; **no trial inference token was confirmed created**, and no API usage was shown.
- Screenshot does **not** prove this browser account's paid/Free billing plan, remaining monthly credit, or API token permissions. A `Get PRO` link is not a billing/plan verification.
- **Important identity gate:** a separately linked Hugging Face OAuth plugin was observed to authenticate as a **different account handle than the account shown in the browser screenshot**. This plugin's scopes are read/profile/MCP/jobs and **do not include a confirmed Inference Providers token permission**. Do NOT mix these two identities or assume the linked connector OAuth credential is the browser account's personal inference token. The user should use the **browser account being configured** for token and billing/screenshots. Avoid recording both identifying handles in public GitHub.
- **Suggested token label only, not an issued token:** `DJMRN-OmniRoute-HuggingFace`. Exact created key name, role, date and permissions **PENDING USER SCREENSHOT**.
- Direct creation entry: https://huggingface.co/settings/tokens ; inside browser `Settings → Access Tokens → Create new token`.
- Exact recommended new token config: role **Fine-grained**, enable **Make calls to Inference Providers**. Unneeded repository write, organization admin and deployment scopes OFF. On creation, store secret only in user-controlled local secure store / OmniRoute private Provider credential; never in GitHub or chat.

## 2. Free account and billing — verified official policy, NOT verified individual balance

**Primary current official source:** https://huggingface.co/docs/inference-providers/pricing (checked 2026-10-26).
- Standard **Free** user: **US$0.10 credit per month**, explicitly `subject to change`, usable on **Inference Providers**. PRO user: **US$2.00/month**, also subject to plan details. THIS IS A **SHARED MONETARY MONTHLY CREDIT**, **NOT** a per-model free daily request count or universally zero-cost endpoint.
- Inference Providers routes are **usage-priced** at the serving provider's rates (Hugging Face states no markup). Thus even open-weight models hosted on HF can exhaust the $0.10 included balance. After credits are depleted, **additional purchased credits / paid usage** would be required. Do NOT enable, buy credits, add payment details, or upgrade without specific user approval; never configure a fallback whose price/charging behavior is unknown.
- Adding a **bank card** does not, by itself, prove an increase in the FREE included monthly credit. Buying credits enables extra paid usage rather than changing the standard Free monthly entitlement. No billing methods/actual account charges verified.
- `Routed by Hugging Face`: HF account is billed, monthly HF credit applied automatically, no separate upstream provider account needed. `Custom Provider Key` (bring own API key): calls may be relayed but are billed **by the external provider**, not by Hugging Face, and **do not use the HF monthly credits**. Since DJMRN already has direct Groq/Cohere/etc. accounts, avoid double counting or assuming their free quotas become additional HF free credit.
- HF docs mention >200 available hosted models across partnered inference providers, but that **does not mean 200 free models**. Open Hugging Face model repositories are **not the same** as hosted, callable, free inference APIs. Personal account eligibility, remaining balance, reset moment/timezone, quotas, whether a payment method is saved and current provider prices remain **UNKNOWN** until browser screens and actual queries.

### Actual user-account checkpoints STILL REQUIRED
1. HF browser `Settings → Access Tokens`: after token creation, confirm **label**, **fine-grained type**, **inference permission**, **created status**; mask any token material.
2. `Settings → Billing` / `Settings → Inference Providers`: Free/PRO plan, currently included and remaining monthly dollar credit, consumption breakdown per model/provider, paid credit balance and payment settings. **Do not infer** from the other linked HF plugin identity.
3. `Settings → Inference Providers`: provider preference, custom external keys (if any), and chosen accounting route (HF-routed or external custom key).
4. Never store full token, partial secret, personal email, account ID or account handle in this **public** repo. Only create/verification status and nonsecret assigned project label belong here.

## 3. Current Inference Providers API integration technical contract (official docs)

- **OpenAI-compatible Chat endpoint (for OmniRoute evaluation):** `https://router.huggingface.co/v1/chat/completions`, base URL `https://router.huggingface.co/v1`; Header `Authorization: Bearer <USER_PRIVATE_HF_FINE_GRAINED_TOKEN>`. This OpenAI-compatible compatibility mode is presently documented for **chat completions**; don't assume embeddings/image/audio routes use this same path.
- **GET models public API:** `https://router.huggingface.co/v1/models` lists chat-completion served models and provider metadata such as provider status, pricing, context length, and tools/structured-output support when available. Access to the live JSON from assistant's web access was **NOT VERIFIED** (tool returned unavailable); save extraction as **PENDING LIVE MODEL CATALOG ENUMERATION**, not a finished 200-model audit.
- **Alternative Hub models API:** `https://huggingface.co/api/models?inference_provider=all` with optional pipeline/tag filters. The `hf models ls --warm --json` CLI also enumerates models served by at least one provider. The same Hub contains countless downloadable weights NOT served by Inference Providers. `inference_provider=all` should be treated as hosted metadata only; not a free-price filter.
- **Routing policy suffixes documented:** `:fastest` (default), `:cheapest`, `:preferred`, or `:<specific-provider>`, appended to model ID. `:cheapest` means *cheapest among offered paid rates*, **NOT FREE**, and `:fastest` can choose a higher-priced upstream automatically. Thus for DJMRN use a vetted exact `model:provider` mapping when needed, compare published per-provider prices and verify cost cap before automatic OmniRoute activation.
- **Example IDs present in official docs, not confirmed available under this account/key today:** `openai/gpt-oss-120b` (documented chat example), `deepseek-ai/DeepSeek-R1`, `deepseek-ai/DeepSeek-V3-0324`. Model existence on public Hub, examples, routing/provider availability and free entitlement are **distinct gates**; never choose targets solely based on example strings.
- **Supported provider families (2026 docs, not claim that free/account enabled):** Cerebras, Cohere, Groq, HF Inference, Novita, Together, Fireworks, DeepInfra, Nscale, OVHcloud AI Endpoints, Z.ai, etc. Hugging Face is an *aggregator* as well as a model Hub; it does **not** grant independently separate free usage quotas across all upstream partners.
- **Security/privacy:** Hugging Face says it does not store request/response bodies when routing and retains debugging logs for up to 30 days, but third-party upstream providers have distinct privacy policies; no assurance on all intermediaries without reviewing provider terms. Source: https://huggingface.co/docs/inference-providers/security .
- **Legacy:** do not assume old `api-inference.huggingface.co/models/...` endpoint is the primary current multi-provider Chat path. Prefer current router base and verify OmniRoute 3.8.52's native HF Provider configuration and auth on the actual installed UI.

## 4. DJMRN free-budget / model-discovery rules to preserve before OmniRoute

| Domain | Verified/public | Individual-account state / outcome |
|---|---|---|
| Standard included HF Free monthly inference credit | $0.10/month, subject to change | User's exact remaining credit/reset not observed |
| Daily free requests per model | **No blanket daily number established** | UNKNOWN, must not invent |
| Per-model/token price (in/out), context, tool support | Available by public model+provider metadata where supplied | **NOT extracted row-by-row; PENDING** |
| HF model catalog versus callable hosted models | Different sets | Don't assume all public repo weights are API-callable |
| HF billing versus custom upstream provider key | Different billing authorities; HF $0.10 applies only to HF-routed requests | Confirm any custom provider keys/account setup |
| Production suitability | Pricing and provider terms apply; cloud billing may be metered | UNKNOWN / no production activation |
| Token, inference and OmniRoute | `fine-grained` + inference permission is official docs | `TOKEN_NOT_YET_CREATED_CONFIRMED`, no request |
| Actual zero-paid protection after $0.10 exhausted | **No verified configured hard stop in OmniRoute** | STOP if payment/purchased credits or paid fallback possible |
| First tested role grouping | DJMRN existing `DJMRN-Persian-L1` one AI Horde model with real HTTP 200, separate historical evidence | **NO HF model inside it yet**, no automatic failover |

**Bounded next test, not executed:** after creation/confirmation and while no paid credit/billing exists, inspect current `GET /v1/models`, choose one actually served and low-priced compatible text model, send one tiny synthetic Chat request via HF direct or installed OmniRoute, observe response/http status/actual provider, cost/credit change; classify `FREE_CREDIT_USED` not `UNLIMITED_FREE`. Preserve remaining cents; no expensive 200+ call sweep.

## 5. Task continuation / phase boundary

1. **Now (user in browser):** Settings → Access Tokens → Create new token; `Fine-grained`; label `DJMRN-OmniRoute-HuggingFace`; check **Make calls to Inference Providers**; finish generation, securely save secret. A screenshot of **masked token list only** confirms issue without exposure. Next followup should request the next browser form to guide precisely.
2. Then browser Billing and Inference Providers settings snapshots: verify plan/credit/payment/usage and available provider routing. Account credits and model pricing are not shown by the initial screenshot.
3. Complete this dossier's PENDING fields upon user-provided evidence; issue **one GitHub update only when user requests saving it**, no secret.
4. **Then return to OmniRoute**: reconcile prior Gemini/Groq/OpenRouter/Mistral/Cloudflare/Cohere/HF free model catalog, quota and reset terms; add upstream keys privately, enumerate actual usable models, one-call smoke each, then build/extend capability-based named Combos. Don't create one Combo per model unless the use case demands it. Model success, no paid leakage and 429/failover testing needed; Agno downstream after routed inference.
5. Preserve NVIDIA status `PHONE_VERIFICATION_BLOCKED / SUPPORT_EMAIL_SENT / API_KEY_NOT_CREATED` separately; no delay for provider list.
6. Do not copy this provider dossier to Notion/Research-Bridge/Freelance. Primary operational continuity and daily status normally belongs to `07-operations-and-continuity/CURRENT-STATUS.md` under single-record policy; user specifically asked for this provider dossier beside the other provider-specific files.

## 6. Official references read/reviewed on 2026-10-26
- Token instructions and required Inference Providers fine-grained permission: https://huggingface.co/docs/inference-providers/index
- HF access-token security and separate-per-app tokens: https://huggingface.co/docs/hub/security-tokens
- Monthly Free/PRO credit, purchased credits, custom provider key distinction: https://huggingface.co/docs/inference-providers/pricing
- Router Chat API and provider suffix semantics: https://huggingface.co/docs/inference-providers/index
- Model list and API/CLI discovery: https://huggingface.co/docs/inference-providers/hub-api
- Provider selection/Hub filtered models: https://huggingface.co/docs/inference-providers/hub-integration
- Provider security and debug log caveats: https://huggingface.co/docs/inference-providers/security
- Settings tokens page: https://huggingface.co/settings/tokens
- Inference Providers settings (user-login): https://huggingface.co/settings/inference-providers
- Inference Playground: https://huggingface.co/playground
- Authored provider queue: [DJMRN Free Cloud API Provider Queue](DJMRN-FREE-CLOUD-API-KEY-QUEUE-2026-10-26.md)

**Evidence grading:** `USER_SCREENSHOT` for login; `OFFICIAL_PUBLIC_DOC` for API, pricing/authorization; `HF_CONNECTOR_DIFFERENT_ACCOUNT_OBSERVED` not equal to browser account; `PENDING` for token creation, user plan/balance, full live model/price catalog, all inference, OmniRoute.
