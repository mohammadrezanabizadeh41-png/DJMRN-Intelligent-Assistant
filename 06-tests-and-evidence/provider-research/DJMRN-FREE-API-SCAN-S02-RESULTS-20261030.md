# DJMRN — Free hosted model API eligibility scan S02 of S09

**Research date:** 2026-10-30. **Locked OmniRoute v3.8.52 API-key source rows:** 31–60. **Question only:** Does each provider publish a genuinely free, repeating hosted MODEL inference API allowance, rather than a one-time trial, short-term promo, paid inference with free gateway shell, or free website chat?

**Status:** 30/30 rows screened against publicly accessible operator pricing/docs, operator GitHub/blog or closest evidence. **14 qualifying, source-supported recurring-free public candidates:** 13 advertised recurring free API model/request allocations and 1 renewable free inference credit. The rest are paid, temporary, conditionally key-funded, PoW-gated/unverified, or app-only. **Public terms are not proof of DJMRN account entitlement or successful API inference**. No API keys, model calls, payments, signups, billing settings or installed OmniRoute configurations changed.

**Evidence caution:** For Chat Oripe, the operator advertises 2M free tokens monthly but the service/account and claimed model provenance are untested. FreeInference logs and may publish anonymized prompts (research service), making it unsuitable for confidential data without approval. ChatAnywhere states non-commercial free API restriction. OrcaRouter requires historical GitHub identity for a no-payment route. BazaarLink defaults to PAID fallback when account is funded unless `X-Free-Fallback: false` is used. g4f.space proxy's PoW proof-of-work credits do not count as unconditional recurring free API. Qiniu's current free offer expires November 30, 2026.

## All 30 providers, no omissions

| Catalog # | Provider ID | Provider | Research status | Evidence and limitations | Source | Evidence strength |
|---:|---|---|---|---|---|---|
| 31 | `cloudcode-one` | CloudCode.ONE | `KEY_REQUIRES_CREDIT_OR_COUPON` | Free model IDs were previously mentioned, but official key provisioning requires a deposit or coupon. No unconditional no-payment API access verified. | [Operator / audit source](https://cloudcode.one/) | OFFICIAL |
| 32 | `ofoxai` | OfoxAI | `TEMPORARY_PROMO_ONLY` | Ofox offers $0 promotional models, but its operator describes Qwen Image 3.0 Pro :free as explicitly limited-time/quota-limited, not a renewing committed free API tier. Its free desktop client is not free inference. | [Operator / audit source](https://ofox.ai/blog/qwen-image-3-0-pro-free-api-2026/) | OFFICIAL |
| 33 | `zerolimitai` | ZeroLimitAI | `TRIAL_ONLY` | Developer API free for 7 days (25 calls/day); normal API is included with annual paid plan. Not renewable after trial. | [Operator / audit source](https://www.zerolimitai.com/) | OFFICIAL |
| 34 | `chatanywhere` | ChatAnywhere | `RECURRING_FREE_API` | Operator GitHub offers free API key (GitHub-linked) with renewable points and daily requests; README gives 50,000 points/week, 100 requests/day and separately up to 200 requests/day per IP/key. Free use is personal/educational/noncommercial ONLY; conflicting caps should be verified in account. | [Operator / audit source](https://github.com/chatanywhere/GPT_API_free) | OPERATOR_REPO |
| 35 | `helyxai` | Helyx AI | `RECURRING_FREE_API` | Official site offers OpenAI-compatible model API and 100,000 free tokens per day; no evidence of mandatory purchase for Free plan. | [Operator / audit source](https://helyxai.space/api) | OFFICIAL |
| 36 | `auriko` | Auriko | `PLATFORM_FREE_INFERENCE_PAID` | Free $0 routing plan charges pay-as-you-go model API inference; 1000 platform RPM is capacity, not free model calls. BYOK uses separately billed upstream keys. | [Operator / audit source](https://www.auriko.ai/platform/pricing) | OFFICIAL |
| 37 | `poixe-ai` | Poixe AI | `RECURRING_FREE_API` | Operator blog documents daily-reset no-pay API models with :free suffix: large group 2 RPM/5 RPD and small group 20 RPM/50 RPD; model lineup may change. Public blog is dated 2025, newer model eligibility must be checked in account. | [Operator / audit source](https://blog.poixe.com/303/) | OPERATOR_BLOG |
| 38 | `naga-ai` | Naga AI | `RECURRING_FREE_API` | Published Free pricing lists 10+ $0 models with 10 RPM/100 RPD for chat/API; nonzero-paid models require paid account credits. | [Operator / audit source](https://naga.ac/pricing) | OFFICIAL |
| 39 | `chat-oripe` | Chat Oripe | `RECURRING_FREE_API` | Official site's published free tier advertises OpenAI-compatible API and 2,000,000 tokens/month with no card. No actual calls tested; provider legitimacy, claimed hosted models and access are UNVERIFIED; high due-diligence priority. | [Operator / audit source](https://api.oriper.com/docs) | OFFICIAL_CLAIM_UNTESTED |
| 40 | `freeinference` | FreeInference | `RECURRING_FREE_API` | Operator offers hosted OpenAI-compatible API with no card for research/open-source/education, free model endpoints and account keys. No permanent fixed numeric quota; application/approval, 18+ age and logging/research data sharing. NOT safe for confidential user data. | [Operator / audit source](https://freeinference.org/) | OFFICIAL_RESEARCH_RESTRICTED |
| 41 | `free-ai` | Free.ai | `RECURRING_FREE_API` | Free accounts: 30,000 self-hosted-model tokens/day plus API maximum 1,000 calls/month (60 RPM) as explicitly published in /api. Premium/external models billed separately; avoid automatic overage. | [Operator / audit source](https://free.ai/api/) | OFFICIAL |
| 42 | `dgrid` | DGrid | `RECURRING_FREE_API` | Official DGrid Free Models Router dgridai/free: free Standard tier at 10 RPM / 100 RPD per account. $5 qualifying top-up ONLY to upgrade limits (20 RPM / 1000 RPD), not required for standard free route. | [Operator / audit source](https://docs.dgrid.ai/ai-gateway/free-models-router) | OFFICIAL |
| 43 | `qiniu` | Qiniu | `TEMPORARY_PROMO_ONLY` | Conatus free model campaign 2026-10-24 through 2026-11-30, daily free tokens for identity-verified accounts. Explicit termination date; not long-term renewing free API. Unverified Chinese real-name verification eligibility. | [Operator / audit source](https://www.qiniu.com/ai/free-models/conatus-2026) | OFFICIAL_TIMEBOXED |
| 44 | `orcarouter` | OrcaRouter | `RECURRING_FREE_API` | Official offers page lists rotating zero-price API models without trial clock, but access requires established GitHub account/history link OR any paid purchase. First no-payment path depends on meeting GitHub eligibility; no quota promise. | [Operator / audit source](https://www.orcarouter.ai/offers) | OFFICIAL_CONDITIONAL_GITHUB |
| 45 | `api-airforce` | Api.airforce | `RECURRING_FREE_API` | Official Free $0/month tier gives model API access to basic/free models, 1 RPM / up to 1000 RPD. Model :free requires exact catalog variant; per-day token caps may also apply. | [Operator / audit source](https://api.airforce/pricing/) | OFFICIAL |
| 46 | `crof` | CrofAI | `PAID_ONLY` | Official pricing: token-metered pay-as-you-go. Free account registration is not a no-cost model inference allowance. | [Operator / audit source](https://crof.ai/pricing) | OFFICIAL |
| 47 | `bazaarlink` | BazaarLink | `RECURRING_FREE_API` | Official API docs: selected models get recurring free quota, base 10 RPM/60 daily units per free model (long contexts may consume multiple units); auto:free routing. DANGER: if account funded, default over-quota may silently fall back to PAID; send X-Free-Fallback:false. | [Operator / audit source](https://bazaarlink.ai/en/docs) | OFFICIAL_PAID_FALLBACK_RISK |
| 48 | `synthetic` | Synthetic | `PAID_ONLY` | Official Synthetic API either subscription $30/month or pay-per-token usage; the $24 weekly credits regenerate within PAID subscription, not a $0 free plan. | [Operator / audit source](https://synthetic.new/pricing) | OFFICIAL |
| 49 | `kilo-gateway` | Kilo Gateway | `RECURRING_FREE_API` | Kilo Gateway offers :free hosted models with $0 tokens; official gateway docs allow anonymous/free calls subject to up to 200 requests/hour/IP, no paid model fallback implied. | [Operator / audit source](https://kilo.ai/docs/gateway/authentication) | OFFICIAL |
| 50 | `wafer` | Wafer AI | `PAID_ONLY` | Wafer serverless model inference page lists paid input/output token rates and enterprise dedicated capacity; no published renewable $0 model API quota identified. | [Operator / audit source](https://wafer.ai/) | OFFICIAL_NO_FREE_CLAIM |
| 51 | `opencode-zen` | OpenCode Zen | `NO_FREE_EXTERNAL_API` | Official OpenCode states its free-tier chat models require use INSIDE OpenCode; direct API from other clients (OmniRoute) uses paid models or Go. Free UI/coding use does not qualify. | [Operator / audit source](https://opencode.ai/v2/docs/console/models) | OFFICIAL_EXPLICIT |
| 52 | `opencode-go` | OpenCode Go | `PAID_SUBSCRIPTION_ONLY` | OpenCode Go is a $10/month (or higher) subscription for API, even though some model names include Free promotional access under the subscribed plan; not free independent API. | [Operator / audit source](https://opencode.ai/v2/docs/console/go/) | OFFICIAL |
| 53 | `dahl` | Dahl | `TRIAL_ONLY` | New account receives a one-time welcome pool of 100,000,000 tokens, manually allocated to the issued key; new key starts at zero. No renewed automatic monthly/daily free token grant documented; paid top-ups thereafter. | [Operator / audit source](https://inference.dahl.global/docs/authentication/) | OFFICIAL |
| 54 | `freetheai` | FreeTheAi | `RECURRING_FREE_API` | Official limits: 50 free requests/day to email-confirmed account, +50 if Discord linked, reset at 00:00 UTC; daily check-in unlocks free models. OpenAI-compatible API key at freetheai.org. | [Operator / audit source](https://docs.freetheai.org/concepts/limits) | OFFICIAL_CHECKIN |
| 55 | `g4f-groq` | g4f.space — Groq | `POW_CREDIT_GATED_UNVERIFIED` | Anonymous g4f.space Groq route returned 402 without proof-of-work 'cake' credits; service docs also discuss member key. No guaranteed repeatable zero-effort/zero-payment model API tier confirmed; other direct Groq provider is distinct. | [Operator / audit source](https://github.com/diegosouzapw/OmniRoute/issues/10071) | UPSTREAM_402_REPORT |
| 56 | `g4f-gemini` | g4f.space — Gemini | `POW_CREDIT_GATED_UNVERIFIED` | Same third-party g4f.space family requires PoW cake credits or member key; not equivalent to official Gemini free API nor a currently proven replenishing free API entitlement. | [Operator / audit source](https://github.com/diegosouzapw/OmniRoute/issues/10071) | UPSTREAM_402_REPORT |
| 57 | `g4f-pollinations` | g4f.space — Pollinations | `POW_CREDIT_GATED_UNVERIFIED` | g4f.space proxy returned 402 for anonymous calls until PoW cake credits; direct Pollinations endpoint is a separate service and does not prove this third-party proxy is free. | [Operator / audit source](https://github.com/diegosouzapw/OmniRoute/issues/10071) | UPSTREAM_402_REPORT |
| 58 | `g4f-ollama` | g4f.space — Ollama | `POW_CREDIT_GATED_UNVERIFIED` | g4f.space Ollama hosted proxy anonymous calls gated by PoW cake credits or membership; no unconditionally free regular account API quota evidenced. | [Operator / audit source](https://github.com/diegosouzapw/OmniRoute/issues/10071) | UPSTREAM_402_REPORT |
| 59 | `g4f-nvidia` | g4f.space — NVIDIA | `POW_CREDIT_GATED_UNVERIFIED` | g4f.space NVIDIA proxy anonymous calls gated by PoW cake credits or membership. Official NVIDIA API is distinct; not added as no-payment recurring gateway. | [Operator / audit source](https://github.com/diegosouzapw/OmniRoute/issues/10071) | UPSTREAM_402_REPORT |
| 60 | `vercel-ai-gateway` | Vercel AI Gateway | `RECURRING_FREE_CREDIT` | Official Vercel docs updated Sep 8 2026 show $5 monthly AI Gateway credits for Free tier, restricted to eligible models, without BYOK; buying paid credits transitions to paid tier and forfeits recurring $5 benefit. | [Operator / audit source](https://vercel.com/docs/ai-gateway/pricing) | OFFICIAL |

## S02 positive-only IDs (for canonical master merge)

- #34 `chatanywhere` — ChatAnywhere — RECURRING_FREE_API — https://github.com/chatanywhere/GPT_API_free
- #35 `helyxai` — Helyx AI — RECURRING_FREE_API — https://helyxai.space/api
- #37 `poixe-ai` — Poixe AI — RECURRING_FREE_API — https://blog.poixe.com/303/
- #38 `naga-ai` — Naga AI — RECURRING_FREE_API — https://naga.ac/pricing
- #39 `chat-oripe` — Chat Oripe — RECURRING_FREE_API — https://api.oriper.com/docs
- #40 `freeinference` — FreeInference — RECURRING_FREE_API — https://freeinference.org/
- #41 `free-ai` — Free.ai — RECURRING_FREE_API — https://free.ai/api/
- #42 `dgrid` — DGrid — RECURRING_FREE_API — https://docs.dgrid.ai/ai-gateway/free-models-router
- #44 `orcarouter` — OrcaRouter — RECURRING_FREE_API — https://www.orcarouter.ai/offers
- #45 `api-airforce` — Api.airforce — RECURRING_FREE_API — https://api.airforce/pricing/
- #47 `bazaarlink` — BazaarLink — RECURRING_FREE_API — https://bazaarlink.ai/en/docs
- #49 `kilo-gateway` — Kilo Gateway — RECURRING_FREE_API — https://kilo.ai/docs/gateway/authentication
- #54 `freetheai` — FreeTheAi — RECURRING_FREE_API — https://docs.freetheai.org/concepts/limits
- #60 `vercel-ai-gateway` — Vercel AI Gateway — RECURRING_FREE_CREDIT — https://vercel.com/docs/ai-gateway/pricing

## Classification summary

- `KEY_REQUIRES_CREDIT_OR_COUPON`: 1
- `TEMPORARY_PROMO_ONLY`: 2
- `TRIAL_ONLY`: 2
- `RECURRING_FREE_API`: 13
- `PLATFORM_FREE_INFERENCE_PAID`: 1
- `PAID_ONLY`: 3
- `NO_FREE_EXTERNAL_API`: 1
- `PAID_SUBSCRIPTION_ONLY`: 1
- `POW_CREDIT_GATED_UNVERIFIED`: 5
- `RECURRING_FREE_CREDIT`: 1

## Do not count these as qualified free API

- **OfoxAI** has an operator-documented limited-time promotional free image model; not a sustainable ongoing API guarantee. Static OmniRoute `hasFree:true` alone is not enough.
- **Qiniu** has a real daily-reset promotion through 2026-11-30, conditional on Chinese real-name account verification; this is time-limited, not ongoing.
- **CloudCode.ONE** formerly advertised a free pair of models but its main site now requires paid credit or coupon for key issuance. Not a guaranteed no-payment API.
- **OpenCode Zen** free models require the OpenCode client; other direct API consumers must pay. OpenCode Go is subscription-only.
- **Five g4f.space proxy rows** are NOT the same as Groq/Gemini/NVIDIA/Ollama/Pollinations direct official free plans. Reported 402 PoW cake credits; no evidence of guaranteed free replenishment suitable for OmniRoute automation.

## Publication/source limitations and next action

- No provider account, key or free balance was verified in the user's own account. A valid key can still be denied or billed for a model.
- A negative search is not an authoritative proof that a provider never offers a private promotion; PAID_ONLY means current published offerings lack an unconditional recurring free hosted model API.
- Recheck live quotas and billing behaviors before connecting any new provider. Avoid free tiers restricted to non-commercial use for paid freelance tasks.
- Link this scan to [cumulative positive master](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md). S01 contains 20 previous positive candidates, S02 adds exactly 14 new unique provider IDs: cumulative **34**. S03–S09 not researched.
