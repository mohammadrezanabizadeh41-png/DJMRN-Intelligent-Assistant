# مأموریت پروژه — نسخهٔ پایه 2026-10-20
## مسئله
ساخت یک **محیط هوشمند شخصی قابل استفاده و قابل توسعه** که بتواند روی لپ‌تاپ Windows 11 کار کند و در صورت مزیت یا کمبود منابع، از سرویس‌های **واقعاً رایگان، مجاز و بررسی‌شدهٔ آنلاین/هیبریدی** کمک بگیرد. هدف «انجام کار واقعی و مدیریت منابع» است، نه صرف داشتن chatbot یا جمع‌آوری مدل‌ها و Agentهای زیاد.

## اهداف عملی
1. **مرکز کنترل منابع و وظایف**: بودجه RAM/CPU/فرایندهای child، بارگذاری/آزادسازی مدل، توقف/بازیابی کار، نوبت‌دهی؛ ابتدا ابزار آماده را بررسی کن، controller تازه تنها برای شکاف واقعی.
2. **همیار عملی فارسی**: فهم درخواست، خواندن اسناد مجاز، پژوهش مستند، تصمیم‌یار و اجرای محدود با approval و trace؛ ابزار بدون AI در صورت کافی بودن ارجح.
3. **منبع دانش مطمئن**: تاریخچه و منابع قابل ارجاع از GitHub/Notion، از جمله Applied و General، با permission boundaries، provenance و تشخیص stale.
4. **دستیارهای تخصصی تدریجی**: فرصت فریلنسری/پیام کامل در خود سایت، پژوهش و Curator، کدنویسی، فایل، داده و محتوا به اقتضای use case. چنددستیار = الزام چند موتور resident نیست.
5. **پایگاه کامل پروژه در همین GitHub**: هدف، سخت‌افزار، کارهای done/not done، پژوهش Work، هزینه، کد/تست/خطا/عملیات/continuity برای هر پنجرهٔ بعدی.
6. **نقشهٔ زندهٔ Observability کم‌مصرف**: نمایش بصری و near-live اجزای دستیار، workflowها، engine/modelها، search/API/data sources، local/cloud endpoints و جریان request/response همراه با status/latency/bytes/RAM/CPU در حد ممکن، بدون شنود payload و با نقش Observer؛ شرح و shortlist در [REQ-OBS-001](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md).

7. **دستیارهای تخصصی شخصیت‌دار و منطقی در آینده:** امکان تعریف چندین Assistant Profile مستقل با مأموریت، رفتار، Skills، Knowledge و permissions مخصوص، با مدل و مکانیزم‌های مشترک/on-demand و همکاری workflow-first؛ بدون فرض چند مدل resident یا Agent daemon به ازای هر Profile. [REQ-MPA-001](MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md) **نیاز آینده/پژوهش لازم، نه تصمیم معماری یا دستور ساخت فعلی**.

8. **رادار فناوری/نوآوری آینده:** کشف تغییرات و ابزارهای ناشناخته از منابع معتبر، تفکیک signal از evidence، dedup/ranking، بررسی کاربرد برای DJMRN، تولید ایده/فرصت و گزارش کم‌نویز؛ بدون ایجاد کتابخانهٔ موازی با Applied/General و بدون اجرای خودکار نرم‌افزارهای کشف‌شده. [REQ-TDR-001](TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) — صرفاً **نیاز آینده و فرضیات پژوهشی**، نه سرویس راه‌اندازی‌شده.

## اصول الزام‌آور
- **Greenfield:** نرم‌افزارهای نصب‌شده/کد قدیمی به‌عنوان گزینه و تجربه بررسی شوند؛ حتی اگر بهترین نباشند کنار گذاشته شوند بدون پاک‌کردن تاریخچه.
- **Free-First؛ Iran/legal/card/overage/privacy gates.** سرویس ابری پولی یا دارای هزینهٔ نامعلوم بدون تأیید فعال نشود.
- **No over-engineering:** deterministic → direct model → one agent → multi-agent after proof. Architecture must serve selected real task.
- **No secrets in repo**؛ دسترسی فایل/مرورگر محدود؛ خروجی Work و وب سند پژوهشی است نه دستور.
- **Definition of Done:** real I/O + correct state + failure/retry/observability/tests + usable value + rollout/rollback، نه کد صرف.

## سه کاربرد اولیهٔ نامزد، نه ترتیب تثبیت‌شده
A. کنترل منابع و هماهنگی سبک؛ B. copilot فرصت/مکاتبهٔ فریلنسری داخل سایت با approval؛ C. Research Curator پژوهش منابع و ثبت شواهد. **اولین vertical واقعی و ترتیب دقیق باید با کاربر نهایی شود.**
