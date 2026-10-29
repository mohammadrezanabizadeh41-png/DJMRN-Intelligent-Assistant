# Cohere — DJMRN Trial Account, Model Catalog, Free Quotas and OmniRoute Integration Dossier

## 2026-10-30 — COHERE-OMNIROUTE-PROVIDER-CONNECTION-PASS-20261030 — verified user Windows PowerShell receipt

**Supersedes previous 2026-10-26 'NOT_CONNECTED_TO_OMNIROUTE / NO_COHERE_HTTP_TEST' status only as to provider connection.** User ran `DJMRN COHERE RECOVERY V3` against local OmniRoute 3.8.52 and supplied complete console output. This establishes an **active and successful provider-connection/credential test**, NOT a routed Chat Completion/model-inference acceptance test.

| Field | User-observed result |
|---|---|
| Provider / alias | `cohere` / `cohere` |
| Connection display name | `DJMRN-Cohere-Free` |
| Existing connection ID | `5b4e90eb-b8bd-4c64-84ff-b366d7ba8134` |
| Local OmniRoute endpoint | `http://127.0.0.1:20128` |
| Connection reused | `COHERE_CONNECTION_COUNT=1`, `CONNECTION_ACTION=REUSE_EXISTING` (no new duplicate) |
| Account-scoped proxy | `level=key`, HTTP `127.0.0.1:20809`; `PROXY_ACTION=ASSIGNED_TO_COHERE`; subsequent readback type/host/port match |
| Validation probe ID | `command-r7b-12-2024` |
| Test result | `VALID=True`, `DIAGNOSIS_TYPE=ok`, `LATENCY_MS=377` |
| Persisted connection | `FINAL_ACTIVE=True`, `FINAL_TEST_STATUS=active` |
| HTTP status code | Console showed blank `STATUS_CODE=`; **do not invent an HTTP 200 receipt** |
| API key | Existing user-controlled `DJMRN-OmniRoute-Cohere` **Trial** key; actual value not stored, shared, rotated or replaced |
| Billing/commercial | User screenshot on 2026-10-30 confirmed **Free Account / Trial Keys FREE**, expressly **not for commercial use**; no Production upgrade requested or performed |

**Troubleshooting provenance:** Initial POST `/api/providers` had apparently created the connection but the original assistant script wrongly looked for `$created.id`; release v3.8.52 actually returns `{ connection: { id: ... } }`, so original script halted with `COHERE_CREATED_BUT_CONNECTION_ID_MISSING` before proxy configuration. A subsequent V3 run initially encountered HTTP 403 from local OmniRoute management `GET /api/providers` (not from Cohere); final V3 run using a valid management credential passed, found one existing connection, installed only the Cohere account-scoped proxy, and confirmed connection/test active. Do not ascribe the earlier management 403 to an evidenced specific user mistake.

**Official Cohere Trial allowance and models, rechecked 2026-10-30:**
- `https://docs.cohere.com/v2/docs/rate-limits`: **1,000 Trial API calls per month across Trial usage; NOT 1,000 per model**. Under Chat API 'per model' table, Command R7B/R/R+, Command A/A+/Reasoning/Vision/Translate, North Mini Code are **20 requests/minute per listed Chat model**. RPM and monthly budget are separate limits. Do not multiply shared monthly budget by available model count or trial-key count.
- Non-Chat trial throughput limits differ: Rerank **10 req/min**, Audio Transcriptions **5 req/min**, Embed text **2,000 inputs/min**, Embed images **5 inputs/min**, EmbedJob **5 req/min**, Tokenize **100 req/min**, Parse **500 req/min**. These are different units/capabilities; do not treat an input as a request or route embeddings/rerank into Chat Completions.
- `https://docs.cohere.com/docs/cohere-faqs` corroborates global 1,000 calls/month for trial; `https://cohere.com/pricing` states Trial API calls free but **not allowed in production or commercial use**; Production keys generally billed by usage.
- Precise **account-specific consumed/remaining monthly calls**, monthly reset timestamp/timezone, cross-key aggregation/account enforcement, and entitlement for each candidate model are **NOT yet observed**. Dashboard historical October 26 `$0` does not establish current remaining quota. Do not infer a separate 1,000-call allocation for each model, each new trial key, or model family.
- An OmniRoute `/api/providers/{id}/test` `valid=True` **does not establish** actual `POST /v1/chat/completions` Gateway inference for `cohere/command-r7b-12-2024`. Route-specific `HTTP 200`, actual content, tool-use, and Combo membership remain **PENDING**. Keep cross-provider working model total **18** (Gemini 8, Groq 6, OpenRouter 1, Mistral 1, Cloudflare 2); a *provider connection* is not a newly verified *model*.

**Next approved action boundary:** Low-token synthetic Gateway test using user's **OmniRoute Gateway API key** (distinct from Management and upstream Trial key), one model only; do not send actual paid freelance/client work through Trial Cohere. No GitHub records contain credentials; this research amendment did not mutate Windows OmniRoute, account billing, permissions or Combo routes.

---

## 2026-10-26 — VERIFIED KEY RENAME + MODEL ONBOARDING HANDOFF (USER SCREENSHOT)

**Most recent account-key observation / supersedes only earlier `default` key-label notes**:
- The user's actual screenshot of Cohere Dashboard → API Keys → Trial keys visibly shows **NAME = `DJMRN-OmniRoute-Cohere`**, **CREATED = Oct 26, 2026**, with the key masked. User explicitly reports renaming the existing key. **KEY_RENAME_CONFIRMED / EXISTING_TRIAL_KEY_RETAINED**. This is the **API key's display name**, NOT proof the underlying Cohere account or organization was renamed.
- **Never save** the actual key, its displayed suffix/fingerprint, registered personal email, cookie or screenshot with credentials in this public repository. Its key value remains available only to the owner for later private OmniRoute entry. No additional key was generated.
- Evidence for plan and spend remains the user screenshots: **Cohere Free Account**, **Trial keys are free and rate-limited and prohibited for commercial purposes**, **Billing & Usage 0.00 USD / no tracked usage 2026-10-19 through 2026-10-26**. Payment method, spending-limit controls, future billing rules and Data Controls are **NOT OBSERVED**.
- **Status contract:** `COHERE_TRIAL_KEY_EXISTS_AND_RENAMED` / `NO_COHERE_HTTP_TEST` / `NOT_CONNECTED_TO_OMNIROUTE` / `NO_PRODUCTION_APPROVAL`.

### 2026-10-26 free-trial model/route selection shortlist (research only)

**Rule:** Trial-key API calls are free within evaluation limits, but the account-specific model entitlement and real `200` responses are **not independently established**. Do not call any candidate `VERIFIED_WORKING_FREE_IN_OMNIROUTE`. The official Cohere rate-limit guide sets **1,000 total Trial API calls/month**, not independent pools for each model. `20 RPM` shown below is the documented Chat *rate limit* where named, not a daily free allowance. No model receives autonomous agent production/freelance traffic on a noncommercial Trial key.

| Role for future DJMRN | Candidate exact Cohere native `model` ID | Public vendor evidence / access status | Trial RPM and confidence | OmniRoute handling |
|---|---|---|---|---|
| Persian/intent light L1 | `tiny-aya-earth`, `tiny-aya-global` | Live Chat models; Persian supported by Tiny Aya family, Earth focused on West Asian/African languages; **access with this key untested** | Official specific Chat model RPM row not stated; default endpoint rule documented separately; **validate** | Candidate to benchmark under existing `DJMRN-Persian-L1` only after actual call |
| General small/faster | `command-r7b-12-2024` | Live Chat, RAG/tool candidate; not yet account tested | Trial 20 RPM per model, 1k/month shared | Candidate for L1/L2, quality bench required |
| General agent/tool/RAG | `command-a-03-2025` | Live Chat, current model public catalog | Trial 20 RPM per model, 1k/month shared | L2 candidate; verify tool use separately |
| Advanced multilingual reasoning | `command-a-reasoning-08-2025` | Official model page explicitly says **free for Trial and Production keys up to rate limits**; trial noncommercial remains | Trial 20 RPM per model, 1k/month shared | L3 optional, do not treat reasoning as everyday default |
| Advanced flagship (Persian/text+vision) | `command-a-plus-05-2026` | Official model page explicitly says **free for Trial and Production keys until rate limits**; Persian listed as supported; text+image | Trial 20 RPM per model, 1k/month shared | L3/vision candidate, not a built Combo route |
| Translation Persian | `command-a-translate-08-2025`, `c4ai-aya-expanse-32b` | Public Live Chat; Persian explicitly in vendor language lists | Command A Translate 20 RPM; Aya-specific exact RPM not published; shared trial overall | Task-specific translation benchmark |
| Coding | `north-mini-code-1-0` | Public Live Chat agentic coding, North API evaluation supported | Trial 20 RPM, shared 1k/month | Future coding Combo when needed |
| Vision/document analysis | `command-a-vision-07-2025`, `c4ai-aya-vision-32b` | Public Live Chat with image input; **Command A Vision official language list omits Persian**; Aya Vision family includes Persian | Command A Vision 20 RPM, Aya exact RPM not identified | Validate image input via actual adapter; no assumed automatic bridge |
| Contextual retrieval | `embed-v5.0-fast`, `embed-multilingual-v3.0`, `rerank-v5.0-fast` | Public Embed/Rerank candidates, not chat | Embed text 2000 **inputs**/min; Rerank 10 **requests**/min; shared trial cap applicability to specific endpoints verify | Separate Embeddings/Rerank tool adapter **NOT** Chat Combo |

**Other live public Chat candidates retained in the original catalogue below:** `command-r-08-2024`, `command-r-plus-08-2024`, `north-small-translate-09-2026`, `tiny-aya-fire`, `tiny-aya-water`. Public **33-model inventory** in section 3 includes all live Chat+Embed+Rerank+Parse+Audio models; it is **NOT** a count of currently verified free/authorized account routes.

**Official integration contract (not yet executed):**
- Cohere **OpenAI-compatible base URL**: `https://api.cohere.ai/compatibility/v1`; `/chat/completions` with native exact model ID and private upstream Cohere token. Native Cohere API alternatively `https://api.cohere.com/v2/chat`. OmniRoute's public guide identifies `cohere/` provider prefix but **the running user's v3.8.52 connector was not inspected/tested**. Final OmniRoute request should use *actual* registered model ID/prefix from UI; never assume documentation prefix is proof of routing.
- Authenticated account enumeration after Hugging Face onboarding: `GET https://api.cohere.com/v1/models?page_size=100` with user-held Bearer key, paginate, filter Chat-compatible endpoints and nondeprecated entries, compare to this public snapshot; never paste key into chat/GitHub.
- Next real test only after user chooses: **one small synthetic Persian prompt**, observe HTTP status/body model/429/quota headers/latency/usage, then decide if a specific free and noncommercial model should enter a Combo. Do not create arbitrary separate Combo per public model or duplicate quota by renaming key.
- Recheck actual remaining trial allowance/month reset, model-specific 403/404, data controls, billing/payment and account-level quota before assigning automated routes. Unknown price/right = STOP routing.

**Primary sources re-checked 2026-10-26:**
- Cohere model inventory: https://docs.cohere.com/docs/models
- Cohere Trial/Production limits: https://docs.cohere.com/docs/rate-limits
- Official Command A+ trial/prod free-with-caps: https://docs.cohere.com/docs/command-a-plus
- Official Command A Reasoning trial/prod free-with-caps: https://docs.cohere.com/docs/command-a-reasoning
- Persian Tiny Aya family: https://docs.cohere.com/docs/tiny-aya
- Official Compatibility API: https://docs.cohere.com/docs/compatibility-api
- Authenticated model list docs: https://docs.cohere.com/reference/list-models
- OmniRoute integration guide: https://omniroute.hagicode.com/en-US/getting-started/providers-guide/

**Observed/researched:** 2026-10-26. **Source:** user-provided Cohere dashboard screenshots + Cohere official current documentation (URLs and caveats below).  
**Provider queue slot:** #7 Cohere; **next user priority:** #8 Hugging Face; after both, return to installed OmniRoute and role-based multi-provider setup.  
**Overall state:** `ACCOUNT_CREATED / FREE_PLAN_VISIBLE / DEFAULT_TRIAL_KEY_EXISTS / BILLED_USAGE_0_USD / PUBLIC_MODEL_CATALOG_RESEARCHED / ACCOUNT_MODEL_LIST_NOT_QUERIED / DATA_CONTROLS_NOT_INSPECTED / API_INFERENCE_NOT_TESTED / OMNIROUTE_NOT_CONNECTED`.  
**Important evidence boundary:** User-visible screenshots prove account/UI facts only. Published model names and vendor rate limits do not prove every model is enabled on this particular key, nor do they prove real inference, free commercial rights, or an OmniRoute connection. No private key value or personal email is stored here.

## 1. User account and registration record — 2026-10-26

- Onboarding question `What is your role?`: assistant recommended `Software Engineer`. Whether user actually chose it is **not verified**.
- `What do you plan to do with Cohere?`: proposed `Text Classification, Semantic Search, User Intent Recognition, Text Generation, Entity Extraction, Text Summarization, Chat`; `Content Moderation` optional. Actual saved choices **not independently confirmed**.
- User successfully entered Cohere dashboard; later screenshot **Platform → API Keys** displayed `You're using a Cohere Free Account`; `Trial keys / FREE` and an existing masked `default` key created Oct 26, 2026.
- The screenshot explicitly states **Trial key calls are free of charge, rate-limited, and cannot be used for commercial purposes**. This is decisive even if the long-term DJMRN system may later earn income.
- Assistant initially suggested renaming `default` to `DJMRN-OmniRoute-Cohere`; **user later supplied a screenshot confirming the API key label change**, as recorded in the leading 2026-10-26 addendum. No duplicate trial key needed.
- User screenshot **Settings → Billing & Usage → Usage** displayed `Subtotal: 0.00 USD`, updated Oct 26, 2026; date range `Last 7 days`, message `You don't have any usage between 10/19/2026–10/26/2026`. **This does not prove absence of a payment method, a verified zero-spend hard cap, or future usage remaining zero.**
- The UI contained `Invoices`, `Spending Limit`, `Payment` tabs but their actual contents were **NOT inspected**. `Data Controls` menu exists but settings/toggle state are **NOT inspected**. `Get your Production key` is an upgrade/application path and was **not used**.
- **Key status:** `EXISTS AND RENAMED (MASKED), VALUE NOT RECORDED, ACTUAL API VALIDITY UNTESTED`. No Python/API tests and no OmniRoute Provider account created in this onboarding step.

## 2. Verified Trial terms, rate limits, pricing separation

**Authoritative primary source:** https://docs.cohere.com/docs/rate-limits ; official pricing https://cohere.com/pricing .

- Cohere officially distinguishes **evaluation/trial keys (free, limited, non-production/non-commercial)** from **production keys (generally metered/pay-as-you-go and intended for production)**.
- Official documented trial limit: **1,000 API calls/month**. This is **not 1,000 per model/month**, **not a daily 1,000-call allowance**, and **not a grant of daily calls equal to RPM × minutes**. In particular, the quota allocation across multiple trial keys/account/organization is **not proven**; do not multiply by creating keys. Monthly reset exact date/time/timezone and plan-specific dashboard remaining quota **UNKNOWN**.
- Trial **Chat** endpoints: published **20 requests/minute for each listed model family**: Command A+, Command A Reasoning, Command A Translate, Command A Vision, Command A, Command R+, Command R, Command R7B, and North Mini Code. This is a rate gate, not extra free credits; actual account behavior/headers remain unmeasured.
- Trial **Audio Transcriptions** 5 requests/min; **Embed text** 2,000 inputs/min; **Embed Images** 5 inputs/min; **EmbedJob** 5 requests/min; **Rerank** 10 requests/min; **Tokenize** 100 requests/min. The official latest rate-limits HTML also lists a default catch-all 500 requests/min; **no separate per-model allowance for Aya/Tiny Aya/North Small Translate has been confirmed**, and `parse-v5.0` is in the public model catalog though the presently inspected rate-limit source's endpoint table does not specify Parse. For an unspecified model/endpoint use `RATE_UNKNOWN` until live account checks.
- Cohere docs explicitly state **some newer models (e.g., Command A+ and Command A Reasoning) are free with trial *and production* API keys up to documented caps**, while production deployment at scale may require **paid Model Vault or sales arrangements**. This **does not override the actual on-screen trial-key no-commercial-use restriction**. Cohere Production Key as a general category is not assumed free or spend-capped.
- **Adding a card** or **buying credit** is **NOT VERIFIED to raise recurring FREE monthly/daily API allowance**; instead production access generally involves paying for consumption. `Spending Limit` tab is not evidence that `$0` is enforced or that adding a card is safe. **No card, upgrade, Production Key, Vault, pay-as-you-go or billing activation performed/authorized**. No automatic paid fallback in OmniRoute.
- Relevant support contacts: `support@cohere.com` for limit/key issues, `sales@cohere.com` for production terms; no request was sent.

### Limit tracker for later OmniRoute setup

| Scope | Official trial limit | Monthly quota | Scope caveat | Decision |
|---|---|---|---|---|
| Chat: listed Command variants, R-family, North Mini Code | 20 req/min/model (published) | 1,000 trial API calls/month | Do not multiply shared monthly allowance by model; account reset and headers unknown | DEVELOPMENT_ONLY, after first test |
| Chat: Aya/Tiny Aya/North Small Translate | Exact variant RPM **UNKNOWN** | Shared 1,000 trial calls/month stated generally | Not named in official RPM row | Verify via real response/limits |
| Rerank | 10 req/min | Trial global/monthly rule; endpoint-specific interpretation untested | NOT chat-completion; separate API route | Future search capability |
| Embed text | 2,000 inputs/min | Trial overall monthly call rule; call-vs-input accounting check required | 2,000 inputs is NOT 2,000 requests | Future RAG |
| Embed images | 5 inputs/min | As above | Separate from text embeds | Future multimodal RAG |
| Audio transcription | 5 req/min | General trial monthly calls | 25 MB files by model catalog | Future audio |
| Embed jobs | 5 req/min | General trial monthly calls | Async/batch semantics; not free bulk bypass | Test only if needed |
| Parse | 500 req/min (official Default/Parse row, verified 2026-10-26) | General trial monthly calls; account reality unknown | Separate parse endpoint | Future document extraction |
| Tokenize | 100 req/min | Endpoint billing/call applicability to confirm | Not inference | No priority |

**Control policy:** account/key-level budget tracking, per-model cooldown for HTTP 429, bounded retry, no retry loop that burns the 1,000 shared monthly calls, and no unverified price/paid automatic route. `free_only=true` and global fail-closed must be tested in actual OmniRoute, not assumed supported from sidebar labels.

## 3. Official model inventory (public model overview, NOT authenticated account enumeration)

**Source:** https://docs.cohere.com/docs/models (checked 2026-10-26). **33 distinct 'Live' model IDs in the visible primary overview** counted as 8 Command + 2 North + 6 Aya + 7 Embed + 7 Rerank + 1 Parse + 2 Audio. This is a **source catalog count**, not proof of 33 active models on user's personal trial key. Deprecated, retired and third-party deployment aliases are deliberately NOT included in 33.

### A. Chat / text / vision — candidates for role-based OmniRoute Combos after verification

| Exact Cohere model ID | Public status | Input | Context | Max output | Likely DJMRN role / notes |
|---|---|---|---:|---:|---|
| `command-a-plus-05-2026` | Live | Text + image | 128k | 64k | Advanced reasoning/agentic + multimodal; official limited free evaluation, trial compatibility promising |
| `command-a-03-2025` | Live | Text | 256k | 8k | Full agent tasks, RAG/tool-use; trial use may be free but production token-billed |
| `command-r7b-12-2024` | Live | Text | 128k | 4k | Lightweight-ish RAG/intent, needs measured Persian task quality |
| `command-a-translate-08-2025` | Live | Text | 8k | 8k | Explicit Persian among 23 supported translation languages |
| `command-a-reasoning-08-2025` | Live | Text | 256k | 32k | Complex reasoning/agent tasks; newer model free subject to caps |
| `command-a-vision-07-2025` | Live | Text + image | 128k | 8k | Document/chart OCR and vision; official language list for Vision does **not** include Persian |
| `command-r-08-2024` | Live | Text | 128k | 4k | Retrieval-assisted document chat |
| `command-r-plus-08-2024` | Live | Text | 128k | 4k | More demanding RAG/doc reasoning |
| `north-small-translate-09-2026` | Live | Text | 16k | 16k | >50-language translation candidate; exact Persian support must be verified |
| `north-mini-code-1-0` | Live | Text | 256k | 64k | Agentic coding; 20 RPM listed; coding quality and tool calls untested |
| `tiny-aya-global` | Live | Text | 8k | 8k | Small multilingual L1 candidate; ~3.35B model, test Persian quality |
| `tiny-aya-earth` | Live | Text | 8k | 8k | Western Asian/African languages; strong candidate for Persian benchmark but not automatically superior |
| `tiny-aya-fire` | Live | Text | 8k | 8k | South Asian language specialization |
| `tiny-aya-water` | Live | Text | 8k | 8k | European/Asia-Pacific language specialization |
| `c4ai-aya-expanse-32b` | Live | Text | 128k | 4k | Persian explicitly in Aya 23 languages; multilingual reasoning/translation candidate |
| `c4ai-aya-vision-32b` | Live | Text + image | 16k | 4k | Multilingual image understanding; Persian one of Aya 23 language family |

**Do not use:** deprecated Command aliases `command-r`, `command-r-plus`, `command-light`, `command`, `command-r-03-2024`, `command-r-plus-04-2024`; retired `c4ai-aya-expanse-8b` and `c4ai-aya-vision-8b` (Apr 4, 2026). See https://docs.cohere.com/docs/deprecations . **Model name containing 7B/32B or model weights on Hugging Face does NOT imply 7B/32B model weights run on Windows; these are hosted cloud API routes.**

### B. Embedding — NOT Chat Completions (use embedding interface and distinct quotas)

| Exact model ID | Context | Embedding dims | Intended usage |
|---|---:|---|---|
| `embed-v5.0-pro` | 128k | configurable 256/512/768/1024/1536/2048 | Latest advanced multimodal semantic retrieval |
| `embed-v5.0-fast` | 128k | same configurable dims | Lower-latency first candidate |
| `embed-v4.0` | 128k | configurable 256/512/1024/1536 | Multimodal image/text embeds |
| `embed-english-v3.0` | 512 | 1024 | English only |
| `embed-english-light-v3.0` | 512 | 384 | Light English only |
| `embed-multilingual-v3.0` | 512 | 1024 | Persian/multilingual semantic-search candidate after test |
| `embed-multilingual-light-v3.0` | 512 | 384 | Lighter multilingual search candidate |

Beware model-specific token context and dimension contracts: vector store/index dimensions must match; switching embed model requires re-embedding, not mere agent Combo change. Source model overview. OpenAI-compatibility API documents embeddings with `embed-v4.0`; actual `v5` OpenAI adapter support **NOT VERIFIED**.

### C. Rerank — dedicated rerank endpoint, NOT the chat Combo

| Exact model ID | Context | Notes |
|---|---:|---|
| `rerank-v5.0-pro` | 32k | Latest higher-quality multilingual + context-focus |
| `rerank-v5.0-fast` | 32k | Latest lower-latency multilingual |
| `rerank-v4.0-pro` | 32k | Prior version |
| `rerank-v4.0-fast` | 32k | Prior faster version |
| `rerank-v3.5` | 4k | Multilingual |
| `rerank-english-v3.0` | 4k | English only |
| `rerank-multilingual-v3.0` | 4k | Multilingual |

### D. Specialized endpoints: parsing and audio

| Model ID | Endpoint | Notes |
|---|---|---|
| `parse-v5.0` | Parse | Document-to-structured-data extraction; no assumed OmniRoute Chat support |
| `cohere-transcribe-03-2026` | Audio Transcriptions | Speech-to-text; official maximum 25 MB |
| `cohere-transcribe-arabic-07-2026` | Audio Transcriptions | Arabic specialist; not a Persian-specific model |

Catalog source includes other deprecated/retired variants; source count above is not a lifetime count.

## 4. API endpoints and model discovery for OmniRoute

- **Cohere native Chat v2:** `https://api.cohere.com/v2/chat`. Header: `Authorization: Bearer <private Cohere key>`.
- **Official OpenAI Compatibility API base:** `https://api.cohere.ai/compatibility/v1` documented at https://docs.cohere.com/docs/compatibility-api ; Chat Completions path `/chat/completions`; model field uses **exact IDs in section 3**. This simplifies a potential OmniRoute-compatible account; actual OmniRoute 3.8.52 provider type / base-url acceptance / authentication mapping has **NOT been tested**.
- Supported Compatibility parameters documented: `model,messages,stream,response_format,tools,temperature,max_tokens,stop,seed,top_p,frequency_penalty,presence_penalty`; `reasoning_effort` only `none|high` in the compatibility docs (not generic `low|medium`). Strict tool/JSON and vision require separate specific-model tests.
- **Authenticated model discovery:** Official `GET https://api.cohere.com/v1/models?page_size=100` with Bearer private trial key. Model list returns `models[]`, `name`, `is_deprecated`, `endpoints`, `context_length`, `features` and optional `next_page_token`. API docs: https://docs.cohere.com/reference/list-models . Page through all pages rather than assuming one page or copying entire proprietary catalog; filter `is_deprecated=false` and `endpoints` by required interface. **NOT EXECUTED; requires user-side credential.**
- `GET /v1/models/:model` can confirm a specific model's metadata, though catalog presence alone does not establish trial entitlement or free/commercial status: https://docs.cohere.com/reference/get-model .
- Proposed initial tests **AFTER user finishes Hugging Face and returns to OmniRoute**: one tiny Persian text completion from `tiny-aya-earth` or `command-r7b-12-2024`; one advanced reasoning model `command-a-reasoning-08-2025`; one code sample `north-mini-code-1-0` only if useful and budget allows. Log success/HTTP/actual model/latency/small request counts without secrets or prompts containing sensitive data. Do NOT test all 33 models indiscriminately because of shared monthly budget.
- Example high-level routing targets **CANDIDATE ONLY, NOT CREATED**: existing `DJMRN-Persian-L1` (test possible Tiny Aya Earth/Aya32B); later on-demand Code/Reasoning/RAG named Combos only when useful. An embed/rerank call is a **different endpoint/tool adapter**, not an ordinary Chat Combo step.

## 5. Privacy, data controls and legal use

**Official vendor:** https://cohere.com/enterprise-data-commitments , checked 2026-10-26.
- Dashboard **Settings → Data Controls** offers a training-data opt-out for eligible users. Official vendor instructs toggle **Off** to opt out and says it affects **future data**. **Actual user's setting has not been observed**; the previous assistant's instruction to inspect this page remains outstanding.
- Critical distinction: Cohere explicitly states **Enterprise Data Commitments apply to paying commercial customers with a card on file**; **Trial** users are subject to Terms of Use and Privacy Policy, not automatically the same contractual enterprise guarantees. Do not claim that all Trial prompts are contractually protected by enterprise ZDR.
- Vendor describes SaaS default prompt/generation logs generally retained 30 days, with exceptions for misuse/legal/consented training; **trial-specific retention needs its own policy verification** before personal/customer data. User has not requested a Model Vault, zero data retention approval, or use of sensitive data.
- For evaluation, use synthetic/fictional prompts; don't send private emails/customer documents until user expressly approves and data controls/legal gates have been assessed.
- The Trial key's on-screen **noncommercial-use prohibition** is an operational limit: future DJMRN earning/freelance production jobs cannot be routed automatically to this Cohere Trial key absent separately verified permission and appropriate plan. Offline research and prototyping remain the intended stage.

## 6. Next action queue and outstanding verification (NO EXECUTION YET)

1. **Cohere dashboard optional final audit:** check `Data Controls` status; `Billing & Usage → Payment` for any card; `Spending Limit` availability. The `API Keys` label rename was independently confirmed by user screenshot, and the API key value must never be shown. Do not toggle/change anything without user's instruction.
2. Preserve the user-confirmed `Free/Trial` account and existing key; do not create a duplicate key or request a paid Production Key simply for a higher allowance.
3. **Next provider:** Hugging Face personal account + appropriately scoped **read** or `inference` token for API use, evaluate Inference Providers/credits and real free recurring allowance separately (the provider queue explicitly warns this may not be recurring production-free inference). User will do account/token creation in dashboard; no key exposure.
4. After the provider enrollment phase, private key into OmniRoute `Providers` → select supported Cohere connector or exact OpenAI-compatible custom endpoint; keep the existing live `DJMRN-Persian-L1` Combo untouched until a Cohere model is individually qualified.
5. Retrieve exact account model list; confirm rate/quotas/privacy/terms; test one non-sensitive request; audit request accounting/billing and 429. Only then add a validated free candidate to a role Combo and test failover; no paid fallback.
6. Keep experimental Agno/AgentOS downstream until free-only routing is reliable; the earlier Agno package/import smoke PASSED, but actual Agno → OmniRoute inference is **not verified** and was previously blocked by PowerShell Python-string quoting before HTTP.
7. **Source-of-truth:** all project updates are in `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` `main`, not the separate DJMRN-Research-Bridge or Freelance-Operations repos. This provider-specific dossier is created **because the user explicitly requested the same service-specific provider-research location as existing provider files**. Never silently write another status tracker/Notion copy; the 2026-10-25 single-record governance rule otherwise continues.

## 7. Primary references (checked 2026-10-26)

1. Public/current official Cohere model catalogue (live/deprecated labels; all 33 public live model names): https://docs.cohere.com/docs/models
2. Official trial/production rate limits: https://docs.cohere.com/docs/rate-limits
3. Official pricing & Trial noncommercial policy: https://cohere.com/pricing
4. OpenAI SDK compatibility endpoint and supported parameters: https://docs.cohere.com/docs/compatibility-api
5. Cohere authenticated List Models endpoint and pagination: https://docs.cohere.com/reference/list-models
6. Cohere individual model metadata: https://docs.cohere.com/reference/get-model
7. Official data commitments and Trial exclusion from enterprise terms: https://cohere.com/enterprise-data-commitments
8. Deprecations and Aya8B retired Apr 2026: https://docs.cohere.com/docs/deprecations
9. New Command A+ model specs: https://docs.cohere.com/docs/command-a-plus
10. Command A Reasoning specs and special free limit: https://docs.cohere.com/docs/command-a-reasoning
11. Queue: [DJMRN Free Cloud API Key Queue](DJMRN-FREE-CLOUD-API-KEY-QUEUE-2026-10-26.md)

**Evidence grade:** `SCREENSHOT_USER_ACCOUNT` for account/free/key/zero observed usage; `OFFICIAL_VENDOR_DOC` for catalog/limits/endpoints/general terms; `NOT_VERIFIED_FOR_USER_KEY` for per-model access, quota reset/remaining, payment method, privacy toggle, commercial terms beyond on-screen warning, API inference, endpoint routing and OmniRoute integrations. A successful Git commit is documentation persistence only.
