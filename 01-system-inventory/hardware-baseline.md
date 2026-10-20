# سخت‌افزار لپ‌تاپ — historical verified observations 2026-10-19
> این‌ها از گزارش PowerShell و تصاویر Task Manager **ارسال‌شده توسط کاربر**، و مشخصات رسمی Lenovo استخراج شده‌اند؛ اجرای زنده روی لپ‌تاپ در این مخزن اتفاق نیفتاده است. منبع تفصیلی: [Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3).

| فیلد | مقدار و سطح شاهد |
|---|---|
| سازنده و شناسهٔ خانواده | LENOVO; machine type **81W1** — user PowerShell CIM 2026-10-19 |
| مدل خانوادهٔ رسمی | **Lenovo IdeaPad 3 15ADA05** — [Lenovo PSREF رسمی](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_3_15ADA05/IdeaPad_3_15ADA05_Spec.pdf) |
| CPU | **AMD Ryzen 5 3500U** — observed |
| integrated GPU | **AMD Radeon Vega 8 Graphics** — observed |
| RAM فیزیکی نصب‌شده | **8 GiB DDR4** — 2 رکورد 4GiB در Windows CIM؛ **هر دو الزاماً سوکت قابل تعویض نیستند** |
| RAM speed | **2400 MT/s** — observed |
| توپوگرافی در راهنمای رسمی خانواده | **4GB soldered + یک SO-DIMM**؛ Lenovo configured offering تا **12GB (4+8)**، نه اثبات سازگاری هر ماژول مشخص |
| GPU memory | Task Manager: **2.0 GiB dedicated/preallocated SYSTEM memory** (0.3GiB used snapshot)، **2.9GiB shared maximum dynamic** (0 snapshot)؛ Shared دوم رزرو ثابت نیست |
| OS usable RAM | ~**5.88 GiB** از 8GiB فیزیکی — user-supplied observation؛ علت hardware reserve مرتبط با UMA بسیار محتمل، اما تفکیک کامل تمام مؤلفه‌ها قطعی نیست |
| Hardware reserved | ~**2.1 GiB** در Task Manager — observed |
| GPU driver | **31.0.21024.2004** — reported on 2026-10-19 |
| BIOS | **E8CN34WW** (reported release 2022-04-28) — observed; **امکان دستکاری UMA در BIOS برای همین واحد اثبات نشده** |

**ممنوعیت تبدیل حدس به توصیه:** تغییر BIOS، unlock مخفی، فلش‌کردن firmware، خرید RAM یا تغییر VGA preallocation بدون نیاز واقعی، منبع رسمی و تأیید کاربر انجام نشود. 8GB physical را هرگز به «6GB نصب‌شده» تقلیل ندهید. OS-usable 5.88Gb با RAM فیزیکی 8GiB تفاوت دارد.

**نکات باز:** مدل دقیق ماژول قابل تعویض و وضعیت فعلی نصب (اگر تغییری در سخت‌افزار داده شده باشد)، ظرفیت/سلامت کل دیسک، رفتار منابع هنگام موتور انتخاب‌شده. این‌ها با «UNKNOWN / VERIFY ON DEMAND» مشخص شده‌اند و مانع تشکیل پرونده نیستند.
