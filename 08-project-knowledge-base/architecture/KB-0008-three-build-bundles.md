# KB-0008 — سه مسیر مقایسهٔ عملی معماری DJMRN
- **Tags:** `Windows-native`, `modular-core`, `workflow-first`, `hybrid`, `lightweight manager`, `comparative test`, `resource-aware`.
- **Status:** CURATED-UNVERIFIED / EXPERIMENT PROPOSAL
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## سه بستهٔ پیشنهادی منبع (§10)
| بسته | ترکیب احتمالی (نه installation list) | قوت مورد ادعا | نقطهٔ ریسک |
|---|---|---|---|
| **1. Windows Native** | Task Scheduler + PowerShell/C# + فایل/DB سبک + مدل اختیاری | dependency کمتر، قابلیت بومی | integration/NLP پیچیده‌تر نیاز به افزونه |
| **2. Lightweight Modular Core** | Python **یا** Go **یا** C# + files/SQLite + workers on demand + مدل اختیاری | state/permissions کنترل‌پذیر | نوشتن و نگهداری کد اختصاصی |
| **3. Workflow-First Hybrid** | n8n / Activepieces یا مشابه + ابزارهای آماده + LLM درخواستی | مراحل قابل مشاهده و connectorهای متعدد | هزینهٔ RAM/background/License/hosting |

## fixture مشترک برای مقایسه
یک event مجاز و غیرحساس → ingest + dedup → extraction → durable state → pause on low RAM → restart resume → optional LLM analysis → output human-approved و log. 
Metricهای مورد نیاز: real peak RAM/commit و reclaim، cold-start، throughput/latency، کیفیت فارسی، context/runtime, failed-job recovery, install/storage, security, real-free constraints و effort.

## تحفظ مهم
این **فهرست سه‌گانهٔ پژوهش قبلی** است. «سه تنها انتخاب جهان» نیست؛ معماری آمادهٔ دسکتاپ، برنامهٔ deterministic بدون manager و cloud-hosted valid alternatives نیز باید هم‌سطح بررسی شوند. ترکیب چند زبان/سرویس را پیشاپیش لازم فرض نکن.
**Related:** [KB-0001](KB-0001-capability-first-hybrid.md)، [KB-0002](../build-and-implementation/KB-0002-language-runtime-role-matrix.md)، [comparison plan](../../03-architecture-and-tools/COMPARISON-PLAN.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
