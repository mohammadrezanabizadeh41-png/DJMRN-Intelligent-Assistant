# شکاف‌های دانشی پروژه — نه درخواست Work صادرشده

- [x] **ورودی پژوهش قبلی کاربر** با شناسهٔ [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) دریافت شد؛ 607 خط به‌شکل raw ذخیره و 9 مدخل KB با اعتبار CURATED-UNVERIFIED استخراج شدند. تأیید رسمی ادعاها / آزمون Windows هنوز انجام نشده.
- [ ] معماری‌ها و مسیرهای اجرای deterministic/no-agent در برابر Agent و hybrid برای workload و حافظهٔ واقعی لپ‌تاپ دقیقاً چه تفاوت‌های اثبات‌شده‌ای دارند؟ اول متن کاربر و Applied را ببینید؛ از ابتدا دوباره Work تحقیق نخواهید.
- [ ] نقش‌های manager/resource scheduling، host، engine، model و tool adapter در گزینه‌های واقعی چگونه از هم جدا می‌شوند؟
- [ ] معیار کمترین stack برای اولین کاربرد واقعی چیست؟ در `02/PROJECT-CHARTER` و `02/REQUIREMENTS` هنوز user approval نهایی نیست.
- [ ] چه نکات ثبت‌شده‌ای به آزمون کوتاه، منبع رسمی جدید یا مقایسهٔ Work نیاز دارد، و کدام فقط دانش تاریخی است؟

**Workflow:** شکاف → inspect INDEX/SOURCE REGISTER → source اولیه Applied/General/Work/official research → if truly unresolved create bounded WQ → coordinator review → KB entry → decision/test when applicable. هیچ WQ0001 صرفاً به‌خاطر ایجاد این فایل ساخته یا به Work فرستاده نمی‌شود.

## Gapهای مشخص پس از ورود SRC-0001 (NOT A WORK REQUEST)
- [ ] تأیید رسمی نسخه/مجوز/محدودیت Windows و Free واقعی Task Scheduler/Power Automate Desktop/n8n/Activepieces/Playwright و گزینه‌های مشابه؛ مدخل [KB-0007](tools-and-integrations/KB-0007-ready-made-workflow-products.md).
- [ ] معیار مشترک برای هر سه ترکیب [KB-0008](architecture/KB-0008-three-build-bundles.md)، شامل گزینهٔ ساده‌ترِ بدون manager و معماری‌های جدیدتر (با no prior winner).
- [ ] بررسی عملی normalization/search فارسی در fixture مشترک و تفاوت FTS/BM25/ML/LLM در [KB-0004](knowledge-search-and-memory/KB-0004-non-llm-nlp-persian.md).
- [ ] idle RSS، unload واقعی/زمان راه‌اندازی و child-process ownership روی دستگاه، **فقط بعد از تعیین کار واقعی و مجوز تست**؛ [KB-0006](hardware-and-performance/KB-0006-local-memory-budget.md).
- [ ] تطبیق موجودی Applied v0.47 در زمان مشاهده و منابع رسمی تازه؛ ثبت alias/dedupe قبل از تخصیص WQ0001. 
