# DJMRN — Open Standards Composition Profile (OSCP) v0.1

**تاریخ:** ۲۷ اکتبر ۲۰۲۶ · **وضعیت:** پیش‌نویس قابل بررسی / Design Candidate؛ نه تصویب استقرار یا نتیجه آزمون Windows.  
**هدف:** مونتاژ استانداردهای باز و SDKهای متن‌باز موجود، بدون اختراع قرارداد تازه برای Task/Message/Tool/Artifact/Workflow.  
**محدوده نخست:** دستیار فارسی + قابلیت فقط‌خواندنی اسناد CAP-006؛ مسیر Gmail صرفاً سناریوی طراحی و آزمون آینده است.  
**معماری مقصد:** هسته ماژولار DJMRN با مالک مشخص وظایف و مجوزها، چند Persona، Workerهای Python و سرویس‌های Google.  
**رابطه با پروژه:** منطبق با تصمیم مشروط D-019 و پژوهش‌های 001/002/003؛ جایگزین‌کردن خودکار هیچ تصمیمی مجاز نیست.  
**مسیر GitHub پیشنهادی برای ثبت پس از درخواست صریح کاربر:** `03-architecture-and-tools/` در مخزن اصلی. هیچ فایل GitHub در این نوبت نوشته نشده است.

## اصل محوری: این یک Composition Profile است، نه پروتکل جدید

قراردادهای استاندارد زیر را **بدون تغییر نحو اصلی و نام‌گذاری استاندارد** مصرف می‌کنیم. «پروفایل» فقط تعیین می‌کند هر استاندارد در کدام مرز استفاده شود، کدام نسخه قابل قبول است، مالک داده کیست، چگونه داده‌های یک مرز به مرز بعد نگاشت شوند و چه چیزی باید آزموده شود.

هیچ پروفایل ترکیبی نمی‌تواند بدون **مقدار محدودی پیاده‌سازی اتصال/نگاشت**، مجوزهای واقعی، نگهداری وضعیت و بازیابی تضمین‌شده، به یک محصول اجرایی تبدیل شود. هدف حذف اختراع پروتکل است، نه حذف تمام کدنویسی محصول.

## ۱. استانداردهای انتخاب‌شده و حدود استفاده

| لایه و مرز | قرارداد آماده / نسخه مرجع | پیاده‌سازی موجود | کاربرد در DJMRN | شروع |
|---|---|---|---|---|
| کاربر ↔ دستیار | AG-UI؛ نسخه SDK باید هنگام نصب pin شود | `ag-ui-protocol/ag-ui` و سازگارساز CopilotKit/Agent Runtime | رویداد پیام فارسی، پیشرفت، نمایش درخواست Approval و نتیجه | هنگام اتصال رابط؛ بدون نیاز به سرور AG-UI جدا در P0 |
| Agent مستقل ↔ Agent مستقل | A2A Protocol **v1.0.1** (پین دقیق لازم در PoC) | `a2aproject/a2a-python` و TCK | Agent Card، Message، Task، Artifact، شناسه زمینه و واگذاری مستقل | در P0 صرفاً انتخاب مرز؛ ابتدا handoff داخلی، A2A server در صورت نیاز |
| هسته/Agent ↔ ابزار و منبع | MCP specification **2025-11-25** | `modelcontextprotocol/python-sdk` و سرورهای سازگار | تعریف ابزار، URI منبع، Schema ورودی/خروجی و نتیجه ساختاری | CAP-006 با adapter؛ فراخوانی مستقیم تابع داخل همان فرایند نیز مجاز |
| Workflow و مراحل پایدار | Open Workflow Specification **1.0.3** | `open-workflow-specification`؛ Synapse و دیگر Runtimeها، اعتبارسنجی نسخه ضروری | تعریف قابل حملِ مراحل خواندن → تحلیل → تأیید → پیگیری | برای سناریوهای چندمرحله‌ای، نه اجبار اجرای موتور مستقل در P0 |
| API مدیریت داخلی | OpenAPI 3.1 + JSON Schema Draft 2020-12 | FastAPI/Pydantic / OpenAPI toolchain | توصیف endpointهای میزبان مرکزی بدون binding به Agno | هنگام ساخت API |
| هویت و اتصال Google | OAuth 2.0 Authorization Code + PKCE برای native apps، RFC 8252 | کتابخانه‌های رسمی Google و OAuth | اجازه اتصال به Gmail/Drive/Calendar در سطح scope و refresh | پس از اجازه جداگانه کاربر؛ کلید/توکن در GitHub ممنوع |
| مجوز اقدام داخلی | مدل PARC در **Cedar** | `cedar-policy/cedar`، validator / authorizer | principal/action/resource/context؛ رأی allow/deny از روی سیاست و داده | تعریف policy now؛ انتخاب اجرای engine پس از بررسی footprint |
| منبع و منشأ | W3C **PROV-O** | استاندارد رسمی W3C و کتابخانه‌های provenance | Entity سند، Activity پردازش، Agent ابزار/نقش؛ نسبت استخراج | استفاده سبک در metadata/artifact، بدون اجبار RDF server |
| رخدادهای غیرهم‌زمان | **CloudEvents 1.0** | SDKهای رسمی CloudEvents | آگاه‌سازی «ایمیل بررسی شد»، «وظیفه آماده تأیید است» | اختیاری؛ تنها هنگام نیاز واقعی به چند مصرف‌کننده |
| ردیابی | W3C Trace Context + OpenTelemetry | SDKهای رسمی OTel | شناسه ارتباطی و trace قابل بررسی؛ بدون ذخیره محتوای محرمانه | هنگام اتصال چند Worker |

**خود Google سرویس انحصاری است، نه نرم‌افزار متن‌باز؛** رابط و SDK مورد استفاده می‌تواند متن‌باز باشد. سرور رسمی Gmail MCP در Developer Preview است و ممکن است شرایط عضویت/دسترسی داشته باشد؛ نباید آن را الزام مرکزی قرار داد.

## ۲. قواعد اتصال و مالکیت وضعیت

1. **A2A Task** مرجع استاندارد ارتباط بین سرویس‌های Agent مستقل است؛ وظیفه نباید با payload اختصاصی جایگزین شود. وضعیت‌هایی مثل `WORKING` و `COMPLETED` بر اساس نسخه پین‌شده نگاشت می‌شوند. **پایداری و انجام کار واقعاً توسط A2A تضمین نمی‌شود؛** مالک اجرایی واحدی لازم است (مثلاً یک Runtime آزموده + ذخیره پایدار).
2. **Workflow Run** و **A2A Task** دو واقعیت متفاوت‌اند: Task یعنی درخواست و نتیجه قابل تبادل؛ Workflow Run یعنی عملیات داخلی. `Task.id` و `run_id` در آداپتر ثبت و به هم پیوند می‌شوند، نه اینکه همیشه یکی باشند.
3. **MCP Tool** محدود به یک توانایی با Schema مشخص است. تماس ابزار فقط بعد از بررسی هویت، داده و مجوز همان فراخوانی انجام می‌شود؛ توضیح Tool، خودِ منبع مجوز نیست.
4. **AG-UI event stream** نمایش پیشرفت و کنترل UI است؛ نباید تنها حافظه و مدرک اتمام کار باشد. خواندن دوباره Task/Artifact از منبع پایدار ضروری است.
5. **Cedar decision** فقط در صورت اجرای معتبر سیاست و داشتن اطلاعات قابل اعتماد principal/resource حجت دارد. OAuth scope صرفاً دسترسی نزد Google می‌دهد؛ به معنی اجازه نهایی دستیار برای ارسال نامه نیست.
6. **PROV provenance** باید از شواهد واقعی تولید شود؛ محتوا، شناسه منبع و نسخه/هش باید قابل بررسی باشند. خروجی مدل = پیشنهاد، نه سند تأییدشده یا مجوز اقدام.
7. **CloudEvents** تنها برای انتقال رخدادهای نیازمند مصرف‌کننده مستقل در نظر گرفته می‌شود؛ ثبت/تحویل قطعی، dedupe و outbox وظیفه Runtime/Storage است نه خاصیت تضمین‌شده استاندارد CloudEvents.
8. سیستم باید بعد از خروج/باز شدن، کارهای `pending`، `awaiting approval`، `running` و `unknown outcome` را درست بازیابی کند. صرف وجود Session history یا event log UI کافی نیست.

## ۳. مکانیزم ترکیب: کدام استاندارد کدام بخش را می‌گیرد؟

```
Persian chat UI
   └─ AG-UI messages/events (user ↔ agent UI)
         └─ Trusted Operations API (OpenAPI; authenticated)
              ├─ Authorization boundary (Cedar PARC, local policy)
              ├─ One durable workflow/task executor (actual engine chosen by PoC)
              ├─ Local Python worker (CAP-006 / future mail parser)
              │     └─ MCP Tool schema & structuredContent on exposed boundary
              ├─ Gmail connector
              │     ├─ Option A: Google official Gmail MCP (Developer Preview)
              │     └─ Option B: Gmail REST API + OAuth2/PKCE adapter
              ├─ Agent/runtime A ↔ Agent/runtime B (A2A on independent-service boundary)
              ├─ Source evidence/ARTIFACT (PROV-O concepts + real digest/revision)
              └─ Optional CloudEvents / OTel for asynchronous workers
```

**در روز اول نیازی نیست هر جعبه یک سرویس، Database یا Process مستقل باشد.** AG-UI/A2A/MCP می‌توانند به‌صورت آداپتر روی هسته ماژولار و سازگار پیاده شوند. Open Workflow دستور زبان توصیف کار است، نه تضمین‌کننده عمل‌کردن همه Workerها روی دستگاه کاربر.

## ۴. سناریوی مرجع واقعی: «ایمیل‌های کاری را بررسی کن و پیگیری را آماده کن»

| گام | ورودی / خروجی | پروتکل/حوزه | شرط و مسئولیت |
|---|---|---|---|
| 1 | فرمان فارسی کاربر | AG-UI → API | هویت معتبر؛ درخواست برای کار ثبت شود |
| 2 | دریافت ID/متادیتای ایمیل‌ها | Gmail MCP `search_threads`/`get_thread` یا Gmail REST `messages.list/get` | ابتدا `gmail.readonly` برای خواندن، OAuth scope محدود و مجوز داخلی |
| 3 | ثبت مرجع منبع | PROV Entity + Gmail `messageId`, `threadId`, `historyId`, زمان واکشی | پیام کامل را بی‌نیاز در حافظه دیگر نقش‌ها منتشر نکن؛ رفرنس و گزیده کافی است |
| 4 | تحلیل محتوا/فرصت | MCP/تابع Python + مدل در صورت نیاز | پارس/دسته‌بندی قطعی با Python؛ استدلال فارسی و اولویت‌بندی با مدل اختیاری |
| 5 | تحویل تحلیل برای بازبینی | A2A Message/Task/Artifact در صورت استقلال Agentها | فقط رفرنس و خروجی لازم؛ ممنوعیت انتقال خودکار scope/توکن |
| 6 | ساخت پیش‌نویس پاسخ | محتوای پیشنهادی؛ Gmail MCP `create_draft` یا REST `drafts.create` | عمل ایجاد Draft جدا از خواندن است؛ نیاز به اجازه مناسب `gmail.compose` و سیاست محلی |
| 7 | تأیید انسانی متن/گیرنده | AG-UI / WAITING_APPROVAL + durable receipt | هش دقیق متن، گیرنده، موضوع و پیوست‌ها + صاحب تأیید، expiry، امکان رد/اصلاح |
| 8 | ارسال واقعی | مسیر مستقل Gmail API `drafts.send`/`messages.send`، **نه همان ابزار خواندن** | فقط مجوز صریح مختص هر ارسال؛ جلوگیری از تلاش ارسال مجدد بدون بررسی نتیجه |
| 9 | ذخیره رسید و برنامه پیگیری | Gmail sent message ID/thread reference + artifact/state | تطبیق پاسخ/دوباره‌فرستی، زمان پیگیری و اقدام بعدی در وضعیت پایدار |

**ملاحظات Gmail:** سرور رسمی Gmail MCP فعلی دست‌کم خواندن و `create_draft` را عرضه می‌کند و هنوز Developer Preview است. برای ارسال واقعی نباید فرض کرد همان toolset متد send را فراهم می‌کند؛ مستندات REST برای Send قابل اتکاترند. `gmail.compose` از نظر scope می‌تواند امکان ارسال هم بدهد، بنابراین باید ارسال در مجوز *اجرای محلی* به‌صورت جدا ممنوع باشد تا پس از تأیید دقیق آزاد شود. Gmail `history.list` برای همگام‌سازی افزایشی است؛ `404` برای history منقضی‌شده یعنی نیاز به sync مجدد. Gmail `watch` به Cloud Pub/Sub و تمدید دوره‌ای نیاز دارد؛ برای شروع محلی polling کنترل‌شده آسان‌تر است.

**مرز حریم خصوصی:** قبل از ارسال متن ایمیل به یک مدل ابری، باید مبنای مجاز بودن انتقال و سرویس منتخب مشخص شود. محتوای ایمیل و دستورالعمل داخل آن به‌عنوان *داده نامطمئن* تلقی شود، نه فرمان دارای قدرت دسترسی به Gmail یا سیستم.

## ۵. چه چیزهایی هنوز خاص DJMRN خواهند ماند؟ (بدون اختراع پروتکل تازه)

- ثبت رابطه `A2A Task ID` با `Workflow Run ID` و شناسه thread/mail؛ استانداردها این نگاشت را برای DJMRN به‌طور خودکار نمی‌دانند.
- سیاست واقعی مجوز: آیا این شخص/دستیار روی این حساب/ایمیل/فایل حق اجرای این operation را دارد؟ Cedar نحو عمومی می‌دهد؛ قواعد را مالک سیستم تعیین می‌کند.
- ساخت مرجع منبع قابل استناد از Gmail یا CAP-006، هش/زمان/منشأ، مرز اشتراک اطلاعات و زمان نگهداری.
- تعاریف منابع و قابلیت‌ها، mapping خطاهای واقعی سرویس‌ها و پیکربندی retry/reconciliation؛ اجرای اثر جانبی دقیقاً یک‌بار را نباید وعده داد.
- محدودیت هزینه، مصرف مدل‌های OmniRoute و قوانین جلوگیری از fallback پولی؛ این‌ها استاندارد A2A/MCP نیستند.
- رابط فارسی و کیفیت فهم فارسی به مدل/UX مربوط است، نه اینکه پروتکل زیرساخت فارسی‌سازی شود. همه متن‌ها UTF-8؛ زبان گفتگو `fa-IR`.

این موارد **یک Integration Profile کوچک و منطق سیاست/کسب‌وکار** است، نه طراحی مستقلِ دوباره Task/Message/MCP/Workflow.

## ۶. آزمون‌های حداقلیِ رسمی قبل از تصویب نسخه اجرایی

| تست | PASS باید چه باشد؟ |
|---|---|
| A2A SDK + TCK | Agent Card و مدل Task/Message/Artifact طبق همان نسخه؛ انتقال A→B→A و correlation |
| MCP Schema & tool adapter | انطباق Tool schema CAP-006 و structuredContent، اجازه فقط دو سند؛ رد سند سوم |
| Task vs Run ownership | یک مرجع اجرایی وضعیت و نگاشت قابل بازیابی به A2A Task؛ جلوگیری از DONE زودهنگام |
| Restarts | بازیابی Task/Artifact/approval بعد از بستن و بازکردن؛ وضعیت نیمه‌تمام واضح |
| Gmail read mock | داده مصنوعی Gmail؛ scopes و read-only؛ بدون ارتباط واقعی با حساب |
| Gmail real read | فقط بعد از اجازه، OAuth درست، dedupe message IDs و حفظ history checkpoint |
| Gmail draft separation | تفاوت `gmail.readonly` و `gmail.compose` در سیاست؛ Draft بدون Send |
| Human approve and send | عدم ارسال پیش از approve target/payload; وضعیت نامعلوم بدون ارسال کورِ دوباره |
| Evidence | شناسه ایمیل/فایل، نسخه/هش، نتیجه و مرجع ساخته‌شده/خوانده‌شده سازگار |
| Denied capability | درخواست LLM یا Agent نتواند scope جدید به خود بدهد |
| Alternate runtime | همان Tool و Artifact با Agno/MAF و بدون تغییر پروتکل تبادل |
| Offline fallback | بدون اینترنت هم CAP-006 و دفتر وظایف قابل استفاده بمانند |
| Resource/portability | RAM/CPU/latency/startup روی Windows 8 GB اندازه‌گیری، export/restore واقعی انجام شود |

## ۷. فازبندی شروع: کمترین اجزای لازم، حداکثر سازگاری آینده

- **P0، اکنون (design only):** همین Profile + versions + source links + policy test vectors. مرز دستیار، وظیفه، ابزار، مجوز و منابع روشن؛ ساخت/نصب ضروری نیست.
- **P1، اولین کار واقعی:** یک رابط فارسی آماده یا سبک، Tool موجود CAP-006 و یک مالک وضعیت پایدار. MCP Tool adapter صرفاً در صورت نیاز؛ A2A و AG-UI همواره قابل اضافه شدن باشند.
- **P2، Google:** از mock به OAuth واقعی Gmail و در صورت دسترسی Developer Preview به Gmail MCP؛ اول read-only، سپس drafts با تأیید جدا. اجرای Python worker و evidence.
- **P3، چند دستیار:** A2A واقعی فقط وقتی دو Agent مستقل وجود دارد؛ در یک برنامه استفاده از Agent runtime handoff سبک‌تر است.
- **P4، workflow/scheduling:** اجرای استاندارد Open Workflow با runtime واقعیِ آزموده یا نگاشت به موتور durable انتخابی؛ اجرای موازی بی‌دلیل و چند مرجع وضعیت ممنوع.

## ۸. منابع اولیه رسمی (snapshot 2026-10-27)

- A2A Protocol v1.0.1 specification: https://a2a-protocol.org/v1.0.1/specification/
- A2A official Python SDK: https://github.com/a2aproject/a2a-python
- A2A official TCK: https://github.com/a2aproject/a2a-tck
- MCP specification 2025-11-25: https://modelcontextprotocol.io/specification/2025-11-25
- MCP Python SDK: https://github.com/modelcontextprotocol/python-sdk
- AG-UI: https://github.com/ag-ui-protocol/ag-ui
- Open Workflow Specification 1.0.3: https://open-workflow-specification.org/
- Open Workflow GitHub: https://github.com/open-workflow-specification/specification
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- Cedar authorization request: https://docs.cedarpolicy.com/auth/authorization.html
- JSON Schema draft 2020-12: https://json-schema.org/draft/2020-12/schema
- OAuth native apps RFC 8252: https://www.rfc-editor.org/rfc/rfc8252
- Gmail official MCP Developer Preview reference: https://developers.google.com/workspace/gmail/api/reference/mcp
- Gmail MCP setup: https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server
- Gmail REST scopes: https://developers.google.com/workspace/gmail/api/auth/scopes
- Gmail drafts: https://developers.google.com/workspace/gmail/api/guides/drafts
- Gmail incremental sync: https://developers.google.com/workspace/gmail/api/guides/sync
- Gmail push/watch: https://developers.google.com/workspace/gmail/api/guides/push
- Earlier DJMRN proof: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/05-assistants-and-capabilities/src/document_search_v0/docsearch_v0.py

## ۹. وضعیت تأیید

**Research-backed DRAFT READY:** پروفایل ترکیبی قابل بحث و ارزیابی است؛ فایل‌ها طراحی هستند، نه «پیاده‌سازی رسمی استانداردهای بیرونی». تا زمان اجرای TCK، validation و آزمون Windows هیچ سازگاری محصولی به‌صورت PASS ثبت نمی‌شود. هیچ سرویس نصب و هیچ حساب Google لمس نشده است. تغییر مخزن اصلی فقط با درخواست صریح ثبت از سوی کاربر انجام شود.