# منابع، حقیقت مرجع و نقشهٔ بازیابی

## نقشهٔ مالکیت
| داده/تصمیم | صاحب مرجع | نقش این مخزن |
|---|---|---|
| فایل‌ها، source، commit، PR، CI و کد پروژهٔ جدید | **همین GitHub repo** | AUTHORITATIVE |
| وضعیت پروژه، دفتر وظیفه، تبادل Work و آزمایش پروژه | **همین GitHub repo** | AUTHORITATIVE با ارجاع به evidence |
| اطلاعات سخت‌افزاری واقعی | خروجی تاریخ‌دار خود دستگاه / مدارک سازنده | GitHub = دفتر ثبت evidence با منشأ |
| سیاست بین‌پروژه‌ای و تصمیم معماری سراسری | [Notion Operating Memory](https://app.notion.com/p/3edc8c684690814a9707cb880534f462) و [Governance](https://app.notion.com/p/3edc8c68469081cc90abdd5183f1bdb1) | snapshot کارکردی در PROJECT-RULES؛ همگام‌سازی تغییرات معنادار |
| فهرست ابزار و فناوری عمومی | [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) | صرفاً index + link؛ کپی کل کتابخانه ممنوع |
| کتابخانهٔ تخصصی کاربردی | [Applied Capability Index](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f) و [Mission](https://app.notion.com/p/3fdc8c6846908167a77feab9564dc66d) | هنگام تصمیم روی قابلیت بخوان؛ نسخه و منبع در گزارش بیاور |
| سوابق قدیمی نصب/تست | [Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3) | سند تاریخ‌دار منتخب در 01 و 06؛ هیچ run تازه‌ای ادعا نشود |
| گزارش‌های طولانی پژوهش Applied | [DJMRN-Research-Bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge) | زمینهٔ قبلی/مرجع مستقل؛ در پروژهٔ جدید بازنویسی نکن |
| گزارش‌های پژوهش مخصوص این پروژه | 04-work-research-bridge همین مخزن | PRIMARY for project requests/reports |
| **دانش قابل استفادهٔ استخراج‌شده برای تصمیم/ساخت همین پروژه** | [08-project-knowledge-base](08-project-knowledge-base/README.md) | INDEX + source metadata + source-backed KB entry؛ بدون تکرار ناخواستهٔ متن اصلی |
| پایگاه دادهٔ عملیاتی/اجرای تولید | **هنوز انتخاب نشده** | DON’T INVENT |

## نسخه‌های خوانده‌شده در 2026-10-20
- Applied Capability Index: **v0.47**؛ آخرین گزارش ثبت‌شده و بازبینی‌شده در Index: **A0011** با receipt `PERSISTENCE-VERIFIED-APPLIED004-BRIDGEQ0011-V047`. اگر گزارشی جدید خارج از Index (مثلاً A0012) مطرح شد، بدون خواندن واقعی GitHub/ثبت بازبینی وضعیت را ارتقا ندهید.
- General Discovery: **Discovery054 / CURRENT v52** (فقط checkpoint تاریخی مشاهده‌شده).
- Windows Roadmap قدیمی A–G: HISTORY retained؛ P0–P6 این مخزن **پیشنهاد بازتعریف** است نه ابلاغ انتخاب پلتفرم.
- لینک‌های Notion ممکن است اطلاعات تازه‌تر داشته باشند؛ در تصمیم مهم همیشه recency و supersession را reconcile کنید.

## مسیر بازخوانی
1. README و PROJECT-RULES و CURRENT-STATUS همین repo؛ 
2. [08/INDEX دانشنامه](08-project-knowledge-base/INDEX.md) و فایل موضوعی سیستم/وظیفه/تست؛
3. اسناد منبع اصلی (Notion/رسمی vendor) **در صورت پژوهش یا تغییر اثرگذار**؛
4. بازگشت به گزارش/شواهد دقیق و ثبت تصمیم/نسخه.
هدف repo **قابل بازیابی‌بودن مستقل از حافظهٔ چت** است، نه تبدیل شدن به یک کپی دائم و ناسازگار از همه منابع.

## منابع خارجی canonical نمونه
- [Lenovo official PSREF IdeaPad 3 15ADA05](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_3_15ADA05/IdeaPad_3_15ADA05_Spec.pdf)
- [GitHub REST Git tree](https://docs.github.com/en/rest/git/trees) / [README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- قیمت، quota، نسخه و حقوق استفاده از سرویس‌ها باید برای **زمان تصمیم** از docs رسمی‌شان جداگانه کنترل شود؛ هیچ جدول قیمت تاریخی را فعال‌سازی مجاز فرض نکنید.

## قطعی‌کردن هویت مخزن در Work — D-010 (2026-10-20)
برای هر WQ/WA پروژه فقط `repository_full_name: mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` و URL https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant در branch `main` مقصد مجاز است. مخزن `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` می‌تواند **به‌عنوان منبع پژوهش خوانده شود ولی اجازهٔ نوشتن پاسخ این پروژه را ندارد**. باید metadata واقعی repo قبل از نوشتن و URL/path/commit/blob بعد از نوشتن طبق [REPOSITORY-LOCK](04-work-research-bridge/REPOSITORY-LOCK.md) سنجیده شود. نام نسبی مسیر فایل بدون exact full_name کافی نیست.
