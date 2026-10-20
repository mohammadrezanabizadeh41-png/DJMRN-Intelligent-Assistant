# برنامه‌ها و محیط توسعه — سابقهٔ واقعی، نه stack انتخاب‌شده
**Observed 2026-10-17 تا 2026-10-19 از [Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3).** نسخهٔ امروز ممکن است تغییر کرده باشد. هر سطر = product/observed version/evidence/status/known issue/selection؛ user-installed ≠ benchmark winner.

| مورد | آخرین نسخه/وضعیت مستند | محدودیت |
|---|---|---|
| Python | **3.14.7**؛ `py` و interpreter در user Windows آزمایش شده | `python` PATH در بعضی sessionها موقت بوده؛ wheel/SDK compatibility را مستقل بررسی کنید |
| pip | **26.2.1**، CLI TESTED | جزء Python، نه محصول جدا |
| venv / ensurepip | INSTALLED/TESTED | یکی از پروژه‌های تاریخی .venv واقعی دارد |
| SQLite Python module | **3.50.4**؛ DB/FTS5 synthetic smoke PASS | **نسخهٔ تاریخی**؛ نگرانی WAL-reset: قبل از WAL/concurrency نیاز به ارزیابی وصله/version |
| WinGet | **1.11.510**, TESTED | unrelated to architecture winner |
| Git for Windows | **2.55.0.windows.5**, CLI TESTED | GitHub App connection مستقل از local Git auth است |
| VS Code | INSTALLED **by user report**, version/CLI not verified | الزام پلتفرم نیست |
| Windows Task Scheduler | سرویس Running/Automatic در snapshot P0 | recovery workflow کامل هنوز انتخاب نشده |
| Research Architect v0 | پروژهٔ local historical؛ CLI init/inspect/index/search/packet و SQLite basic POC آزموده | مربوط به تجربهٔ قبلی؛ baseline اجباری برای پروژهٔ greenfield نیست |
| Node.js/npm, Docker, WSL, PowerShell7, .NET, FFmpeg, uv, build tools | **NOT VERIFIED CURRENT** | نصب را صرفاً از وجود در فهرست کتابخانه حدس نزنید |

وضعیت خودکار: `DOWNLOADED_ONLY` با `INSTALLED` و `LAUNCHED` با `FUNCTION_TESTED` و `OPERATIONAL` متفاوت است. برای هر نصب جدید، source/vendor/version/license/download/install logs, security, rollback, RAM/CPU footprint, test outcome و user approval را در 05 و 06 و این فایل ثبت کنید. هیچ نصب تازه‌ای با ایجاد این پرونده انجام نشده است.
