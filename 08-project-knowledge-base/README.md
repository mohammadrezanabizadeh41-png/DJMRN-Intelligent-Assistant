# DJMRN — دانشنامهٔ اختصاصی پروژه | Project Knowledge Base

**وضعیت: 1 منبع پژوهش قبلی کاربر با [SRC-0001](inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) وارد شده و 9 مدخل KB استخراج شده — 2026-10-20. همهٔ مدخل‌ها CURATED-UNVERIFIED هستند.** این پوشه پایگاه دانش **اختصاصی همین پروژه** است: یافته‌های قابل بازیابی از کتابخانهٔ کاربردی، کتابخانهٔ عمومی، منابع رسمی، پژوهش‌های مستقل، پاسخ‌های Work و تجربهٔ آزمایش/پیاده‌سازی. هدف: تبدیل پژوهش قابل استناد به **اطلاعات قابل استفاده هنگام تصمیم و ساخت**، نه کپی‌کردن بی‌نظم متن‌ها یا انتخاب زودهنگام فناوری.

## نقش دانشنامه در معماری مستندات
- `01-system-inventory/`: واقعیت‌های تاریخی/اندازه‌گیری دستگاه و نرم‌افزار؛ **مرجع مشاهده**.
- `03-architecture-and-tools/`: **گزینه‌های قابل مقایسه و تصمیم فنی در حال بررسی**؛ موضوعات پژوهشی از دانشنامه قابل استفاده می‌شوند.
- `04-work-research-bridge/`: **اصل درخواست/پاسخ/بازبینی Work**، بدون حذف و خلاصه‌سازی دلخواه؛ تنها هماهنگ‌کننده مدخل‌های دانشنامه را پس از بررسی می‌نویسد.
- **`08-project-knowledge-base/`**: **دانش استخراج‌شده، قواعد، الگوها، نکات فنی، محدودیت‌ها، مطالعات موردی و لینک به اصل منبع**؛ هر مدخل مستقل، دارای کلیدواژه و قابل ردگیری.
- `02-project-management/DECISION-REGISTER.md`: تصمیم‌های واقعی و تأییدشده؛ «مقالهٔ دانشی» یا گزارش Work به تنهایی مجوز/تصمیم نیست.
- `05...` کد و پیاده‌سازی واقعی؛ `06...` نتیجهٔ تست واقعی. دانشنامه جایگزین شواهد آزمون یا کد نیست.

## شروع
1. [INDEX.md](INDEX.md): **فهرست اصلی قابل جست‌وجو** و وضعیت مدخل‌ها؛ ابتدا این فایل را ببینید.
2. [INTAKE-PROTOCOL.md](INTAKE-PROTOCOL.md): نحوهٔ دریافت متن کاربر/Notion/Work/وب، ثبت اصل منبع، بررسی و استخراج.
3. [SOURCE-REGISTER.md](SOURCE-REGISTER.md): ثبت منشأ منابع بدون ادعای تأیید محتوای آن‌ها.
4. [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md): شکاف‌های دانشی و اولویت‌های پژوهش.
5. [templates/ENTRY-TEMPLATE.md](templates/ENTRY-TEMPLATE.md) و [templates/RAW-RESEARCH-TEMPLATE.md](templates/RAW-RESEARCH-TEMPLATE.md): قالب‌های یکسان برای دریافت متن کامل و ثبت نتیجهٔ تحلیلی.

## حوزه‌ها
| محل | پوشش |
|---|---|
| [architecture/](architecture/README.md) | معماری مستقل/هیبریدی، مرزبندی مؤلفه‌ها، مقایسهٔ topology |
| [build-and-implementation/](build-and-implementation/README.md) | طراحی، ساخت، ابزار ساخت، توسعه و تحویل |
| [hardware-and-performance/](hardware-and-performance/README.md) | ظرفیت RAM/GPU، صف‌بندی، بنچمارک و مدل مصرف |
| [models-engines-and-hosts/](models-engines-and-hosts/README.md) | تفکیک مدل/engine/host/Agent و قابلیت‌های runtime |
| [tools-and-integrations/](tools-and-integrations/README.md) | قابلیت ابزار، MCP، Skills، API، سرویس‌های آنلاین/آفلاین |
| [knowledge-search-and-memory/](knowledge-search-and-memory/README.md) | جست‌وجو، OCR/parse، حافظه، FTS/RAG، provenance |
| [workflow-agents-and-control/](workflow-agents-and-control/README.md) | agent و non-agent، مدیریت وظایف، approval، recovery |
| [security-cost-and-operations/](security-cost-and-operations/README.md) | مجوز، محدودیت قانونی/ایران، هزینه، quota، نگهداری |
| [inbox/](inbox/README.md) | آرشیو متن خام دریافتی، صرفاً پس از sanitize و حفظ منشأ |

**یک نکته:** ممکن است یک مدخل در چند موضوع کاربرد داشته باشد. **فایل محتوایی را فقط یک جا بسازید** و در سایر موضوعات لینک بدهید، نه چند نسخهٔ قابل واگرایی.

## سیاست کیفیت و بی‌طرفی
- پژوهش‌های پیشین یا نصب‌بودن یک ابزار **دستور معماری نیستند**؛ گزینهٔ ساده‌تر، جدیدتر یا آماده را مستقل مقایسه کنید.
- `RAW-RECEIVED`, `CURATED-UNVERIFIED`, `SOURCE-CHECKED`, `TEST-SUPPORTED`, `APPROVED-FOR-REFERENCE`, `SUPERSEDED` وضعیت‌های دانش‌اند، نه وضعیت اجرا. مدخل با `APPROVED-FOR-REFERENCE` هم به معنی انتخاب نرم‌افزار یا مجوز اجرا **نیست**.
- `FACT`، `AUTHOR-CLAIM`، `INTERPRETATION`، `HYPOTHESIS`، `UNKNOWN` تفکیک شوند. نسخه/هزینه/سازگاری زمان‌مندند؛ منبع رسمی روز هنگام تصمیم دوباره چک شود.
- هر مدخل باید **KB-####**، عنوان فارسی و نام‌های انگلیسی/alias، tags/keywords، زمان مشاهده، منبع دقیق (GitHub/Notion/URL/Work ID)، کاربرد برای DJMRN، مزایا/معایب، دامنهٔ اعتماد، سؤال باز، ارتباط با تصمیم/تست و زمان بازبینی داشته باشد.
- اطلاعات حساس، کلید/توکن، مشخصات هویتی/مشتری یا مسیر خصوصی سیستم را هرگز commit نکنید؛ متن خام نیز قبل از ثبت بررسی شود.
- کل متن کتابخانهٔ Applied/General را بی‌هدف کپی نکنید؛ **ارجاعِ نسخه‌دار + برداشت کاربردی پروژه** در مدخل کافی است. متن پژوهش ارسالی کاربر که مجاز و مناسب است به صورت raw با منشأ نگهداری شود.

## جست‌وجو
- فهرست [INDEX](INDEX.md) کلید اصلی کشف، ID/Tag/alias/keyword است؛ برای تصمیم‌های مهم `OPEN-QUESTIONS` را نیز بررسی کن.
- می‌توان از جست‌وجوی فایل GitHub در این repo یا جست‌وجو در کپی محلی استفاده کرد؛ اینکه private code search برای حساب فعال باشد **تضمین نشده**. نام‌گذاری و ایندکس مستقل از سرویس جست‌وجوی خارجی طراحی شده‌اند.

**اولین پژوهش ثبت‌شده:** مقالهٔ قبلی کاربر در SRC-0001، با مدخل‌های [KB-0001..KB-0009](INDEX.md). منبع برای استخراج دادهٔ طراحی مفید است، ولی هیچ کدام selected stack، verified vendor release یا user-approved implementation نیست؛ پژوهش و مقایسهٔ بعدی باید به نقاط باز این مدخل‌ها توجه کند.
