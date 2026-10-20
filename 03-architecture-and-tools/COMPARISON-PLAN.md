# طرح مقایسهٔ مستقل — بدون انتخاب winner
## از کاربرد به اجزا
1. وظیفهٔ واقعی و معیار قبول را تعیین کن (مثلاً خواندن مستند فارسی با cite، مدیریت process خودی، وقفه/بازیابی).
2. نقش‌ها را جدا مقایسه کن: **desktop app/GUI**؛ **agent host**؛ **inference engine**؛ **model weights/quantization**؛ **tool/skills/MCP**؛ **Windows process scheduler**؛ **durable state/retrieval**؛ **web/cloud/remote search**؛ **permissions/approval**؛ **monitoring**.
3. مسیرهای رقیب باید حداقل شامل: (0) راه کاملاً deterministic یا آماده بدون مدل؛ (1) desktop ready app + ابزار؛ (2) مدل مستقیم با code کنترل‌شده؛ (3) یک Agent با چند tool و inference قابل‌تعویض؛ (4) hybrid/free hosted؛ (5) complex multi-agent فقط اگر توجیه یافت.
4. همان نمونهٔ فارسی، منابع و failure fixtures برای گزینه‌ها؛ separate merit from installation time/sunk cost.
5. برای هر گزینه: official URL + release/version/date, Windows x64 dependency, idle/load RAM/CPU/VRAM published vs measured, Persian quality, task correctness, provenance, license, privacy, cost/free/quota/card/overage, Iran eligibility, portability, security, failure recovery and rollback. برنده UNKNOWN تا مقایسه.
6. مصرف RAM لپ‌تاپ را فقط برای جزء local محاسبه کن؛ محاسبات دوردست مستقل است. overage/region UNKNOWN = deny activating remote candidate ولی نگهداری در research catalog مجاز.
7. هر نتیجهٔ Work باید مستقل بررسی و به source اصلی وصل شود؛ ساخت Agent/DB/service خودکار نتیجهٔ پژوهش نیست.

## نمونهٔ سناریوهای آزمون
- ورودی فارسی → جست‌وجوی محدود فایل مجاز → cite filename/line/version → پیشنهاد بدون ویرایش؛ 
- دو پیام مشابه → idempotent/duplicate receipt → restart recovery؛
- درخواست خطرناکِ برگرفته از وب/ایمیل → نادیده‌گرفتن instruction untrusted و approval prompt؛
- RAM under normal foreground work → مدل load/unload → کنترل safe own child processes بدون kill فرایند سیستم؛
- سرویس free API unavailable/limit hit → degrade gracefully به local/قابلیت deterministic، نه paid overage.

**انتخاب فناوری در این repo هنوز NONE است**. جدول نامزدها مرحله به مرحله در CANDIDATE-REGISTER تکمیل می‌شود.
