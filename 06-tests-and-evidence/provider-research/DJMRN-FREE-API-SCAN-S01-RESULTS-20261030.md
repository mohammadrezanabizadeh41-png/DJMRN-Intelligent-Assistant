# DJMRN Free API Study — Stage 01 of 09 (source rows 1–30)

**Research date:** 2026-10-30. **Mission:** investigate ONLY whether each provider offers real **recurring, no-payment hosted inference API** access, rather than temporary/signup promotional credits, marketing-only free chat, or merely a $0/month platform fee with paid tokens.

**Source of exact provider IDs:** [252 OmniRoute v3.8.52 API-key providers](OMNIROUTE-252-APIKEY-PROVIDER-CATALOG-V3852-20261030.md) and [nine-stage frozen manifest](OMNIROUTE-FREE-API-252-NINE-STAGE-RESEARCH-PLAN-20261030.md).

**Result:** 30/30 researched and recorded; **20 positive candidates (16 recurring zero-cost model API allowances; 4 recurring free hosted inference credits)**; 4 trial-only; 3 paid-only; 1 free-in-app but not external API; 1 free-model gated behind PAID balance; 1 unresolved primary-source verification.

**Evidence definition:** `OFFICIAL_PUBLISHED` = official public provider site/docs advertising the tier; `BRAND_LINKED_OFFICIAL_CLAIM` = apparently operator-associated publisher linking to the provider hostname but direct hostname inaccessible; `SECONDARY_ONLY` = independent third-party report without independently accessible primary source. None equals successful account or Gateway HTTP200, proven zero-overage controls, permanent availability, or commercial-use permission.

**Strict policy:** NO new API keys, account creation, billing/credit/top-up, signups, routed inference calls, model tests, or local OmniRoute changes were made. This is READ-ONLY public discovery. API price/free policies can change without notice. Unverified possibilities are NOT included in the positive-only cumulative list.

## All 30 decisions (one primary research question only)

| # | Provider ID | Display name | Classification | Published evidence / qualification | Source | Evidence level |
|---:|---|---|---|---|---|---|
| 1 | `onomeo` | onomeo | `RECURRING_FREE_API` | Free chat models via OpenAI-compatible API, 30 calls per 5 hours per account; pool shared across site; longer prompts may cost more calls. | [Official or closest available source](https://onomeo.com/help) | OFFICIAL_PUBLISHED |
| 2 | `unifically` | Unifically | `TRIAL_ONLY` | New-account promotional balance once; prepaid positive balance thereafter; no renewable free API entitlement verified. | [Official or closest available source](https://unifically.com/ja/terms) | OFFICIAL_PUBLISHED |
| 3 | `oneminai` | 1min.AI | `TRIAL_ONLY` | Free API credits granted on signup; shared finite credit balance; no documented automatic recurring API grant. | [Official or closest available source](https://1min.ai/free-ai-api-for-developers) | OFFICIAL_PUBLISHED |
| 4 | `cheaperinference` | Cheaper Inference | `PAID_ONLY` | Official quickstart requires a funded wallet before first model request; no unconditional renewable free models identified. | [Official or closest available source](https://api.cheaperinference.com/docs) | OFFICIAL_PUBLISHED |
| 5 | `freebuff` | Freebuff | `NO_FREE_EXTERNAL_API` | Free 100 Freebucks/day applies to Freebuff's own CLI/desktop client with ads; explicitly no API key for that free product; paid API listed separately. | [Official or closest available source](https://freebuff.com/perspectives/blog/solution-recommendation/free-coding-agents-worth-trying-before-you-pay-for-a-subscription) | OFFICIAL_PUBLISHED |
| 6 | `charm-hyper` | Charm Hyper | `RECURRING_FREE_CREDIT` | Free $0 plan includes 100 Hypercredits/month for coding-model inference. | [Official or closest available source](https://hyper.charm.land/models) | OFFICIAL_PUBLISHED |
| 7 | `agentrouter` | AgentRouter | `UNVERIFIED` | Community sources describe daily login credit plus signup bonus, but public operator site is protected by WAF and primary-source policy cannot be verified independently. DO NOT add to confirmed positives yet. | [Official or closest available source](https://github.com/cmalf/Free-Claude-Code-API-Credit/blob/main/README.md) | SECONDARY_ONLY |
| 8 | `unorouter` | UnoRouter | `RECURRING_FREE_API` | Official landing page offers no-card API keys and a free model catalog; operator-maintained MCP integration says :free routes use shared rate-limited pools (about 1 request/minute/model). | [Official or closest available source](https://unorouter.com/en) | OFFICIAL_PUBLISHED |
| 9 | `command-code` | Command Code | `PAID_ONLY` | Provider API plan requires paid subscription or funded usage; free-price promotional models are not evidence of a $0 API-access plan. | [Official or closest available source](https://commandcode.ai/docs/provider) | OFFICIAL_PUBLISHED |
| 10 | `openrouter` | OpenRouter | `RECURRING_FREE_API` | :free model routes explicitly $0; current free account limit 50 requests/day, 20 RPM; no credit purchase required for :free variants. | [Official or closest available source](https://openrouter.ai/collections/free-models/) | OFFICIAL_PUBLISHED |
| 11 | `opper` | Opper | `RECURRING_FREE_API` | Official pricing says account/API key available without card and selected free models work through API and playground. | [Official or closest available source](https://opper.ai/pricing) | OFFICIAL_PUBLISHED |
| 12 | `requesty` | Requesty | `RECURRING_FREE_API` | Free $0 API plan, 200 requests/day, limited to published free models; no card required. | [Official or closest available source](https://www.requesty.ai/pricing) | OFFICIAL_PUBLISHED |
| 13 | `zylo-api` | Zylo API | `RECURRING_FREE_API` | Basic $0 plan for Basic-tier text models; 7,200 requests/day, around 200K tokens/day, 10 RPM; premium metered models excluded. | [Official or closest available source](https://zyloai.net/pricing) | OFFICIAL_PUBLISHED |
| 14 | `fastrouter` | FastRouter | `FREE_MODELS_REQUIRE_PAID_BALANCE` | Free :free routes do not deduct credits and reset daily (10 per model per organization), BUT service explicitly blocks free-model access when paid balance is <= $1. Therefore not a no-payment true free API for DJMRN. | [Official or closest available source](https://github.com/fastrouter/docs/blob/main/explore-features/free-model-router.md) | OFFICIAL_PUBLISHED |
| 15 | `anyapi` | AnyAPI AI | `RECURRING_FREE_API` | Free API tier grants 100,000 anyTokens/day; resets midnight UTC, no card. Terms restrict to low-volume/evaluation and allow unilateral termination. | [Official or closest available source](https://anyapi.ai/terms-of-service) | OFFICIAL_PUBLISHED |
| 16 | `electronhub` | Electron Hub | `RECURRING_FREE_CREDIT` | Free forever tier includes $0.25 credit refilled weekly, 5 RPM; extra free-model requests may require ad rewards. | [Official or closest available source](https://www.electronhub.ai/pricing) | OFFICIAL_PUBLISHED |
| 17 | `llmgateway` | LLM Gateway | `RECURRING_FREE_API` | Hosted free zero-priced models through API, 5 requests per 10 minutes per free model for zero-credit organizations; verified email required. | [Official or closest available source](https://docs.llmgateway.io/resources/rate-limits) | OFFICIAL_PUBLISHED |
| 18 | `lyceum` | Lyceum | `TRIAL_ONLY` | Serverless inference priced per token; engineering team can grant evaluation credits on request; no generally available renewable free model API found. | [Official or closest available source](https://lyceum.technology/magazine/how-to-test-an-open-weight-model-for/) | OFFICIAL_PUBLISHED |
| 19 | `llm-kiwi` | LLM.Kiwi | `RECURRING_FREE_API` | Free €0 tier includes starter API keys, AUTO endpoint and direct hrLLM access with baseline rate limits; no published guaranteed lifetime service level. | [Official or closest available source](https://llm.kiwi/pricing) | OFFICIAL_PUBLISHED |
| 20 | `literouter` | LiteRouter | `RECURRING_FREE_API` | Basic $0 tier explicitly free forever, with free-model API calls; fair-use cooldown/rate caps apply (~100/hour). | [Official or closest available source](https://literouter.com/pricing) | OFFICIAL_PUBLISHED |
| 21 | `greenpt` | GreenPT | `TRIAL_ONLY` | Public free API offer is a 14-day trial, not an automatically renewing free inference allowance. | [Official or closest available source](https://www.greenpt.com/api) | OFFICIAL_PUBLISHED |
| 22 | `eurouter` | EURouter | `PAID_ONLY` | The €0 monthly platform plan is PAY-AS-YOU-GO with 15% markup and token charges; 10K requests/month is a cap, not 10K free requests. | [Official or closest available source](https://www.eurouter.ai/pricing) | OFFICIAL_PUBLISHED |
| 23 | `y-api` | Y-API | `RECURRING_FREE_API` | Official site lists four $0-per-call model routes; upstream can withdraw free label and SAME model ID can start charging automatically. Requires fail-closed protection before automatic deployment. | [Official or closest available source](https://y-api.bestvirtualgoods.com/) | OFFICIAL_PUBLISHED |
| 24 | `mnn-ai` | MNN AI | `RECURRING_FREE_CREDIT` | Free $0 subscription includes 1 monthly credit and limits models to free group; 10 RPM; credits expire every billing cycle. | [Official or closest available source](https://mnnai.ru/terms-of-service) | OFFICIAL_PUBLISHED |
| 25 | `meganova-ai` | MegaNova AI | `RECURRING_FREE_API` | Explorer tier: free registration/no card and daily quota 550 messages across eligible hosted inference models. | [Official or closest available source](https://www.meganova.ai/pricing) | OFFICIAL_PUBLISHED |
| 26 | `mixlayer` | Mixlayer | `RECURRING_FREE_API` | Public qwen/qwen3.5-4b-free hosted OpenAI-compatible model has $0 input and output; free tier rate-limited. | [Official or closest available source](https://www.mixlayer.com/pricing) | OFFICIAL_PUBLISHED |
| 27 | `speka` | Speka AI | `RECURRING_FREE_CREDIT` | Free $0 plan includes $1 of model API use per MONTH, no card, 10 requests/min; paid per-token after allowance. | [Official or closest available source](https://speka.me/pricing) | OFFICIAL_PUBLISHED |
| 28 | `tokenreply` | TokenReply | `RECURRING_FREE_API` | Official API docs say Free accounts can call Free models without charge; live pricing lists $0 per request on selected model IDs; daily check-in can add renewable in-plan allowance. | [Official or closest available source](https://www.tokenreply.com/docs/use-api-key) | OFFICIAL_PUBLISHED |
| 29 | `yolo-auto` | Yolo-Auto | `RECURRING_FREE_API` | Free $0 API plan for Qwen3.8 Flash: 15 requests/week, resets Mondays at 00:00 UTC, no card, free forever. | [Official or closest available source](https://yolo-auto.com/pricing) | OFFICIAL_PUBLISHED |
| 30 | `dxnt` | DXNT / DX Token | `RECURRING_FREE_API` | Associated platform AiApiToken publicly advertises dxnt.com/free API routing with 100+ free calls per day; direct dxnt.com page inaccessible to independent fetch. Brand-link and quota require account-specific validation. | [Official or closest available source](https://www.aiapitoken.com/) | BRAND_LINKED_OFFICIAL_CLAIM |

## Strong eligibility and safety notes

- **Do not equate `free` with unrestricted**: free API caps, site-wide pools, an ad reward, credits tied to login, rate limit and limited sets of models all matter. Recurring credit is tracked separately from zero-priced models.
- **OpenRouter** and **Requesty** provide documented renewable free API model pools. Existing DJMRN connected OpenRouter route is independent of this public eligibility evaluation.
- **FastRouter** has $0-priced model calls, but requires more than **$1 paid account balance** first; intentionally excluded from the no-payment positive-only list.
- **AgentRouter** has third-party claims of daily login credit and a one-time signup bonus; operator site blocked by WAF. Until official terms can be fetched or a user-specific account receipt exists, leave as **UNVERIFIED**. Do not assume permanent daily credit.
- **Y-API**: upstream free model label can flip to paid **with unchanged model ID**; future use must hard-stop billable routes, not trust a previously-free tag.
- **Zylo**: official pricing text presents the Basic free allowance and separately describes per-token metering for paid models. Only the Basic-tier free-text route is claimed; no premium-model allowance is assumed.
- **Electron Hub**: recurring weekly $0.25 allowance is counted as credit-based, while ad-reward free model caps are a separate conditional promotional path.
- **DXNT**: brand-linked publisher `aiapitoken.com` points to `dxnt.com/free` and 100+ daily calls, but original hostname was not independently fetched. Keep explicit brand-linked caveat in the cumulative list.
- **User's future goal**: evaluate which confirmed candidates can be registered and used with DJMRN OmniRoute; this stage does NOT test commercial-use terms, account regional restrictions, privacy policies or actual model quality.

## Stage 01 positive IDs (cumulative list seed)

- #1 `onomeo` — onomeo (RECURRING_FREE_API)
- #6 `charm-hyper` — Charm Hyper (RECURRING_FREE_CREDIT)
- #8 `unorouter` — UnoRouter (RECURRING_FREE_API)
- #10 `openrouter` — OpenRouter (RECURRING_FREE_API)
- #11 `opper` — Opper (RECURRING_FREE_API)
- #12 `requesty` — Requesty (RECURRING_FREE_API)
- #13 `zylo-api` — Zylo API (RECURRING_FREE_API)
- #15 `anyapi` — AnyAPI AI (RECURRING_FREE_API)
- #16 `electronhub` — Electron Hub (RECURRING_FREE_CREDIT)
- #17 `llmgateway` — LLM Gateway (RECURRING_FREE_API)
- #19 `llm-kiwi` — LLM.Kiwi (RECURRING_FREE_API)
- #20 `literouter` — LiteRouter (RECURRING_FREE_API)
- #23 `y-api` — Y-API (RECURRING_FREE_API)
- #24 `mnn-ai` — MNN AI (RECURRING_FREE_CREDIT)
- #25 `meganova-ai` — MegaNova AI (RECURRING_FREE_API)
- #26 `mixlayer` — Mixlayer (RECURRING_FREE_API)
- #27 `speka` — Speka AI (RECURRING_FREE_CREDIT)
- #28 `tokenreply` — TokenReply (RECURRING_FREE_API)
- #29 `yolo-auto` — Yolo-Auto (RECURRING_FREE_API)
- #30 `dxnt` — DXNT / DX Token (RECURRING_FREE_API)

**Stage status:** S01 PUBLIC RESEARCH COMPLETED; S02-S09 NOT RESEARCHED. Registry count and validated working model inventory are unchanged.
