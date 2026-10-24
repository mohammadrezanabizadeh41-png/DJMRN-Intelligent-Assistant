# DJMRN — صف رسمی آزمون روترهای هوشمند مدل و سهمیه رایگان
**تاریخ ثبت:** 2026-10-24 | **وضعیت:** ترتیب آزمایش به درخواست کاربر ثبت شد؛ هیچ نصب، دانلود، ثبت‌نام یا مصرف API انجام نشد.

## 2026-10-24 — پس از تلاش نصب OmniRoute، تغییر مسیر به وب (User-reported)
- کاربر فایل `OmniRoute.Setup.3.8.52.exe` (~591MiB در نمایش ویندوز) را دریافت و **چند بار تلاش به نصب** کرد، اما گفته است اجازهٔ اجرا/نصب نمی‌دهد. **هیچ کد خطا یا گزارش قابل بررسی ارائه نشده؛ علت مسدودشدن UNKNOWN است.** این یعنی `BLOCKED` نه نقص قطعی OmniRoute یا FAIL همهٔ توانایی‌های آن. هیچ نسخه/کلید/اطلاعات حساسی در مخزن ذخیره نشد.
- **پژوهش مستقل وب:** سایت `https://omniroute.cheaperinference.com/` وب‌سایت معرفی و مستندات است؛ PWA `http://localhost:20128/dashboard` بدون اجرای backend محلی/سرور مستقل، درگاه مرکزی عملیاتی نیست. مستندات PWA GitHub صریحاً وابستگی به سرور را می‌گویند. سرویس تجاری جداگانهٔ `https://cheaperinference.com/` یک درگاه میزبانی‌شده با شارژ کیف پول (از $5) است و **جایگزین free-only BYOK با سهمیهٔ مستقل تأییدشده نیست**. هیچ حساب، پرداخت یا API اجرا نشد.
- **نامزد بعدی طبق صف D-017:** Cloudflare AI Gateway (میزبانی‌شده، کاملاً تحت وب)، وضعیت `NEXT_WEB_PILOT_PENDING_ACCESS_CHECK`؛ ثبت‌نام/دسترسی/فعال‌سازی Dynamic Routing و قیمت/مدل رایگانِ حقیقی باید در حساب کاربر بررسی شوند؛ Core gateway ظاهراً رایگان، اما API upstream می‌تواند هزینه داشته باشد. اگر این هم مناسب نبود New API و دیگر گزینه‌ها در [صف 27 تایی](ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv) باقی می‌مانند.
- **اقدام بعدی:** فقط بازدید از `https://dash.cloudflare.com/` و بررسی وجود AI Gateway در مرورگر، بدون کلید/API/اتصال حساب دیگر یا ساخت منابع پولی؛ سپس بررسی دقیق قابلیت موجود در صفحهٔ کاربر. OmniRoute HOLD، حذف فایل دانلودشده نیازمند اجازهٔ جدا. یادداشت پژوهشی/محدودیت در [evidence](../06-tests-and-evidence/logs/OMNIROUTE-WINDOWS-INSTALL-BLOCKED-WEB-PWA-CLARIFICATION-20261024.md).

## تصمیم اجرایی
- **نامزد نخست و انتخاب کاربر برای اولین آزمون: OmniRoute** (GitHub: https://github.com/cheaper-inference/OmniRoute). نصب‌کنندهٔ رسمی Windows v3.8.52 در GitHub Releases موجود است: https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52؛ فایل اعلامی `OmniRoute.Setup.3.8.52.exe` با حجم 620,348,073 بایت. انتشار بررسی شده ≠ امنیت یا عملکرد تأییدشده.
- **شرط حرکت در صف:** فقط اگر آزمون OmniRoute معیارهای ضروری را رد کند یا با منابع/امنیت/کاربر ناسازگار باشد، نامزد ردهٔ بعدی آزمایش می‌شود. نتیجه برای هر نامزد باید با PASS / FAIL / BLOCKED / NOT_TESTED همراه تاریخ، منبع و دلیل ثبت شود؛ هیچ‌کدام را ساکت حذف نکنید.
- **تغییر معیار انتخاب:** Windows Installer اجباری نیست. نرم‌افزار آماده با GUI/PWA، SaaS تحت وب و API مرکزی قابل استفاده است؛ پیاده‌سازی رابط اختصاصی، PowerShell روزمره و تجمیع DIY آخرین گزینه‌اند.
- **حفظ سابقه:** Bifrost پیشین فقط HOLD است؛ آزمایش‌های synthetic Linux موفق و نخستین بوت واقعی ویندوز که با timeout فهرست قیمت متوقف شد، تاریخی و مستقل باقی می‌مانند.
- **هزینه و اختیار:** Free-first، بدون ارتقای خودکار به پولی، کاربر قبل از نصب، کلید/API، حساب یا دسترسی سیستمی تصمیم می‌گیرد. اطلاعات شخصی/کلیدها در مخزن عمومی GitHub ممنوع‌اند.

## ترتیب مشخص آزمون (27 نامزد، بر اساس نتیجهٔ پژوهش قبلی)
| اولویت | گزینه | اجرای آماده | دلیل جایگاه | وضعیت |
|---:|---|---|---|---|
| 1 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52) | Windows Setup EXE + PWA/web dashboard | free-catalog, quota-aware pools, task tiers, fallback, GUI, export/import | USER_SELECTED_FIRST |
| 2 | [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) | managed website | visual routing, rate/budget policy, fallback, hosted | WAITING_OMNIROUTE_RESULT |
| 3 | [New API](https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.46) | Windows EXE + web dashboard | channel key pools, group quotas, priority/weight/failover | WAITING_PREVIOUS_RESULT |
| 4 | [Requesty](https://www.requesty.ai/pricing) | managed website | hosted free models and routing | WAITING_PREVIOUS_RESULT |
| 5 | [Portkey Cloud](https://portkey.ai/pricing) | managed website | fallback/routing/virtual keys/dashboard | WAITING_PREVIOUS_RESULT |
| 6 | [free-llm-proxy-router](https://github.com/kaiser-data/free-llm-proxy-router/releases/tag/v0.1.1) | Windows ZIP Go binary | free-provider scanning, 429 cooldown, no web GUI | WAITING_PREVIOUS_RESULT |
| 7 | [CC Switch](https://github.com/farion1231/cc-switch/releases/tag/v4.0.19) | Windows MSI/portable | native GUI & developer tool proxy switching | WAITING_PREVIOUS_RESULT |
| 8 | [free-llm-gateway](https://github.com/malda231125/free-llm-gateway) | source-hosted Node | task-aware free-model routing, SQLite accounting | WAITING_PREVIOUS_RESULT |
| 9 | [Arbiter](https://github.com/koushikch7/arbiter) | self-host dashboard/Redis | free provider pool, fallback, quota dashboard | WAITING_PREVIOUS_RESULT |
| 10 | [LLM Router](https://github.com/JayRajankar/LLM-Router/releases/tag/MSI) | Windows MSI | complexity-aware route & free providers | WAITING_PREVIOUS_RESULT |
| 11 | [free-llm-router](https://github.com/YeomanYe/free-llm-router) | source/CLI | tiers and free model discovery | WAITING_PREVIOUS_RESULT |
| 12 | [llm-router](https://github.com/alienz-dev/llm-router) | Python service | availability/fallback/free provider policy | WAITING_PREVIOUS_RESULT |
| 13 | [Ficelle](https://ficelle.ai/) | local gateway GUI | strict free-only behavior | WAITING_PREVIOUS_RESULT |
| 14 | [OpenRouter Free](https://openrouter.ai/openrouter/free) | managed website + API | hosted zero-cost model selection | WAITING_PREVIOUS_RESULT |
| 15 | [Cherry Studio](https://github.com/CherryHQ/cherry-studio/releases) | Windows installer | GUI/API gateway/backup | WAITING_PREVIOUS_RESULT |
| 16 | [Inference Gateway Desktop](https://github.com/inference-gateway/desktop/releases) | Windows desktop | local provider GUI & gateway | WAITING_PREVIOUS_RESULT |
| 17 | [Maxim Bifrost Gateway](https://github.com/maximhq/bifrost/releases/tag/transports/v2.3.2) | native Windows EXE + web dashboard | virtual keys, budget, provider route, genuine CI synthetic tests | HOLD_PREVIOUS_PILOT |
| 18 | [LiteLLM Proxy](https://github.com/BerriAI/litellm) | self-host gateway | multi-provider virtual-key budgets and failovers | WAITING_PREVIOUS_RESULT |
| 19 | [One API](https://github.com/songquanpeng/one-api) | web dashboard + single binary | model channel aggregation and quotas | WAITING_PREVIOUS_RESULT |
| 20 | [Vercel AI Gateway](https://vercel.com/docs/ai-gateway/authentication-and-byok/byok) | managed website | managed model routing and budgets | ON_HOLD_COST_RISK |
| 21 | [Helicone](https://www.helicone.ai/) | managed website/self-host | observability and AI routing | WAITING_PREVIOUS_RESULT |
| 22 | [Kong AI Gateway](https://konghq.com/products/kong-ai-gateway) | cloud/self-host infra | enterprise routing policies | WAITING_PREVIOUS_RESULT |
| 23 | [Apache APISIX](https://apisix.apache.org/) | self-host infra | gateway policies/extensions | WAITING_PREVIOUS_RESULT |
| 24 | [Higress AI Gateway](https://github.com/alibaba/higress) | self-host infra | cloud routing/plugins | WAITING_PREVIOUS_RESULT |
| 25 | [Agentgateway](https://github.com/agentgateway/agentgateway) | self-host infra | agent traffic policies | WAITING_PREVIOUS_RESULT |
| 26 | [FreeRouter (Laravel)](https://github.com/freerouter/freerouter) | self-host source | BYOK fallback | WAITING_PREVIOUS_RESULT |
| 27 | [FreeRouter (Go)](https://github.com/Abraxas-365/freerouter) | self-host source | cost routing and dashboard | WAITING_PREVIOUS_RESULT |

**فهرست ماشینی:** [ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv](ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv)؛ این فایل منبع ترتیب، وضعیت و آخرین بررسی است. انتخاب شدن برای صف معادل نصب شدن/آزموده شدن نیست. برای پوشش عمیق ۲۷ ابزار و شواهد، [پژوهش اولیه](../03-architecture-and-tools/WIDE-SCAN-FREE-QUOTA-AWARE-MULTI-LLM-ROUTERS-20261024.md) را بخوانید.

## دروازهٔ گذر از نامزد (همهٔ معیارها مهم)
1. محصول واقعاً آمادهٔ استفاده است: Installer معتبر یا صفحهٔ SaaS قابل‌ورود؛ بدون نوشتن رابط مخصوص DJMRN.
2. **یک API مرکزی OpenAI-compatible** که حداقل سه دستیار مستقل را سرویس دهد؛ نه صرفاً چت شخصی.
3. اتصال حداقل دو تأمین‌کنندهٔ **رایگانِ واقعاً مجاز در حساب کاربر**؛ سقف/تجدید سهمیه و وضعیت Billing از منبع رسمی کنترل شوند.
4. دسته‌بندی دستیارها بر اساس توان لازم: High=programming/research؛ Medium=opportunity analysis؛ Low=email classification/background؛ strong-quota reservation در صورت پشتیبانی.
5. سهمیهٔ جداگانه برای دستیار یا virtual keys و محدودیت RPM/TPM/RPD یا مکانیسم معادل؛ شمارنده باید باقی بماند و بعداً قابل‌ممیزی باشد.
6. خطای 429 و 5xx → Fallback به **فقط مدل رایگان و مجاز**؛ ناشناخته/پولی/بدون سهمیه → DENY بدون تماس، نه auto-upgrade.
7. رابط قابل فهم برای دیدن مدل‌ها/مصرف/مسیرها و پشتیبان‌گیری/بازیابی پس از تغییر ویندوز یا رایانه.
8. برای نسخهٔ محلی: RAM و CPU کم‌مصرف روی Windows 11 با 8GB RAM؛ برای SaaS: دسترسی پایدار، داده و حریم خصوصی.
9. عدم نصب certificate root، MITM، proxy کل سیستم، permission گسترده، ماندگاری در startup یا لو دادن API keys مگر با درخواست و تأیید جداگانه.
10. گزارش آزمون با شواهد واقعی؛ **قابلیت ادعاشدهٔ README = VERIFIED DOC، نه PASS عملی**.

## سیاست تصمیم
- اگر همهٔ 1/2/3/5/6/7 در کار واقعی PASS و منابع قابل قبول → `ACCEPTED_FOR_BOUNDED_PILOT`؛ ارتقای تولید مستقل.
- اگر هر الزام ضروری FAIL و راه‌حل آماده/بدون کدنویسی موجود نباشد → `REJECTED_WITH_REASON` و نامزد بعدی در صف.
- اگر امکان آزمون هنوز نیست یا دسترسی/مبلغ نامعلوم است → `BLOCKED_NEEDS_EVIDENCE`، نه موفقیت فرضی.
- برای ابزارهای خطرناک یا متوقف‌شده در صف (مثل BYOK fallback پولی)، فقط پس از رفع ریسک و مجوز مجدد بازبینی.
- در هر نامزد ثبت: `candidate_id, version, source/ref, approval, installation/deployment, test_case, outputs, CPU/RAM, budgets, provider costs, account permission, backup_restore, decision, next candidate`.
- هیچ حساب کلید و دیتابیس خصوصی در GitHub آپلود نشود.

## مسیر ادامهٔ جلسهٔ بعد
1. [آزمون مرحله‌ای OmniRoute](../06-tests-and-evidence/plans/OMNIROUTE-WINDOWS-FIRST-PILOT-20261024.md) را بخوان.
2. از صفحهٔ GitHub Releases، فقط انتشار واقعی/چک‌سام و مجوزها را تأیید کن؛ نسخهٔ توسعهٔ `release/v3.8.53` را با انتشار `v3.8.52` اشتباه نگیر.
3. ابتدا بدون اتصال حساب‌ها، از کاربر برای نصب/اجرای مستقیم دستگاهش مجوز بگیر؛ سپس آزمون‌های P01–P10.
4. اگر رد شد، Cloudflare Dynamic Routing؛ اگر Cloudflare رد شد، New API؛ سپس ادامه مطابق CSV.

**تصمیم دامنه:** [D-017](DECISION-REGISTER.md)؛ **وظیفه:** [TASK-0029](TASK-REGISTER.md). D-005 (انتخاب کل معماری) همچنان باز است.
