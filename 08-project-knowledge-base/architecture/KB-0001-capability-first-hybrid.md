# KB-0001 — معماری قابلیت‌محور و AI اختیاری
- **Tags/aliases:** `capability-first`, `no-agent`, `deterministic-first`, `model-on-demand`, `hybrid architecture`, `معماری قابلیت‌محور`, `Agent-when-justified`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## آنچه پژوهش مطرح می‌کند
- در بخش‌های ۱، ۲ و ۱۲، چهار سطح **برنامهٔ عادی، ML تخصصی، LLM درخواستی و Agent** مستقل/مکمل تعریف شده‌اند؛ اجرای داده/فایل/زمان‌بندی/وضعیت لزوماً به مدل نیاز ندارد. `[SRC-0001 §§1–2,12]`
- یک مسیر پیشنهادی: **رویداد/درخواست → لایهٔ سبک سیاست و وظایف → deterministic tools / ML / LLM/Agent در صورت نیاز → ثبت نتیجه/بازیابی ماندگار**؛ **پیشنهاد** است، نه implementation.
- کنترل permission و تأیید اقدامات حساس باید از تشخیص خود مدل مستقل باشد. حضور Agent در حلقهٔ پیشنهاد نباید آن را مالک مجوز کند.

## کاربرد در DJMRN
این مبنا سبب می‌شود در طراحی اولین جریان واقعی پرسش کنیم «کدام بخش بدون LLM انجام می‌شود؟» و بعد سراغ هزینهٔ RAM/Latency/Coverage برویم. جلوگیری از resident بودن چند مدل یک فرضیهٔ کم‌مصرف‌تر است، نه اندازه‌گیری ثابت‌شده.

## درجهٔ ادعا
| گزاره | نوع | شاهد |
|---|---|---|
| برنامه‌ها/پایگاه داده/زمان‌بند می‌توانند بدون LLM اجرا شوند | اصل فنی عمومی در متن؛ نیازمند تطبیق مصداق | SRC §§1–2 |
| قابلیت‌محوری برای DJMRN بهتر از Agent-first است | HYPOTHESIS / design proposal | SRC §§2,12 |
| با مدل درخواستی RAM به مقدار معینی کاهش می‌یابد | **NOT MEASURED** | SRC §8 |

## رقبا و موارد باز
Agent-ready desktop host، direct-model API، no-agent-only و hybrid workflow ممکن است براساس use case بهتر باشند. نیاز به comparative test یکسان؛ local vs online data boundaries؛ safety enforcement. 
**Related:** [KB-0003](../workflow-agents-and-control/KB-0003-architecture-families.md)، [KB-0008](KB-0008-three-build-bundles.md)، [Architecture comparison](../../03-architecture-and-tools/COMPARISON-PLAN.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
