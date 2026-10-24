# DJMRN — START HERE: گزارش کامل انتقال روتر و مدل‌های رایگان به گفت‌وگوی جدید

**تاریخ انتقال:** 2026-10-24. **مخزن اصلی:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`، شاخه `main`، عمومی (PUBLIC). **وضعیت:** ثبت تاریخچه و برنامهٔ ادامه، نه راه‌اندازی یا نصب تازه. ابتدا این فایل و سپس [CURRENT-STATUS](CURRENT-STATUS.md) را بخوانید؛ اعتبار آخرین تصمیم با وضعیت زندهٔ GitHub است.

## ۱. هدف واقعی و شرایط غیرقابل چشم‌پوشی

ساخت/انتخاب یک **روتر مرکزی آمادهٔ OpenAI-compatible** برای چندین دستیار مستقل DJMRN (برنامه‌نویسی، پژوهش، فرصت‌های فریلنسری، ایمیل و امور سبک). سرویس باید بتواند به ارائه‌دهندگان مختلف رایگانِ مجاز متصل شود، مدل‌ها را بر اساس **درجهٔ هوش/قابلیت کار** (High / Medium / Light) انتخاب کند، سهمیهٔ مدل‌های قوی‌تر را برای کارهای مهم نگه دارد، به هر دستیار **محدودیت مصرف مستقل** بدهد، مصرف و خطا را ثبت کند و هنگام 429/5xx به **مدل رایگان و کافیِ دیگر** با Failover امن منتقل شود. نیازهای مهم: کشف مدل‌های جدید، نمایش سهمیهٔ واقعی یا تخمینی با تفکیک واضح، حداکثر استفادهٔ قانونی از free tiers، جلوگیری قطعی از فعال‌شدن مدل/مسیر پولی و هزینهٔ ناشناخته.

**تغییر صریح شرایط توسط کاربر:** نصب‌کنندهٔ Windows اجباری نیست؛ **نرم‌افزار آمادهٔ دسکتاپ، روتر دارای پنل تحت وب یا SaaS میزبانی‌شده** قابل قبول است. اما ساخت لانچر اختصاصی، استفادهٔ روزمره از PowerShell، برنامه‌نویسی قابل توجه برای پوستهٔ مدیریت و وابستگی مداوم به دستیار خارجی ترجیح ندارد. انتقال به ویندوز/دستگاه جدید با نصب ساده یا login/backup باید ممکن باشد. در رتبه‌بندی نرم‌افزار **محدودیت جغرافیایی ایران را معیار انتخاب قرار ندهید**، اما هنگام اتصال واقعی حساب یا API، مقررات/Eligibility/صورتحساب و هزینهٔ ناشناخته بررسی شود؛ Unknown = Deny. دستگاه: Windows 11 Pro x64؛ AMD Ryzen 5 3500U، RAM 8GB؛ برنامهٔ سنگین Electron باید مصرف RAM آن اندازه‌گیری شود. Free-only، بدون خرید/ارتقا/پرداخت/ API تا تأیید مستقل کاربر.

## ۲. چه کارهایی واقعاً انجام شد؟ مسیر تاریخی

### الف) Maxim Bifrost v2.3.2؛ روتر قبلی — آزمایش واقعی اما راه‌اندازی ناقص
- D-016: `maximhq/bifrost` برای ارزیابی Cloud-First انتخاب شد. به‌صورت **native Windows EXE** عرضه می‌شود و داشبورد وب دارد. `Bifrost Edge` نسخهٔ MSI از همان شرکت اما **Agent سازمانی کنترل Endpoint** است و جایگزین Gateway نیست؛ `bifrost-proxy/bifrost` پروژهٔ کاملاً متفاوت و نامرتبط است.
- نصب/اجرای اولیه با `npx` و cache نامناسب: Windows binary با سرآیند PE ولی تنها **57,943 بایت** در برابر **134,305,792 بایت** رسمی؛ `EFTYPE`. **ZIP راه‌حل قبلیِ تغییرنام cache نباید استفاده شود.**
- سپس فایل کامل اصلی از `https://downloads.getmaxim.ai/bifrost/v2.3.2/windows/amd64/bifrost-http.exe` دانلود شد؛ **134,305,792/134,305,792**، SHA256 **محلیِ اندازه‌گیری‌شده** `430D365584D6F47CC8167AC65A747163AB6FB1ECCF666978F37B263E63C377B2`. امضای Windows Authenticode `NotSigned` بود، SHA منتشرشدهٔ مستقل سازنده **تطبیق نیافت**. بررسی SHA/size و PE64 AMD64 پاس شد، اسکن سفارشی Windows Defender بدون خطای دستور پایان یافت (نه تضمین امنیت).
- **اجرای واقعی user** در 23 اکتبر ساعت 22:39–22:40 (+03:30): Bifrost نسخهٔ 2.3.2 اجرا و config محلی را خواند؛ migration جداول SQLite **موفق** بود؛ سپس درخواست الزامی قیمت به `https://getbifrost.ai/datasheet` با `context deadline exceeded` شکست؛ **Exit code 1**. یعنی API Gateway و داشبورد عملیاتی/سلامت‌شان هرگز ثابت نشد؛ **هیچ تماس واقعی Groq یا Jan از این روتر انجام نشده است**.
- مستند سازنده برای شبکه‌های مسدود، datasource محلی `file://` پیشنهاد می‌کند؛ دستور آماده‌سازی نمونهٔ pricing/model-parameters به کاربر داده شد ولی **اجرای موفق یا اتصال بعدی در شواهد وجود ندارد**. کاربر ادامهٔ PowerShell/لانچر اختصاصی را کنار گذاشت تا نرم‌افزار آماده بیابد.
- **آزمون مستقل CI روی GitHub Actions، نه دستگاه ویندوز:** P2C با Bifrost واقعی + دو upstream *ساختگی* امنیت 401/403 و fallback 429/503 را بررسی کرد؛ P2D admission/quota با SQLite مصنوعی؛ P2E **57/57** تست آفلاین و **10** ادغام مصنوعی موفق؛ P2F **73/73** تست آفلاین و **19** بررسی front/back مصنوعی موفق، با گزارش خطاهای اجراهای پیشین حفظ‌شده. این‌ها **هیچ ربطی به سهمیهٔ واقعی حساب‌های Groq/Gemini، هزینهٔ واقعی، نصب روی دستگاه، یا اجرای تولیدی ندارند**.
- منابع: [دانلود و هش](../06-tests-and-evidence/logs/WINDOWS-BIFROST-FULL-SIZE-DOWNLOAD-20261023.md)، [پیش‌آزمون ویندوز](../06-tests-and-evidence/logs/WINDOWS-BIFROST-USER-DEFENDER-PE-PREFLIGHT-20261023.md)، [لاگ اولین اجرای واقعی](../06-tests-and-evidence/logs/WINDOWS-BIFROST-USER-NATIVE-BOOT-PRICING-TIMEOUT-20261023.md)، [P2C](../06-tests-and-evidence/logs/ROUTER-P002C-REAL-BIFROST-SYNTHETIC-GATEWAY-PASS-20261023.md)، [P2D](../06-tests-and-evidence/logs/ROUTER-P002D-FREE-QUOTA-ADMISSION-TESTED-SYNTHETIC-20261023.md)، [P2E](../06-tests-and-evidence/logs/ROUTER-P002E-LIVE-GATEWAY-ADMISSION-SYNTHETIC-PASS-20261023.md)، [P2F](../06-tests-and-evidence/logs/ROUTER-P002F-LIVE-SEGREGATED-FRONT-AND-RESTART-PASS-20261023.md).

### ب) جست‌وجوی تکمیلی و انتخاب ۲۷ نامزد
کاربر تصریح کرد که صرفاً Windows installer نخواهیم؛ **وب‌سایت فعال، سرویس SaaS، مخزن GitHub و برنامهٔ نصب‌شدنی** همه نامزد هستند، با ارجحیت راه‌حلِ بدون ساخت. گزارش مفصل، قابلیت/ریسک/وضعیت مستند/لینک هر نامزد در [WIDE SCAN](../03-architecture-and-tools/WIDE-SCAN-FREE-QUOTA-AWARE-MULTI-LLM-ROUTERS-20261024.md) و [صف ۲۷ موردی با وضعیت](../02-project-management/ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv) ثبت شد. README یا ستارهٔ GitHub **شاهد عملکرد واقعی، اصالت فایل یا سهمیهٔ در اختیار کاربر نیست**.

### ج) OmniRoute v3.8.52 — اولویت نخست و تلاش نصب
D-017 و TASK-0029: به خواست user، **OmniRoute FIRST**، سپس Cloudflare AI Gateway، New API و دیگر نامزدها به‌ترتیب. صفحهٔ رسمی release: https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52. فایل `OmniRoute.Setup.3.8.52.exe` در GitHub با طول **620,348,073 بایت** و SHA256 منتشرشدهٔ asset `5888fea85c0f9bb092e5d351fda1e5a11c6f71b2e75df6932d3dc008d440154d` معرفی شده است. **SHA فایل دانلودشده روی ویندوز user اندازه‌گیری نشد**؛ کاربر اندازهٔ نمایش داده‌شدهٔ حدود ۵۹۱ MiB را گزارش کرد.
کاربر گفت فایل «اجازهٔ اجرا پیدا نمی‌کند» و با روش‌های مختلف نصب نشده است. **نه تصویر پیام خطا، نه کد Installer، نه وضعیت قطعی Defender/SmartScreen/Smart App Control، نه لاگ رویداد** در اختیار نداریم. وضعیت `BLOCKED_USER_REPORTED_INSTALL_NO_LOG`؛ **نصب موفق یا نقص قطعی نرم‌افزار را ادعا نکنید**. از خاموش‌کردن/دورزدن هشدار امنیتی برای نصب خودداری شود؛ در صورت تغییر تنظیمات امنیتی، بازبینی و فعال‌بودن آنها با GUI ضروری است.
- کاربر پرسید آیا **وب OmniRoute** جای نصب را می‌گیرد؟ PWA/داشبورد OmniRoute معمولاً `http://localhost:20128/dashboard` است و **بدون backend در حال اجرای محلی/سروری کار نمی‌کند**. `https://omniroute.cheaperinference.com/` صفحهٔ معرفی/راهنماست، نه یک gateway hosted رایگان با همهٔ قابلیت‌ها؛ `https://cheaperinference.com/` سرویس تجاری میزبانی‌شدهٔ کیف‌پولی مجزاست و free-only BYOK جامع اثبات نشده. [تحقیق و لاگ بلوکه‌شدن](../06-tests-and-evidence/logs/OMNIROUTE-WINDOWS-INSTALL-BLOCKED-WEB-PWA-CLARIFICATION-20261024.md).
- **OmniRoute اکنون HOLD**، نه «برای همیشه رد شده»؛ اگر بعداً کاربر خواست، علت دقیق مسدودی را ایمن عیب‌یابی کنید. هیچ گفت‌وگوی مدل از OmniRoute و هیچ نصب موفق دیده نشده است.

## ۳. صف دقیق باقی نامزدها؛ ترتیب بازیابی‌پذیر
صف مرجع زنده: [Markdown مفصل](../02-project-management/ROUTER-CANDIDATE-TRIAL-QUEUE-20261024.md) و [CSV ۲۷ موردی](../02-project-management/ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv).
| رتبه | گزینه | نوع/ارزش | وضعیت |
|---:|---|---|---|
| 1 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52) | Windows Setup + PWA؛ سهمیه و free pools و کیفیت مدل | نصب کاربر BLOCKED؛ HOLD |
| 2 | [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) | SaaS/browser؛ Dynamic Routing، policy/fallback/budget | **NEXT: بررسی دسترسی در حساب** |
| 3 | [New API](https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.46) | Windows native EXE + داشبورد وب/کانال‌ها | جایگزین بعدی، NOT_RUN |
| 4 | [Requesty](https://www.requesty.ai/pricing) | SaaS؛ مدل‌های free و fallback | شرایط BYOK و هزینه را بررسی کنید |
| 5 | [Portkey Cloud](https://portkey.ai/pricing) | API مرکزی hosted؛ routing/metrics | Free plan و هزینهٔ upstream نامعلوم |
| 6 | [free-llm-proxy-router](https://github.com/kaiser-data/free-llm-proxy-router/releases/tag/v0.1.1) | Go Windows ZIP، free scan و cooldown | GUI/per-assistant quotas ناکامل |
| 7 | [CC Switch](https://github.com/farion1231/cc-switch/releases/tag/v4.0.19) | Windows MSI/Portable، سوئیچ coding CLIs | کل دستیارها پوشش تأییدشده ندارد |
| 8 | [free-llm-gateway](https://github.com/malda231125/free-llm-gateway) | هوشمندسازی prompt و SQLite quota | پروژهٔ کوچک |
| 9 | [Arbiter](https://github.com/koushikch7/arbiter) | dashboard/Redis و free quota | پیچیدگی استقرار |
| 10 | [LLM Router](https://github.com/JayRajankar/LLM-Router/releases/tag/MSI) | Windows MSI؛ complexity-aware | نسخهٔ اولیه، امنیت/نگهداری نیازمند بررسی |
| 11 | [free-llm-router](https://github.com/YeomanYe/free-llm-router) | tier routing + free detection | Streaming و tool support ناکامل |
| 12 | [llm-router](https://github.com/alienz-dev/llm-router) | سرویس Python free-provider | setup بیشتر |
| 13 | [Ficelle](https://ficelle.ai/) | free-only routing | Free Core ارائه‌دهندگان کم |
| 14 | [OpenRouter Free](https://openrouter.ai/openrouter/free) | hosted free model router | سهمیهٔ مستقل سایر APIها را ادغام نمی‌کند |
| 15 | [Cherry Studio](https://github.com/CherryHQ/cherry-studio/releases) | نصب ویندوز، UI، gateway محلی و backup | بودجهٔ هر دستیار/failover پیشرفته unverified |
| 16 | [Inference Gateway Desktop](https://github.com/inference-gateway/desktop/releases) | UI نصب‌شدنی و API | fallback/complex route نامطمئن |
| 17 | [Maxim Bifrost](https://github.com/maximhq/bifrost) | حرفه‌ای virtual keys/quota/fallback | Windows first boot timeout؛ HOLD |
| 18 | [LiteLLM](https://github.com/BerriAI/litellm) | full proxy/virtual-key budgets | سرویس‌داری/امنیت release |
| 19 | [One API](https://github.com/songquanpeng/one-api) | single binary+dashboard و key quotas | بررسی نگهداری |
| 20 | [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) | SaaS routing | **ریسک paid fallback**؛ HOLD |
| 21 | [Helicone](https://www.helicone.ai/) | routing + logging | Free-discovery محور اصلی نیست |
| 22 | [Kong AI Gateway](https://konghq.com/products/kong-ai-gateway) | زیرساخت enterprise | عملیات سنگین |
| 23 | [Apache APISIX](https://apisix.apache.org/) | API gateway متن‌باز | DevOps |
| 24 | [Higress](https://github.com/alibaba/higress) | gateway/plug-ins | container/infra |
| 25 | [Agentgateway](https://github.com/agentgateway/agentgateway) | policy/agent gateway | سهمیهٔ free مدل اثبات نشده |
| 26 | [FreeRouter Laravel](https://github.com/freerouter/freerouter) | BYOK/fallback | Alpha |
| 27 | [FreeRouter Go](https://github.com/Abraxas-365/freerouter) | Go+dashboard/quotas | تازه و کم‌بررسی |

**کشف مستقل مدل رایگان** (مکمل روتر نه جایگزین): https://freeinference.dev/data/providers.json ، https://llmroster.dev ، https://openrouter.ai/models?pricing=free . مدل‌/سهمیه/قیمت این منابع باید همان روز کنترل شود.

## ۴. چه نرم‌افزارهای دیگری روی ویندوز سابقهٔ نصب و آزمایش دارند؟
[Inventory 21 item historical snapshot](../01-system-inventory/installed-software-snapshot-20261023.csv): Windows 11 Pro x64؛ Node.js v24.22.1، npm/npx؛ Python 3.14.7، Git 2.55.0.windows.5، VS Code، WinGet؛ **Jan Desktop/Jan Agent**, **Ollama 0.40.6-rc1**, **LM Studio کلاسیک و Bionic/llmster**, **LlamaApp v0.12.0**, **KYNXA Desktop v1.7.0**, **Goose Desktop**, ChatGPT Desktop. بعضی نسخه‌ها صرفاً تاریخی‌اند و نباید به‌عنوان status امروز ادعا شوند. **KYNXA UI دیده شد ولی پاسخ واقعی مدل تأیید نشد**؛ **Goose/Gemma 3 1B پاسخ فارسی داد اما کیفیت مناسب نبود**؛ حافظهٔ 8GB برای مدل قوی محلی محدودیت دارد. Jan local API قدیمی `http://127.0.0.1:1337/v1` هنوز به هیچ روتر Cloud-First عملیاتی وصل نشده؛ Docker Desktop روی لپ‌تاپ **تأیید نشده** و اجرای GitHub Actions Docker هیچ چیز دربارهٔ دستگاه اثبات نمی‌کند. هر کدام با شواهد جزئی در [software inventory](../01-system-inventory/software-inventory.md) ثبت شده‌اند.

## ۵. آمار، قواعد، حد و مرز
- [سابقهٔ eventها](../01-system-inventory/installation-events.csv) پس از ثبت download/attempt نصب OmniRoute شامل **18 رویداد** است؛ 18 نصب موفق نیست. [Snapshot تاریخی 21 component](../01-system-inventory/installed-software-snapshot-20261023.csv) ترکیبی از نصب، ناموجود، نامطمئن و سرویس است. [خلاصهٔ 24 اکتبر](../01-system-inventory/ROUTER-INSTALL-AND-TEST-SNAPSHOT-20261024.md).
- ادعای ویژگی در GitHub README = RESEARCHED، وجود فایل release = RELEASE VERIFIED، لاگ user = USER-REPORTED DEVICE، CI با ارائه‌دهنده ساختگی = TESTED-SYNTHETIC؛ هنوز **هیچ اتصال واقعی مدل/API رایگان و هزینهٔ صفر از طریق روتر مرکزی ثابت نشده**.
- مخزن **عمومی** است؛ کلید API، رمز admin، token قبلی، شماره تماس، نام user profile/مسیر حساس، cookie و دادهٔ Gmail/مشتری ثبت نشود. اولین setup token قدیمی در چت تاریخی در معرض قرار گرفته بود و نباید بازاستفاده شود.
- **D-005 انتخاب کامل معماری باز**، D-016 نامزد تاریخی Bifrost، **D-017 ترتیب آزمون**، **TASK-0029 فعلی**. G3B/M1 مجوز فایل‌های شخصی CLOSED. بدون تأیید صریح: نصب، تغییر Defender، پرداخت، ثبت حساب، API key، اتصال Gmail، تماس واقعی مدل و ارسال خارجی انجام نشود.

## ۶. دقیقاً در پنجرهٔ بعدی از کجا شروع کنیم؟
**بازنگری مقایسه‌ای در همان روز به درخواست کاربر:** [OmniRoute npm/backend + وب در برابر Cloudflare میزبانی‌شده](../03-architecture-and-tools/OMNIROUTE-NPM-VS-CLOUDFLARE-WEB-DECISION-REVIEW-20261024.md) با اسناد رسمی بررسی شد. نتیجه فقط **پیشنهاد مشروط انجام یک آزمایش محدود npm** روی ویندوز (Node موجود، بدون Electron installer) پیش از Cloudflare است؛ نه نصب واقعی، نه تغییر D-017 به یک معماری مصوب. Cloudflare Auto Router واقعاً مدل را براساس سختی کار انتخاب می‌کند، اما پیش‌فرض آن شامل مدل‌های پولی است. فهرست رایگان و Radar در OmniRoute نیز مجوز سهمیه یا تضمین هزینه صفر نیست؛ اتصال ارائه‌دهنده/کلید/هزینه مرحلهٔ جداگانه و نیازمند approval است.

**تکمیل ۲۴ اکتبر در پنجرهٔ جدید:** [پیش‌بررسی رسمی Cloudflare AI Gateway و هشدار مسیرهای دارای هزینه](../06-tests-and-evidence/logs/CLOUDFLARE-AI-GATEWAY-READONLY-PREFLIGHT-20261024.md) ثبت شد. Core Gateway رایگان اعلام شده اما inference/upstream رایگان فرض نمی‌شود؛ Dynamic Routes نیازمند بررسی دسترسی حساب است و gateway پیش‌فرض ممکن است Workers AI Standard billing را فعال داشته باشد. مرحلهٔ بعد صرفاً مشاهدهٔ پنل حساب موجود بدون ساخت gateway، اتصال API، کلید، پرداخت یا درخواست مدل است. این مدرک **RESEARCHED** است نه آزمون عملی یا انتخاب معماری.

**قدم پیشنهادی با کمترین نصب:** گزینهٔ دوم فهرست، [Cloudflare Dashboard](https://dash.cloudflare.com/)؛ در رابط وب بررسی کنید آیا AI Gateway و Dynamic Routing (Beta) برای حساب کاربر واقعاً در دسترس است. اگر نیست/تطابق ندارد → [New API](https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.46)، سپس گزینه‌های بعدی طبق CSV. هیچ کلید واقعی، هزینه، API call یا ثبت‌نام را قبل از بررسی و تأیید انجام ندهید. **برای وب OmniRoute، صرف بازکردن landing page جای backend را نمی‌گیرد.** کاربر در صورت تمایل می‌تواند بعداً عیب‌یابی امنیتی نصب‌کنندهٔ مسدودشده را جداگانه انتخاب کند؛ نیازی نیست به PowerShell طولانی یا ساخت UI اختصاصی Bifrost برگردیم.

**طرح‌های فنی:** [OmniRoute pilot 10 gates](../06-tests-and-evidence/plans/OMNIROUTE-WINDOWS-FIRST-PILOT-20261024.md)، [27 candidate queue](../02-project-management/ROUTER-CANDIDATE-TRIAL-QUEUE-20261024.md)، [overview research](../03-architecture-and-tools/WIDE-SCAN-FREE-QUOTA-AWARE-MULTI-LLM-ROUTERS-20261024.md)، [OmniRoute web/install evidence](../06-tests-and-evidence/logs/OMNIROUTE-WINDOWS-INSTALL-BLOCKED-WEB-PWA-CLARIFICATION-20261024.md).
