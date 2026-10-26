# Hugging Face — DJMRN Account, API Token and Inference Providers / OmniRoute Handoff

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
