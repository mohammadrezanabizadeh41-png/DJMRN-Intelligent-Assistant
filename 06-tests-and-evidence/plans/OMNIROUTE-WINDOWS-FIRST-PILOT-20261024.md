# OMNIROUTE-WINDOWS-FIRST-PILOT — برنامهٔ رسمی آزمون اولین نامزد DJMRN
**تاریخ:** 2026-10-24 | **نامزد:** https://github.com/cheaper-inference/OmniRoute | **نسخهٔ مرجع برای شروع:** https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52 | **حالت:** PLAN_READY / NOT_RUN.

## هدف و حدود
شواهد کافی برای تصمیم `PASS / FAIL / BLOCKED` دربارهٔ OmniRoute به‌عنوان **درگاه مرکزی رایگان و قابل نصب** بسازیم. نه صرفاً برنامهٔ گفت‌وگو. دستگاه: Windows 11، RAM 8GB، پردازندهٔ Ryzen 5 3500U؛ جایگزین تحت وب پذیرفته است. کاربر خواهان کمترین عملیات دستی PowerShell و قابلیت backup/restore میان دستگاه‌هاست.

## ترتیب آزمایش — هر گام فقط پس از قبولی گام قبلی
| کد | آزمون | خروجی/معیار موفقیت | وضعیت اولیه |
|---|---|---|---|
| P01 | منبع و سلامت بسته | release واقعی Windows x64، فایل `OmniRoute.Setup.3.8.52.exe`، اندازه 620348073 بایت، checksum یا امضای ناشر در صورت وجود؛ Defender بدون هشدار؛ اگر نامطمئن STOP | NOT_RUN |
| P02 | نصب GUI و قابلیت حذف/نصب مجدد | با اجازهٔ صریح کاربر نصب شود؛ از Start menu اجرا شود، بدون کنسول/اسکریپت روزمره؛ نوع دسترسی requested audit | NOT_RUN |
| P03 | ایمن‌سازی اولیه و منابع | proxy سیستم، MITM, root CA, OAuth/browser cookie harvesting, remote tunnel, startup, MCP broad tools OFF؛ loopback only. Idle RAM/CPU/time snapshot | NOT_RUN |
| P04 | یک API مرکزی | OpenAI-compatible localhost endpoint accessible from 3 independent test clients with distinct credentials or mappings; admin auth and unauthorized deny | NOT_RUN |
| P05 | تأمین‌کنندهٔ رایگان مجاز | با کلید مجاز و بدون افشای آن در چت/گیت‌هاب، مدل‌های Free از دست‌کم Groq + یک ارائه‌دهندهٔ رایگان دیگر با اعتبار حساب کاربر و مدل رسمی بررسی شود؛ **قبل از استفاده، منطقه/صورتحساب/هزینه و عدم overage واقعاً بررسی شود** | NOT_RUN |
| P06 | کشف و دسته‌بندی مدل‌ها | catalog freshness + قابلیت context/tools/quality، High/Medium/Low و خطای stale free flag جداگانه آزموده شود | NOT_RUN |
| P07 | سهمیهٔ اختصاصی دستیار | سه کلید/پروفایل: research-coding، freelance، email-background؛ محدودیت مصرف، سهمیهٔ ذخیره برای High؛ آمار + reset/limits در GUI | NOT_RUN |
| P08 | Fallback و no-paid | با mock یا provider simulation 429/503 و خاموشی تأمین‌کننده؛ خودکار جابه‌جا شود، paid/unknown/model blacklisted قبل از call DENY شود، حداقل تلاش و event logging | NOT_RUN |
| P09 | حفاظت و گزارش | privacy and log retention default, auth; هیچ secret/plain API key در GitHub یا log ارسالی نیست؛ سه دستیار واقعی فقط پس از مجوز جدا | NOT_RUN |
| P10 | بازیابی/انتقال | backup/export، restore روی پروفایل تست دیگر یا ماشین تازه، بررسی paths/keys بدون نشر credential، backup format/README documented | NOT_RUN |

## خروجی‌های اجباری هر گام
`device_test_date`, `product_version`, `source_sha_or_signature`, `status PASS/FAIL/BLOCKED/NOT_RUN`, `evidence`, `resource_cost`, `sensitive-redaction`, `acceptance_gate` و تصمیم دربارهٔ نامزد بعدی. README ادعا را runtime PASS ننام.

## توقف ایمن و راه برگشت
- قبل از دریافت Key یا تغییر system proxy/cert باید اجازهٔ مستقل کاربر باشد. اگر نصب Windows/UAC نیازمند دسترسی admin باشد، فقط پس از نمایش دلیل و تأیید.
- عدم دسترسی به اینترنت، quota سرویس‌دهنده، یا billing مبهم = BLOCKED نه وعدهٔ رایگان.
- اگر installer از منبع ناشناس/سیستم آنتی‌ویروس هشدار بدهد، SmartScreen/Defender را دور نزن.
- اگر idle RAM/CPU دستگاه مختل شود یا UI ناپایدار باشد، pause، log sanitized و پاکسازی فقط با مجوز؛ بدون خودکارسازی نصب ابزارهای دیگر.
- اگر FAIL قطعی: نتیجه در [CSV صف](../../02-project-management/ROUTER-CANDIDATE-TEST-QUEUE-20261024.csv) درج شود، سپس نامزد رتبهٔ ۲ Cloudflare AI Gateway بررسی گردد.

**پیش‌شرط عملی:** هیچ بسته‌ای توسط ChatGPT روی کامپیوتر کاربر نصب نشده و از این سند مجوز نصب خودکار نتیجه نمی‌شود. D-017 only evaluation order; D-005 globally not settled. Preserve Bifrost previous offline pricing failure and GitHub CI synthetic evidence without conflation.
