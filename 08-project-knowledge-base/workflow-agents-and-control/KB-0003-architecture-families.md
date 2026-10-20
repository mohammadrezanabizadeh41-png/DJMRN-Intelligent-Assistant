# KB-0003 — هفت خانوادهٔ معماری از Rule-Based تا Agent Worker
- **Tags:** `rule-based`, `data-centric`, `modular monolith`, `event-driven`, `classical ML`, `LLM-on-demand`, `agent worker`, `workflow`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## طبقه‌بندی دقیق منبع (§4)
- **A — Rule-Based Automation:** رویداد → شرط ثابت → عمل ثابت؛ بدون نیاز ذاتی LLM.
- **B — Data-Centric/Database-First:** داده/سوابق مرکزی، مدل فقط ابزار تحلیل اختیاری.
- **C — Modular Monolith/Capability-Based:** قابلیت‌های جدا و قراردادهای روشن در یک برنامه؛ سرویس مستقل فقط در صورت اثبات نیاز.
- **D — Event-Driven/Workflow:** رویداد آغازگر؛ state/retry/recovery باید مستقل طراحی/از محصول آماده تأمین شود.
- **E — Classical ML + Deterministic:** مدل طبقه‌بندی کوچک و controller عادی بدون chatbot.
- **F — Hybrid AI/LLM-on-Demand:** مسیر عادی deterministic؛ در ابهام از local/remote LLM درخواست؛ structured output validate.
- **G — Agent as Supervisor/Worker:** نقش محدود Agent؛ policy/approval خارج از prompt.

**مهم:** این A–G **طبقه‌بندی معماری داخل منبع** است و با **A–G تاریخی نقشه راه ویندوز پروژه** یکسان نیست؛ شناسهٔ آن‌ها را اشتباه نگیرید.

## فرضیهٔ ترکیبی
B + C + D + F در متن یک ترکیب ممکن معرفی شده، نه برنده. حتی B+C+D+F می‌تواند برای نخستین نیاز over-engineering باشد. باید حداقل معماری هم‌سطح نیاز را با ready products مقایسه کرد.

## مسیر اعتبارسنجی
برای یک event یکسان: شروع/توقف، ذخیره state، duplicate/retry, approval boundary، cold-start RAM، نتیجهٔ واقعی. Work لازم نیست همه گزینه‌ها را «منتخب» بنامد.
**Related:** [KB-0001](../architecture/KB-0001-capability-first-hybrid.md)، [KB-0008](../architecture/KB-0008-three-build-bundles.md)، [KB-0006](../hardware-and-performance/KB-0006-local-memory-budget.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
