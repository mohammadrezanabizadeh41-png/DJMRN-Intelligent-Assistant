# سرویس‌های ایجنت — DJMRN Agent Services Research 2026

**وضعیت:** RESEARCH / REFERENCE ONLY — اتصال، نصب، فعال‌سازی و معماری مصوب نیست  
**ماموریت:** DJMRN-AGENT-TOOLS-RESEARCH-001 (Discovery Expansion)  
**تاریخ snapshot:** ۱۲ نوامبر ۲۰۲۶  
**موضوع:** سرویس‌ها و ابزارهای قابل بررسی برای OpenMausBot 0.1.152 و ایجنت‌های DJMRN

## فایل‌های مرجع این مجموعه

- [DJMRN-Free-Agent-Services-2026.csv](DJMRN-Free-Agent-Services-2026.csv) — **کاتالوگ کامل ۱۵۱ سرویس در ۲۶ حوزه** با ۲۷ ستون؛ مناسب فیلتر در Excel، برنامه‌نویسی و تحلیل.
- [DJMRN-Free-Agent-Services-2026.md](DJMRN-Free-Agent-Services-2026.md) — گزارش کامل Work، جدول‌ها، دایرکتوری MCP، ابزارهای مرورگری، گزینه‌های مقایسه و محدودیت‌های منابع.

**نتیجه گزارش:** ۷۷ ردیف VERIFIED، ۶۸ ردیف PARTIALLY VERIFIED و ۶ ردیف UNVERIFIED. این برچسب‌ها به معنای تایید عرضه/منبع در سطح ذکرشده‌اند، نه تایید عملی اتصال به ایجنت، دسترسی منطقه‌ای، هزینه نهایی یا مجوز استفاده تجاری.

## نحوه جست‌وجو و استفاده

فایل CSV با **UTF-8 BOM** ذخیره شده است؛ آن را با فیلتر روی ستون‌های «حوزه»، «رده رایگان»، «سهمیه»، «کلید حساب کارت»، «هزینه اضافه»، «MCP و نوع»، «مسیر OpenMausBot»، «ایران و منطقه» و «وضعیت مدرک» بررسی کنید.

رده‌ها: F0 = عمومی و بدون کلید؛ F1 = سهمیه رایگان دوره‌ای؛ F2 = اعتبار اولیه/Trial؛ F3 = متن‌باز محلی یا self-host؛ F4 = رابط رایگان مرورگری؛ P = بدون گزینه رایگان مناسب؛ U = وضعیت نامشخص. یک سرویس ممکن است چند رده داشته باشد.

**سیاست اقدام:** هر اتصال MCP، فعال‌سازی Provider، دریافت دسترسی حساب، نصب و مصرف اعتبار باید جداگانه با منابع رسمی جاری، قیمت و quota، شرایط منطقه‌ای و حقوق داده بررسی شود؛ بدون تایید کاربر انجام نشود. UNKNOWN cost / eligibility = DENY. تا زمانی که تست عملی انجام نشده، اتصال به OpenMausBot را UNVERIFIED تلقی کنید.

## تمامیت و منشأ

دو فایل اصلی دقیقاً مطابق فایل‌های تحویلی Work/کاربر در تاریخ snapshot، بدون خلاصه‌سازی یا حذف ردیف، نگهداری شده‌اند.

| فایل | اندازه (bytes) | SHA-256 |
| --- | ---: | --- |
| DJMRN-Free-Agent-Services-2026.csv | 180000 | `f239548e43b91889a47aff39ce81fa65bf4e37c57a189d357d9d405874963d63` |
| DJMRN-Free-Agent-Services-2026.md | 65925 | `db4d7c6ddaa9aa77e78fea157d59cffa650c24149b94c960d695b1537f3b3b6e` |

این پوشه آرشیو پژوهشی موضوع «سرویس‌های ایجنت» است؛ تغییرات وضعیت اجرایی در مراجع canonical پروژه نگهداری می‌شوند. وجود این کاتالوگ به معنی نصب/تأیید استفاده از تمام ۱۵۱ گزینه نیست.

## CURRENT EXPANDED CATALOG — ChatGPT Apps / Plugins (2026-11-12)

**[MASTER catalog, 252 records](DJMRN-Agent-Services-MASTER-2026.csv)** contains 151 original Work services plus 101 newly discovered ChatGPT App/Plugin names. This is a research inventory, not installed functionality.

- [ChatGPT App/Plugin delta — 101 records](CHATGPT-APPS-DISCOVERY-2026-11-12.csv)
- [Discovery comparison and caveats](CHATGPT-APPS-DISCOVERY-2026-11-12.md)
- [Source discovery snapshot (118 app labels)](CHATGPT-PLUGIN-DISCOVERY-SNAPSHOT-2026-11-12.json)
- Original 151-row Work CSV and Markdown preserved unchanged for provenance.

118 distinct ChatGPT app/plugin names were recovered through topical directory searches plus two existing tools. 17 overlap by name; 101 added; 4 are currently NOT_AVAILABLE in the account. The search is not exhaustive. All new entries have **U/UNKNOWN-DENY** free-tier/cost/region/transport statuses until the actual provider is independently verified. ChatGPT App installation does not establish OpenMausBot compatibility or permission. No install, OAuth or spend was performed.
