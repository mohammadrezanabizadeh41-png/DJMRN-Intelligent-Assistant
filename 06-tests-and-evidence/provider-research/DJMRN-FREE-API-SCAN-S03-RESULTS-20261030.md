# DJMRN — Stage S03 (rows 61–90) | recurring truly free hosted model API scan

**Research date:** 2026-10-30. **Status:** all **30/30** provider IDs examined for the single question 'does this provider have recurring genuinely free hosted MODEL API access, rather than just startup trial/paid usage?'. **5 positive public-source candidates**; other entries categorized transparently (including unverified, paid, web-only and temporary promotion). No user account/API-key/inference verification performed. No paid experiment, billing activation or site registration.

**Authoritative roster:** [252 API-key providers, OmniRoute v3.8.52](OMNIROUTE-252-APIKEY-PROVIDER-CATALOG-V3852-20261030.md) and [9-stage manifest](OMNIROUTE-FREE-API-252-NINE-STAGE-RESEARCH-PLAN-20261030.md). Frozen Stage 03 IDs correspond to catalog rows 61–90. This report uses dated operator public pricing/FAQ/docs, or clearly-labeled secondary sources only if the operator website is inaccessible.

**Critical distinction:** `RECURRING_FREE_API` = a published recurring $0 hosted model API route/credit available without payment, with caps or free-model rotation. Does NOT mean permanent guarantee, ability to sign up in user's region, commercial rights, independent inference success or no paid fallback. `UNVERIFIED` means no sufficient evidence of recurrence, NOT proof of paid-only.

## Full 30-provider results

| # | Provider ID | Provider name | Classification | Published basis and free-vs-trial qualification | Source | Evidence class |
|---:|---|---|---|---|---|---|
| 61 | `llm7` | LLM7.io | `RECURRING_FREE_API` | Free developer token: 100,000 combined input/output tokens per rolling 24h; 1 request/s, 60/min, 250/hour. Educational/research service and capacity not guaranteed. | [Read source](https://llm7.io/) | `OFFICIAL` |
| 62 | `llamagate` | LlamaGate | `UNVERIFIED` | Primary llamagate.ai site could not be opened; third-party 2026 catalog lists only positive per-token charges. No renewable zero-priced API model verified. | [Read source](https://models.litellm.ai/providers/llamagate) | `SECONDARY_ONLY` |
| 63 | `gitlawb` | Gitlawb Opengateway (MiMo) | `PAID_ROUTE_WITH_SEPARATE_FREE_MODEL` | Named MiMo v2.5 route is priced by tokens; its shared Gitlawb gateway now has a separate Nemotron 3 Ultra :free route. The MiMo provider entry itself is NOT a free MiMo API entitlement. | [Read source](https://gitlawb.com/opengateway) | `OFFICIAL_SHARED_GATEWAY` |
| 64 | `gitlawb-gmi` | Gitlawb Opengateway (GMI Cloud) | `RECURRING_FREE_API` | Official shared Opengateway currently advertises nvidia/nemotron-3-ultra-550b-a55b:free, zero input/cache/output prices, rate-limited, no credits needed. This GMI-type entry is a match to the free NVIDIA route; static OmniRoute registry 3.8.52 contains superseded 2026-06 'promo ended' note; live Gateway test pending. | [Read source](https://gitlawb.com/opengateway) | `OFFICIAL_CHANGED_SINCE_REGISTRY` |
| 65 | `nanogpt` | NanoGPT | `NO_FREE_EXTERNAL_API` | Official pricing: its one free model is available on WEB only. OpenAI-compatible hosted API is pay-as-you-go tokens, even though platform fee is $0/month. | [Read source](https://nano-gpt.com/pricing) | `OFFICIAL` |
| 66 | `nan` | NaN.Builders | `PAID_ONLY` | OpenAI-compatible hosted inference key requires paid nan_member subscription (€70/month) or premium (€200/month). Free signup does not yield inference access. | [Read source](https://nan.builders/) | `OFFICIAL` |
| 67 | `aimlapi` | AI/ML API | `PAID_ONLY` | Current official FAQ states no free plan and free model tier paused; add prepaid account balance to use models. | [Read source](https://help.aimlapi.com/article/22-managing-your-subscription) | `OFFICIAL` |
| 68 | `novita` | Novita AI | `TRIAL_ONLY` | Operator offers first-time signup credit (historically $0.50) and referral credits, not a renewable no-payment quota for each account. | [Read source](https://blogs.novita.ai/free-llm-api-comparison-2026/) | `OFFICIAL` |
| 69 | `piapi` | PiAPI | `TRIAL_ONLY` | Free $0 subscription explicitly provides NO recurring free API credits. New accounts get $0.50 signup balance; calls metered afterwards. | [Read source](https://piapi.ai/pricing) | `OFFICIAL` |
| 70 | `getgoapi` | GoAPI | `UNVERIFIED_CONFLICTING` | Free pricing matrix says 'free models only', but terms explicitly define 1M free tokens for NEW users and per-model API calls metered. No named ongoing zero-cost API models/reset rule independently verified; exclude pending clarification. | [Read source](https://getgoapi.com/en/terms) | `OFFICIAL_CONFLICTING` |
| 71 | `laozhang` | LaoZhang AI | `TRIAL_ONLY` | Official API Terms: registration/test credits for connectivity verification only. Hosted third-party model inference is prepaid PAYG and does not inherit upstream free tiers. | [Read source](https://www.laozhang.ai/terms) | `OFFICIAL` |
| 72 | `thebai` | TheB.AI | `UNVERIFIED` | Operator theb.ai site returned 502; third-party comparison reports pay-as-you-go and a possible unquantified freemium tier, without verifying a recurring free model API allocation. | [Read source](https://www.uprouter.online/s/thebai) | `SECONDARY_ONLY` |
| 73 | `bai` | b.ai | `TEMPORARY_PROMO_ONLY` | Official B.AI publishes several zero-credit model API offers (e.g., MiMo, Hy3, Qwen3.8 Flash) but explicitly calls them promotions reverting to paid price when the offer ends. Not a durable recurring free entitlement. | [Read source](https://docs.b.ai/llmservice/promotions-and-pricing-notices/) | `OFFICIAL_TIME_LIMIT_UNSPECIFIED` |
| 74 | `fenayai` | FenayAI | `UNVERIFIED` | Primary fenayai.com timed out. Third-party directory shows paid/BYOK routing and no verified renewable free API policy; absence not proven. | [Read source](https://www.uprouter.online/s/fenayai) | `SECONDARY_ONLY` |
| 75 | `empower` | Empower | `PAID_ONLY` | Official documentation describes model hosting as pay-as-you-use inference; no public renewable $0 model API tier identified. | [Read source](https://docs.empower.dev/introduction) | `OFFICIAL_NO_FREE_GRANT` |
| 76 | `poe` | Poe | `UNVERIFIED_FREE_MODEL_API` | Official external-app API is key- and point-based; free users cannot invoke any bot costing >0 points unless they subscribe or purchase points. No specific zero-point external API model and recurring allocation verified; free web chat excluded. | [Read source](https://creator.poe.com/docs/external-applications/external-application-guide) | `OFFICIAL_INCONCLUSIVE` |
| 77 | `chutes` | Chutes.ai | `PAID_ONLY` | Official 2026 pricing FAQ explicitly says no free tier; hosted API is pay-per-token, monthly packages are paid. | [Read source](https://www.chutes.ai/pricing) | `OFFICIAL` |
| 78 | `factory` | Factory | `PAID_SUBSCRIPTION_ONLY` | Factory Droid SDK/API and optional no-extra-cost Droid Core model pool are inside paid Individual subscriptions starting $20/mo, not independent no-payment inference API. | [Read source](https://docs.factory.ai/pricing/individuals) | `OFFICIAL` |
| 79 | `bluesminds` | BluesMinds | `TRIAL_ONLY` | Official free signup grants 500 pi credits ONE TIME, each API request deducts credits; a daily 300-request rate cap does not imply daily CREDIT replenishment, and no replenishment established. Operator doc phrases 'Free plan forever' while no explicit credit refill; exclude as recurring. | [Read source](https://doc.bluesminds.com/) | `OFFICIAL_TRIAL_NO_REFILL` |
| 80 | `freemodel-dev` | FreeModel.dev | `TRIAL_ONLY` | Official site offers free API credits on signup with no card, but no repeating monthly/daily free inference grant. | [Read source](https://freemodel.dev/) | `OFFICIAL` |
| 81 | `freeaiapikey` | FreeAIAPIKey | `RECURRING_FREE_API` | Verified Free accounts get up to 100,000 free tokens/day according to official home page, with free :free model routes and daily request caps per official docs. Free model IDs are limited-time/replaceable; data provenance and terms require vetting. | [Read source](https://freeaiapikey.com/docs) | `OFFICIAL_FREE_MODELS_ROTATE` |
| 82 | `zenmux` | ZenMux | `UNVERIFIED_DUAL_BILLING_MODE` | ZenMux $0 Builder subscription provides Studio Chat ONLY, explicitly NO API; separately the PAYG model catalog publishes zero-priced free API models. Whether new PAYG user can call a free model at zero prepaid balance without paid activation is unverified; do not count positive until confirmed. | [Read source](https://zenmux.ai/docs/guide/subscription.html) | `OFFICIAL_CONFLICTING_MODES` |
| 83 | `openadapter` | OpenAdapter | `RECURRING_FREE_API` | Official $0 Free API plan: 50 weighted request credits/day with 200 credits/month limit, variable credit cost per model, replenishing daily; free models and other tiers depending eligibility, no card required. | [Read source](https://openadapter.dev/rate-limits) | `OFFICIAL` |
| 84 | `dit` | DIT.ai | `PAID_ONLY` | Official DIT comparison says its multi-provider model API has no permanent free tier, uses per-request market pricing. | [Read source](https://dit.ai/blog/llm-api-providers) | `OFFICIAL` |
| 85 | `tokenrouter` | TokenRouter | `UNVERIFIED` | Official tokenrouter.com site offers claimable free initial credits and PAYG model charges; OmniRoute static metadata claims free MiniMax 3, but no specific recurring zero-price model or grant confirmed in live official docs. Other tokenrouter.io and .me are separate businesses and should not be conflated. | [Read source](https://www.tokenrouter.com/) | `OFFICIAL_INCONCLUSIVE` |
| 86 | `token-kiosk` | Token Kiosk | `PAID_ONLY` | Current Token Kiosk (gaib.ai) documentation says mandatory funding via x402 in USDC/USDT BEFORE inference, with requests billed from prepaid balance. No recurring free model routes published. | [Read source](https://token-kiosk.gaib.ai/docs) | `OFFICIAL` |
| 87 | `sumopod` | SumoPod | `UNVERIFIED_PAID_PUBLIC_LIST` | Official ai.sumopod.com inaccessible; independent model list reports positive input/output token prices. No confirmed zero-price hosted API model or recurring free credit; cannot conclude permanent paid-only without operator source. | [Read source](https://aigratis.my.id/en/provider/sumopod) | `SECONDARY_ONLY` |
| 88 | `x5lab` | X5Lab | `TRIAL_ONLY` | Official trial grants a ONE-TIME 500,000-token API balance for first users. Then $0.7+ paid top-ups. No renewing free model quota. | [Read source](https://x5lab.dev/pricing) | `OFFICIAL` |
| 89 | `chenzk` | Chenzk API | `UNVERIFIED` | Official chenzk.top is a JS-only New API panel with no publicly readable pricing/free quota proof; no recurring free model API grant established. | [Read source](https://chenzk.top/) | `OFFICIAL_OPAQUE` |
| 90 | `kenari` | Kenari | `RECURRING_FREE_API` | Zero-balance accounts can call :free models and kenari-free route. Operator publishes free-model request quotas and 50 calls/day, 5 RPM for no-topup Solo plan. Higher allowance with paid top-up is separate. | [Read source](https://kenari.id/en/docs/free-models) | `OFFICIAL` |

## Confirmed advertised positive eligibility (append to master)

- Source row 61 · `llm7` · **LLM7.io** — Free developer token: 100,000 combined input/output tokens per rolling 24h; 1 request/s, 60/min, 250/hour. Educational/research service and capacity not guaranteed. — https://llm7.io/
- Source row 64 · `gitlawb-gmi` · **Gitlawb Opengateway (GMI Cloud)** — Official shared Opengateway currently advertises nvidia/nemotron-3-ultra-550b-a55b:free, zero input/cache/output prices, rate-limited, no credits needed. This GMI-type entry is a match to the free NVIDIA route; static OmniRoute registry 3.8.52 contains superseded 2026-06 'promo ended' note; live Gateway test pending. — https://gitlawb.com/opengateway
- Source row 81 · `freeaiapikey` · **FreeAIAPIKey** — Verified Free accounts get up to 100,000 free tokens/day according to official home page, with free :free model routes and daily request caps per official docs. Free model IDs are limited-time/replaceable; data provenance and terms require vetting. — https://freeaiapikey.com/docs
- Source row 83 · `openadapter` · **OpenAdapter** — Official $0 Free API plan: 50 weighted request credits/day with 200 credits/month limit, variable credit cost per model, replenishing daily; free models and other tiers depending eligibility, no card required. — https://openadapter.dev/rate-limits
- Source row 90 · `kenari` · **Kenari** — Zero-balance accounts can call :free models and kenari-free route. Operator publishes free-model request quotas and 50 calls/day, 5 RPM for no-topup Solo plan. Higher allowance with paid top-up is separate. — https://kenari.id/en/docs/free-models

## High-risk distinctions requiring future follow-up

- **Gitlawb:** the bundled OmniRoute 3.8.52 static note says both routes lost earlier free promos. Operator's current October site NOW advertises **Nemotron 3 Ultra `:free` with no credits needed**, while MiMo itself is priced; preserve source/date change, and test exact GMI route later. Do not count both source rows 63 and 64 for one service's new free Nemotron route.
- **ZenMux:** the Free subscription explicitly has no API access; separate Pay-As-You-Go includes $0 model SKUs and may be usable at zero prepaid balance, but official policy did not clearly prove the zero-payment eligibility; keep PENDING, not free-positive nor definitively paid-only.
- **GoAPI:** its pricing comparison table shows 'Free models only', but the terms describe **1M tokens only for new users** and ordinary model inference billed per token. Explicitly UNVERIFIED until an independent published no-cost model ID/reset rule is found.
- **BluesMinds:** 300 requests/day is a rate/quantity limit, while the 500 pi credits are described as signup credits spent by every call; unless fresh credits actually replenish, this is a finite trial, not a recurring free API.
- **TokenRouter:** distinguish `tokenrouter.com` in the OmniRoute provider entry from **tokenrouter.io** and **tokenrouter.me**, which have different products and terms; `free to sign up` or a $0 gateway shell cannot prove free hosted inference.
- **b.ai:** current API can have multiple `0 Credits` promotional models; operator explicitly says pricing returns to normal at promotion end, even though not every end date is public. Do not silently treat promotional model access as a permanent renewable pool.
- **FreeAIAPIKey:** the provider advertises a genuine free account grant of 100K tokens/day but says selected `:free` models can be deactivated without notice. Its claim of recycled upstream credits also warrants operational privacy and authorization review; do not auto-send client data.
- **Poe:** $0 desktop/web chat and creator API key existence do not prove repeatable free model calls through the API; paid bots explicitly require an active subscription/add-on balance.
- **Kenari:** free-model usage works at zero rupiah balance; no top-up needed for the standard low-quota Free tier. Account regional eligibility is still untested.

## Classification counts

- `RECURRING_FREE_API`: 5
- `UNVERIFIED`: 5
- `PAID_ROUTE_WITH_SEPARATE_FREE_MODEL`: 1
- `NO_FREE_EXTERNAL_API`: 1
- `PAID_ONLY`: 6
- `TRIAL_ONLY`: 6
- `UNVERIFIED_CONFLICTING`: 1
- `TEMPORARY_PROMO_ONLY`: 1
- `UNVERIFIED_FREE_MODEL_API`: 1
- `PAID_SUBSCRIPTION_ONLY`: 1
- `UNVERIFIED_DUAL_BILLING_MODE`: 1
- `UNVERIFIED_PAID_PUBLIC_LIST`: 1

**All 30 rows accounted for.** All 5 positive IDs deduplicated against 34 previous stage entries; cumulative should become **39 (20 S01 + 14 S02 + 5 S03)** once master merge confirmed. Stages S04–S09 remain pending.
