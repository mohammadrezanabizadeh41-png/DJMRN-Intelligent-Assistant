# KB-0007 — پیش از ساخت اختصاصی، ابزارهای آمادهٔ Workflow را بررسی کن
- **Tags:** `Task Scheduler`, `Power Automate Desktop`, `n8n`, `Activepieces`, `Playwright`, `ONNX Runtime`, `ready-made`, `workflow`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## نامزدها و نقش ادعاشده (§9)
- Windows Task Scheduler: شروع کار با زمان/event؛ state business چندمرحله‌ای مستقل.
- Power Automate Desktop: RPA محلی با حضور کاربر؛ **unattended licensing and resource requirements** در متن ادعا شده و برای تصمیم باید مستند رسمی نسخهٔ روز بررسی شود.
- n8n: workflow integrations؛ خودمیزبان Community و محدودیت Sustainable Use License طبق متن؛ **free ≠ open-source unrestricted**.
- Activepieces: self-host low-code؛ متن از MIT برای core و تفکیک enterprise/cloud یاد می‌کند؛ release/license/feature امروز نیازمند تأیید.
- Playwright: browser automation در سناریوی مجاز؛ browser RAM footprint مستقل.
- ONNX Runtime: مدل ML بدون Agent؛ وزن مدل و task quality جداگانه.

## معیار اصلی پژوهش
در برابر minimal script + Task Scheduler، هزینهٔ نصب/idle RAM/ports/background services, account permissions, recovery state, retry/idempotency, license/commercial terms, free quota/card/overage/Iran/legal و نگهداری هر محصول را در همان کاربرد واقعی بسنجید.

**هیچ‌کدام از سرویس‌ها روی laptop جدید نصب/فعال نشده‌اند و هیچ قیمت/قانونی از این منبع به‌عنوان وضعیت کنونی تأیید نشده است.**
**Related:** [KB-0008](../architecture/KB-0008-three-build-bundles.md)، [KB-0002](../build-and-implementation/KB-0002-language-runtime-role-matrix.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
