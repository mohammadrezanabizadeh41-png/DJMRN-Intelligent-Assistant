# KB-0009 — مکان‌یابی مستقل کارها و دروازه‌های هزینه/امنیت
- **Tags:** `local-vs-remote`, `hybrid placement`, `offline`, `Iran eligibility`, `free-tier`, `quota`, `privacy`, `approval`, `cloud execution`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## چارچوب منبع (§§7,11)
- ذخیرهٔ اصلی و status/recovery می‌تواند local باشد و مدل online اختیاری. پردازش پرونده/جست‌وجو/طبقه‌بندی هم بسته به latency/cost/confidentiality محل متفاوت دارند.
- لپ‌تاپِ خاموش **محل اجرای task نیست**؛ زمان‌بندی در خاموشی نیازمند runtime بیرونی/زمان‌بندی remote و مقررات خودش است.
- دریافت اعلان فرصت کاری → dedupe → بررسی منبع اصلی → extraction → فراخوانی اختیاری LLM → **approval انسانی برای ارسال/نوشتن خارجی** → receipt/state؛ نمودار منبع صرفاً مفهوم است، هیچ اتصال واقعی ساخته نشده.
- سرویس remote جدا از footprint local ارزیابی شود؛ privacy/security, legal/region, actual free quota/card, overage و commercial terms قبل از activation بررسی شوند.

## ارزیابی اعتبار
سازگاری حقوقی/ایران/قیمت/برنامهٔ Free هیچ provider خاص در سند مستقل verify نشده؛ **UNKNOWN / HOLD** برای انتخاب اجرایی. فرآیند خارجی مانند reply/mail/website posting بدون مجوز صریح ممنوع.
**Related:** [KB-0003](../workflow-agents-and-control/KB-0003-architecture-families.md)، [KB-0008](../architecture/KB-0008-three-build-bundles.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
