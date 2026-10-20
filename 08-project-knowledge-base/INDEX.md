# فهرست اصلی دانشنامه — Knowledge Index
**Current:** 2026-10-20 | **9 مدخل استخراجی از 1 منبع پژوهشی واقعی** | **همهٔ 9 مورد CURATED-UNVERIFIED و هیچ معماری منتخب نیست**. این سند برای خواندن آغازین توسط دستیار/Work و پیدا کردن منابع موردنیاز است.

## جدول مدخل‌ها
| KB ID | عنوان | حوزه | Keywords/aliases | Source ID(s) | وضعیت اعتبار | مرتبط با تصمیم/تست | آخرین بازبینی |
|---|---|---|---|---|---|---|---|
| [KB-0001](architecture/KB-0001-capability-first-hybrid-architecture.md) | معماری قابلیت‌محور و AI اختیاری | architecture | capability, agent, hybrid | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0002](build-and-implementation/KB-0002-language-runtime-role-matrix.md) | زبان‌ها و Runtimeهای مستقل از هوش مصنوعی | build-and-implementation | Python, Go, C#, Rust, JS | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0003](workflow-agents-and-control/KB-0003-architecture-families.md) | هفت خانوادهٔ معماری و Workflow | workflow-agents-and-control | rule-based, modular, workflow | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0004](knowledge-search-and-memory/KB-0004-non-llm-nlp-persian.md) | NLP فارسی بدون LLM | knowledge-search-and-memory | NLP, Persian, FTS5 | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0005](knowledge-search-and-memory/KB-0005-persistent-data-source-of-truth.md) | حافظه و دادهٔ ماندگار مستقل از مدل | knowledge-search-and-memory | SQLite, DB, provenance | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0006](hardware-and-performance/KB-0006-local-memory-budget.md) | مصرف RAM و LLM درخواستی | hardware-and-performance | RAM, Job Objects, unload | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0007](tools-and-integrations/KB-0007-ready-made-workflow-products.md) | ابزارهای آمادهٔ Workflow | tools-and-integrations | Task Scheduler, n8n, Activepieces | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0008](architecture/KB-0008-three-build-bundles.md) | سه مسیر مقایسهٔ معماری | architecture | Windows-native, modular, workflow | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |
| [KB-0009](security-cost-and-operations/KB-0009-hybrid-placement-and-gates.md) | مکان‌یابی Hybrid و مجوز/هزینه | security-cost-and-operations | local, cloud, quotas | [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) | CURATED-UNVERIFIED | [P3 comparison](../03-architecture-and-tools/COMPARISON-PLAN.md), no adoption | 2026-10-20 |

## راهنمای شماره‌گذاری
- وقتی اولین متن واقعاً به GitHub وارد شد و ساختار مدخل مشخص شد، با بررسی **فایل‌های واقعی** و این Index شناسهٔ `KB-0001` ایجاد شود؛ سپس `KB-0002`...
- متن اصلی طولانی در `inbox/` با شناسهٔ منبع `SRC-####` نگهداری و لینک شود؛ هر یک از مدخل‌های موضوعی ممکن است یک یا چند `SRC` داشته باشند.
- چند نکتهٔ مستقل و قابل استفاده از یک متن می‌توانند چند KB جدا بسازند، اما آن‌ها را به یک آرشیو raw واحد وصل کنید. مدخل تکراری با alias جدید نسازید؛ اول `INDEX` و فایل‌ها را جست‌وجو کنید.
- `KB` برای **دانش**، `SRC` برای **منبع خام/مستند**، `WQ/WA` برای **تبادل Work**، `TASK` برای **کار**، `D` برای **تصمیم**، `TEST` برای **آزمون**. این شناسه‌ها مستقل هستند.

## قرارداد کلمه‌های کلیدی
برای هر مقاله 4–12 keyword فارسی/انگلیسی و alias به‌شکل دقیق اضافه کن، مثلاً `hybrid architecture`, `معماری هیبریدی`, `no-agent`, `Python`, `Windows`, `local inference`. این مثال‌ها فقط واژگان جست‌وجو هستند و مدخل/نامزد فنی واقعی ثبت‌شده محسوب نمی‌شوند.

## نحوهٔ نگهداری
ثبت ورودی و وضعیت را طبق [INTAKE-PROTOCOL](INTAKE-PROTOCOL.md) انجام دهید. در پایان هر دریافت، source register، KB entry، INDEX، relevant topic README/index، OPEN-QUESTIONS و اگر واقعاً وظیفه تغییر کرد TASK/CURRENT را با commit/readback به‌روزرسانی کنید. تاریخچهٔ قدیمی را پاک نکنید.
