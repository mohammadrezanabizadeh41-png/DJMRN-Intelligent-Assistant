# DJMRN PROJECT ↔ ChatGPT Work Research Bridge — پروتکل الزام‌آور

**این bridge فقط برای پژوهش اختصاصی پروژهٔ جدید است و در همین private repo اجرا می‌شود.** مخزن قدیمی [Applied Research Bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge) را برای این WQ/WA تغییر ندهید. آزمایش انتقال T0001 در 2026-10-20 **PASS** (خواندن، نوشتن و بازخوانی روی همین repo؛ [commit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/d70a9a406a7057a7b40e11ad99e70d2574536e5c), blob `8094f76e732305fcc8d22a48639cb0e347325874`). این به معنی دسترسی تضمین‌شده در sessionهای بعدی، پژوهش معتبر یا Agent/اجرای عملی نیست.

## چرخهٔ دقیق
1. **هماهنگ‌کننده** از `README.md`, `PROJECT-RULES.md`, `07/CURRENT-STATUS.md`, نیاز واقعی و فایل‌های 01/03 شروع می‌کند. سپس از [Applied Library](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f)، [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) و شواهد قبلی مرتبط استفاده می‌کند؛ محصول تکراری را با alias/identities dedupe می‌کند.
2. اگر gap معنادار هنوز موجود است، **درخواست هدفمند Work** را در `requests/WQ0001.md` (شماره بعدی از LEDGER و خود پوشه بعد از بررسی GitHub) ثبت می‌کند: goal, exact acceptance, independent alternatives, sources, out-of-scope, negative evidence, hardware/remote locality, current free/cost/region/security gates. Write successful = readback needed.
3. **کاربر** فقط به Work می‌گوید: «در مخزن خصوصی `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` دستور `04-work-research-bridge/requests/WQ0001.md` را بخوان و طبق README همان بخش عمل کن.» آزمایش synthetic `T0001` اکنون با readback تأیید شده؛ پژوهش بعدی فقط با فایل WQ واقعی و هدف مشخص اجرا شود.
4. **Work** اصل درخواست و قوانین را **از GitHub** می‌خواند، جست‌وجوی عمیق official-source انجام می‌دهد و گزارش **کامل** `responses/WA0001.md` با شماره متناظر در همین repo ثبت می‌کند؛ بعد با بازخوانی واقعی صحت فایل را می‌سنجد؛ فقط شناسه و نتیجهٔ فشرده را در Chat می‌گوید.
5. کاربر می‌گوید «WA0001 آماده است». هماهنگ‌کننده فایل **واقعی** را fetch می‌کند، ادعاها/نسخه و negative findings را جدا بررسی می‌کند، `reviews/WQ0001.md` شامل accepted/rejected/unverified/impacts/next را می‌نویسد.
6. یافته‌های تأییدشده و مناسب وارد `03-architecture-and-tools` و/یا `05` و `02/TASK-REGISTER` می‌شوند؛ اگر **کاتالوگ عمومی/Applied** جدید لازم شد، از روال canonical Notion و مسئول مربوط ثبت شود، نه خودسرانه تغییر کتابخانه. مهم: **گزارش Work = evidence candidate، نه اجازهٔ نصب، نوشتن فایل حساس یا پذیرش معماری**.
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
- `WQ0001/WA0001` = اولین پژوهش واقعی **NOT YET CREATED**. `LEDGER.md` را برای وضعیت/شناسه ببینید.
- گزارش‌های شماره‌دار قدیمی `Q0001/A0001...` در مخزن کتابخانهٔ قبلی متعلق به این کانال جدید نیستند.

## ورودی/خروجی الگو
[قالب درخواست](templates/REQUEST-TEMPLATE.md)؛ [قالب پاسخ](templates/RESPONSE-TEMPLATE.md)؛ [قالب بازبینی](templates/REVIEW-TEMPLATE.md)؛ [دفتر اتصال](LEDGER.md).
