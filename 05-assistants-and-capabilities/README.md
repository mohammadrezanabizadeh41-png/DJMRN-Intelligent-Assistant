# پیاده‌سازی قابلیت‌ها — CAP-006 V0 ساخته شد؛ هنوز هیچ Agent/Host منتخب نیست
اینجا هر قابلیت پس از تعریف Use Case و approval صاحب کد/مستندات/خطای واقعی می‌شود. **ایجاد پوشه به معنی ساخت Agent نیست.**

- [دفتر قابلیت و اجرا](IMPLEMENTATION-REGISTER.md)
- [معیار نخستین vertical](FIRST-VERTICAL.md)
- [محل کد آینده](src/README.md)
- مطالعهٔ [Gates](../PROJECT-RULES.md) الزامی است.
کدهای تاریخی `Research Architect v0` یا `djmrn` بدون بررسی نیاز و مجوز migration وارد این repo نشوند. در مورد یک مدل/host/runtime به خاطر آزمایش قبلی assumption نسازید.

## نخستین زیرقابلیت واقعی (2026-10-20)
[CAP-006 document search](src/document_search_v0/README.md)؛ محدود به فقط‌خواندن فایل‌های مشخص، JSON result با نام فایل/خط/SHA256. **16 synthetic tests PASS in isolated container**, no test on user's Windows and no manager/LLM. [Approval scope](../02-project-management/V0-BUILD-DECISION.md), [test](../06-tests-and-evidence/logs/NEW-V0001-20261020.md).
