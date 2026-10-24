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
- **تکمیل مبتنی بر گزارش کاربر، ۲۴ اکتبر ۲۰۲۶:** آدرس مرورگری ارائه‌شده `http://localhost:20128` هنگام بازبودن برنامه **با موفقیت در مرورگر باز شد** (`USER_REPORTED_BROWSER_UI_PASS`؛ پاسخ /v1 و استفاده از مدل هنوز آزمایش نشده). کاربر تصمیم گرفت **نسخه دسکتاپ v3.8.52 را رابط اصلی** قرار دهد؛ نصب موتور دوم با npm/PowerShell انجام نشود. مرورگر صرفاً مسیر دسترسی اختیاری به موتور محلی موجود است. بستن سرور/انتخاب Quit ممکن است دسترسی وب را متوقف کند؛ آزمایش نشده.
- **نکته امنیتی:** فقط `localhost` را تست کنید؛ نه Public Link/port-forwarding، نه reverse proxy و نه expose سیستم. معیار انتخاب وب: آیا کار روزمره با UI روان‌تر است و بدون اجرای دوم موتور کار می‌کند؟ صرفاً نمایش در Chrome دلیل نصب Node دوم نیست.

## ۵. تداوم و شواهد

- [پیش‌زمینه: اجرای Home و اعلان zero-config](../../../06-tests-and-evidence/logs/OMNIROUTE-WINDOWS-HOME-DASHBOARD-AUTHENTICATED-20261024.md).
- داده‌های حساس از تصاویر استخراج و ذخیره نشده است. مسیر `%APPDATA%\omniroute\server.env` متعلق به اسرار محلی است؛ **محتوا را درخواست/کپی/آپلود نکنید**.
- این سند شناسهٔ ثابت دارد؛ تغییرات گزینه‌ها در نسخه‌های بعدی باید در همین مسیر به‌عنوان نسخهٔ تاریخ‌دار و با تصاویر واقعی یا اسناد رسمی بررسی شوند؛ از ساخت منبع CURRENT موازی بپرهیزید.

## ۶. 2026-10-24 — Security screen observed (current actual UI)
- **User screenshot:** `Configuration → Security` is accessible on Windows Desktop v3.8.52. `Require login` toggle is ON; a green `Password updated successfully` message is visible after password update. **UI success only**: persistence/re-login and password rejection of previous default still NOT_VERIFIED.
- `IP Access Control` displays Disabled/Blacklist/Whitelist/WL Priority; **Disabled selected**. Do not enable Whitelist until actual local bind/firewall exposure and rollback behavior are verified; this avoids accidental lockout. Whether `/v1` API authentication is mandatory remains UNKNOWN even though dashboard login is ON.
- **Detailed sanitized observation:** [OMNIROUTE-SECURITY-UI-PASSWORD-UPDATE-20261024.md](../../../06-tests-and-evidence/logs/OMNIROUTE-SECURITY-UI-PASSWORD-UPDATE-20261024.md). No password or keys stored.
- **Immediate next screen:** `OmniProxy → Endpoints` for read-only inspection of local base URL and endpoint authentication. Blur/cover keys, tokens and any token-bearing URLs in screenshots. No provider login or real call yet.

## ۷. Endpoints — تصاویر واقعی ۲۴ اکتبر ۲۰۲۶
- کاربر سه اسکرین‌شات جدید از کل صفحهٔ **OmniProxy → Endpoints** ارسال کرد. همهٔ عکس‌ها بدون تغییر و با هش مستقل در Library به‌صورت ZIP حفظ شدند: `/DJMRN/OmniRoute/2026-10-24/DJMRN_OmniRoute_Endpoints_Screenshots_20261024.zip`، شناسه `libfile_3c1be637e36c8191ae114a4a196ea92a`. فایل‌های تصویری خام در GitHub عمومی قرار نگرفتند.
- **جزئیات دقیق و آدرس‌ها، وضعیت سرور، Tunnelها و مدل‌ها:** [شواهد و هش‌های قابل بازیابی](../../../06-tests-and-evidence/logs/OMNIROUTE-ENDPOINTS-UI-20261024.md).
- در صفحه یک API محلی OpenAI-compatible با نشانی `http://localhost:20128/v1` و وضعیت سبز `Local Server Running` دیده می‌شود؛ آدرس شبکه خصوصی LAN نیز دیده می‌شود، ولی امکان اتصال سایر دستگاه‌ها آزمایش نشده است.
- مدل مکالمه، تصویر، صوت و ویدئو: **۰ مدل در کاتالوگ جاری**؛ شمارش **۲۸ مورد Web Search** به معنای سهمیه رایگان واقعی یا مدل چت نیست. هیچ ارائه‌دهنده و مدل بیرونی واقعاً تست نشده است.
- Tunnelهای خارجی فعال نیستند (۰/۳)، Cloud OmniRoute غیرفعال، Cloudflare و Tailscale نصب نیستند، ngrok نیازمند احراز هویت است؛ گزینهٔ Custom System Prompt خاموش است.
- **اولویت امنیتی جدید:** روشن‌بودن Require Login لزوماً /v1 را محافظت نمی‌کند. مستند سازنده در بعضی محیط‌ها `REQUIRE_API_KEY=false` و bind عمومی `0.0.0.0` را ذکر می‌کند؛ وضعیت نصب کاربر **نامشخص** است. پیش از اتصال هر Provider، فقط به‌صورت خواندنی `Configuration → Advanced` را بررسی کنیم، اگر وضعیت host/auth مشخص نشد فقط یک آزمون خواندنی محدود؛ تغییر IP ACL یا خاموش‌کردن فایروال مجاز نیست.
- **از کاربر عکس تکراری Endpoints نخواهید.** اگر صفحه Advanced یا Providers برای ارزیابی داخلی باز شد، فقط همان را درخواست کنید. `Test endpoint`، `Install & Enable`، فعال‌سازی حساب و Token را فعلاً اجرا نکنید.

## ۸. Advanced — چهار تصویر جدید، ۲۴ اکتبر ۲۰۲۶
- تصاویر **Configuration → Advanced** با ۴ تصویر بدون تغییر و manifest هش SHA-256 در Library خصوصی بایگانی شده‌اند: `/DJMRN/OmniRoute/2026-10-24/DJMRN_OmniRoute_Advanced_Screenshots_20261024.zip`، شناسه `libfile_d76258f5f930819189e6fc7eb07e461a`. باینری‌ها در GitHub عمومی نیستند. [گزارش دقیق و هش چهار تصویر](../../../06-tests-and-evidence/logs/OMNIROUTE-ADVANCED-UI-READONLY-20261024.md).
- **Debug Mode OFF / Log Tool Sources OFF.** Payload Rules چهار آرایهٔ خالی `default/override/filter/defaultRaw` (هر کدام صفر). Request Body Limit = **10 MB**. بدون نیاز به تغییر یا Save.
- **CLIProxyAPI Fallback OFF / Status Not detected.** دکمه Import accounts امکان واردکردن OAuth حساب‌های موجود دارد؛ **بدون مجوز نباید بزنیم**. Headroom proxy آدرس پیشنهادی محلی `http://localhost:8787` دارد؛ فعال‌بودنش اثبات نشده و اکنون مورد نیاز نیست.
- **هیچ گزینه‌ای برای Require API Key یا Host/Bind در تصاویر Advanced دیده نشد.** Require Login داشبورد قبلاً ON بوده ولی آن را با auth درخواست `/v1` یکسان ندانید. نشانی LAN مشاهده‌شده در Endpoints دلیل لزوم آزمون scope است، نه اثبات دسترسی بدون مجوز.
- **گام بعدی واحد و خواندنی** با PowerShell عادی: `Get-NetTCPConnection -State Listen -LocalPort 20128 | Select-Object LocalAddress,LocalPort,OwningProcess`، بدون نصب/تغییر/ارائه کلید. `0.0.0.0` یا `::` نشان‌دهنده bind روی همهٔ رابط‌هاست (نه لزوماً عبور از فایروال)؛ `127.0.0.1` یا `::1` محلی است. تا روشن‌شدن scope و API auth هیچ provider واقعی وصل نشود. پس از آن فقط درصورت approval تنظیم امن انجام می‌شود.
- از کاربر دوباره عکس‌های همین Advanced را نخواهید. برای بررسی شبکه خروجی همین دستور کافی است؛ دادهٔ حساب/رمز درخواست نشود.

## ۹. نتیجهٔ واقعی PowerShell: پورت 20128 فقط Loopback (۲۴ اکتبر ۲۰۲۶)
- کاربر دستور خواندنی `Get-NetTCPConnection -State Listen -LocalPort 20128 | Select-Object LocalAddress,LocalPort,OwningProcess` را روی ویندوز اجرا کرد. خروجی دقیق: `LocalAddress=127.0.0.1, LocalPort=20128, OwningProcess=6556` و ردیف دیگری دیده نشد؛ **`LOCAL_TCP_LISTEN_LOOPBACK_IPV4_PASS`** برای همین زمان. شناسهٔ فرایند موقتی است و نمی‌تواند به‌عنوان ID پایدار برنامه تلقی شود.
- بنابراین **فعلاً IP whitelist، Windows Firewall یا تونل‌ها را تغییر ندهید**؛ آدرس LAN نشان‌داده‌شده در Endpoints بر خلاف برداشت اولیه، به‌تنهایی اثبات شنود روی LAN نیست. احتمال رفتار متفاوت پس از راه‌اندازی مجدد یا expose شدن به روش دیگر همچنان جداگانه بررسی می‌شود.
- **تفاوت الزام ورود داشبورد و الزام کلید API مهم است:** طبق [راهنمای رسمی inference auth](https://omniroute.hagicode.com/en-US/security/inference-auth-posture/) مسیر `GET /v1/models` تحت قوانین داشبورد است و یک 401 از آن به معنی بسته‌بودن `POST /v1/chat/completions` نیست. فعلاً API key enforcement `NOT_VERIFIED`، هیچ مدل/Provider واقعی اجرا نشده است. [سند شواهد واقعی ویندوز](../../../06-tests-and-evidence/logs/OMNIROUTE-LOCAL-TCP-LOOPBACK-VERIFIED-20261024.md).
- **مرحلهٔ بعد:** فقط آزمون محدود authentication روی مسیر inference با مدل ساختگی و بدون هیچ کلید، یا مشاهدهٔ وضعیت امنیت API از UI معتبر؛ بدون اجازهٔ جداگانه به مدل واقعی یا provider دسترسی ندهیم.
