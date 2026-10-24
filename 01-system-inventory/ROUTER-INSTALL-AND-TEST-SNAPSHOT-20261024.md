# DJMRN — وضعیت آماری نصب و آزمون روتر مرکزی (2026-10-24)
**منبع:** گزارش‌های کاربر، مخزن GitHub و شواهد تاریخی ثبت‌شده؛ **اسکن جدید ویندوز انجام نشده است**. [START HERE کامل](../07-operations-and-continuity/ROUTER-WINDOW-RESTART-HANDOFF-20261024.md).

| گروه | شمارش/وضعیت | معنای معتبر |
|---|---|---|
| اجزای سیستم و نرم‌افزارهای گزارش‌شده تا 23 اکتبر | **21 ردیف** | [موجودی تاریخی](installed-software-snapshot-20261023.csv) شامل نصب‌شده، ناموجود و نامطمئن؛ نه 21 نصب موفق |
| رویدادهای نصب/دانلود/آزمون | **18 ردیف پس از I018** | [CSV رویدادها](installation-events.csv)، شامل FAIL و NOT_RUN؛ نه 18 نصب |
| نامزدهای روترهای SaaS/Web/Windows/GitHub | **27 مورد** | [صف مرتب](../02-project-management/ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv)، همگی نگهداری شدند |
| Maxim Bifrost v2.3.2 Windows | **REAL PROCESS STARTED; NOT OPERATIONAL** | SQLite migration PASS؛ remote datasheet timeout و exit 1 |
| Maxim Bifrost در GitHub Actions | **BOUNDED SYNTHETIC PASS** | P2C–P2F با gateway واقعی و providerهای ساختگی؛ آخرین P2F: 73/73 آزمون و 19 live mock assertions |
| OmniRoute v3.8.52 Setup | **USER_REPORTED_DOWNLOADED / INSTALL BLOCKED** | `OmniRoute.Setup.3.8.52.exe` حدود 591MiB در GUI، کد خطا/هش محلی موجود نیست |
| OmniRoute PWA | **NO READY HOSTED BACKEND VERIFIED** | PWA به server در حال اجرا نیاز دارد، landing page جای gateway نیست |
| Cloudflare AI Gateway | **NEXT_BROWSER_ACCESS_CHECK** | Login/account/Dynamic Routing not checked، بدون API |
| New API, Requesty, Portkey و بقیه | **WAITING / NOT RUN** | صف پیگیری، نه راه‌اندازی |
| اتصال واقعی Groq/Gemini از طریق روتر مرکزی | **0 verified** | سهمیهٔ واقعی/هزینه/مدل فعلی هر حساب UNKNOWN |
| دسترسی به فایل‌های شخصی | **G3B/M1 CLOSED** | مجوزی برای scan گسترده داده نشده |

### رشتهٔ شواهد تاریخ‌دار
- I015: دانلود کامل باینری Bifrost، 134305792 بایت؛ local SHA256 `430D365584D6F47CC8167AC65A747163AB6FB1ECCF666978F37B263E63C377B2`، NotSigned؛ این هش مستقلاً با چک‌سام ناشر تأیید نشده.
- I016: PE64 PASS؛ Defender custom scan command completed بدون خطای فرمان، بدون ضمانت امنیت.
- I017: اجرای واقعی native Bifrost، SQLite init PASS، remote pricing fetch timeout، exit 1.
- **I018: گزارش کاربر از دانلود و تلاش نصب Windows OmniRoute Setup 3.8.52؛ اجازهٔ اجرا/نصب نگرفته؛ خطا و digest محلی نامعلوم، NOT_INSTALLED.**

### احتیاط و ادامه
وضعیت محافظ‌های Windows Security پس از تلاش نصب OmniRoute **نامعلوم** است؛ اگر تغییری انجام شده باید محافظت بررسی و فعال بماند، بدون دورزدن هشدار. GitHub مخزن **PUBLIC** است؛ رمزها، setup token، شمارهٔ تلفن، API key و جزئیات خصوصی نباید ثبت شوند.

**گام بعدی طبق D-017:** بررسی رابط [Cloudflare AI Gateway](https://dash.cloudflare.com/) به‌صورت مرورگری، بدون فعال‌کردن سرویس پولی یا کلید؛ اگر مناسب نبود New API. تمام جزئیات در [CURRENT](../07-operations-and-continuity/CURRENT-STATUS.md) و [Handoff](../07-operations-and-continuity/ROUTER-WINDOW-RESTART-HANDOFF-20261024.md).
