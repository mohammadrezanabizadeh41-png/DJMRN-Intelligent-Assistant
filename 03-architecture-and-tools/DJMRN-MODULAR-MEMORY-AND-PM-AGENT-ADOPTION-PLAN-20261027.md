# DJMRN — نقشه معماری ماژولار، حافظه بلندمدت و انتخاب اولین Agent مدیر پروژه

**شناسه:** DJMRN-MODULAR-MEMORY-PM-AGENT-PLAN-20261027  
**تاریخ:** 2026-10-27  
**وضعیت:** USER-REQUESTED RESEARCH + ROADMAP ARCHIVE؛ تصمیم اجرای نرم‌افزار/مدل، نصب جدید، تغییر تنظیمات یا استقرار نیست.  
**منبع حقیقت:** مخزن اصلی DJMRN-Intelligent-Assistant و قراردادهای OSCP v0.1 / DJMRN Coordination Contract v1.0؛ این سند هیچ‌کدام را لغو یا جایگزین نمی‌کند.

## 0. مرزهای قطعی و اصلاح وضعیت جاری

- کاربر اعلام کرده است **آزمایش‌ها و تنظیمات OmniRoute قدیمی پایان یافته‌اند و باید کنار گذاشته شوند**. همه تصمیم‌های اجرایی جدید مدل/کلید/Combo/Family باید از **نمونه تازه OmniRoute و وضعیت جاری واقعی حساب** خوانده و آزمایش شوند. از نتیجه یا خطای قدیمی برای رد یا قبول اتصال جدید استفاده نشود. ممکن است اسناد تاریخی قدیمی در مخزن باقی بمانند؛ صرفاً تاریخچه‌اند، نه تنظیم فعال.
- راه اصلی امروز: **OmniRoute جاری → AGNT installed environment → اولین شخصیت فارسی مدیر پروژه → افزوده‌شدن ماژول‌های مستقل فقط در صورت نیاز**. Agno / AgentOS و سایر موتورهای Agent مکمل و نامزدهای آینده‌اند، نه پیش‌نیاز راه‌اندازی شخصیت اول.
- هدف مدیر فارسی: گفت‌وگو، فهم هدف، پیشنهاد طرح، مشخص‌کردن قابلیت لازم، پیش‌نویس واگذاری و گزارش نتیجه؛ **عدم اجرای مستقیم جست‌وجو/Gmail/تغییر مجوز/اعمال تغییر بدون مسیر مورد تأیید**.
- قاعده "ماژولار" = مرز قرارداد، مالکیت داده، قابلیت تعویض و توسعه. **به معنی نصب یک Agent، مدل، دیتابیس یا فرایند جداگانه برای هر جزء نیست**.
- محدودیت مصرف: انتخاب مدل نقش‌محور، حداقل سطح لازم، رایگان/سهمیه تأییدشده، توقف fallback پولی، مدل قوی صرفاً هنگام نیاز. **هیچ ادعایی درباره 1M context یا quota مدل‌های فعلی تا بررسی ID واقعی و مدل/حساب معتبر نیست**.
- محل اولیه توسعه: Windows / 8GB RAM؛ هر سرویس، Docker و مدل پرهزینه فقط با آزمون میزان حافظه و هزینه پذیرفته می‌شود.

## 1. معماری منطقی و مالکیت

\`\`\`text
فارسی کاربر
   |
   v
AGNT / Persona: DJMRN Project Manager #01
   |             | chat + proposal + human approvals
   |             +----> OmniRoute current model families (inference only)
   |
   v
DJMRN Coordination Contract / Hub adapter (task, authorization, dispatch, audit)
   |
   +---> Knowledge/Memory Port ----------> AGNT built-in memory [first experiment]
   |                                 \----> Independent DJMRN archive/retrieval [future]
   |                                 \----> Mem0/Cognee/Graphiti [conditional]
   |
   +---> Search Specialist + workflow ----> web search + sourced retry
   +---> Mail Specialist + workflow ------> approved Gmail read/draft/send
   +---> Developer/CAP-006/other workers -> Python/Go/Rust/.NET/container
   +---> Policy Gate ---------------------> deterministic allowlist; Cedar [conditional]
   |
   +---> receipt/result/evidence_ref ----------> AGNT PM Persian reply
\`\`\`

**هسته قراردادی** مالک task/message/permission/dispatch/audit و شواهد ارجاعی رسمی است؛ **AGNT** مالک شخصیت تعاملی و workflowهای داخلی خود؛ **OmniRoute** مالک مسیریابی مدل و provider؛ **ماژول حافظه** مالک متن/تاریخچه/نمایه و چرخه عمر دانش. هیچ جزء نباید بدون قرارداد مالکیت داده، "منبع حقیقت" دومی برای وضعیت کار ایجاد کند. اتصال‌ها با مرزهای JSON Schema/OpenAPI/MCP/A2A حسب نیاز؛ SDKهای استاندارد را از نو نمی‌نویسیم.

## 2. اصل مهم: Agent یا ماژول آماده یا Workflow بدون LLM؟

| کار | انتخاب اولیه | چه زمانی Agent منطقی است | گزینه‌های آمادهٔ مورد ممیزی |
|---|---|---|---|
| مدیر پروژه و گفت‌وگوی فارسی | **یک Agent در AGNT** | از روز نخست چون تحلیل و گفت‌وگو ضروری است | AGNT Agent/Goals/Workflows؛ Agno مشروط برای توسعه، نه جایگزینی خودکار |
| ذخیره پیام خام، CRUD و شناسه | **DB و API قطعی** | معمولاً نه | SQLite + API/JSON Schema |
| جست‌وجوی تاریخچه گفتگو و اجرای کار | **AGNT memory FTS5 را اول تست کن** | فقط برای تفسیر/جمع‌بندی نتایج پیچیده | AGNT Memory API / SQLite FTS5؛ بعدها Mem0 |
| تشخیص خاطرات و استخراج تصمیمات | workflow قطعی + **curator LLM محدود و اختیاری** | وقتی تشخیص معنا، تعارض و ارزش ذخیره انسانی/هوشمند لازم است | Mem0 (Apache-2.0)، Cognee (Apache-2.0) |
| گراف دانش و تصمیم‌های متغیر زمانی | سرویس مستقل در فاز پیشرفته | curator اختیاری، نه لازمه انبار داده | Graphiti (Apache-2.0)، Cognee |
| مجوزها، اجرای قرارداد و تأیید دسترسی | **policy gate قطعی، fail closed** | ناظر هوشمند فقط علت خطا را توضیح دهد/پیشنهاد کند | JSON Schema + Cedar (Apache-2.0)، OpenFGA برای روابط پیچیده |
| سرچ وب تخصصی | Search Specialist جدا با ابزار محدود و Workflow retry | تحلیل چندمنبعی/قضاوت کیفیت نیاز به Agent دارد | AGNT Agent+Workflow + ابزار جست‌وجو؛ مستقل از OmniRoute LLM calls |
| محاسبه، CAP-006 و تبدیل فایل | worker deterministic | فقط هنگام نیاز به تصمیم‌گیری پیچیده | Python/Go/Rust/.NET، MCP adapter |
| پیگیری طولانی پروژه | ابتدا AGNT Goals/Workflow + ledger قراردادی | PM Agent برای اولویت‌بندی و replanning | AGNT؛ OpenProject بعدها اگر برد/گانت/همکاری تیمی نیاز شد |
| خطا/ترمیم | خطایابی قطعی، ثبت و retry محدود | Supervisor on-demand برای تشخیص مبهم/پیشنهاد اصلاح | AGNT workflows + optional specialized reviewer |

**نتیجه:** یک Agent برای هر جدول، فایل، مجوز و retry نسازید. "شخصیت‌دار بودن" یعنی نقش گفت‌وگویی/تحلیلی قابل تفویض؛ سرویس API و دیتابیس را بی‌دلیل به Agent تبدیل نکنید. تمام ماژول‌ها می‌توانند بعداً یک facade/persona هوشمند اختیاری داشته باشند.

## 3. پژوهش GitHub و ارزیابی انتخاب ابزارهای آماده

### AGNT — نخستین Agent مدیر پروژه
- GitHub: https://github.com/agnt-gg/agnt
- مستند API Agents و Orchestration: https://agnt.gg/docs/api/agents
- Memory & Insights: https://agnt.gg/docs/api/memory-insights
- Models/Custom Providers: https://agnt.gg/docs/api/models-providers
- Agents: persona/systemPrompt, assignedTools, assignedSkills, assignedWorkflows, provider/model, chat. Workflows/Goals: اجرا و مراحل و واگذاری/پیگیری. Memory: API خاطرات agent-scoped و جست‌وجوی FTS5 در conversation, execution, outputs, insights, memories, workflow_versions.
- **هشدار فنی مهم:** در مستند فعلی، \`toolAccessMode: restricted\` همچنان **baseline tools از جمله web_search و discover_tools** را در اختیار می‌گذارد. بنابراین برای شرط "فقط Search Specialist اجازه سرچ وب دارد"، صرفاً prompt یا انتخاب restricted کافی نیست؛ قابلیت واقعی حذف/deny web_search برای PM باید در نسخه نصب‌شده آزموده شود یا اجرای ابزار در tool gateway مستقل و allowlist شده قطع گردد. پیش از تست، به Agent اول ابزار خطرناک/حساب واقعی ندهید.
- **مجوز:** AGNT Community Core License، source-available **و نه مجوز استاندارد متن‌باز**. سورس در دسترس است ولی فورک/بازتوزیع و برخی کاربردهای پولی/ارائه خدمات محدودند: https://github.com/agnt-gg/agnt/blob/main/LICENSE.md . استفاده شخصی/برخی کسب‌وکارهای کوچک طبق شرایط مجوز؛ وابستگی قفل‌شونده باید با adapter و export پرهیز شود. انتقال مدل‌ها/گفتگوها/حافظه ممکن است export سفارشی بخواهد؛ \`/api/agents/export\` بنا به API خودِ حافظه و credentials را در envelope صادر نمی‌کند.
- نتیجه: مناسب‌ترین مسیر آغاز در شرایط فعلی، **تا زمانی که اتصال OmniRoute جاری و کنترل tools در عمل پاس شود**؛ نه اثبات برتری مطلق یا انتخاب انحصاری برای همیشه.

### Mem0 — موتور حافظه تخصصی
- GitHub: https://github.com/mem0ai/mem0 ؛ Apache-2.0.
- لایه حافظه قابل نصب به‌عنوان کتابخانه یا سرور؛ استخراج و جست‌وجوی memory مستقل از Persona و AGNT. کاندید قوی برای تعویض‌پذیری و چند Agent. **جایگزین دفتر تصمیمات رسمی و نسخه‌دار نیست**؛ fact extraction ممکن است اشتباه کند و باید provenance/approval ثبت شود.
- مستندات پیش‌فرض OSS: LLM و embeddings پیش‌فرض از OpenAI استفاده می‌کنند؛ storage کتابخانه Qdrant local و history SQLite؛ self-hosted stack Postgres/pgvector. برای استفاده با OmniRoute باید سازگاری LLM و **embedding** جداگانه و رایگان/هزینه/ارسال داده سنجیده شود. https://github.com/mem0ai/mem0/blob/main/docs/open-source/overview.mdx
- پروژه **mem0ai/mem0-mcp** در 2026-03-24 archived است؛ آن را به‌عنوان server آماده فعال/maintained پیشنهاد ندهید. https://github.com/mem0ai/mem0-mcp

### Graphiti — گراف دانشی زمانی
- GitHub: https://github.com/getzep/graphiti ؛ Apache-2.0.
- نقطه قوت: ارتباط اشخاص/پروژه‌ها، اعتبار زمانی و تاریخ تغییر حقیقت؛ مناسب سوال «چه چیزی قبلاً درست بود و الان منسوخ شده؟». از Neo4j/FalkorDB/Neptune و LLM+embedding پشتیبانی می‌کند، پیش‌فرض OpenAI. dependency و حافظه بیشتر؛ شروع با آن روی Windows 8GB بدون آزمون توجیه ندارد.
- مستند: https://github.com/getzep/graphiti/blob/main/README.md

### Cognee — حافظه و دانش Graph/RAG
- GitHub: https://github.com/topoteretes/cognee ؛ Apache-2.0 برای repo.
- مناسب ingestion و retrieval دانش اسناد و حافظه چندمنبعی؛ dependency و سرویس/پیکربندی بیشتری دارد. در مستند repo، بخشی از روش Postgres graph به‌عنوان demo و نسخه production آن licensed معرفی شده؛ **فرض نکن تمام قابلیت‌های تجاری یکسان آزادند**.
- بعد از سنجش AGNT memory و Mem0 وارد مقایسه هم‌بار شود، نه نصب هم‌زمان.

### Cedar — کنترل مجوز به‌جای «شخصیت نگهبان قرارداد»
- GitHub: https://github.com/cedar-policy/cedar ؛ Apache-2.0.
- ابزار قطعی principal/action/resource/context، policy و validator؛ مناسب اجرای مستقل از مدل، نه پایگاه داده وظایف. بررسی معنادار خطای policy می‌تواند Agent مشاور جدا داشته باشد؛ رأی اجرایی صادر نمی‌کند.

### Agno و LangGraph / OpenProject — گزینه‌های تکمیلی
- Agno: https://github.com/agno-agi/agno ؛ Apache-2.0؛ Agent/Team/Workflow/Memory. مناسب آزمون **وقتی AGNT واقعاً محدودیت فنی اثبات‌شده‌ای دارد**؛ از ابتدا دو runtime agent فعال نکنیم.
- LangGraph: https://github.com/langchain-ai/langgraph ؛ stateful orchestration toolkit؛ جایگزین احتمالی معماری runtime در موارد تخصصی، نه ابزار حافظه یا مدیر پروژه مستقل.
- OpenProject: https://www.openproject.org/docs/api/ ؛ سیستم مدیریت پروژه و API، ولی برای نخستین چت فارسی بیش از نیاز؛ اگر برنامه‌های کاری/Gantt/team collaboration لازم شد ارزیابی شود.

## 4. شخصیت اولیه — DJMRN-PM-01 (تعریف پیشنهادی، اجرا نشده)

**نام:** DJMRN — مدیر پروژه فارسی (PM-01)  
**محیط اجرا:** AGNT Agent (نسخه نصب‌شده کاربر باید بررسی شود)  
**مدل:** یکی از مدل‌های **فعلی** OmniRoute پس از تست واقعی; Lite/General برای گفتگو/طبقه‌بندی؛ ارتقا به Reasoning صرفاً براساس پیچیدگی قابل‌اندازه‌گیری. نام مدل، context limit، سهمیه، pricing و tool-call support هنوز VERIFIED نیست.  
**دسترسی آغازین:** چت فارسی، فهرست قابلیت‌های تعریف‌شده و پیشنهاد وظیفه؛ **بدون** ارسال ایمیل، اجرای shell، سرچ وب خودکار، ویرایش پروژه، credential یا policy. کنترل فنی ابزارها باید مستقل از system prompt تأیید شود.  
**ماموریت:** درک متن فارسی، نگهداری بافت گفت‌وگو در محدوده مجاز، پرسیدن سؤال فقط وقتی ضروری، تجزیه هدف به مراحل، تشخیص متخصص و ریسک، صدور *proposal* در ساختار قرارداد و پاسخ فارسی.  
**تفاوت proposal با execution:** مدل مجاز است پیشنهاد دهد «باید از Search Specialist بخواهیم»؛ **اجرای واقعی** فقط توسط Hub/policy adapter معتبر و capability ثبت‌شده پذیرفته می‌شود.  
**رفتار منابع:** دانش قبلی و آخرین تصمیمات مستند را با timestamp/validity بررسی کن؛ اگر اطلاعات ناقص است صریح اعلام کن؛ هرگز سابقه قدیمی OmniRoute را به‌عنوان وضعیت فعلی نپذیر.  
**حافظه:** شروع AGNT scoped chat/memory برای گفتگوهای همین شخصیت، آینده ماژول مستقل با adapters. هیچ خودکارسازی حفظ همه اطلاعات، استخراج شخصی یا ارتقای خاطره خام به حقیقت نهایی بدون provenance.
**شخصیت ثانویه:** "Memory Curator"/"Contract Reviewer" فقط پس از نیاز اثبات‌شده، می‌توانند Agent اختیاری باشند؛ مالکیت داده و policy gate آن‌ها deterministic است.

### وظیفه آزمایشی نخست و تست پذیرش

1. فقط **Custom Provider فعلی** OmniRoute را در AGNT بررسی کن؛ هیچ config قدیمی را از آرشیو کپی نکن.
2. تست چت فارسی با **یک مدل موجودِ تأییدشده از حساب فعلی** (no tools در صورت امکان). خروجی فقط پاسخ فارسی، مصرف، خطا، model ID، status HTTP. context window واقعی را از provider/model دریافت کن؛ عدد 1M ادعای عمومی نیست.
3. ساخت PM-01 با systemPrompt و محدودترین ابزار واقعی؛ ثابت کن PM نمی‌تواند مستقیم web_search یا send_mail را اجرا کند. اگر چنین امکانی در AGNT فعلی قابل deny نیست، استفاده عملی از PM را تا فراهم شدن gateway جداگانه محدود به sandbox بدون ابزار نگه دار.
4. سه سناریوی گفت‌وگو: پرسش عمومی؛ درخواست تحلیل و تولید plan؛ درخواست «از متخصص جست‌وجو سؤال کن» که فقط **proposal** می‌دهد و هیچ web call اجرا نمی‌شود.
5. ثبت یک \`TASK_SUBMISSION\` آزمایشی در format قرارداد v1 و صحت‌سنجی JSON Schema؛ تولید/ثبت task ID اصلی صرفاً توسط trusted Hub در مرحله بعد.
6. پس از پاس، Agent را به یک adapter مجاز Hub وصل کن. بعداً Memory Port با یک API و سنجش AGNT builtin vs Mem0؛ متخصص‌ها و workflowها تدریجی.

**معیار توقف:** مدل Tool Calling را ندارد اما AGNT اجباراً tool schemas ارسال می‌کند؛ PM با ابزار ممنوع/غیرقابل‌کنترل مواجه است؛ مدل پرداخت یا fallback ناشناخته دارد؛ پاسخ فارسی یا JSON قراردادی ناهمخوان است. با نام‌بردن مسئله و سنجش جایگزین حل کن، نه نصب بی‌برنامه.

## 5. نقشه حافظه ماژولار پیشنهادی (قرارداد و داده مهم‌تر از Agent)

**طبقات منطقی** (در فاز اول لزوماً 5 دیتابیس نیست):
1. **Conversation Archive:** پیام خام، گفتگو/جلسه، نقش، زمان، منبع و دسترسی؛ append-only و exportable.
2. **Decision Register:** تصمیم، تاریخ آغاز/پایان اعتبار، supersedes، منبع مدرک، تأیید کاربر؛ تصمیم منسوخ حذف یا به حقیقت جاری تبدیل نشود.
3. **Execution/Incident Ledger:** وظایف، dispatchها، نتایج، خطا، retry، رسید اجرای ابزارها و idempotency.
4. **Knowledge Corpus:** فایل‌های پروژه، پژوهش، هش، نسخه، URL، تاریخ مشاهده، trust status.
5. **Experience/Skill Store:** الگوهای موفق، lessons learned و پیشنهادها؛ هر استنباط LLM به‌عنوان proposal برچسب‌گذاری شود.

**interface آینده، مستقل از زبان/AGNT**: \`remember(event)\`, \`query(query,scope,as_of)\`, \`get_source(ref)\`, \`propose_update\`, \`approve\`, \`invalidate\`, \`export\`, \`delete\`؛ نام‌های نمونه طراحی، **نه endpointهای ساخته‌شده**. مالکیت Task در Hub، مالکیت content/knowledge در Memory Service؛ پیام بین‌عاملی فقط با authenticated origin و scoped references.

**قواعد حیاتی:** حافظه هنگام هر درخواست مرتبط بازیابی می‌شود نه اینکه تمام تاریخچه در prompt جا داده شود؛ citation + provenance + as_of؛ رد یا جداسازی مطالب خصوصی؛ backfill از ChatGPT فقط از Exportی که خود کاربر ارائه کند؛ snapshot/backup، retention و امکان حذف؛ cache/embedding قابل بازسازی و اصل متن قابل انتقال. AGNT memory built-in می‌تواند مرحله اول باشد، ولی نباید تنها نسخه غیرقابل‌انتقال تصمیمات باشد.

## 6. مسیر توسعه مرحله‌ای و نقاط تصمیم

**مرحله A — همین حالا (فقط یک Agent):** وضعیت جدید OmniRoute + AGNT Custom Provider، مدل با توان فارسی و کنترل ابزار؛ ساخت و آزمون PM-01 چت فارسی. **هیچ پایگاه دانش خارجی یا Agent حافظه جدید لازم نیست.**

**مرحله B:** تأیید ساختار پیشنهاد Task توسط JSON Schema قرارداد، اتصال محصور PM-01 به Hub؛ تمایز status/receipt و پیشنهاد LLM، ثبت وضعیت قطعی.

**مرحله C:** حافظه پایه: بررسی AGNT built-in conversation/FTS5، export و backup؛ سناریوهای تصمیم قدیمی/جدید و ارجاع منبع. پس از سنجش، SQLite/FTS5 مستقل یا Mem0، نه نصب همزمان ابزارهای اضافی.

**مرحله D:** Specialist Research/Search + scoped web tool + retry workflow؛ بعد Mail/Python/CAP-006؛ ابزار بدون نیاز به LLM ابتدا deterministic.

**مرحله E:** Memory Curator/Quality Reviewer اختیاری؛ اگر تحلیل تعارض حافظه/کیفیت واقعاً مشکل داشت. اگر گراف زمانی لازم شد Graphiti/Cognee، با تست کیفیت فارسی و RAM/embedding budgets.

**مرحله F:** چند runtime/language و استقرار hybrid در صورت نیاز؛ AGNT adapters و future Agno/MCP/A2A، Docker/Go/Rust/.NET. مهاجرت باید بدون از دست‌دادن شناسه‌ها/تصمیمات ممکن باشد.

## 7. تصمیم ثبت‌شده و قیود پژوهش

- **RECOMMENDATION (NOT FINAL STACK APPROVAL):** AGNT-first PM persona + current OmniRoute; start with native memory features and module ports; external Mem0/Graphiti/Cognee as candidates; deterministic authority for contracts/DB.
- هیچ کلید، متن ایمیل، محتوای خصوصی، حساب واقعی یا اتصال مدل در این سند ثبت نشده است.
- ممیزی فوق از اسناد رسمی و source/README و license است؛ **بنچمارک اجرایی Windows، کیفیت فارسی، RAM، مدل‌های حساب جاری OmniRoute، پشتیبانی واقعی JSON Tool Calling و export AGNT هنوز انجام نشده‌اند.**
- وضعیت قدیمی OmniRoute به درخواست کاربر **منسوخ** است؛ فقط مقایسه تاریخی مجاز، نه مبنای تصمیم/اتصال.

### منابع اصلی
- AGNT: https://github.com/agnt-gg/agnt , https://agnt.gg/docs/api/agents , https://agnt.gg/docs/api/memory-insights , https://agnt.gg/docs/api/models-providers , https://github.com/agnt-gg/agnt/blob/main/LICENSE.md
- Mem0: https://github.com/mem0ai/mem0 , https://github.com/mem0ai/mem0/blob/main/docs/open-source/overview.mdx , https://github.com/mem0ai/mem0-mcp
- Graphiti: https://github.com/getzep/graphiti
- Cognee: https://github.com/topoteretes/cognee
- Cedar: https://github.com/cedar-policy/cedar
- Agno: https://github.com/agno-agi/agno
- LangGraph: https://github.com/langchain-ai/langgraph
- OpenProject: https://www.openproject.org/docs/api/
- SQLite FTS5: https://www.sqlite.org/fts5.html

**NEXT ACTION:** آزمون اتصال *جدید* OmniRoute به AGNT و ساخت PM-01 با ابزارهای واقعاً محصور، نه ساخت Agent حافظه یا اجرای کامل چندماژوله.
