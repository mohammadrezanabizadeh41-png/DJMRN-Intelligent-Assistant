# DJMRN — Intelligent Assistant System | نقطهٔ ورود پروژه

**Private project repository — 2026-10-20.** این مخزن «دفتر جامع قابل بازیابی» پروژهٔ احیاشدهٔ دستیار هوشمند Windows 11 است: مشخصات لپ‌تاپ، تاریخچهٔ واقعی، پژوهش، مقایسهٔ گزینه‌ها، ارتباط با Work، کدهای آینده، آزمایش‌ها، تصمیم‌ها و وضعیت ادامهٔ کار. **وجود سند به معنی نصب/اجرای قابلیت نیست.**

## اگر این اولین باری است که وارد پروژه می‌شوید
1. [قواعد مستقل کار در پروژه](PROJECT-RULES.md) را بخوانید؛ برای ادامهٔ عادی نیازی به بازتعریف پروژه از گفتگو یا خواندن اجباری Notion نیست.
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
| [05-assistants-and-capabilities](05-assistants-and-capabilities/README.md) | طراحی و بعداً کد/قابلیت عملی؛ فعلاً هیچ پلتفرمی تصویب نشده |
| [06-tests-and-evidence](06-tests-and-evidence/README.md) | آزمون‌های قدیمی/جدید، خروجی، شکست، اندازه‌گیری، صحت شواهد |
| [07-operations-and-continuity](07-operations-and-continuity/README.md) | وضعیت یکتا، ادامهٔ کار، بازیابی، ثبت تغییرات |
| [08-project-knowledge-base](08-project-knowledge-base/README.md) | **دانشنامهٔ پروژه**: منابع خام پژوهش، مدخل‌های موضوعی قابل جست‌وجو، یافته‌های معماری و ساخت، درجهٔ اعتبار و شکاف‌های دانشی |

## اطلاعات مهم
- مخزن پروژه: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant (خصوصی). مالک مرتبط در GitHub تأیید شد؛ این README منبع اطلاعات جاری پروژه است.
- **کتابخانهٔ کاربردی DJMRN** در [Notion Applied Capability Index](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f) آخرین checkpoint خوانده‌شده **v0.47 (2026-10-20)**؛ [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) checkpoint خوانده‌شده Discovery 054 / v52. **این‌ها کاتالوگ پژوهشی هستند، نه فهرست اجبار نصب.**
- [نقشهٔ راه قدیمی A–G](https://app.notion.com/p/3fcc8c684690813a82b3d0ce909534e3) و [دفتر تاریخی Windows](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3) منابع اولیهٔ انتقال شواهد هستند؛ خلاصهٔ مستند مرتبط در خود این repo آمده است.
- مخزن مستقل [DJMRN-Research-Bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge) برای پژوهش *کتابخانهٔ کاربردی* است. **مکاتبهٔ مخصوص این پروژه فقط در بخش 04 همین repo ثبت می‌شود.**
- فارسی زبان اصلی تعامل؛ English نام فایل/شناسه/برخی اصطلاحات فنی. اطلاعات حساس و رازها هرگز در Git commit نشوند.

## وضعیت در زمان آغاز
**INIT / REPOSITORY DOCUMENTATION ONLY:** اطلاعات تاریخی وارد سند شده؛ یک معماری فنی/عامل/مدل/host انتخاب یا روی لپ‌تاپ نصب نشده است. T0001 **PASS** — [پاسخ واقعی Work](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/04-work-research-bridge/responses/T0001.md), [commit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/d70a9a406a7057a7b40e11ad99e70d2574536e5c), blob `8094f76e732305fcc8d22a48639cb0e347325874` با بازخوانی مستقل تأیید شد؛ پژوهش واقعی `WQ0001` هنوز ایجاد نشده. رویدادهای تازه فقط پس از شواهد در CURRENT-STATUS ثبت شوند.

> مسیر سریع: برای **دانش پژوهشی قابل استفاده**، 08/INDEX و 08/INTAKE-PROTOCOL؛ برای پرسیدن از Work، 04/README؛ برای فهم کارهای انجام‌شده، 07/CURRENT-STATUS؛ برای RAM، 01/hardware-baseline و resource-observations؛ برای انتخاب ابزار، PROJECT-RULES و 03.
