# ویندوز و محیط پایه

| مورد | آخرین مشاهده / توضیح |
|---|---|
| سیستم‌عامل | **Windows 11 Pro** — user PowerShell P0 report 2026-10-19 |
| Build | **26300** — گزارش 2026-10-19؛ UBR/به‌روزرسانی فعلی در 2026-10-20 **UNKNOWN** |
| Windows PowerShell | اجرای CIM و دستورهای قبلی موفق؛ نسخهٔ دقیق جاری ثبت نشده |
| Task Scheduler | `Running / Automatic` در نمونهٔ P0 2026-10-19، نه تضمین امروز |
| Pagefile | `AutomaticManagedPagefile=True` در 2026-10-19، Allocation حدود 1664 MiB؛ System Managed را بدون تست و approval دستکاری نکنید |
| API محلی Jan Desktop | در یک تست قبلی `127.0.0.1:1337/v1` پاسخ GET catalog داشته؛ **اکنون running ثابت نشده** |
| Storage | تنها free C: در نمونه‌ها ~141 GiB ثبت شده؛ total/SSD health/other volumes در این snapshot کامل **UNKNOWN** |
| Git | `2.55.0.windows.5` در 2026-10-17 CLI tested، نه الزام stack |
| WinGet | `1.11.510` verified at historical test |
| VS Code | کاربر نصب را 2026-10-17 گزارش کرده؛ version/CLI status UNKNOWN |

**تاریخ و منبع:** [دفتر نصب Windows](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3)؛ داده‌های پروفایل سیستم از user-executed commands است. ثبت username/path دقیق خانگی، سریال، Device ID و فایل شخصی در GitHub لازم نیست. تغییرات Windows فقط با اجازهٔ روشن و ثبت rollback انجام شود.
