# DJMRN-AGTEAM-001 — Professional Multi-Agent Teams & Workflows

**زیرپروژه جدید در DJMRN-Intelligent-Assistant** | تاریخ آغاز: 2026-10-30 | مالک تصمیم: کاربر | وضعیت: **RESEARCHED / PROPOSED / IMPLEMENTATION NOT AUTHORIZED**

> هدف: ایجاد یک تیم واقعی از ایجنت‌های مستقل با هویت، حافظه، ابزار و مجوز جداگانه که در غیاب کاربر کار زمان‌بندی‌شده انجام دهند، مستقیماً با هم مشورت کنند، یافته‌ها را به‌صورت تخصصی نقد کنند، اختلاف را با شواهد بررسی کنند و برای اقدامات حساس متوقف شوند. محیط بصری برای نظارت و مدیریت تیم نیز لازم است؛ صرفِ چند شخصیت با پاسخ‌های پشت‌سرهم در یک چت، معیار پذیرش نیست.

## تصمیم‌های این نوبت
- **تصمیم قطعی کاربر:** این موضوع یک زیرپروژه قابل پیگیری در مخزن اصلی باشد؛ **تعریف/مستندسازی اکنون**، **نصب/اتصال/پرداخت/فعال‌سازی بعداً و فقط با مجوز جدید**.
- **فرضیه معماری برای آزمایش؛ نه انتخاب اجرایی نهایی:** OpenClaw برای runtime مستقل، حافظه و ارتباط میان ایجنت‌ها؛ OpenAgents Workspace برای فضای همکاری، مشاهده، Tasks و رابط انسانی؛ OpenAgents Launcher یا agn CLI برای اتصال دستگاه/Runtime؛ OmniRoute به‌عنوان مسیر inference فقط پس از آزمون.
- **یک تیم واقعی، نه دو کپی موازی:** هر Agent دارای شناسه و مالک اجرای مشخص؛ در صورت امکان نماینده همان Agent در Workspace عرضه شود. اینکه چند Agent داخلی یک OpenClaw Gateway در Workspace به‌صورت چند عضو مستقل مدیریت شوند **UNVERIFIED / PILOT BLOCKER** است.
- **ثبت فعلی پژوهشی است:** هیچ نصب، token، Workspace، Runtime، schedule یا مدل در این اقدام ایجاد یا تست نشده است. آزمایش AGNT قبلی به رضایت کاربر نرسید؛ AGNT حذف/غیرفعال نمی‌شود.

## اسناد این زیرپروژه
1. [ARCHITECTURE-AND-INTEGRATION.md](ARCHITECTURE-AND-INTEGRATION.md) — نقش محصولات، مرزهای داده، مسیر اتصال، گزینه‌های جایگزین و نقطه حساس نمایش مستقل هر Agent.
2. [AGENT-ROLES-AND-COLLABORATION.md](AGENT-ROLES-AND-COLLABORATION.md) — هویت‌ها، مأموریت‌ها، پروتکل مشورت، نظارت متقابل، اختلاف‌نظر و اختیار.
3. [OPERATIONS-SECURITY-AND-COST.md](OPERATIONS-SECURITY-AND-COST.md) — زمان‌بندی unattended، حافظه، سطح دسترسی، ریسک امنیتی، هزینه، RAM، خاموشی دستگاه و گزارش‌ها.
4. [ROADMAP-AND-ACCEPTANCE.md](ROADMAP-AND-ACCEPTANCE.md) — گیت‌های توسعه، پایلوت فقط‌خواندنی، آزمون‌های قابل‌قبول و توقف.
5. [RESEARCH-AND-OPEN-QUESTIONS.md](RESEARCH-AND-OPEN-QUESTIONS.md) — یافته‌های مستند به منابع رسمی، موارد قطعی/نامعلوم، رقبا و سؤال‌های ادامه.

## هم‌راستایی با بخش‌های قدیمی
- [REQ-MPA-001 — Many Logical Specialized Assistants](../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md): نیاز قبلیِ پرسوناهای تخصصی را حفظ می‌کند؛ AGTEAM-001 مسیر عملیاتی خاص برای آزمون همکاری خودگردان است، نه بازنویسی نیاز.
- [REQ-OBS-001 — Live Observability Map](../02-project-management/LIVE-OBSERVABILITY-MAP-REQUIREMENT.md): UI Workspace «نقشه telemetry همه مؤلفه‌ها» نیست؛ صرفاً یکی از نماهای همکاری است.
- [نقشه نقش‌محور مصرف مدل رایگان](../02-project-management/FREE-CLOUD-MODEL-QUOTA-AND-ROLE-ROUTING-POLICY-20261025.md): مدل و Provider با اجازه/سهمیه سنجیده می‌شود؛ شخصیت مستقل به معنی مدل مقیم جداگانه نیست.
- [PROJECT-RULES](../PROJECT-RULES.md) و [CURRENT-STATUS](../07-operations-and-continuity/CURRENT-STATUS.md) حاکم‌اند. بخش فعلی اسناد موضوعیِ صریحاً درخواست‌شده است؛ **مرجع روزانه پیشرفت فقط CURRENT-STATUS** است. بعداً برای هر گام واقعی فقط با دستور صریح ثبت می‌شود.

## برای ادامه در گفتگوی آینده (START HERE)
1. این README و ابتدای CURRENT-STATUS و PROJECT-RULES را بخوان.
2. اسناد پنج‌گانه این پوشه را بررسی کن.
3. قابلیت‌ها، نسخه‌ها، قیمت‌ها، امنیت و سازگاری Windows/OpenAgents/OpenClaw/OmniRoute را **دوباره از منبع رسمی و زمان اجرا** بررسی کن.
4. هیچ ادعای «وصل است»، «ایجنت‌ها در Workspace مستقل دیده می‌شوند»، «رایگان قطعی برای حساب کاربر»، «RAM مناسب»، «Cron اجرا شده» بدون آزمون واقعی نکن.
5. اولین عملیات پس از موافقت تازه کاربر: پایلوت کوچک ۲ یا ۳ Agent فقط‌خواندنی، بدون اطلاعات محرمانه و بدون پرداخت؛ Gateهای پذیرش در ROADMAP.
