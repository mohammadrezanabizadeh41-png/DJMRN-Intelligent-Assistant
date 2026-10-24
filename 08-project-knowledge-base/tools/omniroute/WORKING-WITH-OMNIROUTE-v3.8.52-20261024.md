# کار کردن با نرم‌افزار OmniRoute — راهنمای منو و آرشیو تصویری DJMRN

**کد سند:** DJMRN-OMNIROUTE-UI-001 · **تاریخ عکس‌ها:** 2026-10-24 · **نسخهٔ مشاهده‌شده:** Windows Desktop OmniRoute v3.8.52 · **وضعیت:** USER-SCREENSHOT-VERIFIED-MENU-LAYOUT · **نوع:** راهنمای یافتن صفحات، نه تأیید عملکرد قابلیت‌ها.

> این همان سندی است که برای همهٔ پنجره‌های بعدی باید بازیابی شود؛ از کاربر برای بازشناسی همین ده منوی بازشده مجدداً تصویر درخواست نکنید. تنها اگر قرار است گزینه‌ای در **داخل** یک صفحه تنظیم یا آزمایش شود، تصویر همان صفحهٔ جزئی را در صورت نیاز بخواهید.

## ۱. فایل‌های اصلی تصاویر و محل بازیابی

**هر ۱۰ فایل PNG اصلی بدون تغییر در یک ZIP** ذخیره شده‌اند؛ عکس‌ها صرفاً منو هستند و در آنها کلید API/رمز/دادهٔ حساب دیده نمی‌شود.

- **محل نسخهٔ تصویری در ChatGPT File Library:** `/DJMRN/OmniRoute/2026-10-24/DJMRN_OmniRoute_Menu_Screenshots_20261024.zip`
- **شناسهٔ نسخهٔ آرشیوشده (برای بازیابی مستقل):** `libfile_00432e2cf984819187c3192cf5a68486` (مخزن GitHub خودش این شناسهٔ داخلی را به‌عنوان URL قابل دانلود ارائه نمی‌دهد).
- **محتوای ZIP:** `screenshots/*.png` (ده تصویر)، `manifest.json` (هش SHA-256 هر تصویر و نام فایل اولیه)، `README-FA.txt`.
- **نکتهٔ تعیین‌کننده:** اصل فایل‌های PNG در آرشیو Library است و *در GitHub به‌صورت binary هنوز آپلود نشده‌اند*. **این سند و فهرست دقیق تصویری در GitHub است**؛ هرگز ادعا نکنید باینری تصاویر خودشان در GitHub موجود است. در صورت نیاز به تصاویر، به این محل Library مراجعه کنید. برای خواندن منوها نیازی به تصاویر نیست.

| # | فایل داخل آرشیو | بخش نمایش‌داده‌شده | SHA-256 تصویر اصلی |
|---|---|---|---|
| 01 | `screenshots/01-omni-proxy.png` | OmniProxy | `28a07ccfa399d0b3bb7ae77c80627471a4e827fd5ca7c6d240b836545e49db11` |
| 02 | `screenshots/02-analytics.png` | Analytics | `8617f74027cf72586eb5e0815f4e9d17187cd53831ae027c344c24facfe3ada6` |
| 03 | `screenshots/03-costs.png` | Costs | `85f4b4aa756db6b24592b235ad56dbb14626302b6a8ebe3a8f3c532fc028cd7c` |
| 04 | `screenshots/04-monitoring.png` | Monitoring | `cc4871021a238f09fb497addc64dad8c11b0d73953b8d3075aaa80977bdc6b76` |
| 05 | `screenshots/05-dev-tools.png` | Dev Tools | `fdbe846f708b5fe5105e3bd120500c99708ac282e2e7cd39a12277843401c634` |
| 06 | `screenshots/06-agentic-features.png` | Agentic Features | `ec6ea4a39d04be7faca7d3df883f9314b0ae723f21b1f6b855de049103a4bb16` |
| 07 | `screenshots/07-other-features.png` | Other Features | `0d87cd2128490f5b7791c1e384d2b530f475e0b535e72daa8f1f7538fd3df221` |
| 08 | `screenshots/08-configuration-part1.png` | Configuration / 1 | `bf4ff9ada7951056bba529673990914b2ee659526774ff0b1b3ee65ea425f693` |
| 09 | `screenshots/09-configuration-part2.png` | Configuration / 2 | `c1e548b09757ab0ced6b98ccf061589b1f6163742be4d49623757bebb44718b9` |
| 10 | `screenshots/10-support-navigation.png` | Docs, Issues, Changelog | `f0923b833e40db50d1aaf43631af0d8579d44934ad5e1045f925423e1ec7d2ce` |

## ۲. نقشهٔ کامل منوی سمت چپ، عیناً بر اساس تصاویر

**OmniProxy (۹ آیتم)** — اتصال و مسیریابی مدل:
1. **Endpoints** — `Your AI connection URLs` — آدرس‌های اتصال کلاینت‌ها.
2. **API Keys** — `Manage API keys and access` — مجوز/کلید دسترسی همیارها (کلیدها نباید در عکس/گیت‌هاب ظاهر شوند).
3. **Providers** — `Manage AI providers` — ثبت و تنظیم تأمین‌کننده؛ اتصال واقعی نیازمند بررسی شرایط، هزینه و تأیید است.
4. **Models & Combos** — `Browse models and combos acr...` (توضیح در تصویر بریده شده) — مشاهدهٔ مدل‌ها و گروه‌ها.
5. **Embedded Services** — `Optional local services` — سرویس‌های محلی اختیاری.
6. **Combos** — `Group providers for failover` — گروه‌بندی تأمین‌کننده‌ها برای جایگزینی.
7. **Combo Studio** — `Live routing cascade` — طراحی/نمایش زنجیرهٔ مسیریابی.
8. **Provider Quota** — `Track provider usage limits` — پیگیری محدودیت سهمیهٔ ارائه‌دهنده.
9. **Quota Sharing** — `Share provider quotas across keys` — اشتراک سهمیه بین کلیدها.

**Analytics (۸ آیتم)** — مشاهده و تحلیل مصرف:
1. **Usage** — `Traffic and usage stats`.
2. **Combo Health** — `Combo target reliability`.
3. **Utilization** — `Provider utilization`.
4. **Cache** — `Cache hit rates`.
5. **Compression** — `Token savings stats`.
6. **Search** — `Search tool analytics`.
7. **Evals** — `Eval suite results`.
8. **Provider Stats** — `Latency and performance metrics`.

**Costs (۵ آیتم)** — سیاست مالی:
1. **Overview** — `Consolidated cost analysis`.
2. **Pricing** — `Per-model pricing rules`.
3. **Budget** — `Budget limits`.
4. **Free-Tier Budget** — `Monthly free-token allowances`.
5. **Free Provider Rankings** — `Best free providers ranked by m...` (توضیح در تصویر بریده شده).

**Monitoring (۴ آیتم/سرگروه دیده‌شده)**:
1. **Activity** — `Friendly feed of recent events`.
2. **Logs** — زیرمنوی خود دارای فلش؛ *باز نشده*.
3. **Audit** — زیرمنوی خود دارای فلش؛ *باز نشده*.
4. **System** — زیرمنوی خود دارای فلش؛ *باز نشده*.

**Dev Tools (۳ آیتم)**:
1. **Translator** — `Format conversion`.
2. **Playground** — `Test prompts live` (اجرای تست می‌تواند تماس مدل/مصرف داشته باشد).
3. **Search Tools** — `Search tool registry`.

**Agentic Features (۷ آیتم)** — صرف وجود منو به معنی فعال‌بودن Agent نیست:
1. **Memory** — `Persistent agent memory`.
2. **AgentSkills** — `A2A skill registry`.
3. **Chaos Mode** — `Multi-model parallel execution` (ممکن است مصرف را چند برابر کند؛ فعلاً غیرفعال).
4. **OmniSkills** — `Sandbox skill registry`.
5. **MCP Server** — `MCP server controls`.
6. **A2A Server** — `A2A protocol server`.
7. **Plugins** — `Plugin marketplace & installs`.

**Other Features (۲ آیتم/سرگروه دیده‌شده)**:
1. **Gamification** — فلش دارد، زیرمنو باز نشده.
2. **Media** — `Cached media files`.

**Configuration (۱۲ آیتم)** — دو تصویر پشت‌سرهم از یک بخش:
1. **Storage** — `Database and backups`.
2. **Appearance** — `Theme and layout`.
3. **AI Settings** — `AI behavior defaults`.
4. **Modality Bridge** — `Image/audio → text fallback for ...` (توضیح در تصویر بریده شده).
5. **Global Routing** — `Global routing rules`.
6. **Resilience** — `Retries and breakers`.
7. **Advanced** — `Power user options`.
8. **Security** — `Auth and encryption`.
9. **Access Tokens** — `Scoped CLI tokens for remote m...` (توضیح در تصویر بریده شده).
10. **Feature Flags** — `Toggle system capabilities`.
11. **Cache** — `Model catalog and response cac...` (توضیح در تصویر بریده شده).
12. **Sidebar** — `Customize sidebar layout`.

**بخش پایینی / کمک (۳ آیتم)**:
1. **Docs** — Documentation.
2. **Issues** — Report a bug.
3. **Changelog** — Release notes.

**جمع: ۵۳ آیتم/سرگروه مشاهده‌شده در تصاویر**، بدون احتساب گزینه‌های پنهان Logs / Audit / System / Gamification.

## ۳. دقیقاً برای DJMRN از کدام بخش‌ها استفاده کنیم؟

| اولویت | صفحه | هدف عملی | وضعیت آزمون |
|---|---|---|---|
| P0 | **Configuration → Security** | بررسی تغییر رمز پیش‌فرض، auth و local-only exposure بدون افشای کلید | NOT_CHECKED |
| P1 | **OmniProxy → Endpoints** | دیدن endpointهای واقعی و چگونگی اتصال کلاینت‌ها | NOT_CHECKED |
| P1 | **OmniProxy → Providers** | بررسی فهرست و وضعیت اتصال *بدون ساخت حساب* | NOT_CHECKED |
| P1 | **OmniProxy → Models & Combos** | مدل‌های ارائه‌شده/قابلیت‌ها، تجمیع و availability | NOT_CHECKED |
| P2 | **OmniProxy → Provider Quota** و **Quota Sharing** | مشاهدهٔ quota و تمایز limit تخمینی در UI با quota واقعی provider | NOT_CHECKED |
| P2 | **Costs → Free-Tier Budget / Budget / Pricing** | کنترل هزینهٔ صفر، paid-deny و نرخ/سهمیه | NOT_CHECKED |
| P2 | **OmniProxy → API Keys** | مجوزهای مجزای هر همیار؛ عدم انتشار کلید | NOT_CHECKED |
| P3 | **Combos / Combo Studio / Global Routing / Resilience** | failover 429/503 فقط به مدل رایگان و هم‌سطح؛ خطای نامعلوم DENY | NOT_CHECKED |
| P3 | **Monitoring / Analytics / Storage** | مصرف واقعی، audit، تداوم سهمیه و backup/restore | NOT_CHECKED |
| LATER | **Agentic Features / Plugins / Chaos Mode** | فقط در صورت نیاز عملیِ آزموده و مجوز جدا | NOT_ACTIVATED |

**استاندارد کار:** ابتدا خواندن UI و هزینه/مجوز سرویس؛ سپس تأیید کاربر برای provider/account/API، بعد یک آزمایش واقعی محدود؛ اطلاعات کلید و session بیرون از GitHub عمومی. هیچ صفحه‌ای صرفاً به‌خاطر وجود اسمش، قابلیت عملیاتی محسوب نمی‌شود.

## ۴. وب در مقابل برنامهٔ دسکتاپ

- تصمیم فعلی: **نسخهٔ Windows Desktop v3.8.52 نصب و ورود Home موفق است**؛ نصب مجدد با PowerShell / npm در این مرحله ارزش افزودهٔ اثبات‌شده ندارد.
- مستند رسمی Electron توضیح می‌دهد که Desktop یک Next.js standalone server محلی را اجرا و Web dashboard را در پنجرهٔ Electron نشان می‌دهد. منوی tray امکان **Open Dashboard** در مرورگر دارد. [Vendor Electron Guide](https://github.com/cheaper-inference/OmniRoute/wiki/Electron-Guide).
- آدرس مستند پیش‌فرض پنل `http://localhost:20128` یا `http://localhost:20128/dashboard` است؛ **این آدرس برای دستگاه کاربر هنوز مستقیماً آزمون نشده** و Desktop می‌تواند از پورت دیگری استفاده کند. ترجیح: در System Tray بر آیکون OmniRoute راست‌کلیک و **Open Dashboard** را بزن، اگر وجود داشت. پنل خارجی و پنجرهٔ دسکتاپ همان backend را استفاده می‌کنند؛ بسته‌شدن سرور/انتخاب Quit می‌تواند دسترسی وب را هم متوقف کند.
- **نکته امنیتی:** فقط `localhost` را تست کنید؛ نه Public Link/port-forwarding، نه reverse proxy و نه expose سیستم. معیار انتخاب وب: آیا کار روزمره با UI روان‌تر است و بدون اجرای دوم موتور کار می‌کند؟ صرفاً نمایش در Chrome دلیل نصب Node دوم نیست.

## ۵. تداوم و شواهد

- [پیش‌زمینه: اجرای Home و اعلان zero-config](../../../06-tests-and-evidence/logs/OMNIROUTE-WINDOWS-HOME-DASHBOARD-AUTHENTICATED-20261024.md).
- داده‌های حساس از تصاویر استخراج و ذخیره نشده است. مسیر `%APPDATA%\omniroute\server.env` متعلق به اسرار محلی است؛ **محتوا را درخواست/کپی/آپلود نکنید**.
- این سند شناسهٔ ثابت دارد؛ تغییرات گزینه‌ها در نسخه‌های بعدی باید در همین مسیر به‌عنوان نسخهٔ تاریخ‌دار و با تصاویر واقعی یا اسناد رسمی بررسی شوند؛ از ساخت منبع CURRENT موازی بپرهیزید.
