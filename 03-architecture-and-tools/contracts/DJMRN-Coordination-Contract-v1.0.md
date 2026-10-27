# DJMRN — قرارداد مرجع هسته هماهنگی سبک و شبکه دستیارهای تخصصی

**شناسه:** DJMRN-COORDINATION-CONTRACT-001  
**نسخه:** 1.0.0-design-baseline · **تاریخ مرجع:** 2026-10-27  
**وضعیت:** مشخصات طراحی تکمیل‌شده برای بررسی و آزمون؛ **نه تصویب نصب، نه سامانه پیاده‌شده، نه گواهی انطباق A2A/MCP/AG-UI**.  
**سند مادر:** `DJMRN-Open-Standards-Composition-Profile-v0.1.md` و Manifest v0.1؛ این سند نقش هسته و قواعد اتصال آن استانداردها را تکمیل می‌کند، آنها را تغییر نمی‌دهد.  
**محدوده اولیه:** Windows 11 / 8GB RAM؛ رابط فارسی؛ CAP-006 فقط‌خواندنی؛ اتصال‌های Gmail صرفاً طراحی آینده؛ سرویس‌های تخصصی قابل فعال‌سازی بر حسب نیاز.

## ۱. تصمیم معماری پیشنهادی (قابل تبدیل به تصمیم رسمی، نه مصوب)

**Lightweight Hub-and-Spoke / Modular Coordination Core**. مرکز، دستیار چت و مدل زبانی بزرگ و همیشه‌فعال نیست. فقط مرجع ثبت درخواست/وظیفه، ثبت پیام، کنترل دسترسی، انتخاب قابلیت بر اساس سیاست/رجیستری، پیگیری، شواهد نتیجه و ارجاع به دانش است. هر متخصص (جست‌وجو، ایمیل، پردازش اسناد، تحقیق، برنامه‌نویسی) Worker یا Agent خودش و دفتر اجرای داخلی خود را دارد. مرکز از جزئیات ریز اجرای تخصصی آگاه نیست، اما آغاز، مقصد، نتیجه، خطا و شواهد ارجاعی همه تبادلات رسمی را ثبت می‌کند.

**هوش اختیاری:** ابتدا تصمیم قواعد صریح و رجیستری قابلیت‌ها. فقط ابهام تشخیص مقصد، کیفیت پاسخ، تعارض شواهد یا برنامه‌ریزی غیربدیهی می‌تواند درخواست بازبینی یک Supervisor Agent محدود و قابل حسابرسی ایجاد کند. Supervisor نمی‌تواند مجوز صادر کند یا وضعیت تکمیل را بدون رسید تغییر دهد.

**اصل معماری:** «مرکز کنترل و هماهنگی»، «مرکز دانش»، «دستیار تخصصی»، «موتور مدل» و «موتور Workflow» پنج نقش منطقی متفاوت‌اند؛ لزوماً پنج سرویس، پایگاه داده یا فرایند متفاوت نیستند. مراکز عملیات و دانش، مالکیت متفاوت دارند؛ ثبت metadata در مرکز به معنی انبارکردن محتوای کامل ایمیل یا اسناد همه نقش‌ها نیست.

## ۲. تصویر منطقی و مسیرهای استاندارد

```text
فارسی/دسکتاپ/وب ── [AG-UI برای stream اختیاری، OpenAPI برای درخواست‌ها] ──> DJMRN HUB
                                                                             │
                دفتر عملیات پایدار: Task + Dispatch + Inbox/Outbox + Audit     │
                Policy/PARC + Capability Registry + Routing Rules              │
                ResourceRef / EvidenceRef + approval                            │
                                                                             │
                  ┌───────────────────┬─────────────────────┬─────────────────┤
                  ▼                   ▼                     ▼                 ▼
            Knowledge Service    Search Specialist     Mail Specialist   Python CAP-006
            scoped read/write    تنها مجری مجاز وب      Gmail MCP/API     فایل‌های مجاز
                  │                   │                     │                 │
                  └──────────── نتیجه/شواهد/وضعیت از مسیر HUB ──────────────────┘

دستیار مستقلِ خارج از فرایند  ↔ A2A Adapter ↔ HUB ↔ A2A Adapter ↔ دستیار دیگر
Agent/UI events ↔ AG-UI Adapter؛ Tool exposure ↔ MCP Adapter؛ External API ↔ OAuth/REST adapter.
```

هیچ Agent، MCP server یا Worker اجازه ندارد با پرش از Policy در HUB (و بررسی مجدد در مجری) به حساب/منبعی دسترسی بگیرد. ارتباط بین سرویس‌های مستقل می‌تواند مستقیم از نظر TCP باشد اما از نظر **کنترل، authorization، ارجاع وظیفه و ثبت audit** از مرکز عبور می‌کند؛ الزام proxy کردن تمام بایت‌های فایل یا API از هسته وجود ندارد.

## ۳. قراردادهای مورد استفاده و محدوده دقیق آنها

| مرز | قرارداد/سورس موجود | مسئولیت | محدودیت |
|---|---|---|---|
| UI ↔ برنامه | HTTP/OpenAPI 3.1، optional AG-UI events | درخواست، نمایش فارسی، progress | رویداد UI رسید دائمی نیست |
| Hub ↔ ابزار | MCP Tool/Resource و JSON Schema؛ داخل همان پروسه فراخوانی typed function معادل مجاز است | توصیف ابزار و اجرای محدود | MCP مجوز خودکار نمی‌دهد |
| Agent ↔ Agent مستقل | A2A + Agent Card/Message/Task/Artifact | پروتکل تبادل بین سرویس‌ها | A2A صاحب Task DB داخلی HUB نیست |
| اجرای چندمرحله‌ای | Open Workflow Definition / یا موتور منتخب | تعریف مراحل specialist، retry، pause | DSL تضمین دوام اجرا نمی‌دهد |
| داده داخلی | JSON Schema 2020-12، OpenAPI | قرارداد داده و API؛ آزمون تغییر نسخه | **DJMRN Local Control Records** الگوی تطبیق است، استاندارد جهانی نیست |
| مجوز | مدل Cedar principal/action/resource/context + policy decision point | کنترل درخواست و ابزار در هر dispatch | تأیید مدل یا OAuth scope جایگزین مجوز داخلی نیست |
| منشأ نتیجه | مفاهیم W3C PROV-O و SHA256 واقعی | منشأ، revision، actor، زمان و خط | خروجی مدل مدرک مستقل نیست |
| رخداد بین سرویس‌ها | CloudEvents 1.0 (اختیاری) | خبرهای غیرهم‌زمان بین Workerها | قابلیت dedupe/durable delivery را پیاده‌سازی باید بدهد |
| ردگیری | OpenTelemetry/W3C Trace Context (اختیاری) | correlation و زمان‌بندی | لاگ‌ها نباید Secret و متن محرمانه ایمیل را نشت دهند |

نسخه‌ها/SDKهای دقیق در زمان اتصال نصب/پین می‌شوند و باید همان نسخه در TCK/آزمون ثبت شود. این پروفایل، **A2A را بازنویسی نمی‌کند**؛ فقط میان `hub_task_id` و `a2a_task_id`/`workflow_run_id` نگاشت ذخیره می‌کند. A2A Server در P0/P1 لازم نیست.

## ۴. تعاریف ماشینی ارائه‌شده در بسته

`schemas/hub-record.schema.json` مرجع نسخه‌دار طراحی ماست و هفت شیء دامنه را با فیلد `kind` تعریف و validate می‌کند: `TASK_SUBMISSION`, `TASK_RECORD`, `DISPATCH_RECORD`, `CAPABILITY_RECORD`, `RESOURCE_REF`, `WORKER_RESULT`, `APPROVAL_RECORD`, `AUDIT_EVENT`. هر فیلد یا Enum به انگلیسی ثابت، متن نمایش فارسی با `locale=fa-IR` و UTF-8. برای ورودی‌های بیرونی، هویت معتبر را **سرور** تولید/بازیابی می‌کند، نه متن آزاد پیام.

- **Task:** شناسه UUID/ULID صادرشده HUB و ماندگار، creator/correlation، intent و capability، زمان و status. `CAP-006.task_id` صرفاً fingerprint تکرارپذیر و در receipt نگاشت می‌شود، نه Task عملیاتی.
- **Capability:** نام/نسخه، owner specialist، شکل ورودی و نتیجه و طبقه اثر جانبی، مدل نیازمندی مجوز، اینکه آیا دانشنامه اول چک شود، retry class و budget.
- **Dispatch:** `from`/`to`, correlation و parent task، ID یکتای dispatch، refهای منبع مجاز، مجوز مشتق‌شده و expiration، attempt شمارش‌شده، وضعیت ACK. مقصد تنها پس از validate شدن انتخاب می‌شود.
- **ResourceRef:** نوع سند/ایمیل/نتیجه جست‌وجو، canonical resource ID، version/sha256، owner، حساسیت، خطوط/بخش‌ها، زمان و ابزار مولد؛ هیچ URI اجازه دسترسی خودکار نیست.
- **Worker Result:** success/partial/error، artifact refs و evidence refs، category خطا، retryable flag و operation receipt؛ وضعیت Task در HUB فقط پس از validate و durable commit تغییر می‌کند.
- **Approval:** هدف دقیق (action/target/payload_digest)، شخص تصمیم‌گیر، زمان صدور و انقضا، status و receipt؛ محتوای تغییرکرده به approval جدید نیاز دارد.
- **Audit:** شناسه رخداد، task/dispatch، actor، نوع اتفاق، timestamp، outcome، ref به evidence؛ لاگ append-only منطقی و قابل بررسی.

## ۵. مدیر وظایف و وضعیت رسمی

Owner **فقط HUB Task Ledger** است؛ Workflow engine می‌تواند run ledger جداگانه داشته باشد ولی حق اعلام نهایی Task از جانب خودش ندارد. برای روز اول SQLite transaction + queue table (یا همان DB با Inbox/Outbox) کافی است؛ هنوز عملکرد واقعی اثبات نشده. وضعیت‌های پیشنهادی داخلی:

`RECEIVED` → `VALIDATED` → `QUEUED` → `DISPATCHED` → `RUNNING` → `SUCCEEDED`; شاخه‌های `WAITING_APPROVAL`, `RETRY_WAIT`, `DENIED`, `FAILED`, `CANCELLED`, `UNKNOWN_OUTCOME`.

- فقط حرکت مجاز state machine؛ با CAS/version row برای جلوگیری از races؛ پذیرش دوباره یک message ID باید dedupe شود.
- `SUCCEEDED` تنها وقتی Worker Result معتبر و evidence/artifact references در تراکنش HUB پایدار شده باشد؛ event push/UI text به معنای success نیست.
- اگر Worker قبل از ACK قطع شد، وضعیت تا زمان reconcile روشن باشد؛ اگر عمل خارجی مثل ارسال ایمیل ممکن است انجام شده باشد، **UNKNOWN_OUTCOME** و توقف تلاش مجدد تا تطبیق.
- retry روی خطای موقت read-only (timeout/5xx/429 با احترام به Retry-After و سقف) قابل تعریف است؛ 401/403، نقض policy، 404 قطعی، و تغییر scope بدون تأیید retry خودکار ندارند.
- Hub task و specialist run رابطه one-to-many با attempt دارند، نه necessarily 1:1.

## ۶. مسیریابی و نقش دانشنامه

`Capability Registry` اعلام می‌کند `research.web` فقط owner=`search_specialist`، `knowledge.lookup` فقط owner=`knowledge_service`، `gmail.read` فقط owner=`mail_specialist` و `documents.search.v0` در اختیار CAP-006 یا adapter مجاز است. دستیارهای دیگر **مجاز به وب‌گردی مستقیم نیستند**؛ فقط درخواست `research.web` به HUB می‌دهند. credentialهای search/Gmail نزد specialist یا vault scopeدار می‌مانند.

Router ابتدا rule-based با ترجیح **اول بازیابی دانش برای سؤال‌های دارای منبع ثابت** عمل می‌کند؛ برای «اخبار امروز/قیمت فعلی/محتوای صفحه جاری» freshness policy، TTL و منبع را بررسی می‌کند و ممکن است مستقیماً به search specialist ارجاع دهد. نتیجه دانشنامه تنها همراه با `source_ref` و `revision` و `as_of` پذیرفته می‌شود. انتشار دانش پایدار/مرجع جدید برای کل سیستم نیازمند فیلتر کیفیت/منشأ و policy است؛ هر متن تازه یا خروجی LLM خودکار به عنوان fact مشترک منتشر نمی‌شود.

اگر مقصد مشخص نیست: روتر اجازه ندارد دلخواه ابزار جدید اجرا کند؛ درخواست به `NEEDS_REVIEW` در سطح dispatch/خطا یا Supervisor **اختیاری** می‌رود، سپس Policy دوباره اجرا می‌شود. مدل فقط route را پیشنهاد می‌کند؛ آخرین رأی با policy/registry است.

## ۷. قرارداد کاری تخصصی هر دستیار

هر specialist به‌جای ساخت API متفاوت یک `CAPABILITY_RECORD` دارد: `capability_id`, `owner_role`, `input_schema_ref`, `output_schema_ref`, `side_effect`, `required_permissions`, `knowledge_policy`, `retry_policy`, `time_budget_sec`, `model_budget`, `privacy_scope`, `dependency_ids`, `healthcheck` و نسخه. می‌توان چند قابلیت را به یک Worker سپرد و چند Worker را نوبتی در یک process اجرا کرد. نصب Agent runtime برای specialist ساده اجباری نیست.

**مثال Search Specialist:** `research.web` تنها مسیر سرچ؛ stages: request accepted → query plan → checked knowledge → web fetch → verify source/error classification → normalize/source citations → save evidence → result to hub → optional knowledge staging. Specialist ledger نگهدارنده URLهای بازدیدشده، error per URL، `Retry-After`, caching، زمان و status است. HUB یک `task_id` و result summary/evidence refs نگه می‌دارد، نه تمام HTML تمام صفحات. زمان/سقف جست‌وجو و قواعد permission/crawling رعایت شوند.

## ۸. پیام تخصصی از یک دستیار به دیگری

مثال `mail_specialist` برای تحقیق درباره شرکت درخواست می‌فرستد: `TASK_SUBMISSION(capability='research.web', parent_task_id=mail_task)` → HUB validates identity & permission → creates `TASK_RECORD`, `DISPATCH_RECORD` to `search_specialist` → specialist ACK → سرچ و مستندسازی → `WORKER_RESULT` → hub durable commit → notify origin + reference to knowledge staging. **هیچ دستیار دیگری به search API credential نیاز ندارد.** پیام بین Agentهای مستقل بیرونی می‌تواند به A2A Task/Message نگاشت شود؛ دستیارهای داخل یک Process همان Task/Dispatch رکورد را استفاده می‌کنند، نه A2A Server اضافی.

**نمونه Google:** mail reads via approved Gmail MCP/API; Python worker preprocess; knowledge lookup; if current company details missing hub creates search task; search returns evidence; mail drafts response; draft creation و `send` side effects جداگانه ارزیابی می‌شوند؛ send فقط بعد از approval دقیق recipient+body+attachment hash، با receipt و unknown-outcome reconciliation. متن ایمیل untrusted data است و نباید instruction/policy تلقی شود.

## ۹. API مرکزی (برای پیاده‌سازی، نه مستقر)

`openapi/hub.openapi.json` مسیرهای طراحی را اعلام می‌کند: `POST /v1/tasks`, `GET /v1/tasks/{task_id}`, `POST /v1/dispatches`, `POST /v1/worker-results`, `GET /v1/capabilities`, `POST /v1/approvals/{approval_id}/decision` و `GET /v1/tasks/{task_id}/events`. همه endpointهای خصوصی با local-auth token/identity معتبر، عامل و مجوز جدا، لاگ و محدودیت اندازه درخواست حفاظت می‌شوند؛ `localhost` به‌تنهایی authentication نیست. `POST /v1/dispatches` فقط caller داخلی معتبر. Schemaهای JSON بسته پایه اعتبارسنجی هستند، نه اجرای API. در نسخه بعد این قراردادها را با FastAPI/Pydantic/OpenAPI codegen می‌توان به runtime تبدیل کرد.

**سطح اجرای اولیه:** در همان Process، آداپترهای تابعی به جای HTTP worker قابل قبول‌اند. گزینه HTTP داخلی برای جایگزینی process یا cloud در آینده است. `AG-UI` eventها نمای UI هستند. `A2A` تبادل مستقل و استاندارد را بعداً فراهم می‌کند. `MCP` برای عرضه ابزارها به میزبان Agent خارجی یا اجرای حدود tools فعال می‌شود. بنابراین انباشت سرورهای استاندارد در روز اول الزامی نیست.

## ۱۰. مدل‌ها، هزینه و RAM

OmniRoute فقط **Inference Adapter** است، نه DB یا حاکم سیاست. Supervisor همیشه‌فعال یا یک process مدل مستقل به ازای هر شخصیت ممنوع در baseline. Agentهای مختلف می‌توانند با role profileهای مستقل و **یک مدل cloud به‌صورت سریالی** کار کنند. هر inference قبل از call: provider/model allowlisted؛ free-first و no paid fallback؛ quota/cost admission؛ privacy scope و confirmation ارسال داده به مدل ابری. timeout و retry مدل محدود و ثبت‌شده. HTTP 200 مدل = اثبات انجام Task/Send نیست.

روی Windows 8GB، ابتدا 1 coordination process + 1 SQLite file + adapters on-demand و OmniRoute موجود (در صورت ضرورت) آزموده می‌شوند. افزودن Redis/Docker/Dapr/Orleans/Workflow Engine تنها بعد از نیاز واقعی و اندازه‌گیری RAM مجاز است.

## ۱۱. مهاجرت نسخه/تغییر قرارداد

Versionها SemVer برای قرارداد DJMRN، دقیقاً pinned برای پروتکل هر مرز. فیلدهای جدید optional با default و feature negotiation؛ حذف/تغییر معنای field، state یا permission نیازمند major. تست contract روی تمام adapterها قبل از upgrade. Migration از CAP-006: `legacy_cap006_fingerprint_task_id` در receipt نه authoritative `hub_task_id`. Idempotency key با fingerprint داده برابر نیست؛ جداگانه توسط caller/Hub تولید شود. قراردادهای A2A/MCP/AG-UI در payload اصلی خود تغییر داده نمی‌شوند؛ در مرزها adapter map دارند.

## ۱۲. آزمون پذیرش اجباری قبل از اعلام «اجرایی/نهایی مصوب»

1. JSON Schema همه مدل‌ها، مثال‌های معتبر و نامعتبر را درست validate کند؛ OpenAPI syntax بررسی شود.
2. CAP-006 روی دو فایل مجاز با digest و source line کار کند و تلاش برای فایل سوم DENIED شود؛ عدم اجرای LLM.
3. خواندن Task پس از restart، idempotency duplicate، تحویل retry شده بدون ایجاد task تکراری، ack و crash mid-run امتحان شود.
4. mail→hub→knowledge→search→hub→mail با داده مصنوعی، provenance/line/status و خطاهای موقت/قطعی اجرا شود؛ فقط search specialist حق وب دارد.
5. approval «draft/ارسال» با تغییر گیرنده یا متن invalid شود؛ ناشناختگی نتیجه send منجر به توقف retry و reconcile شود.
6. درخواست LLM یا A2A خارج از scope نتواند اجازه جدید یا credential به دست آورد؛ audit persisted باشد.
7. نسخه رسمی A2A با TCK و MCP Tool Schema و UI نمایش رویداد (در صورت اتصال) آزمون شوند، نه ادعای PASS بدون آزمایش.
8. benchmark RAM، restart، token quota و کیفیت فارسی روی Windows 8GB و یک اجرای واقعی end-to-end ثبت شود؛ export/restore قابل انجام باشد.

**DESIGN COMPLETE ≠ SOFTWARE COMPLETE**. تا زمانی که آزمون‌ها PASS نشده‌اند، قرارداد «Baseline طراحی آماده اجرای مرحله P1» است نه نرم‌افزار ساخته‌شده یا گواهی سازگاری. هر اقدام روی Gmail، انتقال محرمانه به مدل ابری، نصب و فرستادن ایمیل مجوز مجزا می‌خواهد.

## ۱۳. محل استفاده واقعی در کد و مخزن

**GitHub canonical:** `03-architecture-and-tools/contracts/DJMRN-Coordination-Contract-v1.0.md` همراه با `.../schemas`, `.../openapi`, `.../examples`, `.../tests` در مخزن اصلی. **نسخه فعلی research OSCP v0.1** در مسیر `03-architecture-and-tools/DJMRN-Open-Standards-Composition-*` باقی می‌ماند. این قرارداد تازه جایگزین مستندات تصمیم D-005/D-019 یا معماری ترکیبی قبلی نیست مگر کاربر تصویب کند.

**در اجرای واقعی:** رابط فارسی برای `POST /tasks`؛ HUB برای API / rule / DB؛ هر Worker برای Capability/Dispatch/Result؛ مرکز دانش برای ResourceRef/Evidence؛ هسته مدل برای inference adapter؛ A2A/MCP/AG-UI برای اتصال استاندارد بیرونی. هر قطعه در CI آزمون انطباق را پاس کند؛ رجیستری دستورها و شناسه‌ها از همین فایل/schema خوانده و version-locked شود.

## ۱۴. منابع استانداردهای باز

- A2A https://a2a-protocol.org/v1.0.1/specification/ و Python SDK https://github.com/a2aproject/a2a-python
- MCP https://modelcontextprotocol.io/specification/2025-11-25 و SDK https://github.com/modelcontextprotocol/python-sdk
- AG-UI https://github.com/ag-ui-protocol/ag-ui
- JSON Schema 2020-12 https://json-schema.org/draft/2020-12/schema و OpenAPI 3.1 https://spec.openapis.org/oas/v3.1.1.html
- W3C PROV-O https://www.w3.org/TR/prov-o/ ؛ Cedar https://www.cedarpolicy.com/ ؛ CloudEvents https://cloudevents.io/
- Open Workflow https://open-workflow-specification.org/ ؛ Gmail API https://developers.google.com/workspace/gmail/api/reference/rest
- پروژه اجرایی موجود: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/05-assistants-and-capabilities/src/document_search_v0/docsearch_v0.py

## ۱۵. مدیریت تصمیم

**کاربر درخواست بسته نهاییِ قابل استفاده کرد؛ تهیه مستندات و نمونه قرارداد از جانب دستیار انجام می‌شود.** این امر به معنی «تصویب نصب هسته»، «انتخاب نهایی Agent Runtime»، «اتصال Gmail» یا «انتخاب DB اجرایی پس از benchmark» نیست. سند v1.0 یک **پایه طراحی جامع قابل اجرا و قابل تست** است. در مرحله بعد، اولین vertical: *درخواست فارسی → ثبت Task → CAP-006 → نتیجه مستند و بازیابی* ساخته خواهد شد، نه یک مرکز هوشمند بزرگ و همیشه‌فعال.