# نمونه‌های تاریخی RAM، Commit، GPU و دیسک

هر مورد **snapshot** است و نباید برای مصرف لحظه‌ای آینده به کار رود.

| تاریخ/شرایط | Installed | OS visible | Available | Committed / Limit | Disk/Pagefile |
|---|---|---|---|---|---|
| 2026-10-17، نمونه هنگام اجرای برنامه‌ها | 8 GiB | ~5.9 GiB | حدود **2.29 GiB** در یک نمونه؛ پس از بستن برنامه‌ها ~**3.36 GiB** در نمونه‌ای دیگر | not standardized here | از Windows Journal |
| 2026-10-18، گزارش تجربی کاربر | 8 GiB | حدود 5.9 GiB | **معمولاً 2–3 GiB**، تا حدود 4GiB پس از بستن بعضی برنامه‌ها (تخمین کاربر) | n/a | user estimate |
| 2026-10-19، CIM مجزا | 8 GiB | **5.88 GiB** | حدود **2.0–2.1 GiB** | **4.66 / 7.50 GiB** | C: ~141.01 GiB free؛ pagefile allocated **1664 MiB**, used **35 MiB** |
| 2026-10-19، P0 پیش از P1-A | 8 GiB | 5.88 GiB | **2.24 GiB** | **5.49 / 7.50 GiB** | C: **141.85 GiB** free |
| 2026-10-19، Task Manager screenshots | 8 GiB | ~5.9 GiB | ~2.2 GiB | **4.3 / 7.5 GiB** | hardware reserved 2.1 GiB; Vega 8 dedicated preallocated 2.0 GiB |

- **RAM آزاد با Commit headroom یا اندازهٔ GGUF یکی نیست**؛ Pagefile SSD جایگزین RAM سریع نمی‌شود.
- P1-A PASS به معنی ثبت RAM اوج پردازش P1-A **نیست**؛ اوج بار/بازیابی در مدل انتخاب‌شده باید جداگانه، فقط وقتی واقعاً تست می‌شود، اندازه‌گیری شود.
- وقتی کاربر اجازهٔ benchmark محدود داد، snapshot کوتاه **قبل/حین/بعد یک workload** با CPU، RAM، commit، GPU، proc child tree و latency و منابع معتبر کافی است؛ D0 کامل تاریخی مجدد نخواهید.
- پردازش‌های سرویس‌های remote از RAM لپ‌تاپ مصرف اصلی خود را نمی‌گیرند؛ client/browser محلی هنوز هزینه دارد.

Evidence: [Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3), Windows user PowerShell logs Oct17/19 and Task Manager screenshots referenced therein. No new user-machine test for this file.
