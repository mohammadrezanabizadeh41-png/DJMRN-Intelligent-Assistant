# KB-0006 — مصرف RAM، LLM درخواستی و مدیریت فرایندهای مالکیت‌دار
- **Tags:** `RAM budget`, `8GB`, `Ryzen 5 3500U`, `Vega 8`, `model-on-demand`, `Windows Job Objects`, `process ownership`, `pagefile`, `load/unload`.
- **Status:** CURATED-UNVERIFIED / hardware snapshots are separately dated in inventory
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## ادعاهای منبع (§8)
با عبور کارهای ساده از مسیر deterministic، مدل چندمیلیاردپارامتری بی‌دلیل بارگذاری نمی‌شود. LLM محلی ممکن است weights/KV cache/runtime resident داشته باشد؛ مدل remote RAM اصلی استنتاج روی server دارد ولی local client overhead می‌ماند. پس `LLM-on-demand` **بدون اثبات unload** لزوماً به RAM آزاد تبدیل نمی‌شود.

## دادهٔ دستگاه — از منبع و دفتر ثبت پیشین، نه اندازه‌گیری جدید
- physical installed: 8GiB؛ OS-visible در sample 2026-10-19 حدود 5.88GiB؛ historical available حدود 2–3GiB معمول.
- Windows Job Objects برای owned-process grouping مطرح شده، ولی Work orchestration, persisted job status و recovery را کامل نمی‌کند.
- پیشنهاد منبع: آغاز با حدود یک کار سنگین در هر لحظه به‌عنوان **فرضیهٔ محافظه‌کارانه**، نه اندازه‌گیری کارایی نهایی.

## معیار قابل آزمون آینده
Idle overhead coordinator/ready tool، total RAM+commit قبل/حین/بعد، peak model/worker, true memory reclaim after unload, CPU/GPU, latency, foreground browser responsiveness, subprocess owns, shutdown/crash/restart. **منبع benchmark اجرایی جدید ندارد**؛ نه مقدار saving مشخص و نه بستن اجباری Task Manager.
**Related:** [resource observations](../../01-system-inventory/resource-observations.md)؛ [Resource management comparison](../../03-architecture-and-tools/RESOURCE-MANAGEMENT.md)، [KB-0008](../architecture/KB-0008-three-build-bundles.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
