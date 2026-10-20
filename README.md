# DJMRN — Intelligent Assistant System | نقطهٔ ورود پروژه

## New saved future requirement — 2026-10-21
**Many logical specialist assistant profiles on shared/on-demand models** (not many permanent Agent/model processes) was submitted in full by the user and is now an explicitly **deferred future requirement**, not a selected architecture or current build. [REQ-MPA-001](02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md) / [full original SRC-0004 (1,583 lines)](08-project-knowledge-base/inbox/SRC-0004-djmrn-multi-persona-logical-assistants-future-20261020.md) / TASK-0014. The separate [future low-RAM Live Observability Map](02-project-management/LIVE-OBSERVABILITY-MAP-REQUIREMENT.md) remains deferred as TASK-0013. **See [CURRENT-STATUS](07-operations-and-continuity/CURRENT-STATUS.md) for the latest CAP-006 Windows verified-real and UTF-8 results; earlier smoke-status notes in this README are historical.** No new vendor/agent/stack/Windows/Cloud action approved.


**Private project repository — 2026-10-20.** این مخزن «دفتر جامع قابل بازیابی» پروژهٔ احیاشدهٔ دستیار هوشمند Windows 11 است: مشخصات لپ‌تاپ، تاریخچهٔ واقعی، پژوهش، مقایسهٔ گزینه‌ها، ارتباط با Work، کدهای آینده، آزمایش‌ها، تصمیم‌ها و وضعیت ادامهٔ کار. **وجود سند به معنی نصب/اجرای قابلیت نیست.**

## اگر این اولین باری است که وارد پروژه می‌شوید
1. **ابتدا [خلاصهٔ جامع و خودبسندهٔ پروژه](07-operations-and-continuity/PROJECT-STATE-HANDOFF-20261020.md) را بخوانید؛** سپس [قواعد مستقل کار در پروژه](PROJECT-RULES.md) را بخوانید؛ برای ادامهٔ عادی نیازی به بازتعریف پروژه از گفتگو یا خواندن اجباری Notion نیست.
2. [وضعیت جاری — فقط یک CURRENT](07-operations-and-continuity/CURRENT-STATUS.md) و [راهنمای انتقال به گفتگو/دستیار جدید](07-operations-and-continuity/HANDOFF.md) را بخوانید.
3. [اهداف](02-project-management/PROJECT-CHARTER.md)، [نقشهٔ راه](02-project-management/ROADMAP.md)، [ثبت وظایف](02-project-management/TASK-REGISTER.md) و [نقشهٔ منابع](SOURCES-AND-AUTHORITY.md) را بخوانید.
4. برای دستگاه [موجودی سیستم](01-system-inventory/README.md)؛ برای پژوهش [دانشنامهٔ اختصاصی پروژه](08-project-knowledge-base/README.md) و [پروتکل Work](04-work-research-bridge/README.md)؛ برای پیاده‌سازی [دفتر اجرا](05-assistants-and-capabilities/IMPLEMENTATION-REGISTER.md)؛ برای شواهد [دفتر آزمایش](06-tests-and-evidence/TEST-REGISTER.md) را بخوانید.
5. **قبل از هر نوشتن:** وضعیت و commit واقعی GitHub را بازخوانی کنید؛ حق ایجاد فایل/تغییر تنظیمات/هزینه را از دستور جاری کاربر استنباط کنید، نه از یک گزارش.

## نقشهٔ پوشه‌ها
| بخش | کارکرد |
|---|---|
| [01-system-inventory](01-system-inventory/README.md) | سخت‌افزار، Windows، RAM، دیسک، نرم‌افزار، موتور و مدل؛ تاریخ، منشأ و میزان اطمینان |
| [02-project-management](02-project-management/README.md) | هدف‌ها، نیازمندی‌ها، نقشهٔ راه پیشنهادی، وضعیت کارها، تصمیم‌های باز |
| [03-architecture-and-tools](03-architecture-and-tools/README.md) | گزینه‌های مستقل، مقایسهٔ فناوری، منابع و معماری، هزینه و ریسک |
| [04-work-research-bridge](04-work-research-bridge/README.md) | پرسش شماره‌دار به Work، گزارش کامل Work، بازبینی و چرخهٔ نتایج |
| [05-assistants-and-capabilities](05-assistants-and-capabilities/README.md) | **CAP-006 V0:** ابزار اولیهٔ مستقل بدون Agent ساخته و فقط با دادهٔ ساختگی در محیط جداگانه آزموده شد؛ هیچ Agent/host منتخب نیست |
| [06-tests-and-evidence](06-tests-and-evidence/README.md) | آزمون‌های قدیمی/جدید، خروجی، شکست، اندازه‌گیری، صحت شواهد |
| [07-operations-and-continuity](07-operations-and-continuity/README.md) | وضعیت یکتا، ادامهٔ کار، بازیابی، ثبت تغییرات |
| [08-project-knowledge-base](08-project-knowledge-base/README.md) | **دانشنامهٔ پروژه**: منابع خام پژوهش، مدخل‌های موضوعی قابل جست‌وجو، یافته‌های معماری و ساخت، درجهٔ اعتبار و شکاف‌های دانشی |

## اطلاعات مهم
- مخزن پروژه: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant (خصوصی). مالک مرتبط در GitHub تأیید شد؛ این README منبع اطلاعات جاری پروژه است.
- **کتابخانهٔ کاربردی DJMRN** در [Notion Applied Capability Index](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f) آخرین checkpoint زندهٔ مشاهده‌شده در پژوهش قبلی **v0.48 (2026-10-20)**؛ [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) checkpoint خوانده‌شده Discovery 054 / v52. **این‌ها کاتالوگ پژوهشی هستند، نه فهرست اجبار نصب.**
- [نقشهٔ راه قدیمی A–G](https://app.notion.com/p/3fcc8c684690813a82b3d0ce909534e3) و [دفتر تاریخی Windows](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3) منابع اولیهٔ انتقال شواهد هستند؛ خلاصهٔ مستند مرتبط در خود این repo آمده است.
- مخزن مستقل [DJMRN-Research-Bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge) برای پژوهش *کتابخانهٔ کاربردی* است. **مکاتبهٔ مخصوص این پروژه فقط در بخش 04 همین repo ثبت می‌شود.**
- فارسی زبان اصلی تعامل؛ English نام فایل/شناسه/برخی اصطلاحات فنی. اطلاعات حساس و رازها هرگز در Git commit نشوند.

## وضعیت در زمان آغاز
**LATEST 2026-10-20:** تصمیم D-009 (قرارداد سبک + قابلیت قطعی نخست) با تأیید کاربر تصویب شد. [CAP-006 V0](05-assistants-and-capabilities/src/document_search_v0/README.md) ساخته و ۱۶ آزمون **فقط در محیط جداگانه و دادهٔ ساختگی** موفق بوده‌اند؛ هنوز روی Windows کاربر اجرا نشده است. [تصمیم/دلایل](02-project-management/V0-BUILD-DECISION.md)، [مقایسهٔ روش](03-architecture-and-tools/V0-TECH-CHOICE.md)، [شواهد آزمون](06-tests-and-evidence/logs/NEW-V0001-20261020.md). WQ0001/WA0001 پیش‌تر ثبت و بازبینی شده؛ هیچ Agent، موتور استنتاج یا مدیر دائمی RAM انتخاب نشده. آخرین وضعیت را از CURRENT-STATUS بخوانید.

> مسیر سریع: برای **دانش پژوهشی قابل استفاده**، 08/INDEX و 08/INTAKE-PROTOCOL؛ برای پرسیدن از Work، 04/README؛ برای فهم کارهای انجام‌شده، 07/CURRENT-STATUS؛ برای RAM، 01/hardware-baseline و resource-observations؛ برای انتخاب ابزار، PROJECT-RULES و 03.

## Latest next step — 2026-10-20
User authorized a **synthetic-only on-Windows CAP-006 smoke test** (not yet run). [Exact PowerShell guide](05-assistants-and-capabilities/src/document_search_v0/WINDOWS-SMOKE-PROTOCOL.md) and [self-contained project snapshot](07-operations-and-continuity/PROJECT-STATE-HANDOFF-20261020.md) are canonical. Original Work WQ0001/WA0001 and 10 project KB entries already persisted. No Notion library duplication or further Agent/resource manager research prerequisite.
