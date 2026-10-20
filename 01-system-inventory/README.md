# دفتر مرجع سیستم — snapshot و آزمایش واقعی را جدا نگه دارید
این بخش تمام مشخصات شناخته‌شدهٔ لپ‌تاپ و نرم‌افزارهای قبلی را با تاریخ و provenance ثبت می‌کند. اطلاعات جدید فقط پس از مشاهدهٔ معتبر اضافه شود؛ تکرار تشخیص‌های کامل RAM/CPU/Windows قبلی الزامی نیست.

- [سخت‌افزار ثابت و نکات ارتقا](hardware-baseline.md)
- [Windows و درایورها](windows-baseline.md)
- [مشاهده‌های RAM/Commit/دیسک](resource-observations.md) — زمان‌مند
- [نرم‌افزارهای توسعه و سیستم](software-inventory.md)
- [موتورهای AI و مدل‌های محلی](models-and-engines.md)
- [ابهام‌ها و موارد نیازمند اندازه‌گیری محدود](open-verification.md)

**درج اطلاعات جدید:** فیلدهای `field | value | status | observed_at | source | context | last_review`. وضعیت‌های `USER-OBSERVED`, `TOOL-TESTED`, `OFFICIAL-SPEC`, `HISTORICAL`, `UNKNOWN`, `CONFLICT` را تفکیک کنید. هر تغییر نسخه را به تاریخ snapshot ببندید، مقدار پیشین را بدون ثبت دلیل حذف نکنید. هرگز serial شخصی یا credential ثبت نکنید. اصل شواهد تاریخی: [Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3).
