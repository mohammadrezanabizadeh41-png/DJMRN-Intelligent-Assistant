# DJMRN — سیاست الزام‌آور انتخاب مدل رایگان بر اساس وظیفه، بودجه درخواست و سهمیه

**شناسه:** DJMRN-MODEL-ROLE-QUOTA-POLICY-20261025 · **تاریخ:** 2026-10-25 · **وضعیت:** USER-DIRECTED / ADOPTED GOVERNANCE REQUIREMENT (NO AUTOMATION IMPLEMENTED) · **تصمیم مرتبط:** D-018 · **محدوده:** همهٔ مدل‌های Cloud-First/OmniRoute و دستیاران DJMRN، نه انتخاب نهایی یک موتور.

## اصلاح و تفکیک معیارها — 2026-10-25

**User explicit amendment / effective immediately.** Account registration, OAuth login, API token or PAT issuance, entering a self-obtained key in the installed OmniRoute UI, and using an officially available free account are **NOT selection exclusions or negative ranking factors**. User expressly approves recommending/accounting for these normal onboarding steps for Iran-direct reachable Providers; prefer a registered free tier over anonymous when it improves real availability, queue priority, quotas or quality. Clearly separate **network accessibility**, **account creation**, **free quota/price**, **provider's legitimate region eligibility**, and **actual OmniRoute inference success**. A 401 is a prompt to identify the correct credential route, **not a verdict of filtering**. Do not silently treat No-auth as superior to API Key. The user's free-first/no unapproved charge and secret-handling guardrails remain; **registration is not payment**, no claim of registered account or connected API until observed. This amendment supersedes wording in earlier instructions prioritizing anonymous accounts just to avoid sign-up.

### Direct finding for AI Horde #001

- User ran one short Persian Playground chat, received **exact 401**: `You didn't provide an API key. You need to provide your API key in an Authorization header using Bearer [REDACTED]`. Actual network/model response not established; set `HTTP_401_AUTH_ERROR_IN_PLAYGROUND` and no success.
- Official [AI Horde account registration](https://stablehorde.net/register) issues a recoverable personal API key via supported OAuth sign-in (GitHub/Google/Discord). Creating an unrecoverable pseudonymous key without sign-in is possible but not the recommended durable approach. Accounts and inference are volunteer-supported free; registered key can provide Kudos and higher priority than shared anonymous key.
- Crucial upstream [OmniRoute issue/discussion #15232](https://github.com/cheaper-inference/OmniRoute/discussions/15232): on 2026-10-01 another user reported **this exact 401 despite registering and adding a Horde key**. Maintainer 2026-10-02 said the integration should send the documented anonymous key but could not explain why 401 occurs; asked whether key was added as a provider connection versus model picker and for redacted logs. Therefore **neither a missing internal OmniRoute key nor a missing Horde key is confirmed as root cause**. Personal Horde account remains a good option independently; if one correctly configured key still produces identical 401, label the OmniRoute integration `BLOCKED_401_UPSTREAM_UNRESOLVED` and move to candidate #002 without repeated network audits. No bypass, paid service or speculative key header edits.
- Correct manual workflow: register a Horde account on the official site; obtain and privately save unique API Key; within OmniRoute `Providers → AI Horde → Add PAT` create a **provider-owned connection** using that Horde key, if the Add PAT form accepts it; select the newly created key/connection in Playground (not `default` if not bound); make at most one brief test. Do not confuse this provider PAT with the local OmniRoute client/gateway access key. **No key is to be pasted into chat, logs or GitHub.**
- Status: personal API account and model inference `NOT_DONE`; user action pending.

## دستور صریح کاربر

برای هر Provider رایگان/دارای سهمیه رایگان، **مدل را متناسب با وظیفه انتخاب کن** تا توان کافی با حداقل مصرف معقول requests/tokens/credits/kudos/compute/latency به‌دست بیاید. برای لایه‌های ابتدایی تعامل فارسی، تشخیص قصد، دریافت/ساخت دستور و انتقال امن پیام به لایه اجرایی، به‌طور پیش‌فرض از کوچک‌ترین مدل *واقعاً کافی و قابل‌دسترسی* استفاده شود؛ مدل قوی فقط برای کار تخصصی/استدلال پیچیده و پس از نیازسنجی. هدف کاهش جابه‌جایی دستی مکرر مدل‌ها، مدیریت سقف‌های رایگان و استفاده مؤثر از چند Provider رایگان است. این **الزام طراحی پذیرفته‌شده** است، نه ادعای ساخته‌شدن Route/Agent/ارسال پیام.

## قواعد الزام‌آور اجرایی

1. **Zero-model first:** کاری که parser/rule/FTS/validator/CLI قطعی امن می‌تواند انجام دهد، بدون مصرف توکن مدل انجام شود؛ مدل برای فهم فارسی و ابهام‌های واقعی. متن خام هر رویداد داخلی را بی‌دلیل دوباره به مدل نفرست.
2. **Capability tiers by role:** L0 = deterministic/no LLM، L1 = مدل سبک چندزبانه برای intent triage/خلاصه کوتاه/پاسخ ساده/ساخت پیام تحویل‌دادنی، L2 = مدل متوسط برای کدنویسی یا وظایف تخصصی، L3 = استدلال عمیق فقط با نیاز واقعی/تأیید. نقش و نمونه تست ملاک است، نه برند یا تعداد پارامتر به‌تنهایی.
3. **Sticky routing + bounded failover:** برای هر نقش یک primary پایدار و یک fallback مشروط تعریف شود. با هر درخواست مدل عوض نشود؛ فقط هنگام quota exhausted، worker unavailable، latency/quality failure یا نیاز به توان بیشتر و با محدودیت تعداد تلاش تغییر کند. fallback **تنها از allowlist رایگانِ واقعاً تأییدشده**؛ مسیر `auto` نامحدود/پرداختی مجاز نیست.
4. **Provider quota as first-class state:** نوع محدودیت جداگانه ثبت شود: requests/day/hour/minute، tokens/day/minute، free monetary credits، trial-only، concurrent slots، queue/volunteer workers، kudos/priority، per-model max context/output، account-level shared pools، refresh time، terms/region. مجهول را UNKNOWN ثبت کن؛ هرگز به همه سرویس‌ها سقف ساختگی ثابت نسبت نده.
5. **Admission gate Free-first:** Zero price and no card/overage, free model ID/limit, eligibility for an Iranian user, reachable actual inference route, permitted usage/ToS, privacy and account/session requirements **independently verify** before production activation. If cost/region/terms uncertain => `NOT_VERIFIED / DO_NOT_AUTO_ROUTE`. Trial/one-time credit را سهمیهٔ روزانه دائمی فرض نکن.
6. **Token economy:** context را متناسب با وظیفه محدود، تاریخچه را فشرده و dedupe، خروجی را کوتاه، `n=1`، retries bounded، `max_output_tokens` یا `max_length` کنترل‌شده و `max_context_length` کوچک ولی کافی نگه دار. تعداد پارامتر مدل **برابر با تعداد توکن مصرفی نیست**؛ الگوریتم tokenization و طول متن فرق دارد. در هر Provider cap واقعی را از API/GUI بخوان، نه اینکه صرفاً فرض شود.
7. **Safety of actions and user data:** LLM متن را بفهمد و یک **پیشنهاد ساختاریافتهٔ دستور** تولید کند؛ اجرای فایل/ارسال به سایر دستیارها/ایمیل/کدنویسی حساس با کنترل‌گر و مجوز انسانی انجام شود. صرف chat یا provider native tool calling، اتصال عملی agentها را اثبات نمی‌کند. داده مشتری/فایل خصوصی را به volunteer workers بدون مجوز نفرست.
8. **Real evidence:** provider را `CONNECTED_VERIFIED_FREE` فقط پس از تست کوچک واقعی و مشاهده پاسخ درست، هزینه صفر، سازگاری OmniRoute و ثبت مدل/مسیر بزن؛ پیش از آن `UI_ENABLED_NO_INFERENCE`/ `CONFIGURED_NOT_TESTED` بماند. آزمون شبکه GET فقط دسترسی HTTP است.
9. **Consumption ledger:** برای هر Provider × Model × Role این فیلدها را نگه دار: `provider_id`, `model_id`, `role_tier`, `free_verified`, `region_eligible`, `quota_type`, `limit`, `remaining_or_unknown`, `renewal`, `max_output`, `context_cap`, `request_count`, `observed_latency`, `success/failure`, `fallback_reason`, `last_checked`. هیچ secret/API-key/OTP/cookie در مخزن ذخیره نشود.
10. **Monitoring and upgrade boundaries:** review periodically when free terms/worker pool change; no automatic subscription/credit purchase/paid tier. Keep original evidence immutable, update effective allowlist only on fresh proof. No mass re-scans by default, no unauthorized external action.

## اولین پایلوت — OmniRoute Provider 001, AI Horde

**Observed user GUI:** AI Horde `Enabled=ON`; No authentication required; 0 connections (no personal PAT); three built-in text candidates labelled `Free (Assumed)`; Playground `Model=2DN` initially (this is an image model, not suitable for Persian chat); `Select key=(default)`. User opened a long model picker with many image models. No actual chat response yet. [UI evidence log](../06-tests-and-evidence/logs/OMNIROUTE-AIHORDE-001-UI-AND-LIGHT-MODEL-20261025.md).

**Provider accounting facts:** Anonymous API key is `0000000000`, used automatically by OmniRoute No-auth; anonymous lowest queue priority and possibly restricted under load. AI Horde is a volunteer-based free service with a `kudos` priority system, **not a documented fixed 100k/day token allowance**. Worker availability fluctuates and user must not treat 3 built-in *Assumed Free* items as guaranteed stable. No account, personal PAT or spending required for first anonymous test. Sources:
- https://github.com/Haidra-Org/AI-Horde/blob/main/README.md
- https://aihorde.net/
- https://oai.stablehorde.net/
- https://horde-sdk.readthedocs.io/en/stable/how-to/generate-text/
- https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.52/docs/reference/PROVIDER_REFERENCE.md

**Recommended first model:** `koboldcpp/gemma-4-E4B-it` (Gemma 4 E4B instruct) if it appears in the live `Model` dropdown / after import. Light multilingual chat candidate for early Persian command parsing, **not proven by a user's inference run**. A live official text-model status inspection reported at least one worker for this exact model, but online status is transient. Compared options: `google/gemma-4-31b` for higher-quality tasks (larger) and `Qwen/Qwen3.5-122B-A10B` for deep reasoning (limited volunteer availability); these are **not primary L1**. `2DN` is image-oriented and should not be selected for text chat.

**Single low-consumption first test:** select `koboldcpp/gemma-4-E4B-it` in Playground, `Select key=(default)`, send **one** short non-sensitive Persian message: `سلام. فقط در یک جمله فارسی بگو: آماده دریافت دستور هستم.`. Do not create additional personal PAT. If UI exposes output limit, start with `max_output_tokens ≈ 64` (API `max_length` 64; not necessarily exposed by GUI); if context limit exposed set ~512–1024 for this one-line task; `n=1`, no repeat storms. If those controls are absent, leave defaults and keep prompt short. Wait for one response/result. Observe HTTP/timeout/queue and quality; **do not claim success until actual response**.

**Architecture gap:** a Persian message being answered by the model does **not** imply ability to send instructions to other assistants. Real multi-agent dispatch, tools, authority, model quota controls and persistent state require separate orchestration, not provided or approved by this test. No architecture implementation authorized yet.

## Follow-up acceptance checklist

- [ ] `AI Horde / 001`: select **actual text model**, not image/roleplay; one real Persian Playground completion observed.
- [ ] Confirm runtime access from user's own ISP without VPN (prior GET 405 is not inference proof).
- [ ] Record effective limits/queue if shown; do not invent daily token allowance.
- [ ] Record user's observed answer/latency/error (sanitized) in tracker, not API secret.
- [ ] Keep free-only status; only then mark model operational for L1, and research additional official role-based fallback.

**User approval status:** Approval to **document this reusable policy** and **run one minimal user-directed GUI test** is present. No approval for developing a dispatcher/agent bridge, batch performance test, auto failover or paid inference.
