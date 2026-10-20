# DJMRN PROJECT ↔ ChatGPT Work Research Bridge — پروتکل الزام‌آور

**این bridge فقط برای پژوهش اختصاصی پروژهٔ جدید است و در همین private repo اجرا می‌شود.** مخزن قدیمی [Applied Research Bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge) را برای این WQ/WA تغییر ندهید. آزمایش انتقال T0001 در 2026-10-20 **PASS** (خواندن، نوشتن و بازخوانی روی همین repo؛ [commit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/d70a9a406a7057a7b40e11ad99e70d2574536e5c), blob `8094f76e732305fcc8d22a48639cb0e347325874`). این به معنی دسترسی تضمین‌شده در sessionهای بعدی، پژوهش معتبر یا Agent/اجرای عملی نیست.

## قفل هویت مخزن — D-010 (الزامی برای همهٔ WQ/WA آینده)

**Only write target:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` → https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant (branch `main`). Work باید [REPOSITORY-LOCK.md](REPOSITORY-LOCK.md) را بخواند، `full_name` واقعی و branch را با این مقدار مطابقت دهد و **فقط پس از تأیید هویت مخزن** گزارش را به مسیر WQ/WA آن بنویسد. `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` یک مخزن پژوهشی **جدا و فقط منبع خواندنی** برای همین وظایف است. mismatch یا نبودِ امکان تأیید repository = **BLOCKED و توقف؛ بدون انتخاب مقصد جایگزین**. بعد از Commit، fetch باید از **همان مخزن** باشد و رسید Work شامل `repository_full_name`, commit، blob و readback باشد. هماهنگ‌کننده نیز مستقل بررسی می‌کند. درخواست/پاسخ‌های قدیمی تغییر نمی‌کنند.

## پروتکل اجباری پژوهش ترکیبی: Applied Library + Independent Search — 2026-10-21

**وضعیت:** این بخش یک **تکمیل اجراییِ پروتکل موجود** است، نه پروژهٔ Discovery جدید، نه مخزن/کتابخانهٔ موازی، و نه مجوز ایجاد خودکار درخواست. **برای هر درخواست WQ که از Work «تحقیق، سرچ، یافتن ابزار/مدل/روش، ارزیابی یا مقایسهٔ گزینه‌ها» می‌خواهد، Work باید خودکار این مسیر را اجرا کند، بدون اینکه کاربر بار دیگر به خواندن Notion تذکر بدهد.** دامنهٔ پژوهش از پرسش WQ می‌آید؛ این دستور مجوز sweep بی‌پایان یا مرور تمام ۱۷ شاخه در هر بار نیست.

### پیش‌پرواز منبع و دامنه
1. **قفل مقصد** [REPOSITORY-LOCK](REPOSITORY-LOCK.md): نام کامل مخزن/branch/WQ/WA را احراز کن. نسخهٔ زندهٔ درخواست، [PROJECT-RULES](../PROJECT-RULES.md)، [CURRENT](../07-operations-and-continuity/CURRENT-STATUS.md)، تصمیم‌ها/تست‌های مرتبط و [دانشنامهٔ پروژه](../08-project-knowledge-base/INDEX.md) را بخوان. خواندن تاریخچه به معنی برتر شمردن نرم‌افزار نصب‌شده نیست.
2. **نیاز پیش از ابزار:** مسئلهٔ مشخص، I/O، ارزش خروجی، محدودیت مجوز/هزینه/RAM/منطقه، معیار پذیرش و شکاف دانشی را از WQ استخراج کن. سؤال قبلاً پاسخ‌داده‌شده را دوباره پژوهش نکن؛ امکان اینکه «ابزار جدید لازم نیست» یکی از خروجی‌هاست.
3. **مسیر A، کتابخانهٔ کاربردی Notion (مطالعهٔ زنده و هدفمند، READ-ONLY):**
   - [Applied Capability Index](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f) را زنده باز کن، نسخه/تاریخ و شاخه‌های مرتبط از ۱۷ شاخه را تعیین کن. [Applied Mission](https://app.notion.com/p/3fdc8c6846908167a77feab9564dc66d) و روش CURRENT آن را بررسی کن.
   - **متن همان بخش‌های مرتبط، شناسه‌های فناوری، نتایج/آزمون‌ها و منابع ثبت‌شدهٔ مرتبط را واقعاً بخوان**؛ صرف داشتن URL، نتیجهٔ جست‌وجوی نام یا حافظهٔ مدل «READ» محسوب نمی‌شود. از [General Discovery Living Research](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) برای منبع اولیهٔ فناوری و هویت/alias و نامزدهای رقیب لازم استفاده کن؛ در صورت نیاز شواهد Applied قبلی [Research Bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge) را **فقط بخوان**.
   - ثبت کن **کدام URL/page/branch/نسخه/تاریخ را عملاً خواندی**، کدام فناوری از قبل در کتابخانه هست، چه محدودیت/شاهدی قبلاً ثبت شده، و کدام بخش را نتوانستی بخوانی. ۱۷ شاخه نقشهٔ طبقه‌بندی‌اند، نه ۱۷ ماژول الزامی پروژه و نه الزام مطالعهٔ غیرمرتبط.
4. **مسیر B، سرچ مستقل تازه (متعصب به فهرست موجود نباش):** مستقل از فناوری‌های استخراج‌شده از کتابخانه، برای همان نیاز **نامزدهای تازه و بدیل** را از منابع رسمی جاری/مخزن توسعه‌دهنده/راهنمای محصول پیدا و با گزینه‌های مندرج در Notion مقایسه کن. حداقل گزینهٔ سادهٔ بدون LLM/Agent، ابزار آماده، کدنویسی اختصاصیِ کمینه (فقط در صورت نیاز)، local و remote/hybrid مناسب را ارزیابی کن؛ نامزد تازه و نصب تاریخی هر دو بدون امتیاز پیشینی هستند. اخبار/Reddit/trending صرفاً سیگنال‌اند؛ ادعای واقعی باید به منبع اولیه و تاریخ بررسی متکی باشد.
5. **ادغام A+B به‌جای دو فهرست جدا:** identity/alias dedupe؛ `EXISTING-IN-LIBRARY`، `EXISTING-ENRICHED`، `NEW-CANDIDATE`، `UNVERIFIED` را از هم جدا کن. برای گزینه‌های قابل‌مقایسه نقش، پذیرش/رد مبتنی بر نیاز، قابلیت واقعی، نسخه/زمان، Windows یا Cloud، منبع/RAM (اندازه‌گیری‌شده در برابر ادعای سازنده)، خروجی فارسی، وابستگی، true Free/Trial/card/overage/renewal، اجازهٔ ایران، license/حریم خصوصی/نگهداری و ریسک امنیت/بازیابی را ثبت کن. `UNKNOWN` را حدس یا برنده حساب نکن؛ `UNKNOWN cost / region = DENY ACTIVATION`. به دام فهرست طولانی بدون مقایسه نیفت.
6. **جمع‌بندی اجرایی و قابل رد:** حداکثر ۳ گزینه/مسیر با ارزش واقعی، یک پیشنهاد **مشروط**، معیار نقض پیشنهاد و کوچک‌ترین آزمون برگشت‌پذیر روی کاغذ؛ هیچ محصول/مدل/Agent/host الزاماً برنده نیست. خروجی Work «پیشنهاد پژوهشی» است، نه تصمیم پروژه و نه اجرای سیستم.

### رسیدهای الزامی داخل WA هر درخواست پژوهشی
گزارش `WA####.md` باید دو بخش مستقل با این فیلدها داشته باشد:
- **APPLIED_LIBRARY_READ_RECEIPT:** `status=READ/PARTIAL/NOT_READ`; لینک دقیق Index و Mission، آخرین نسخه/checked_at واقعی، شماره/عنوان شاخه‌های مطالعه‌شده، صفحات یا مدخل‌های واقعاً خوانده‌شده، شناسه/لینک نامزدهای قبلی و منابع پشتیبان؛ General Discovery و گزارش Applied قدیمیِ *واقعاً خوانده‌شده* را جدا ذکر کن. اگر اتصال Notion نیست، صریحاً `NOT_READ (reason)` بزن و **حق نداری ادعا کنی کتابخانه کامل بررسی شده**؛ تحلیل مستقل می‌تواند ادامه پیدا کند اما ادغام/نتیجهٔ کتابخانه را `PARTIAL/BLOCKED` برچسب بزن.
- **INDEPENDENT_SEARCH_RECEIPT:** موضوع و محدودهٔ سرچ، روز بررسی، فهرست اصلی‌ترین منابع رسمی مستقل با URL و تاریخ نسخه/انتشار، بدیل‌های خارج از کتابخانه، یافته‌های منفی و `UNKNOWN`. سرچ مستقل بدون تحلیل موردنیاز جای خواندن کتابخانه را نمی‌گیرد.
- **MERGED_CANDIDATE_MATRIX:** شناسه و منبع گزینهٔ موجود/جدید، مقایسهٔ کارکردی و انتخابِ مشروط، علت رد رقبا، شکاف شواهد و *مرحلهٔ بعد فقط با تأیید کاربر*.

### توقف و محدودهٔ اختیار
- Work در همین مخزن **فقط فایل پاسخ شماره‌دار `responses/WA####.md`** را ایجاد/Commit/readback می‌کند. Work درخواست، LEDGER، کد، Notion، کتابخانهٔ Applied یا General و مخزن مجزای Research Bridge را تغییر نمی‌دهد.
- خواندن Notion به Work مجوز انتشار خصوصی‌ها یا دادهٔ حساس در GitHub نمی‌دهد؛ فقط خلاصهٔ sanitized، شناسه و لینک شواهد لازم. هیچ نصب، آزمون Windows، ثبت‌نام/احراز، اتصال حساب، هزینه/کارت، API token، اجرای workflow، ارسال پیام یا اقدام تولیدی بدون اجازهٔ جدید.
- اگر Work به کتابخانه دسترسی ندارد، حق درخواست تغییر مقصد یا ادعای اینکه پژوهش «دو مسیرهٔ کامل» بوده را ندارد؛ **نتیجهٔ جزئی صادقانه** و مسیر رفع مانع را ثبت می‌کند. نقص دسترسی به کتابخانه سبب رها کردن تحقیق مستقل نمی‌شود، ولی نتیجهٔ نهایی مربوط به قابلیت‌های *پیشتر بررسی‌شده* تا مطالعهٔ واقعی کتابخانه نامطمئن می‌ماند.
- پژوهش‌های صرفاً «بازخوانی/بازبینی یک گزارش ثبت‌شده» و بدون درخواست search/discovery خارج از الزام سرچ مستقل هستند؛ **WQ با فرمان پژوهش/سرچ** به‌صورت خودکار مشمول این سیاست است.

## چرخهٔ دقیق
1. **هماهنگ‌کننده** از `README.md`, `PROJECT-RULES.md`, `07/CURRENT-STATUS.md`, نیاز واقعی، [دانشنامهٔ اختصاصی پروژه](../08-project-knowledge-base/README.md) و [INDEX آن](../08-project-knowledge-base/INDEX.md) و فایل‌های 01/03 شروع می‌کند. **SRC-0001 / KB-0001..KB-0009 پژوهش معماری قبلی کاربر است، نه خروجی Work؛ به عنوان input فاقد تأیید رسمی بخوان و سؤال‌های تکراری بی‌دلیل صادر نکن.** سپس از [Applied Library](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f)، [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) و شواهد قبلی مرتبط استفاده می‌کند؛ محصول تکراری را با alias/identities dedupe می‌کند.
2. اگر gap معنادار هنوز موجود است، **درخواست هدفمند Work** را در `requests/WQ0001.md` (شماره بعدی از LEDGER و خود پوشه بعد از بررسی GitHub) ثبت می‌کند: goal, exact acceptance, independent alternatives, sources, out-of-scope, negative evidence, hardware/remote locality, current free/cost/region/security gates. Write successful = readback needed.
3. **کاربر** فقط به Work می‌گوید: «در مخزن خصوصی `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` دستور `04-work-research-bridge/requests/WQ0001.md` را بخوان و طبق README همان بخش عمل کن.» آزمایش synthetic `T0001` اکنون با readback تأیید شده؛ پژوهش بعدی فقط با فایل WQ واقعی و هدف مشخص اجرا شود.
4. **Work** اصل درخواست و قوانین را **از GitHub** می‌خواند، جست‌وجوی عمیق official-source انجام می‌دهد و گزارش **کامل** `responses/WA0001.md` با شماره متناظر در همین repo ثبت می‌کند؛ بعد با بازخوانی واقعی صحت فایل را می‌سنجد؛ فقط شناسه و نتیجهٔ فشرده را در Chat می‌گوید.
5. کاربر می‌گوید «WA0001 آماده است». هماهنگ‌کننده فایل **واقعی** را fetch می‌کند، ادعاها/نسخه و negative findings را جدا بررسی می‌کند، `reviews/WQ0001.md` شامل accepted/rejected/unverified/impacts/next را می‌نویسد.
6. پس از بازبینی واقعی، **یافته‌های قابل استفادهٔ Work ابتدا با SRC/KB و provenance طبق [پروتکل دانشنامه](../08-project-knowledge-base/INTAKE-PROTOCOL.md) به [دانشنامه پروژه](../08-project-knowledge-base/README.md) ارجاع/استخراج می‌شوند**. سپس نتایج تصمیم/اقدام تأییدشده در `03-architecture-and-tools` و/یا `05` و `02/TASK-REGISTER` ثبت می‌شوند؛ اگر **کاتالوگ عمومی/Applied** جدید لازم شد، از روال canonical Notion و مسئول مربوط ثبت شود، نه خودسرانه تغییر کتابخانه. مهم: **گزارش Work = evidence candidate، نه اجازهٔ نصب، نوشتن فایل حساس یا پذیرش معماری**.
7. `LEDGER.md`, `07/CURRENT-STATUS.md`, `07/CHANGELOG.md` و ارتباط source/commit همیشه بعد از پذیرش و action به‌روز شوند. سؤال بعدی فقط از gapهای واقعی، نه پاسخ تکراری.

## مالکیت فایل‌ها و شناسه‌ها
- Coordinator فقط نویسندهٔ `requests/WQ####.md`, `reviews/WQ####.md` و LEDGER/STATUS است.
- Work فقط گزارش پاسخ `responses/WA####.md` را ایجاد می‌کند و نباید دیگر اسناد پروژه، کد، Notion یا عملیات حساب را تغییر دهد.
- همهٔ سؤال/جواب **immutable by convention** پس از ثبت؛ اصلاحیه با فایل suffix جدید و لینک ثبت شود. هر زوج WQ/WA عدد یکسان دارد. Work task identifiers مستقل از TASK-#### هستند.
- روی خطای نامطمئن GitHub write، ابتدا fetch; شمارهٔ جدید اختراع یا overwrite نکنید.
- raw user/customer private data, credentials, secret/token, paid APIs, provider logins و اعمال سایت **خارج از دامنه** پژوهش است.
- تأیید success از repository readback لازم است؛ Work session ممکن است مجوز repo جدید نداشته باشد: **BLOCKED → user connector setting check**، نه ادعای خودکار اتصال.

## شمارنده
- `T0001` = آزمون انتقال غیرحساس؛ درخواست آماده در requests/T0001.md، پاسخ Work [ثبت و مستقل تأیید شده](responses/T0001.md).
- `WQ0001/WA0001` = اولین پژوهش واقعی ثبت، پاسخ و بازبینی شده است؛ به‌علت خطاهای دو source SHA در WA0001، بازبینی هماهنگ‌کننده `ACCEPTED-PARTIAL` است. `LEDGER.md` را برای وضعیت و شمارهٔ بعدی ببینید.
- گزارش‌های شماره‌دار قدیمی `Q0001/A0001...` در مخزن کتابخانهٔ قبلی متعلق به این کانال جدید نیستند.

## ورودی/خروجی الگو
[قالب درخواست](templates/REQUEST-TEMPLATE.md)؛ [قالب پاسخ](templates/RESPONSE-TEMPLATE.md)؛ [قالب بازبینی](templates/REVIEW-TEMPLATE.md)؛ [دفتر اتصال](LEDGER.md).

## New-chat continuity after WQ0001 (2026-10-20)
Research pair WQ0001/WA0001 already finished and reviewed. The user **approved D-009 sequencing**, and code CAP-006 is in repo; **do not repeat the research** as a condition for synthetic-only Windows test. Read [project snapshot](../07-operations-and-continuity/PROJECT-STATE-HANDOFF-20261020.md) and [current status](../07-operations-and-continuity/CURRENT-STATUS.md). Keep the mandatory exact-repository lock for any *future* Work research.
