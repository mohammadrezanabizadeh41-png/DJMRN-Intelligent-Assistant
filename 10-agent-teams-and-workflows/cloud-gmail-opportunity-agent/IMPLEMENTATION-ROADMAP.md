# DJMRN — نقشه راه اجرایی ساخت بستر ابری چندمنظوره ایجنت‌ها

**Project home:** DJMRN-CLOUD-GMAIL-OPPORTUNITY-001 (historical identifier retained to avoid breaking links)
**Current project meaning:** DJMRN Cloud Agent Foundation — reusable cloud agent execution capability; Gmail and job follow-up are future applications.
**Revision:** 2026-11-12 — FOUNDATION-FIRST / OWNER CORRECTION. This document **SUPERSEDES the previous Gmail/portfolio-first R0–R10 roadmap**. Preserve old Git version in commit history rather than mixing two current plans.
**Priority:** next DJMRN project; first build cloud environment, then prove agents/model/tools/state/scheduling, then select applications.
**Status:** ROADMAP / NOT DEPLOYED / NO HOST SELECTED / NO CLOUD AGENT RUNNING.
**Authority:** GitHub code/spec/tests; Notion accepted architecture/decisions; one selected database for runtime state; cloud service for actual runtime; human for permissions. Sole rolling progress: 07-operations-and-continuity/CURRENT-STATUS.md.
**Safety:** Repository observed PUBLIC; no personal data, account IDs, email body, secrets, API keys, OAuth tokens, session cookies or private customer information in this document.

## 0. تعریف درست هدف، معیار موفقیت و مرز پروژه

هدف فعلی **ساخت فضای ابری مستقل، امن، کم‌هزینه و چندمنظوره** است که در زمان خاموش‌بودن لپ‌تاپ نیز بتواند چند وظیفه محدود را روی سرویس ابری انجام دهد، با مدل‌های دارای API رسمی کار کند، ابزارهای مجاز را فراخوانی کند، وضعیت را نگه دارد، نتیجه و خطا را ثبت کند و در آینده بتواند با ایجنت‌های ویندوز و چند کاربرد متفاوت همکاری کند.

**این پروژه در فاز زیرساخت به Gmail، رزومه، پورتفولیو، استخدام یا معاملات وابسته نیست.** اینها بعداً ماژول/مأموریت‌های قابل اتصال خواهند بود؛ حق ساخت امروز را ایجاد نمی‌کنند.

**Definition of first operational value (Cloud Agent V0):**
1. یک سرویس ابری با پلن رایگان پایدار و مجاز، مستقل از لپ‌تاپ و VPN محلی، وجود داشته باشد.
2. یک وظیفه محدود و بی‌خطر با ورودی واقعی عمومی (برای مثال خواندن یک URL مستندات عمومی یا RSS) اجرا شود؛ اگر لازم بود یک مدل با API موجود و مجاز آن را خلاصه کند. اجرای نمادین/صرفاً نصب = DONE نیست.
3. خروجی، منبع، شناسه job، وضعیت و خطا در یک محل پایدار مورد تأیید نگه‌داری شود، اجرای تکراری باعث کار تکراری نشود، و پس از خاموشی/اجرای دوباره قابل بازیابی باشد.
4. زمان‌بندی محدود، سقف رایگان و توقف در quota/error قابل آزمون باشد؛ کاربر بتواند خروجی را از تلفن/وب بدون لپ‌تاپ دریافت کند.
5. هیچ پورت ویندوزی باز، داده خصوصی منتشر، هزینه پرداخت یا ابزار اضافی بدون approval ایجاد نشود.

**بستر ابری لزوماً VM همیشه‌روشن نیست.** Serverless/Functions که با schedule یا HTTP بیدار می‌شوند و state پایدار دارند، برای مأموریت‌های دوره‌ای ممکن است بهتر و رایگان‌تر باشند. اگر بعداً واقعاً agent session زنده و طولانی یا UI دائمی نیاز شد، میزبان دائم را جدا ارزیابی می‌کنیم.

## 1. نقشه لایه‌ها و نقش‌های قابل جایگزینی (PROPOSAL)

- **Cloud Runtime / Executor:** فضای واقعی اجرای کد/Agent، فراخوانی ابزارها و نگهداری حداقل session در حافظه هنگام اجرا. یک مالک اجرایی برای هر job.
- **Agent Logic:** فعلاً یک agent/worker با قرارداد ورودی/خروجی مشخص؛ Google ADK 2.0 یا چارچوب آماده فقط در صورت نیاز عملی و سازگاری runtime. بدون تیم دائمی ۷ ایجنت از ابتدا.
- **Model Providers:** Gemini API و سایر کلیدهای رسمی قبلاً موجود نزد مالک؛ *هیچ کلیدی در GitHub/چت کپی نشود*. مدل و سهمیه را مستقل از runtime مدیریت کن. Cloud runtime نباید به OmniRoute لوکال در زمان خاموشی PC وابسته باشد.
- **Tool Adapters:** ابتدا یک ابزار عمومی بی‌خطر HTTP GET برای منبع عمومی و یک ابزار deterministic. MCP/Google APIs/GitHub/Email/Browser بعداً با مجوز کمینه و نقش مشخص.
- **Durable State / Jobs:** یک store منتخب برای job ID, status, timestamps, retries, result pointer, provenance, model usage, budget و errors. Reuse پیش از ساخت DB/queue تازه.
- **Scheduler / Trigger:** زمان‌بندی کوتاه و قابل توقف؛ نه daemon غیرضروری یا چند scheduler همزمان.
- **Observability / Control:** health, sanitized logs, per-model usage, hard stop, approval log و دسترسی کاربر به نتیجه.
- **Windows Bridge (future):** اتصال خروجی امن به ایجنت‌های MausBot/Windows وقتی لپ‌تاپ روشن شد؛ بدون بازکردن inbound port و بدون authority موازی.
- **Applications (future):** Gmail/job follow-up، پایش فرصت‌ها، پژوهش اینترنتی، تحلیل مالی و دیگر مأموریت‌های منتخب؛ هرکدام boundary/permissions/contract خودش را دارد، نه یک agent با دسترسی نامحدود.

## 2. گزینه‌های میزبانی و انتخاب Free-First: هنوز هیچ گزینه‌ای برنده قطعی نیست

| نامزد | شکل اجرای واقعی | سهمیه/هزینه شناخته‌شده از اسناد رسمی | نسبت با نیاز کنونی | گیت یا مانع |
|---|---|---|---|---|
| **Neon Functions + Postgres (موجود در DJMRN)** | Node.js Functions, Cron/HTTP و DB کنار runtime | Free: 1M invocation/month, 10 active + 400 waiting capacity-hours/month, 1GB DB/project, 100 CU-hours/month | **اولین مسیر برای بررسی دوباره و reuse**؛ job کوتاه، ذخیره پایدار، مدل Gemini با fetch | شاخه‌های پروژه موجود در مشاهده قبلی Archived و triggers خاموش بودند؛ بررسی plan/branch/liveness؛ ADK Python مستقیم در Node Functions اجرا نمی‌شود |
| **Activepieces Hosted Free** | Flow/Agent managed UI در Cloud | فعلاً Free forever، 100 credits/day؛ BYOK AI keys در Plus تبلیغ می‌شود | رقیب GUI برای ساخت سریع Agent و workflow محدود؛ می‌تواند اولین میزبان شود اگر امکانات/هزینه کافی باشند | آیا کلیدهای موجود روی Free از مسیر API/HTTP پشتیبانی امن و مجاز دارند؟ quota per AI action و data privacy باید بررسی شوند |
| **Google Cloud Run + Google ADK 2.0** | سرویس Python/TS/Go قابل استقرار، scale-to-zero | free usage resource allowances ولی نیازمند Google Cloud billing setup و سایر هزینه‌های محتمل؛ **هزینه صفر تضمین‌نشده** | بهترین candidate برای agent runtime کامل و code-first ADK در صورت نیاز واقعی | **UNKNOWN/DENY** تا billing/overage/IAM/region/secret/deploy costs و امکان hard spending stop تأیید نشود |
| **Google Apps Script** | JavaScript cloud script + time-driven triggers | Consumer: 90 min aggregate trigger runtime/day و 6 min per execution | گزینه سبک برای worker محدود، API polling و Dispatcher؛ **کل بستر full ADK نیست** | مجوزهای اکوسیستم Google و محدودیت وقت اجرا/Storage؛ برای چندایجنت پیچیده کافی نیست |
| **Supabase Edge Functions** | Deno Edge worker + Postgres/backend | Free: 500k invocations/month، 500MB database؛ function free duration و sleep limits | گزینه آماده backend + triggers/REST، قابل مقایسه با Neon | اضافه‌کردن authority دوم، inactivity pause؛ Node/Python ADK قابل‌حمل مستقیم نیست |
| **Cloudflare Workers Free** | HTTP/Cron short-lived JS Worker | 100k requests/day؛ 10ms CPU/request/cron؛ 5 Cron triggers/account | مناسب dispatch سبک، proxy مجاز API، webhook و اعلان | CPU بسیار محدود برای agent واقعی و پردازش حجیم؛ no default |
| **GitHub Actions Free** | ephemeral scheduled CI job | GitHub Free private-hosted minutes 2000/month baseline; cron may delay/drop | CI و smoke / fallback scheduler | برای state/runtime اصلی و job با زمان دقیق مناسب نیست |
| **n8n Cloud** | managed workflow UI | **فقط trial 14-day**؛ Free پایدار hosted ندارد | برای پایه free-forever رد می‌شود | n8n Community خودمیزبان می‌تواند بعداً مکمل شود، اما میزبان رایگان مجزا لازم دارد |

**مقایسه بر اساس:** تمدید دائمی Free، واقعی‌بودن اجرای خارج از لپ‌تاپ، امکان استفاده قانونی از APIهای موجود، محدودیت call/token/CPU/wall time، انتخاب مدل، Agent/Tool/MCP، UI/API، storage/state، مجوز کاربری تجاری/منطقه‌ای، private networking، billing/card/auto-charge، تعمیر و migration، observability و قابلیت توقف کامل.

**No vendor lock-in at project-level:** قرارداد ساده input -> execution -> result/status کافی است؛ یک سامانه routing عمومی، چند پایگاه‌داده، event bus یا multi-agent orchestration تا وقتی آزمون نیاز را اثبات نکرده مجاز نیست.

## فاز C0 — ممیزی زیرساخت‌های ابری موجود و محدودیت‌های واقعی (فقط‌خواندنی)

1. از Notion/GitHub canonical فهرست پروژه‌های مرتبط، معماری‌های قبلی و provider decisions را بررسی کن؛ از ابتدا استک جدید حدس نزن.
2. وضعیت اکانت‌های متصل/قبلی Neon, Supabase, Google Cloud/AI Studio/Apps Script, Activepieces, Cloudflare, GitHub Actions و سایر نامزدهای قبلی را **تنها با دسترسی موجود و در صورت ارزش واقعی فقط خواندنی** بررسی کن؛ ثبت‌نام یا فعال‌سازی API جدید نکن.
3. تفاوت پلن رایگان تجدیدپذیر با trial/credit ثبت‌نامی، نیاز به کارت، auto-overage، محدودیت منطقه‌ای/حریم خصوصی و commercial terms را از official docs و داشبورد حساب تأیید کن.
4. وضعیت Neon قبلی (free_v3، شاخه‌های Archived و schedules disabled در مشاهده 2026-11-12) مجدداً فقط خواندنی ارزیابی شود. هیچ restore/wake/schedule enable به‌عنوان اثر جانبی انجام نشود.
5. به جای انتخاب از پیش، خروجی یک ماتریس معتبر با FACT / ASSUMPTION / UNKNOWN و فقط ۲ گزینه منتخب برای آزمایش باشد.

**PASS:** حداقل یک نامزد در سطح Free تجدیدپذیر، مجاز، با cloud runtime واقعی و بدون هزینه ناخواسته؛ همچنین توان حذف/rollback و مدیریت secret مشخص باشد. **STOP:** cost UNKNOWN، billing الزام‌آور بدون hard-stop مورد تأیید، شرایط منطقه‌ای مبهم یا تعارض با canonical DB.
**نتیجه مرحله:** پیشنهاد تأییدمحور برای انتخاب *یک* میزبان اولیه.

## فاز C1 — انتخاب یک Cloud Host و تعریف کوچک‌ترین هسته ایجنتی

1. بین **مسیر A: serverless code-first (اول Neon موجود)**، **B: GUI hosted (Activepieces Free)** و **C: ADK full runtime on verified-free host** روی سناریوی مشترک سبک مقایسه عملی/قیمت/مجوز کن. ADK یک framework است نه حساب ابری مستقل.
2. یک deployment boundary و یک job owner انتخاب کن. Provider role: Runtime, Model, State, Tool, Observer و Alternative مشخص باشد.
3. قرارداد پایه CloudJob v0 محدود به: job_id, purpose, public_input_ref, requested_tool, model_alias, budget_limit, created_at, status, result_ref, source_provenance, error و attempts. از ساخت domain registry و policy engine حجیم پرهیز کن.
4. test/health endpoint و مسیر نتیجه/خطا و stop button/disable schedule از همان اول در تعریف باشد.
5. مشخص کن که source code اصلی در همین GitHub و runtime/secret/state در میزبان منتخب می‌مانند.

**PASS:** یک plan اجرایی قابل برگشت، جداسازی مسئولیت، هزینه صفر قابل دفاع، تایید کاربر برای انتخاب/ایجاد محیط. **STOP:** اضافه‌کردن host دوم بدون نیاز یا وابستگی به سیستم روشن محلی.

## فاز C2 — ایجاد Cloud Workspace/Runtime پایه (با تأیید مستقل)

1. در میزبان تأییدشده کوچک‌ترین project/service/function یا workspace لازم ایجاد شود؛ مجوزهای IAM/API/secret را حداقلی تعریف کن؛ دسترسی public و token در URL ممنوع.
2. اگر سرویس قبلی مناسب است، **Reuse existing**؛ پروژه دوم فقط در صورت نیاز واقعی به جداسازی محیط، اعتبار یا مرز امنیتی.
3. ابتدا یک hello/health endpoint یا اجرای job deterministic با داده ساختگی؛ هیچ مدل/کلید/اکانت شخصی لازم نیست.
4. log sanitized، quota meter و stop/rollback واقعی را تست کن؛ هنگام fail و restart سناریوی bounded را تکرار کن.
5. داشبورد/URL داخلی مشاهده نتیجه از مرورگر موبایل (بدون دسترسی عمومی ناامن) مشخص شود.

**PASS:** اجرای Cloud مستقل از لپ‌تاپ + دسترسی مجاز به وضعیت + صفر هزینه + توقف. **NOT DONE:** صرفاً ساخته‌شدن project یا نصب package.

## فاز C3 — اولین ایجنت ابری و اتصال محدود به یک مدل موجود

1. ابتدا **یک agent/worker**، نه چند agent؛ وظیفه سنجش‌پذیر غیرحساس تعریف کن: گرفتن یک منبع عمومی رسمی با HTTP GET، استخراج بخش کوچک، در صورت نیاز خلاصه با مدل و ارائه نتیجه/منبع.
2. یکی از APIهای مدل *از قبل موجود نزد کاربر* مثل Gemini یا free model verified از روتر مستقل cloud را از طریق secret storage رسمی host متصل کن؛ **کلید را در chat/GitHub/log چاپ یا کپی نکن**.
3. با یک free model متناسب، tool calling واقعی و خروجی structured JSON را بررسی کن. ابتدا deterministic test بدون مدل و بعد یک call واقعی/مجاز با سقف مصرف سخت.
4. محدودیت region/account و privacy را بررسی کن: نباید از هویت جعلی، VPN bypass غیرمجاز یا تغییرات proxy برای نقض ToS استفاده شود؛ cloud IP حل تضمینی مشکل API نیست.
5. نسخه مدل، تعداد call، tokens/requests، latency و هزینه (صفر مورد تأیید) ثبت شود؛ اگر Free provider محدود/قطع شد، fail-safe بدون paid fallback.

**PASS:** یک کار واقعی و قابل تکرار public I/O + ابزار واقعی + مدل مجاز + نتیجه قابل مشاهده؛ لپ‌تاپ می‌تواند خاموش باشد. **STOP:** مدل/منطقه یا هزینه unverifiable.

## فاز C4 — حافظه و وضعیت پایدار به‌اندازه نیاز واقعی

1. از یک DB منتخب/موجود استفاده کن؛ پیش از ایجاد جدول schema و اختیارات writes را با canonical وضعیت قبلی تطبیق بده (schema migration فقط پس از approval).
2. حداقل fields برای job: ID, input hash/ref, model, tool, status, timestamps, result, retryCount, last_error, expected_next_run, budget_used. نگهداری raw evidence فقط در منبع مجاز و با retention روشن.
3. دو بار اجرای همان job نباید دو نتیجه/اقدام خارجی ثبت کند؛ restart باید resume یا terminal failure واضح داشته باشد.
4. Job history و یک view انسانی برای خواندن نتایج، نه لزوماً UI اختصاصی یا Vector DB، بساز.
5. مالک state مشخص شود؛ local Windows صرفاً نسخه sync/observer است، authority دوم برای همان job نشود.

**PASS:** پس از shutdown/idle دوباره نتایج قابل بازیابی؛ duplicate/delay/error درست مدیریت شود.

## فاز C5 — سیستم ابزارها و دسترسی‌ها، ساده و قابل توسعه

1. فقط ابزارهایی را اضافه کن که نخستین مأموریت به آنها نیاز دارد: HTTP public read، parsers، یک bounded public search اگر نیاز واقعی بود، one permitted model call؛ ابزار داخلی deterministic ارجح.
2. برای هر ابزار input/output schema, required scopes, source provenance, timeout, rate limit, sensitive actions و fallback روشن باشد.
3. MCP و Google Apps Toolsets به‌عنوان **tool interface گزینه آینده** ثبت می‌شوند؛ MCP خودِ permission یا OAuth نیست.
4. ابزارهای دارای Gmail/send/browser/GitHub-write/financial/provider activation باید مستقل مورد تأیید قرار گیرند؛ به agent عمومی full toolset نده.
5. prompt injection از متن سایت یا پیام نمی‌تواند دستور تغییردسترسی/ارسال/ذخیره secret محسوب شود. deny by default.

**PASS:** یک ابزار واقعی بدون privilege creep، تست failure/timeout، reproducible results.

## فاز C6 — زمان‌بندی، سهمیه رایگان، بازیابی و گزارش‌گیری

1. یک Trigger مشخص، مثلاً اجرای محدود روزانه روی داده عمومی/ساختگی؛ schedule ownership واحد، بدون Cron تکراری در ۳ ابزار.
2. سقف RPM/TPM/RPD برای مدل و محدودیت request/CPU/time برای میزبان را در اندازه‌گیری واقعی کنترل کن.
3. 429 → backoff؛ 5xx/timeout → retry محدود؛ duplicate job → idempotent skip؛ rate-limit/unknown billing → STOP؛ provider downtime → گزارش status.
4. قبل از آزمایش disconnect/local VPN، مطمئن شو هیچ dependency به localhost/Windows وجود ندارد.
5. اعلان نتیجه یا گزارش خلاصه از کانال کم‌مجوز و مورد تأیید کاربر، با لینک وضعیت نه متن حساس.
6. نتیجه را در دسترس مرورگر موبایل/کاربر نگه دار؛ برای استفاده نیازی به PowerShell روی ویندوز نباشد.

**PASS:** اجرای واقعی Cloud در یک بازه زمان‌بندی‌شده حتی با لپ‌تاپ خاموش؛ نتیجه پایدار و گزارش خطا و مصرف صفر.

## فاز C7 — سنجش نیاز به Google ADK 2.0 و چندایجنتی واقعی

1. **ADK 2.0 کاندید مهم و ثبت‌شده** برای multi-agent, graph workflow, subagents, tool delegation, testing. اما هیچ ضرورت ندارد نخستین Worker ساده را با آن بسازی.
2. اگر C3–C6 نشان داد یک job به تفکیک coordinator/reviewer/worker نیاز دارد، مقایسه ۱ agent با ۲ agent (Coordinator + Reviewer) روی داده عمومی یکسان انجام شود. معیار: کیفیت مستقل، زمان، خطای factual، trace، quota.
3. اگر Runtime انتخابی Node Functions باشد، ADK Python را نمی‌توان بدون سازگاری و میزبان دیگری مستقیم در Neon Node Function اجرا کرد؛ **host migration** فقط با نیاز و approval. می‌توان TypeScript ADK را با host سازگار بررسی کرد، نه فرض سازگاری.
4. Google ADK Cloud Run گزینه رسمی اما service account/IAM/secret/billing/auto-scaling/region و قیمت جداگانه دارد. هیچ public unauthenticated ADK UI/API در پروژه خصوصی.
5. MCP/agent-to-agent protocol/skills فقط برای قابلیت واقعی و با ownership و security جداگانه.
6. از ساخت تیم بزرگ یا سرویس کنترل مرکزی قبل از سنجش ساده‌ترین راه پرهیز شود.

**PASS:** multi-agent بهبود قابل اندازه‌گیری و بدون cost/security regression؛ در غیراینصورت single-agent باقی می‌ماند.

## فاز C8 — ارتباط با تیم ایجنت‌های ویندوز DJMRN (اختیاری)

1. ابتدا Cloud بدون لپ‌تاپ کاملاً قابل استفاده باشد؛ سپس Windows MausBot هنگام اتصال outbound pull به job/result store بزند، نه پورت باز inbound.
2. Job ownership و acknowledge دقیق، جلوگیری از دو بار اجرای task، فاصله قطع/وصل و تغییر VPN تست شود.
3. Cloud به gateway/OmniRoute محلی به‌عنوان primary provider تکیه نکند؛ فقط زمانی که laptop روشن است تکمیل‌کننده باشد.
4. حداقل یک نتیجه cloud در ویندوز توسط یک عامل تخصصی خوانده و receipt ثبت شود.

**PASS:** laptop offline → cloud job completed → laptop online → safe sync once.

## فاز C9 — اضافه‌کردن نخستین اپلیکیشن واقعی پس از آماده شدن هسته

**این مرحله عمداً بعد از ایجاد و اثبات فضای Cloud قرار گرفته است.** انتخاب application با درخواست آینده مالک است. مثال‌ها:
- Gmail/job follow-up با OAuth scopes و privacy review مستقل؛ Gmail App Script می‌تواند یک **Domain Executor** باشد نه Host واحد برای تمام مأموریت‌ها.
- فرصت‌های عمومی فریلنسری با API/RSS/Job Hunter موجود.
- پژوهش فناوری‌ها/ابزارهای رایگان، هشدارهای دوره‌ای یا تحلیل اطلاعات عمومی.
- تحلیل بازارهای مالی عمومی/قیمت بدون معاملات خودکار.
- تولید محتوا، پرسش‌وپاسخ یا برنامه‌های دیگر با contracts جدا.

**پورتفولیو، رزومه فارسی/انگلیسی، Gmail Draft، پاسخ خودکار کارفرما و پیگیری شغلی الان مرحله زیرساخت نیستند.** اینها در صورت انتخاب مأموریت بعدی تعریف و مجوزدهی می‌شوند و نسخه قبلی roadmap که آنها را R1 قرار داده بود SUPERSEDED است.

**PASS:** یک domain adapter واقعی با مجوز خودش و بدون تخریب cloud base موجود.

## فاز C10 — معیار نهایی عملیاتی شدن فونداسیون

فونداسیون ابری فقط وقتی **OPERATIONAL** است که موارد زیر با شواهد واقعی و اجازه مستقل PASS باشند:
- Host واقعی انتخاب، مستقر و قابل دسترس بدون لپ‌تاپ.
- Agent کوچک یک درخواست/وظیفه عمومی واقعی با حداقل یک ابزار انجام داده.
- Model call مجاز با مصرف رایگان ثبت‌شده؛ خروجی منبع‌دار.
- durable job state پس از stop/resume، dedup و retries.
- schedule مستقل، metrics, alerts, health, stop switch, no unexpected charge.
- permission/security audit و مسیر انتقال/خروج از host.
- نتیجه قابل مشاهده به کاربر، راه توسعه به domainهای آینده.
- مزیت استفاده واقعی اندازه‌گیری‌شده، نه فقط تست مصنوعی.

**اگر عملیات شدن به انبوه agent framework, service, queue, database, control plane و registry وابسته شد، STOP و راه ساده‌تر را بررسی کن.**

## ترتیب approval و اجرای نوبت بعد

| Gate | قبل از اقدام چه باید روشن شود | مجوز/اقدام |
|---|---|---|
| C0 | وضعیت حساب‌ها/سهمیه/Terms/آلترناتیوها | فقط‌خواندنی؛ هیچ provision |
| C1 | یک Host از روی مقایسه، رایگان و قابل توقف | انتخاب طرح؛ تأیید مستقل برای ایجاد پروژه |
| C2 | runtime/IAM/secrets/environment | ایجاد/فعال‌سازی سرویس فقط با proposal و approval |
| C3 | Gemini یا سایر کلیدهای موجود و privacy | اتصال مجاز یک provider، بدون دسترسی به کلید در گفتگو |
| C4–C6 | DB، schedule، API cost، endpoints و permissions | write/schema/deploy/scheduler هرکدام gate جدا |
| C7 | مزیت واقعی Google ADK یا چند Agent | approval آزمایش جدید و هر provider/host اضافی |
| C8 | Windows Bridge و identity | authorization جدا؛ no inbound Windows port |
| C9 | یک کاربرد مشخص Gmail یا موارد دیگر | قرارداد و مجوز مخصوص Domain |

**First next action (NOT EXECUTED):** C0 read-only inventory and host comparison in the existing connected accounts. Then present **one minimal architecture + one genuine free hosted alternative** for owner approval. No registration, payment, cloud deployment, API activation, secret transfer, production job, Gmail permission, portfolio work, or message send during this roadmap revision.

## شواهد رسمی / تاریخ بازبینی 2026-11-12

- Neon Functions & Free quotas: https://neon.com/blog/neon-free-plan-1-gb-per-project
- Neon Backend/AI Gateway separate price: https://neon.com/blog/neon-backend-is-ga
- Activepieces Hosted Free / BYOK key distinction: https://www.activepieces.com/pricing
- Cloudflare Worker limits: https://developers.cloudflare.com/workers/platform/limits/
- Supabase Edge Functions quota/limits: https://supabase.com/docs/guides/platform/billing-on-supabase ; https://supabase.com/docs/guides/functions/limits
- Google Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas
- Google ADK 2.0: https://adk.dev/2.0/
- ADK cloud deployment options: https://adk.dev/deploy/
- ADK Cloud Run deploy and security: https://adk.dev/deploy/cloud-run/
- Google Cloud Run pricing: https://cloud.google.com/run/pricing
- n8n Cloud trial vs Community: https://support.n8n.io/article/how-do-i-cancel-my-trial ; https://n8n.io/pricing/
- Canonical DJMRN governance: https://app.notion.com/p/3edc8c684690814a9707cb880534f462 ; https://app.notion.com/p/3edc8c68469081cc90abdd5183f1bdb1

**Documentation change only, not architecture adoption.** Previous Gmail-first roadmap is retained by Git history and remains useful only as a future domain plan; this C0–C10 foundation-first roadmap is CURRENT in this project path.
