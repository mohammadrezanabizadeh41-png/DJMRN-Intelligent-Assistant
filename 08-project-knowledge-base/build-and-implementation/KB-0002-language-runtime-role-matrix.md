# KB-0002 — زبان‌ها و Runtimeهای مستقل از هوش مصنوعی
- **Tags/aliases:** `Python`, `Go`, `C#`, `.NET`, `Rust`, `Node.js`, `PowerShell`, `Deno`, `Bun`, `Windows-native`, `language selection`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## ۸ خانوادهٔ مطرح‌شده در پژوهش (§3)
| گزینه | نقش احتمالی در منبع | نکته/محدودیت ادعاشده |
|---|---|---|
| Python | پردازش متن/داده/مدل کوچک/worker | کتابخانه‌های سنگین می‌توانند RAM را بالا ببرند |
| Go | orchestration و CLI سبک | اکوسیستم NLP کوچکتر از Python |
| C# / .NET | هماهنگی و رابط Windows | Native AOT و COM/reflection باید جدا سنجیده شوند |
| Rust | جزء resource-sensitive/performance | هزینهٔ توسعه/توسعه‌دهنده بالاتر ممکن است |
| TypeScript / Node.js | API و وب/رویداد | CPU-heavy و Browser overhead مستقل هستند |
| PowerShell | وظایف سیستمی قطعی Windows | نگهداری منطق بزرگ دشوارتر ممکن است |
| Deno | TS/JS با permission scoped | permissionها OS sandbox کامل نیستند |
| Bun | JS/TS runtime با dev tooling | startup/performance ادعایی بنچمارک این لپ‌تاپ نیست |

## دامنهٔ تصمیم
**نصب‌بودن Python 3.14.7 امتیاز فنی نیست.** زبان، engine inference و مدل LLM یک انتخاب واحد نیستند. فرایند می‌تواند چندزبانه باشد ولی **چند زبان اجباری نیست**؛ ابتدا راه سادهٔ یکزبانه/برنامهٔ آماده را بسنج.

## پرسش‌های باز برای Work/official-check
Idle/process memory on Windows x64، concurrency و child-process lifecycle، API compatibility، packaging، build size، startup، Windows-specific security و هزینهٔ نگهداری. **در این منبع هیچ benchmark مشترک عددی ثبت نشده است.**
**Related:** [KB-0001](../architecture/KB-0001-capability-first-hybrid.md)، [KB-0008](../architecture/KB-0008-three-build-bundles.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
