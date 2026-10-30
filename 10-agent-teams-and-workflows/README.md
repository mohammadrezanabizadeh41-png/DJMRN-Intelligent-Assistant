# DJMRN-AGTEAM-001 — Professional Multi-Agent Teams & Workflows

**زیرپروژه جدید در DJMRN-Intelligent-Assistant** | تاریخ آغاز: 2026-10-30 | مالک تصمیم: کاربر | وضعیت: **KICKOFF / DOWNLOAD PREPARATION / NOT INSTALLED**

> هدف: ایجاد یک تیم واقعی از ایجنت‌های مستقل با هویت، حافظه، ابزار و مجوز جداگانه که در غیاب کاربر کار زمان‌بندی‌شده انجام دهند، مستقیماً با هم مشورت کنند، یافته‌ها را به‌صورت تخصصی نقد کنند، اختلاف را با شواهد بررسی کنند و برای اقدامات حساس متوقف شوند. محیط بصری برای نظارت و مدیریت تیم نیز لازم است؛ صرفِ چند شخصیت با پاسخ‌های پشت‌سرهم در یک چت، معیار پذیرش نیست.

## راهبرد اجرایی و شروع فاز نخست — 2026-10-30 (USER APPROVED)

**Status: KICKOFF / DOWNLOAD PREPARATION; NOT INSTALLED, NOT RUNNING.** این زیرپروژه به‌صورت عملیاتی آغاز می‌شود، اما اولین مرحله محدود به دریافت فایل رسمی OpenClaw و بررسی پیش‌نیازهای Windows است. نصب، راه‌اندازی سرویس، اتصال حساب/مدل و تغییر امنیتی هنوز اجرا یا تأیید جداگانه نشده است.

### Isolation — بدون مداخله در پروژه‌های موازی
- مالک فعالیت حاضر فقط `DJMRN-AGTEAM-001` در `10-agent-teams-and-workflows/` است. سایر پروژه‌های موازی شامل Opportunity Hunter، تحقیق APIهای رایگان، مرورگر خودکار، OmniRoute، AGNT و سایر خدمات **کاملاً دست‌نخورده** می‌مانند.
- از محیط runtime، فایل‌ها، زمان‌بندی، پورت یا سهمیه پروژه‌های دیگر بدون بررسی تداخل و مجوز مستقل استفاده نکن. تغییرات مرحله‌ای فقط در همین شاخه موضوعی GitHub و در صورت درخواست صریح کاربر در `07-operations-and-continuity/CURRENT-STATUS.md` ثبت می‌شوند.
- هیچ حذف AGNT، بازنویسی تنظیمات OmniRoute، انتقال state، اجرای فرمان نصب یا ساخت حساب جدید صرفاً بر پایه این سند مجاز نیست.

### تقسیم نقش قطعی دو نرم‌افزار و مراحل اتصال
1. **OpenClaw Gateway = Runtime/Execution/Agent Identity.** فاز نخست: دانلود نصب‌کننده رسمی برای ویندوز، بررسی Node و RAM، نصب محدود پس از مجوز، راه‌اندازی فقط local، سپس هویت مستقل و session جدا برای PM-01، ARCH-01 و RESEARCH-01؛ پیام مستقیم و بازبینی متقابل باید با trace واقعی اثبات شود.
2. **OpenAgents Launcher + Workspace = Coordination UI / Presentation.** فاز دوم: فقط بعد از PASS فاز نخست، نصب Launcher و اتصال Runtime به Workspace برای مشاهده، همکاری، کارهای تیمی و وضعیت. Workspace یک هویت اجرایی موازی و برنامه زمان‌بندی دوم برای همان کار نسازد؛ یک مالک مشخص برای هر job.
3. **OmniRoute = Existing model provider gateway.** صرفاً یک dependency خارجی برای مدل رایگان با API سازگار OpenAI پس از آزمایش model/tool calling، سیاست quota و overage؛ این پروژه حق دستکاری تنظیمات جاری OmniRoute را ندارد.
4. **Compatibility P0:** آیا چند ایجنت داخلی یک OpenClaw Gateway به‌عنوان چند عضو جداگانه و قابل خطاب در OpenAgents نمایش داده می‌شوند؟ **UNVERIFIED**. تا آزمون واقعی، ادعای مدیریت کامل دوطرفه یا همگام‌سازی خودکار شخصیت‌ها ممنوع است.

### Windows 11: دانلود و پیش‌نیازها (بررسی منابع رسمی: 2026-10-30)
- نام صحیح نرم‌افزار **OpenClaw** است (کاربر با عنوان گفتاری OpenCloud به آن اشاره کرده).
- گزینه اول برای کاهش پیچیدگی در لپ‌تاپ 8GB: Windows-native CLI/Gateway از اسکریپت رسمی `https://openclaw.ai/install.ps1`، مستند: `https://docs.openclaw.ai/platforms/windows`. **اول فقط فایل را دانلود و بررسی کن؛ اسکریپت را مستقیم اجرا نکن.** Windows-native CLI از WSL2/Docker اجباری نیست.
- گزینه GUI رسمی: Windows Hub، فایل x64 `OpenClawCompanion-Setup-x64.exe` در `https://github.com/openclaw/openclaw-windows-node/releases/latest`. Setup محلی Hub می‌تواند WSL مخصوص خود ایجاد کند؛ تا بررسی RAM و نصب تکراری، آن را همراه CLI نصب نکن.
- Node مورد نیاز CLI طبق مستند انگلیسی جدید: Node 26.1+ (وصله امن توصیه‌شده 26.12.1+) یا Node 24.16+ (وصله امن توصیه‌شده 24.22.1+)، نه Node 22/23/25. Installer رسمی در صورت نیاز Node را نصب می‌کند. مرجع: `https://docs.openclaw.ai/install/node-compatibility`.
- پورت پیش‌فرض Gateway: 18789؛ تداخل پورت و دسترسی شبکه فقط‌خواندنی بررسی شود. Gateway روی loopback با احراز هویت باقی بماند و بدون تأیید روی LAN/Internet در دسترس قرار نگیرد: `https://docs.openclaw.ai/gateway/security/network-exposure`.
- قبل از نصب: PowerShell، OS، RAM واقعی/آزاد، Node/npm، WSL، نسخه نصب‌شده قبلی، فرآیندها و پورت‌ها فقط‌خواندنی شناسایی و هزینه/حجم/امنیت بررسی شوند. اعداد عملکرد و سازگاری OmniRoute تا تست روی دستگاه **UNKNOWN** هستند.

### گیت‌های اجرایی و معیار توقف
K0 ثبت راهبرد در مخزن → K1 دانلود فایل رسمی بدون اجرا و بررسی URL/hash → K2 تشخیص فقط‌خواندنی Windows و نسخه‌ها → K3 مجوز مستقل برای نصب یک Gateway → K4 تست health/local UI، RAM و کنترل دسترسی → K5 دو ایجنت مستقل و تبادل واقعی بدون کپی دستی → K6 اتصال OpenAgents و بررسی نمایش مستقل شخصیت‌ها → K7 زمان‌بندی unattended، بازبینی تخصصی، توقف امن، recovery و گزارش.
هر مرحله باید با evidence واقعی **PASS/FAIL/BLOCKED** گزارش شود. هزینه ناشناخته = عدم فعال‌سازی؛ تغییر حساس = تأیید انسانی. دستگاه در حالت Sleep/خاموش، Runtime محلی را اجرا نمی‌کند؛ وعده فعالیت شبانه‌روزی بدون میزبان همیشه روشن ممنوع.
**NEXT:** کاربر فقط installer رسمی را دانلود کند و سپس خروجی تشخیص PowerShell را بفرستد. هیچ نصب یا عملکرد عملی هنوز تأیید نشده است.

## تصمیم‌های این نوبت
- **تصمیم قطعی کاربر:** این موضوع یک زیرپروژه قابل پیگیری در مخزن اصلی باشد؛ **آماده‌سازی دانلود اکنون؛ نصب، اتصال و هزینه فقط با تأیید جداگانه**.
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
