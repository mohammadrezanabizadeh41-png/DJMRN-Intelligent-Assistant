# نقشهٔ راه بازتعریف‌شده — Proposed P0–P6 | 2026-10-20
**وضعیت: PROPOSAL برای ترتیب اجرا؛ نه انتخاب معماری/stack.** نقشهٔ قدیمی A–G در [Notion original](https://app.notion.com/p/3fcc8c684690813a82b3d0ce909534e3) حفظ شده و تاریخچهٔ عملی آن حذف نمی‌شود.

## ترجمهٔ نقشهٔ قدیمی A–G
- A: فهرست دستگاه و نصب‌ها؛ بخش بزرگی از hardware/RAM/system و چند CLI **قبلاً مستند**؛ inventory live و کل تکمیل مدل‌ها **ناقص**.
- B: جست‌وجو، مقایسهٔ محصولات و معماری‌ها؛ **بسیاری از گزارش‌های کتابخانه/Work وجود دارند ولی هیچ winner پروژهٔ جدید تصویب نشده**.
- C: engine/model validation؛ **basic API/inference و چند خطای تاریخی واقعی** ثبت؛ benchmark منصفانهٔ full-stack انجام‌نشده.
- D: نخستین assistant؛ Jan محدود file read مشاهده شده و P1-A synthetic deterministic PASS کاربر گزارش داده؛ **دستیار عملی یکپارچه کامل نشده**.
- E: memory/search/Notion integration؛ **پیشنهاد و پژوهش، نه یک ماژول عملی پذیرفته‌شده**.
- F: specialist collaboration؛ **هنوز هیچ همکاری Agent عملی اثبات نشده**.
- G: stable daily service؛ **انجام‌نشده**.

## مسیر پیشنهادی جدید — deliverable-based
| Phase | خروجی واقعی | گیت خروج |
|---|---|---|
| **P0 — PROJECT FOUNDATION** | مخزن خصوصی با full rules, device history, model/tool inventory, source links, CURRENT, task index, Work exchange protocol | GitHub file/commit readback PASS؛ gaps برچسب دارند |
| **P1 — USE CASE & ACCEPTANCE** | تعریف یک کار کوچک واقعی با ورودی/خروجی، consent و خروجی قابل سنجش | کاربر اولویت/حدود را تأیید کند |
| **P2 — OPTIONS RESEARCH** | بر اساس Applied/General + official live + Work گزارش رقابتی same-role options و failure modes | source, license, free/cost/region/security, alternative quality مشخص |
| **P3 — IMPLEMENTATION DECISION** | حداقل stack قابل تست؛ deterministic baseline و ready product/agent/hybrid comparison؛ rollback/BOM | تصویب محدودهٔ نصب/تست، نه پذیرش کور معماری |
| **P4 — SMALLEST WORKING VERTICAL** | real I/O, correct state, bounded permissions, failure recovery, performance observation، log/metrics | آزمون واقعی روی workload مجاز، not only synthetic |
| **P5 — INCREMENTAL EXPANSION** | فقط نیازهای ثابت‌شده: knowledge, source citations, tool interfaces, specialist capabilities | هر capability جداگانه acceptance دارد |
| **P6 — DAILY OPERATION** | resource-aware lifecycle, resume/recovery, backups, maintenance and observed costs | usable/durable support + simple rollback |

Cross-cutting: امنیت، observability، cost gates و tests از P0/P1 مطرح می‌شوند؛ P6 به معنی تعویق امنیت نیست. کار پژوهش Work بخشی از P2 و حتی P4 در صورت نیاز است، نه یک پروژهٔ research بی‌پایان.

**اولین محور باز در برابر کاربر:** دقیقاً کوچک‌ترین وظیفهٔ عملی باارزش چیست؟ A resource foundation اولویت قبلی بود، اما انتخاب نصب نرم‌افزار یا ساخت controller هنوز با آزمون/approval انجام نشده است.
