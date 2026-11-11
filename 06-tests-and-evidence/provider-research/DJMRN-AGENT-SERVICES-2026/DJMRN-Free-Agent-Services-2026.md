# DJMRN — کشف جهانی ابزارها و سرویس‌های رایگان ایجنت‌ها

**DJMRN-AGENT-TOOLS-RESEARCH-001 · ۱۲ نوامبر ۲۰۲۶ · OpenMausBot 0.1.152**

## A — کاتالوگ کامل

۱۵۱ رکورد یکتا در ۲۶ حوزه. CSV همراه ۲۷ ستون دارد و بازهٔ سهمیه، حساب و کارت، هزینه اضافه، API، MCP، مسیر اتصال، داده، ایران، رقیب و شواهد را برای هر سرویس نشان می‌دهد. محصولات مستقل با کاربرد و حدود مجزا، مانند GitHub Pages و Codespaces، رکورد مستقل دارند.

**رده‌ها** F0 عمومی بدون کلید و پرداخت · F1 سهمیه یا ظرفیت دوره‌ای رایگان · F2 اعتبار شروع یا Trial · F3 متن‌باز محلی یا self-host · F4 رابط وب رایگان · P خارج از دسترس رایگان برای کاربر تازه · U نامشخص یا خارج از این رده‌ها. چند رده ممکن است همزمان برقرار باشند. Free نرم‌افزار هزینه hosting، مدل یا bandwidth را حذف نمی‌کند.

**وضعیت‌ها** VERIFIED یعنی عرضه پایه و سهمیه ثبت‌شده یا ماهیت ابزار محلی با شاهد رسمی بررسی شد. PARTIALLY VERIFIED یعنی بخشی از عرضه یا شرایط تأیید شده است. UNVERIFIED یعنی بازیابی رسمی یا شواهد کافی به دست نیامد. تأیید محصول به معنی تأیید حساب ایران یا اجرای زنده روی ایجنت‌ها نیست. هزینه یا eligibility نامشخص در اتصال حساب **UNKNOWN/DENY** است.

**مسیرها** A = API/HTTP، B = Browser، L = محلی/CLI/SDK، M = MCP، R = RSS، N = Browser داخلی. در ستون MCP، O = رسمی، C = Community یا امکان آداپتر، U = مجهول و N = MCP تأیید نشده. C:adapter نام بستهٔ بررسی‌شده نیست.

### 1. جست‌وجوی وب و پژوهش

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 001 [Tavily](https://tavily.com) | جست‌وجوی وب و استخراج | F1 · 1000 credits/month; 100 RPM shared; basic 1 and advanced 2 credits | A | O:remote/stdio | [سند](https://docs.tavily.com/documentation/api-credits) | VERIFIED |
| 002 [Exa](https://exa.ai) | جست‌وجوی معنایی و متن نتایج | F1 F2 · $10/month + $10 onboarding; Lite from $4/1000 | A | O:remote/stdio | [سند](https://exa.ai/pricing) | VERIFIED |
| 003 [Brave Search API](https://brave.com/search/api) | شاخص مستقل وب | F1 · $5/month; ~1000 Search calls at $5/1000 | A | C:adapter | [سند](https://api-dashboard.search.brave.com/documentation/resources/help-feedback) | VERIFIED |
| 004 [SerpApi](https://serpapi.com) | نتایج ساختاری چند موتور | F1 · 250 searches/month | A | O:remote/stdio | [سند](https://serpapi.com/pricing) | VERIFIED |
| 005 [Serper](https://serper.dev) | نتایج Google به JSON | F2 · 2500 signup queries; recurring unverified | A | C:adapter | [سند](https://serper.dev) | VERIFIED |
| 006 [SearchAPI.io](https://searchapi.io) | SERP و جست‌وجوی عمودی | F2 · 100 signup requests; reset unverified | A | C:adapter | [سند](https://searchapi.io/pricing) · [شاهد](https://www.searchapi.io/) | VERIFIED |
| 007 [Parallel Search](https://parallel.ai) | جست‌وجو و استخراج شواهد وب | F0 F1 F2 · public MCP quota UNKNOWN; card API $5/month | A M | O:remote | [سند](https://parallel.ai/pricing) | VERIFIED |
| 008 [SearXNG](https://searxng.org) | متاجست‌وجوی self-host و JSON | F3 · upstream/instance dependent | A B L | C:adapter | [سند](https://docs.searxng.org/dev/search_api.html) | VERIFIED |
| 009 [DuckDuckGo](https://duckduckgo.com) | جست‌وجوی UI و پاسخ فوری عمومی | F0 F4 · Keyless public UI; Instant Answers is not a general SERP API | A B | N | [سند](https://duckduckgo.com/api) · [شاهد](https://duckduckgo.com/) | PARTIALLY VERIFIED |
| 010 [Google Search](https://google.com) | کشف موردی منابع در رابط وب | F4 · UI quota UNKNOWN | B | N | [سند](https://support.google.com/websearch) | PARTIALLY VERIFIED |
| 011 [Bing](https://bing.com) | کشف وب و تصاویر از UI | F4 · UI quota UNKNOWN; legacy API retired | B | N | [سند](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement) | PARTIALLY VERIFIED |
| 012 [Marginalia Search](https://marginalia-search.com) | کشف وب مستقل و سایت‌های کوچک | F4 F3 · UI public; API quota UNKNOWN | A B L | N | [سند](https://docs.marginalia-search.com) | UNVERIFIED |
| 013 [Google Custom Search JSON API](https://programmablesearchengine.google.com) | جست‌وجوی JSON برای حساب‌های قدیمی | P · closed to new users; legacy 100/day, retires 2027-01-01 | A | N | [سند](https://developers.google.com/custom-search/v1/overview) | VERIFIED |


### 2. مرورگر، CDP و RPA

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 014 [Playwright](https://playwright.dev) | مرور DOM، snapshot و کار تکراری | F3 · local hardware and site limits | L | O:stdio Node | [سند](https://github.com/microsoft/playwright-mcp) | VERIFIED |
| 015 [Chrome DevTools MCP](https://developer.chrome.com) | خواندن console و performance مرورگر | F3 · local hardware limits | L | O:stdio Node | [سند](https://github.com/ChromeDevTools/chrome-devtools-mcp) | VERIFIED |
| 016 [Browser Use](https://browser-use.com) | اتوماسیون مرحله‌ای با Python | F3 U · local framework; Cloud allowance UNKNOWN | L M | O:remote Cloud; verify plan | [سند](https://github.com/browser-use/browser-use) | PARTIALLY VERIFIED |
| 017 [BrowserOS](https://browseros.com) | مرورگر agent و ابزارهای ناوبری | F3 · local resources | B L M | O:local; endpoint version dependent | [سند](https://github.com/browseros-ai/BrowserOS) | VERIFIED |
| 018 [Selenium](https://selenium.dev) | اجرای UI قابل‌تکرار با WebDriver | F3 · local resources | L | C:adapter | [سند](https://selenium.dev/documentation/webdriver) · [شاهد](https://www.selenium.dev/documentation/webdriver/) | VERIFIED |
| 019 [Browserbase](https://browserbase.com) | مرورگر ابری Playwright/CDP | F1 · 1 browser-hour/month published | A M | O:provider MCP; scope verify | [سند](https://browserbase.com/pricing) | VERIFIED |
| 020 [Browserless](https://browserless.io) | Chromium remote و rendering | F1 F3 · 1000 units/month on Free | A L | C:adapter | [سند](https://docs.browserless.io/baas/billing/usage-and-limits) · [شاهد](https://docs.browserless.io/overview/unit-consumption) | VERIFIED |
| 021 [OpenMausBot Browser](https://openmausbot.com) | مرور عمومی، snapshot و تب در میزبان | F3 · local hardware and website limits | N | Native tool | [سند](https://github.com/milind-soni/OpenMausBot/blob/main/docs/computer-use-integration.md) | PARTIALLY VERIFIED |
| 022 [Browser MCP](https://browsermcp.io) | کنترل مرورگر موجود با افزونه | U · local resources; source/license and current distribution verify | L M | C:independent extension/stdio; publisher is not the browser vendor | [سند](https://docs.browsermcp.io) | PARTIALLY VERIFIED |


### 3. استخراج، پایش و RSS

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 023 [Firecrawl](https://firecrawl.dev) | جست‌وجو، scrape و crawl | F1 F3 · 1000 credits/month; search 2/10 results | A M L | O:remote/stdio | [سند](https://firecrawl.dev/pricing) · [شاهد](https://www.firecrawl.dev/pricing) | VERIFIED |
| 024 [Jina Reader](https://jina.ai) | URL به متن و جست‌وجوی وب | F0 F2 · Reader 20 RPM keyless; keyed 500 RPM; 10M initial tokens; Search 100 RPM on free key | A | C:adapter | [سند](https://jina.ai/reader) | VERIFIED |
| 025 [Scrapy](https://scrapy.org) | استخراج مجاز و pipeline HTML | F3 · local hardware; site limits | L | C:adapter | [سند](https://docs.scrapy.org/en/latest/) | VERIFIED |
| 026 [changedetection.io](https://changedetection.io) | پایش تغییر متن و قیمت صفحات | F3 · self-host resources | B L | C:adapter | [سند](https://github.com/dgtlmoon/changedetection.io) | VERIFIED |
| 027 [FreshRSS](https://freshrss.org) | خواندن RSS/Atom و تجمیع خبر | F3 · host resources and upstream feeds | A B R L | C:adapter | [سند](https://github.com/FreshRSS/FreshRSS) | VERIFIED |
| 028 [Miniflux](https://miniflux.app) | فید سبک و API وضعیت خبر | F3 · host resources | A B R L | C:adapter | [سند](https://miniflux.app/docs/api.html) | VERIFIED |


### 4. توسعه، Git و مستندات

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 029 [GitHub](https://github.com) | کد، repo، issues، releases و CI | F0 F1 F4 · REST core generally 60/h anonymous, 5000/h authenticated; Search separate | A B M L | O:remote/stdio Go | [سند](https://github.com/github/github-mcp-server) | PARTIALLY VERIFIED |
| 030 [GitLab](https://gitlab.com) | مخزن و pipeline جایگزین | F1 F3 F4 · Free service limits vary by offering; exact UNKNOWN here | A B L | O:server availability by plan verify | [سند](https://docs.gitlab.com/api/rest/) | PARTIALLY VERIFIED |
| 031 [Context7](https://context7.com) | بازیابی مستندات نسخه‌دار | F1 · 1000 API calls/month | A M L | O:remote/stdio Node | [سند](https://context7.com/pricing) | VERIFIED |
| 032 [MDN Web Docs](https://developer.mozilla.org) | مرجع وب، CSS و JS | F0 F4 · public docs; no numerical allowance | B L | C:adapter | [سند](https://github.com/mdn/content) | PARTIALLY VERIFIED |
| 033 [PyPI](https://pypi.org) | نسخه و metadata بسته Python | F0 F4 · public metadata; service limits apply | A B | C:adapter | [سند](https://docs.pypi.org/api/json/) | PARTIALLY VERIFIED |
| 034 [npm Registry](https://npmjs.com) | نسخه و وابستگی JS | F0 F4 · public metadata; exact quota UNKNOWN | A B L | C:adapter | [سند](https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md) | PARTIALLY VERIFIED |
| 035 [Stack Exchange API](https://stackexchange.com) | نمونه‌های حل مسئله و Q&A | F0 F1 F4 · default 10000/day by quota scheme; IP throttle 30/s | A B | C:adapter | [سند](https://api.stackexchange.com/docs/throttle) | PARTIALLY VERIFIED |


### 5. IDE و اجرای آنلاین

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 036 [GitHub Codespaces](https://github.com/features/codespaces) | IDE و محیط اجرای ابری توسعه | F1 F4 · personal Free 120 core-hours and 15 GB-month where eligible | B L | N | [سند](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) | VERIFIED |
| 037 [GitHub.dev](https://github.dev) | ویرایشگر وب مخزن و بررسی کد | F4 · browser editor; compute runtime separate | B | N | [سند](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor) | PARTIALLY VERIFIED |
| 038 [Google Colab](https://colab.research.google.com) | Notebook اجرای Python و داده نمونه | F1 F4 · dynamic resources; fixed free quota not guaranteed | B | N | [سند](https://research.google.com/colaboratory/faq.html) | PARTIALLY VERIFIED |
| 039 [Kaggle Notebooks](https://kaggle.com) | Notebook و داده عمومی | F1 F4 · compute quota varies; exact UNKNOWN | B | N | [سند](https://kaggle.com/docs/notebooks) · [شاهد](https://www.kaggle.com/docs/efficient-gpu-usage) | PARTIALLY VERIFIED |
| 040 [CodePen](https://codepen.io) | نمایش و آزمایش HTML/CSS/JS | F4 · free public pen limits UNKNOWN | B | N | [سند](https://codepen.io/features) | PARTIALLY VERIFIED |
| 041 [StackBlitz](https://stackblitz.com) | IDE وب و اجرای frontend | F4 · public/free feature limits as plan; exact UNKNOWN | B | N | [سند](https://stackblitz.com/pricing) | PARTIALLY VERIFIED |

### 6. Google Workspace

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 042 [Gmail](https://gmail.com) | خواندن ایمیل مجاز و جست‌وجوی پیام | F4 · API quota units 1200000/min project and 15000/min user; mailbox limits separate | A B M | O:remote developer preview | [سند](https://developers.google.com/workspace/gmail/api/reference/quota) | VERIFIED |
| 043 [Google Drive](https://drive.google.com) | فهرست فایل و بازخوانی سند مجاز | F1 F4 · Consumer storage 15 GB shared with Gmail/Photos; API quota separate | A B M | O:remote developer preview | [سند](https://developers.google.com/drive/api/guides/limits) | PARTIALLY VERIFIED |
| 044 [Google Docs](https://docs.google.com) | خواندن یا تنظیم ساختار اسناد | F4 · API rate quotas by project/user; exact not recorded | A B M | O:remote developer preview | [سند](https://developers.google.com/workspace/docs/api/limits) | PARTIALLY VERIFIED |
| 045 [Google Sheets](https://sheets.google.com) | گزارش جدولی و داده محدوده | F4 · 300 reads/min/project and 60/min/user; writes separate | A B M | O:remote developer preview | [سند](https://developers.google.com/workspace/sheets/api/limits) | VERIFIED |
| 046 [Google Calendar](https://calendar.google.com) | خواندن تقویم و availability | F4 · project/user quotas; exact account limit UNKNOWN | A B M | O:remote developer preview | [سند](https://developers.google.com/workspace/calendar/api/guides/quota) | PARTIALLY VERIFIED |
| 047 [Google People API](https://developers.google.com/people) | فهرست مخاطب با Scope محدود | F4 · API allowance UNKNOWN; Contacts UI free for account | A B | C:adapter; official Workspace MCP for Contacts not established | [سند](https://developers.google.com/people/api/rest) | PARTIALLY VERIFIED |
| 048 [Google Slides](https://slides.google.com) | خواندن ارائه و ساختار اسلاید | F4 · API quota by user/project; exact omitted | A B M | O:remote developer preview | [سند](https://developers.google.com/workspace/slides/api/limits) | PARTIALLY VERIFIED |


### 7. Microsoft Productivity

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 049 [Microsoft 365 for the web](https://microsoft.com/microsoft-365/free-office-online-for-the-web) | Word/Excel/PowerPoint در وب | F4 · free web apps; storage separate | B | N | [سند](https://support.microsoft.com/office) | PARTIALLY VERIFIED |
| 050 [Microsoft Graph](https://developer.microsoft.com/graph) | API مجاز فایل، ایمیل و تقویم | U · standard vs metered API endpoint-specific | A | C:adapter | [سند](https://learn.microsoft.com/en-us/graph/throttling) | PARTIALLY VERIFIED |
| 051 [Outlook.com](https://outlook.live.com) | ایمیل و تقویم تحت حساب Microsoft | F1 F4 · consumer email storage 15 GB published; account policy applies | A B | C:adapter via Graph | [سند](https://support.microsoft.com/office/storage-limits-in-outlook-com) · [شاهد](https://support.microsoft.com/en-us/outlook/storage-limits-in-outlook-com) | VERIFIED |
| 052 [OneDrive](https://onedrive.live.com) | خواندن فایل و لینک اشتراک | F1 F4 · 5 GB free storage | A B | C:adapter via Graph | [سند](https://microsoft.com/microsoft-365/onedrive/compare-onedrive-plans) · [شاهد](https://support.microsoft.com/en-us/onedrive/microsoft-storage-faqs) | VERIFIED |


### 8. مدیریت پروژه و دانش

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 053 [Notion](https://notion.com) | خواندن دانش و پروژه | F4 · Free workspace constraints; MCP allowance UNKNOWN | A B M | O:remote OAuth | [سند](https://developers.notion.com/docs/mcp) | PARTIALLY VERIFIED |
| 054 [Linear](https://linear.app) | کارها، مسئله و وضعیت تیم | F4 · Free 250 issues and 2 teams published; verify plan before use | A B M | O:remote OAuth | [سند](https://linear.app/pricing) | VERIFIED |
| 055 [Trello](https://trello.com) | خواندن کارت و وضعیت Kanban | F4 · Free workspace limits; exact current account allowance UNKNOWN | A B | C:adapter | [سند](https://trello.com/pricing) | PARTIALLY VERIFIED |
| 056 [Obsidian](https://obsidian.md) | دانش Markdown و ارجاع فایل محلی | U · Free proprietary desktop app. Local use falls outside F0–F4 | L | C:community; vault trust | [سند](https://help.obsidian.md) | PARTIALLY VERIFIED |
| 057 [Joplin](https://joplinapp.org) | یادداشت و جست‌وجوی پایگاه محلی | F3 · local files/storage | A L | C:adapter | [سند](https://joplinapp.org/help/api/references/rest_api/) | VERIFIED |


### 9. پایگاه داده و ذخیره

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 058 [Supabase](https://supabase.com) | Postgres، storage و API داده | F1 F3 · 500 MB DB/project, 1 GB file storage and 50000 MAU on Free; other limits separate | A B M L | O:remote project/read_only | [سند](https://supabase.com/pricing) | VERIFIED |
| 059 [Neon](https://neon.com) | Postgres مدیریت‌شده و branch | F1 · 100 CU-hours/month/project and 1 GB storage/project on Free | A B M | O:remote/stdio OAuth or key | [سند](https://neon.com/pricing) | VERIFIED |
| 060 [SQLite](https://sqlite.org) | تحلیل فایل داده با mode=ro | F3 · local disk/memory | L | C:adapter | [سند](https://sqlite.org/uri.html) | VERIFIED |
| 061 [DuckDB](https://duckdb.org) | SQL روی CSV/Parquet محلی | F3 · local disk/memory | L | C:adapter | [سند](https://duckdb.org/docs/stable/) | VERIFIED |
| 062 [Cloudflare R2](https://cloudflare.com/developer-platform/products/r2/) | خواندن و ذخیره object | F1 · standard 10 GB-month, 1M Class A, 10M Class B/month | A B M | O:Cloudflare tools; check R2 scopes | [سند](https://developers.cloudflare.com/r2/pricing/) | VERIFIED |


### 10. Cloud و پایش

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 063 [Cloudflare Workers](https://workers.cloudflare.com) | تابع edge و API سبک | F1 · 100000 requests/day Free; CPU limits separate | A B M | O:remote provider MCP | [سند](https://developers.cloudflare.com/workers/platform/pricing/) | VERIFIED |
| 064 [Vercel](https://vercel.com) | میزبانی سایت و dashboard | F1 F4 · Hobby allowances by metric; personal/non-commercial policy | A B M | O:remote approved clients | [سند](https://vercel.com/docs/plans/hobby) | PARTIALLY VERIFIED |
| 065 [Render](https://render.com) | اجرای demo و مشاهده logs | F1 · 750 free instance hours/month per workspace as documented | A B M | O:remote provider MCP | [سند](https://render.com/docs/free) | VERIFIED |
| 066 [Railway](https://railway.com) | میزبانی برنامه و logs | F1 F2 U · $5 trial for 30 days, then $1 monthly usage credit on Free | A B M L | O:remote/stdio via CLI | [سند](https://railway.com/pricing) | VERIFIED |
| 067 [GitHub Pages](https://pages.github.com) | سایت استاتیک و مستندات | F1 F4 · 1 GB published site; 100 GB/month soft bandwidth | B A | O:GitHub server; Pages actions verify | [سند](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) | VERIFIED |
| 068 [UptimeRobot](https://uptimerobot.com) | پایش uptime و خواندن وضعیت | F1 F4 · Free monitoring; exact current account limits UNKNOWN | A B | C:adapter | [سند](https://uptimerobot.com/pricing/) | PARTIALLY VERIFIED |
| 069 [Netlify](https://netlify.com) | میزبانی وب و build statics | F1 · 300 credits/month on credit-based Free | A B M | O:provider MCP; endpoint verify | [سند](https://netlify.com/pricing/) · [شاهد](https://www.netlify.com/pricing/) | VERIFIED |

### 11. استنتاج هوش مصنوعی

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 070 [Google Gemini API](https://ai.google.dev) | مدل متن و چندوجهی | F1 · Model/project-specific; live rate limits vary | A B | C:adapter; model API | [سند](https://ai.google.dev/gemini-api/docs/pricing) | PARTIALLY VERIFIED |
| 071 [OpenRouter](https://openrouter.ai) | مسیریابی مدل‌های رایگان | F1 · free variants 20 RPM; 50/day below 10 credits purchased; 1000/day after qualifying purchase | A B | C:adapter; model API | [سند](https://openrouter.ai/docs/api/reference/limits) | VERIFIED |
| 072 [GroqCloud](https://groq.com) | مدل متن و speech کم‌تأخیر | F1 · RPM/TPM/RPD by model and tier | A B | C:adapter | [سند](https://console.groq.com/docs/rate-limits) | PARTIALLY VERIFIED |
| 073 [Hugging Face Hub and Inference Providers](https://huggingface.co) | کشف مدل و اجرای inference میزبان | F0 F1 F4 · Hub limits by tier; Inference Free $0.10/month published | A B M | O:remote Hub MCP | [سند](https://huggingface.co/docs/inference-providers/pricing) | VERIFIED |
| 074 [Cloudflare Workers AI](https://cloudflare.com/developer-platform/products/workers-ai/) | مدل متن، vision و embeddings در edge | F1 · 10000 Neurons/day Free as documented | A B | C:adapter | [سند](https://developers.cloudflare.com/workers-ai/platform/pricing/) | VERIFIED |
| 075 [AI Horde](https://aihorde.net) | inference اشتراکی متن و تصویر | F0 · anonymous queue; dynamic availability, no fixed guaranteed quota | A B | C:adapter | [سند](https://aihorde.net/api/) | PARTIALLY VERIFIED |


### 12. گرافیک و تصویر

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 076 [GIMP](https://gimp.org) | ویرایش و تبدیل عکس محلی | F3 · local resources | L | C:adapter | [سند](https://gimp.org/docs/) · [شاهد](https://github.com/GNOME/gimp) | VERIFIED |
| 077 [Krita](https://krita.org) | نقاشی، layout و پردازش گرافیک | F3 · local resources | L | C:community | [سند](https://docs.krita.org/en/) | VERIFIED |
| 078 [Photopea](https://photopea.com) | ویرایش PSD و لایه در وب | F4 · free ad-supported UI; exact limits UNKNOWN | B | N | [سند](https://photopea.com/learn/) · [شاهد](https://www.photopea.com/api/) | PARTIALLY VERIFIED |
| 079 [Canva](https://canva.com) | طرح، ویدئو و تصویر تحت حساب | F4 · free template/editor; AI quotas feature-dependent | B M | O:remote; plan/scope verify | [سند](https://canva.com/pricing/) | PARTIALLY VERIFIED |
| 080 [Adobe Express](https://adobe.com/express/) | قالب گرافیک و ویدئو | F4 · Free feature and credit caps vary | B L | O:developer docs MCP, not editor access | [سند](https://adobe.com/express/pricing) | PARTIALLY VERIFIED |
| 081 [ComfyUI](https://comfy.org) | تولید تصویر با workflow محلی | F3 · model and GPU/RAM dependent | A B L | C:adapter | [سند](https://github.com/Comfy-Org/ComfyUI) | VERIFIED |
| 082 [Figma](https://figma.com) | خواندن طرح، component و design tokens | F4 · MCP calls by seat/plan; free UI separate | A B M | O:remote/desktop official | [سند](https://developers.figma.com/docs/figma-mcp-server/) | PARTIALLY VERIFIED |
| 083 [Penpot](https://penpot.app) | طراحی و مشاهده prototype متن‌باز | F3 F4 · cloud free feature limits; exact UNKNOWN | A B L | U: MCP status not established in this sweep | [سند](https://github.com/penpot/penpot) | PARTIALLY VERIFIED |


### 13. ویدئو

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 084 [FFmpeg](https://ffmpeg.org) | تبدیل، برش و استخراج صدا/فریم | F3 · local CPU/disk | L | C:adapter | [سند](https://ffmpeg.org/documentation.html) | VERIFIED |
| 085 [HandBrake](https://handbrake.fr) | فشرده‌سازی و تبدیل فایل ویدئو | F3 · local CPU/disk | L | C:adapter | [سند](https://handbrake.fr/docs/) | VERIFIED |
| 086 [Shotcut](https://shotcut.org) | ویرایش ویدئو با GUI محلی | F3 · local resources | L | N | [سند](https://shotcut.org/tutorials/) | VERIFIED |
| 087 [Clipchamp](https://clipchamp.com) | ویرایش و export ویدئو از مرورگر | F4 · free exports up to 1080p where listed | B | N | [سند](https://clipchamp.com/en/pricing/) | VERIFIED |
| 088 [YouTube Data API](https://youtube.com) | جست‌وجوی metadata و channel عمومی | F1 F4 · default project quota policy; search cost check quota calculator | A B | C:adapter | [سند](https://developers.google.com/youtube/v3/getting-started) | PARTIALLY VERIFIED |


### 14. صوت، گفتار و ترجمه

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 089 [Whisper](https://openai.com/research/whisper) | رونویسی و تشخیص زبان آفلاین | F3 · model-dependent resources | L | C:adapter | [سند](https://github.com/openai/whisper) | VERIFIED |
| 090 [Vosk](https://alphacephei.com/vosk/) | رونویسی سبک آفلاین | F3 · local CPU/model footprint | L | C:adapter | [سند](https://github.com/alphacep/vosk-api) | VERIFIED |
| 091 [Piper](https://github.com/OHF-Voice/piper1-gpl) | تولید گفتار با مدل محلی | F3 · local model; voice licensing varies | L | C:adapter | [سند](https://github.com/OHF-Voice/piper1-gpl) | VERIFIED |
| 092 [Audacity](https://audacityteam.org) | بررسی و ویرایش صوت محلی | F3 · local CPU/disk | L | N | [سند](https://manual.audacityteam.org) | VERIFIED |
| 093 [LibreTranslate](https://libretranslate.com) | ترجمه self-host با API | F3 · model and host dependent | A B L | C:adapter | [سند](https://github.com/LibreTranslate/LibreTranslate) | VERIFIED |


### 15. PDF، OCR و تبدیل

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 094 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | OCR تصویر و زبان فارسی با داده مدل | F3 · local CPU; language files separate | L | C:adapter | [سند](https://tesseract-ocr.github.io/tessdoc/) | VERIFIED |
| 095 [OCRmyPDF](https://ocrmypdf.readthedocs.io) | ساخت لایه متن برای PDF اسکن‌شده | F3 · local CPU; Tesseract and PDF dependencies | L | C:adapter | [سند](https://github.com/ocrmypdf/OCRmyPDF) | VERIFIED |
| 096 [PDF24 Tools](https://tools.pdf24.org) | فشرده‌سازی و تبدیل PDF از وب | F4 · free UI; quotas UNKNOWN | B | N | [سند](https://tools.pdf24.org/en/) | PARTIALLY VERIFIED |
| 097 [LibreOffice](https://libreoffice.org) | خواندن و تبدیل Office/PDF با CLI | F3 · local CPU/disk | L | C:adapter | [سند](https://help.libreoffice.org) | VERIFIED |
| 098 [PDF.js](https://mozilla.github.io/pdf.js/) | نمایش و بازیابی متن PDF | F3 · browser resources; scanned PDFs need OCR | B L | C:adapter | [سند](https://github.com/mozilla/pdf.js) | VERIFIED |

### 16. پژوهش دانشگاهی

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 099 [arXiv](https://arxiv.org) | پیش‌چاپ و جست‌وجوی علمی | F0 F4 · one request/3s, one connection | A B R | C:adapter | [سند](https://info.arxiv.org/help/api/tou.html) | VERIFIED |
| 100 [OpenAlex](https://openalex.org) | استناد و جست‌وجوی پژوهشی | F0 F1 F4 · $1/day keyed allowance; operation prices vary | A B | U: MCP status not established in this sweep | [سند](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication) | VERIFIED |
| 101 [Semantic Scholar](https://semanticscholar.org) | استناد و metadata مقاله | F0 F4 · initial key 1 RPS; public shared capacity | A B | C:adapter | [سند](https://semanticscholar.org/product/api) · [شاهد](https://www.semanticscholar.org/product/api) | PARTIALLY VERIFIED |
| 102 [Crossref](https://crossref.org) | DOI و شناسه مقاله | F0 · public/polite by route; response headers govern | A | C:adapter | [سند](https://crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/) · [شاهد](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication) | PARTIALLY VERIFIED |
| 103 [Europe PMC](https://europepmc.org) | جست‌وجوی متون زیست‌پزشکی و OA | F0 F4 · numeric cap UNKNOWN | A B | C:adapter | [سند](https://europepmc.org/RestfulWebService) · [شاهد](https://staging.europepmc.org/RestfulWebService) | PARTIALLY VERIFIED |
| 104 [PubMed / NCBI E-utilities](https://pubmed.ncbi.nlm.nih.gov) | جست‌وجوی مقالات و metadata | F0 F4 · 3/s keyless and 10/s standard key | A B | C:adapter | [سند](https://ncbi.nlm.nih.gov/books/NBK25497/) · [شاهد](https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/) | VERIFIED |
| 105 [DOAJ](https://doaj.org) | مجلات و مقاله‌های دسترسی آزاد | F0 F4 · public read; exact quotas UNKNOWN | A B | C:adapter | [سند](https://doaj.org/api/) | UNVERIFIED |


### 17. بازار و اقتصاد

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 106 [CoinGecko](https://coingecko.com) | قیمت و metadata کریپتو | F1 F4 · 10000 calls/month Demo; 100 RPM published | A B M | U: provider MCP entitlement/endpoint not established | [سند](https://coingecko.com/en/api/pricing) · [شاهد](https://www.coingecko.com/en/api/pricing) | VERIFIED |
| 107 [Kraken public market data](https://kraken.com) | کندل عمومی و بازار | F0 · up to 720 recent OHLC; open candle included | A B | C:adapter | [سند](https://docs.kraken.com/api/docs/rest-api/get-ohlc-data/) | VERIFIED |
| 108 [FRED](https://fred.stlouisfed.org) | سری‌های اقتصادی و نرخ بهره | F4 · API key requested free; exact current allowance UNKNOWN | A B | C:adapter | [سند](https://fred.stlouisfed.org/docs/api/fred/) | PARTIALLY VERIFIED |
| 109 [Alpha Vantage](https://alphavantage.co) | داده سهام و FX برای پژوهش | F1 · Free numerical allowance pending official support page verification | A | C:adapter | [سند](https://alphavantage.co/support/) | UNVERIFIED |
| 110 [World Bank Indicators API](https://data.worldbank.org) | شاخص توسعه و اقتصاد کشورها | F0 F4 · public; numeric cap UNKNOWN | A B | C:adapter | [سند](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) | PARTIALLY VERIFIED |
| 111 [Coinbase Exchange Market Data](https://coinbase.com) | کندل و داده عمومی بازار | F0 · max 300 candles per request | A | C:adapter | [سند](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles) | VERIFIED |


### 18. نقشه و GIS

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 112 [OpenStreetMap Nominatim](https://nominatim.org) | جست‌وجوی نام مکان و geocoding | F0 F3 F4 · public server absolute max 1 request/s; policy limits | A B L | C:adapter | [سند](https://operations.osmfoundation.org/policies/nominatim/) | VERIFIED |
| 113 [Overpass API](https://overpass-api.de) | گرفتن POI و داده OSM | F0 F3 · public limits depend on instance | A L | C:adapter | [سند](https://wiki.openstreetmap.org/wiki/Overpass_API) | PARTIALLY VERIFIED |
| 114 [QGIS](https://qgis.org) | تحلیل GIS و لایه محلی | F3 · local RAM and dataset size | L | C:adapter | [سند](https://docs.qgis.org/) | VERIFIED |
| 115 [Natural Earth](https://naturalearthdata.com) | لایه‌های نقشهٔ عمومی | F0 · public downloads | B L | N | [سند](https://naturalearthdata.com/about/terms-of-use/) | UNVERIFIED |


### 19. امنیت دفاعی

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 116 [OSV.dev](https://osv.dev) | تطبیق dependency با advisory | F0 · public query API; quota UNKNOWN | A B | C:adapter | [سند](https://google.github.io/osv.dev/api/) | PARTIALLY VERIFIED |
| 117 [GitHub Advisory Database](https://github.com/advisories) | شناسایی هشدار و نسخه اصلاح‌شده | F0 F4 · GitHub REST quotas apply | A B | O:potential through GitHub MCP; advisory tool availability UNKNOWN | [سند](https://docs.github.com/en/rest/security-advisories/global-advisories) | PARTIALLY VERIFIED |
| 118 [NVD](https://nvd.nist.gov) | CVE و CVSS برای اولویت‌بندی وصله | F0 F4 · 5 requests/30s keyless; 50/30s with key | A B | C:adapter | [سند](https://nvd.nist.gov/developers/start-here) | VERIFIED |
| 119 [Trivy](https://trivy.dev) | اسکن دفاعی dependency و image | F3 · local downloads and CPU; DB refresh | L | C:adapter | [سند](https://trivy.dev/latest/docs/) | VERIFIED |


### 20. بازاریابی، SEO و تحلیل

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 120 [Google Trends](https://trends.google.com) | روند نسبی جست‌وجو و مقایسه موضوع | F4 · free UI; API availability/quotas separate | B | N | [سند](https://support.google.com/trends/) | PARTIALLY VERIFIED |
| 121 [Google Search Console](https://search.google.com/search-console) | داده عملکرد سایت متعلق به کاربر | F4 · search analytics and URL inspection quotas differ | A B | C:adapter | [سند](https://developers.google.com/webmaster-tools/limits) | PARTIALLY VERIFIED |
| 122 [Google Analytics 4](https://analytics.google.com) | گزارش رویداد و تحلیل سایت مجاز | F4 · standard token quotas by property; exact endpoint-specific | A B M | O:Google analytics MCP; scopes verify | [سند](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas) | PARTIALLY VERIFIED |
| 123 [Matomo](https://matomo.org) | تحلیل سایت self-host و گزارش | F3 · host resources; privacy config | A B L | C:adapter | [سند](https://developer.matomo.org/api-reference/reporting-api) | VERIFIED |
| 124 [Bing Webmaster Tools](https://bing.com/webmasters) | گزارش index و SEO سایت مجاز | F4 · free site tools; API quotas UNKNOWN | A B | C:adapter | [سند](https://learn.microsoft.com/en-us/bingwebmaster/) | PARTIALLY VERIFIED |

### 21. کالا و شرکت

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 125 [Open Food Facts](https://openfoodfacts.org) | کاتالوگ بارکد و محصول غذایی | F0 F4 · limits by product/search/facet endpoint | A B | C:adapter | [سند](https://openfoodfacts.github.io/openfoodfacts-server/api/) | PARTIALLY VERIFIED |
| 126 [eBay Browse API](https://ebay.com) | جست‌وجوی کالای بازار و قیمت اعلامی | F4 U · API access and production quota depend on approval | A B | C:adapter | [سند](https://developer.ebay.com/api-docs/buy/browse/overview.html) | PARTIALLY VERIFIED |
| 127 [OpenCorporates](https://opencorporates.com) | اطلاعات عمومی شرکت و شناسه ثبت | F4 U · public UI; free API eligibility for specific users/projects | A B | C:adapter | [سند](https://api.opencorporates.com/documentation/API-Reference) | PARTIALLY VERIFIED |
| 128 [GLEIF LEI API](https://gleif.org) | شناسه حقوقی شرکت و رابطه سازمانی | F0 F4 · public API; numeric quota UNKNOWN | A B | C:adapter | [سند](https://gleif.org/en/lei-data/gleif-api) · [شاهد](https://www.gleif.org/en/lei-data/gleif-api) | PARTIALLY VERIFIED |


### 22. ارتباط و گردش‌کار

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 129 [Slack](https://slack.com) | جست‌وجوی همکاری و خواندن کانال مجاز | F4 · 90-day visible history on Free; API limits separate | A B M | U: MCP status not established in this sweep | [سند](https://slack.com/pricing) | VERIFIED |
| 130 [Discord](https://discord.com) | خواندن کانال با bot مجاز | F4 · route-specific API limits from headers | A B | C:adapter | [سند](https://discord.com/developers/docs/topics/rate-limits) | PARTIALLY VERIFIED |
| 131 [Telegram Bot API](https://telegram.org) | دریافت اعلان با Bot رسمی | F4 · standard Bot API limits; paid broadcast optional | A B | C:adapter | [سند](https://core.telegram.org/bots/api) | PARTIALLY VERIFIED |
| 132 [n8n Community Edition](https://n8n.io) | جریان کاری و خواندن/تبدیل داده | F2 U · Community Edition self-host under Sustainable Use License; Cloud trial separate | A B L M | O:instance MCP; version/scope verify | [سند](https://docs.n8n.io/hosting/community-edition-features/) | PARTIALLY VERIFIED |
| 133 [Node-RED](https://nodered.org) | جریان HTTP و تبدیل داده روی Node | F3 · local resources | A B L | C:adapter | [سند](https://nodered.org/docs/) | VERIFIED |


### 23. داده عمومی و آمار

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 134 [Wikidata Query Service](https://wikidata.org) | دانش ساختاری و شناسه‌ها | F0 F4 · public SPARQL time and rate constraints | A B | C:adapter | [سند](https://wikidata.org/wiki/Wikidata:SPARQL_query_service) · [شاهد](https://www.wikidata.org/wiki/Wikidata%3AData_access/en) | PARTIALLY VERIFIED |
| 135 [Data.gov Catalog](https://data.gov) | کشف مجموعه‌های عمومی آمریکا | F0 F4 · catalog public; upstream data limits vary | A B | C:adapter | [سند](https://resources.data.gov/resources/datagov/) · [شاهد](https://resources.data.gov/catalog-api-interactive/) | PARTIALLY VERIFIED |
| 136 [Eurostat API](https://ec.europa.eu/eurostat) | آمار رسمی اروپا | F0 F4 · public; large query restrictions | A B | C:adapter | [سند](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access) | PARTIALLY VERIFIED |
| 137 [Our World in Data](https://ourworldindata.org) | داده و نمودار توسعه جهانی | F0 F4 · public access; numeric allowance UNKNOWN | A B | C:adapter | [سند](https://docs.owid.io/projects/etl/api/) | PARTIALLY VERIFIED |
| 138 [Open-Meteo](https://open-meteo.com) | داده هواشناسی و پیش‌بینی JSON | F0 F1 F3 · 10000/day and 300000/month, non-commercial Free | A B L | C:adapter | [سند](https://open-meteo.com/en/pricing) | VERIFIED |


### 24. ویندوز و مدیریت سیستم

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 139 [PowerShell](https://learn.microsoft.com/powershell) | خواندن counters و diagnostics ویندوز | F3 · local resources | L | C:adapter | [سند](https://github.com/PowerShell/PowerShell) | VERIFIED |
| 140 [Microsoft Sysinternals](https://learn.microsoft.com/sysinternals) | مشاهده process و فایل و diagnostics | U · free proprietary download; local resource limits | L | N | [سند](https://learn.microsoft.com/en-us/sysinternals/downloads/) | PARTIALLY VERIFIED |
| 141 [Power Automate Desktop](https://powerautomate.microsoft.com) | اتوماسیون attended ویندوز | U · entitlement depends on Windows/account/feature | L | N | [سند](https://learn.microsoft.com/en-us/power-automate/desktop-flows/requirements) | PARTIALLY VERIFIED |
| 142 [AutoHotkey](https://autohotkey.com) | کارهای تکراری GUI و hotkey | F3 · local resources | L | C:adapter | [سند](https://github.com/AutoHotkey/AutoHotkey) | VERIFIED |


### 25. ابزارها و استانداردهای MCP

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 143 [Official MCP Registry](https://registry.modelcontextprotocol.io) | جست‌وجوی publisher و metadata ابزار | F0 F3 · public discovery; exact cap UNKNOWN | A B L | N | [سند](https://github.com/modelcontextprotocol/registry) | PARTIALLY VERIFIED |
| 144 [MCP Inspector](https://modelcontextprotocol.io) | دیدن schema و discovery در محیط بررسی | F3 · local Node/runtime | B L | Utility, not a service server | [سند](https://github.com/modelcontextprotocol/inspector) | VERIFIED |
| 145 [MCP Reference Filesystem Server](https://modelcontextprotocol.io) | خواندن فایل در مسیر allowlist | F3 · local Node/RAM | L M | O:reference stdio Node | [سند](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) · [شاهد](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) | VERIFIED |
| 146 [Agent Skills](https://agentskills.io) | تعریف workflow و دستور قابل استفاده مجدد | F3 · local spec/files; execution resources depend on skill | B L | N | [سند](https://agentskills.io/specification) | VERIFIED |

### 26. آرشیو و منابع باز

| شناسه و سرویس | کار عامل | رده و سهمیه | مسیر | MCP | مدرک | وضعیت |
| --- | --- | --- | --- | --- | --- | --- |
| 147 [Internet Archive Wayback Machine](https://web.archive.org) | نسخه تاریخی صفحه و evidence URL | F0 F4 · public availability endpoint; numeric quota UNKNOWN | A B | C:adapter | [سند](https://archive.org/help/wayback_api.php) | PARTIALLY VERIFIED |
| 148 [Common Crawl](https://commoncrawl.org) | داده crawl عمومی برای پژوهش | F0 · public index/datasets; own compute limits | A B | C:adapter | [سند](https://commoncrawl.org/get-started) | PARTIALLY VERIFIED |
| 149 [Open Library](https://openlibrary.org) | metadata کتاب و ISBN | F0 F4 · public API; traffic policy and identification apply | A B | C:adapter | [سند](https://openlibrary.org/developers/api) | PARTIALLY VERIFIED |
| 150 [Wikimedia Commons](https://commons.wikimedia.org) | یافتن تصویر و metadata مجوز | F0 F4 · public API with limits and User-Agent policy | A B | C:adapter | [سند](https://mediawiki.org/wiki/API:Main_page) | UNVERIFIED |
| 151 [Openverse](https://openverse.org) | کشف تصویر/صوت با مجوز باز | F0 F4 · public or authenticated rate limit tiers | A B | C:adapter | [سند](https://api.openverse.org/v1/) | UNVERIFIED |

## B — مقایسهٔ جست‌وجو و پژوهش

| نیاز | گزینه‌ها | تفاوت |
| --- | --- | --- |
| جست‌وجوی موردی | Google، Bing، DuckDuckGo و Marginalia | مرور وب برای کشف و مراجعه به سند. CAPTCHA یا منع اتوماسیون، شرط توقف است. |
| جست‌وجوی ساختاری وب | Tavily، Exa و Firecrawl | Tavily basic یک credit و advanced دو. Exa Lite پایه $4/1000. Firecrawl search دو credit در ده نتیجه؛ scrape موجودی مشترک. |
| Google SERP و چند موتور | Serper، SearchAPI.io و SerpApi | ۲۵۰۰ query آغازین، ۱۰۰ query آغازین و ۲۵۰ search ماهانه، به‌ترتیب. اعتبار شروع را به‌عنوان quota تکرارشونده حساب نکن. |
| شاخص مستقل | Brave Search API و SearXNG | Brave $5 اعتبار ماهانه با کارت. SearXNG self-host و وابسته به Terms و rate limit موتورهای بالادست. |
| MCP عمومی | Parallel؛ hosted Exa در صورت عرضه و شرایط مجاز | سقف دقیق keyless UNKNOWN. Parallel API کارت‌دار بعد از اعتبار ماهانه می‌تواند هزینه داشته باشد. |
| URL معلوم | HTTP، RSS، Jina Reader، Firecrawl | خواندن منبع مستقیم از API جست‌وجو بی‌نیاز است. Jina Reader بدون کلید؛ Search کلیددار. برای استخراج چندصفحه‌ای هزینهٔ واحدها را بررسی کن. |
| پژوهش علمی | arXiv، Crossref، OpenAlex، Semantic Scholar، Europe PMC و PubMed | پیش‌چاپ، DOI، citation graph و زیست‌پزشکی پوشش متفاوت دارند. حقوق متن کامل جداست. |
| مسیرهای پایان‌یافته | Bing Search APIs؛ Google Custom Search JSON API | Bing API در ۲۰۲۵ بازنشسته شد. Custom Search برای مشتری جدید بسته و تاریخ پایان اعلام‌شده ۱ ژانویه ۲۰۲۷ است. |

## C — دایرکتوری MCP

| سرویس و سند | ناشر و مسیر | کاربرد و Scope | بدیل |
| --- | --- | --- | --- |
| 001 [Tavily](https://docs.tavily.com/documentation/mcp) | O:remote/stdio | جست‌وجوی وب و استخراج · key/account; no card | Exa |
| 002 [Exa](https://github.com/exa-labs/exa-mcp-server) | O:remote/stdio | جست‌وجوی معنایی و متن نتایج · key/account; free no card | Tavily |
| 004 [SerpApi](https://github.com/serpapi/serpapi-mcp) | O:remote/stdio | نتایج ساختاری چند موتور · key/account; no card on Free | Serper |
| 007 [Parallel Search](https://parallel.ai/pricing) | O:remote | جست‌وجو و استخراج شواهد وب · public MCP keyless; API key/card | Exa |
| 014 [Playwright](https://github.com/microsoft/playwright-mcp) | O:stdio Node | مرور DOM، snapshot و کار تکراری · local Node/browser; no service account | Selenium |
| 015 [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | O:stdio Node | خواندن console و performance مرورگر · Node + Chrome; browser consent for attach | Playwright |
| 016 [Browser Use](https://github.com/browser-use/browser-use) | O:remote Cloud; verify plan | اتوماسیون مرحله‌ای با Python · Python/browser; model credentials if applicable | Playwright |
| 017 [BrowserOS](https://github.com/browseros-ai/BrowserOS) | O:local; endpoint version dependent | مرورگر agent و ابزارهای ناوبری · separate browser; accounts per site | OpenMausBot browser |
| 019 [Browserbase](https://github.com/browserbase/mcp-server-browserbase) | O:provider MCP; scope verify | مرورگر ابری Playwright/CDP · account/key; card UNKNOWN | Browserless |
| 022 [Browser MCP](https://docs.browsermcp.io) | C:independent extension/stdio; publisher is not the browser vendor | کنترل مرورگر موجود با افزونه · extension and local process | Playwright |
| 023 [Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server) | O:remote/stdio | جست‌وجو، scrape و crawl · cloud key/account; free no card | Jina Reader |
| 029 [GitHub](https://github.com/github/github-mcp-server) | O:remote/stdio Go | کد، repo، issues، releases و CI · public UI; token/OAuth for private | GitLab |
| 030 [GitLab](https://docs.gitlab.com/api/rest/) | O:server availability by plan verify | مخزن و pipeline جایگزین · account for private; token for API | GitHub |
| 031 [Context7](https://github.com/upstash/context7) | O:remote/stdio Node | بازیابی مستندات نسخه‌دار · key/account for quota; keyless MCP limits UNKNOWN | official docs |
| 042 [Gmail](https://developers.google.com/workspace/mcp) | O:remote developer preview | خواندن ایمیل مجاز و جست‌وجوی پیام · Google account/OAuth | Outlook |
| 043 [Google Drive](https://developers.google.com/workspace/mcp) | O:remote developer preview | فهرست فایل و بازخوانی سند مجاز · Google account/OAuth | OneDrive |
| 044 [Google Docs](https://developers.google.com/workspace/mcp) | O:remote developer preview | خواندن یا تنظیم ساختار اسناد · Google account/OAuth; public links when enabled | Word for Web |
| 045 [Google Sheets](https://developers.google.com/workspace/mcp) | O:remote developer preview | گزارش جدولی و داده محدوده · Google account/OAuth | Excel for Web |
| 046 [Google Calendar](https://developers.google.com/workspace/mcp) | O:remote developer preview | خواندن تقویم و availability · Google account/OAuth | Outlook |
| 048 [Google Slides](https://developers.google.com/workspace/mcp) | O:remote developer preview | خواندن ارائه و ساختار اسلاید · Google OAuth; public link if allowed | PowerPoint for Web |
| 053 [Notion](https://developers.notion.com/docs/mcp) | O:remote OAuth | خواندن دانش و پروژه · account/OAuth; permission mirrors workspace | Obsidian |
| 054 [Linear](https://linear.app/docs/mcp) | O:remote OAuth | کارها، مسئله و وضعیت تیم · account/OAuth | Trello |
| 058 [Supabase](https://supabase.com/docs/guides/getting-started/mcp) | O:remote project/read_only | Postgres، storage و API داده · account; project key/OAuth | Neon |
| 059 [Neon](https://neon.com/docs/ai/neon-mcp-server) | O:remote/stdio OAuth or key | Postgres مدیریت‌شده و branch · account and credentials | Supabase |
| 062 [Cloudflare R2](https://developers.cloudflare.com/r2/pricing/) | O:Cloudflare tools; check R2 scopes | خواندن و ذخیره object · account and billing setup; S3 credentials | Supabase Storage |
| 063 [Cloudflare Workers](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/) | O:remote provider MCP | تابع edge و API سبک · Cloudflare account | Deno Deploy |
| 064 [Vercel](https://vercel.com/docs/mcp/vercel-mcp) | O:remote approved clients | میزبانی سایت و dashboard · account/OAuth | Cloudflare Pages |
| 065 [Render](https://render.com/docs/mcp-server) | O:remote provider MCP | اجرای demo و مشاهده logs · account; card policy UNKNOWN | Koyeb |
| 066 [Railway](https://docs.railway.com/ai/mcp-server) | O:remote/stdio via CLI | میزبانی برنامه و logs · account; verification and payment policy | Render |
| 067 [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) | O:GitHub server; Pages actions verify | سایت استاتیک و مستندات · GitHub account; public repo on Free | Cloudflare Pages |
| 069 [Netlify](https://netlify.com/pricing/) | O:provider MCP; endpoint verify | میزبانی وب و build statics · account; billing policy by plan | Cloudflare Pages |
| 073 [Hugging Face Hub and Inference Providers](https://huggingface.co/docs/hub/hf-mcp-server) | O:remote Hub MCP | کشف مدل و اجرای inference میزبان · public Hub keyless; inference account/token | OpenRouter |
| 079 [Canva](https://www.canva.dev/docs/connect/) | O:remote; plan/scope verify | طرح، ویدئو و تصویر تحت حساب · account; OAuth for integration | Adobe Express |
| 080 [Adobe Express](https://developer.adobe.com/express/add-ons/) | O:developer docs MCP, not editor access | قالب گرافیک و ویدئو · account | Canva |
| 082 [Figma](https://developers.figma.com/docs/figma-mcp-server/) | O:remote/desktop official | خواندن طرح، component و design tokens · account and OAuth; desktop option plan-dependent | Penpot |
| 117 [GitHub Advisory Database](https://docs.github.com/en/rest/security-advisories/global-advisories) | O:potential through GitHub MCP; advisory tool availability UNKNOWN | شناسایی هشدار و نسخه اصلاح‌شده · anonymous public read or token | OSV.dev |
| 122 [Google Analytics 4](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas) | O:Google analytics MCP; scopes verify | گزارش رویداد و تحلیل سایت مجاز · account/OAuth and property permission | Matomo |
| 132 [n8n Community Edition](https://docs.n8n.io/advanced-ai/accessing-n8n-mcp-server/) | O:instance MCP; version/scope verify | جریان کاری و خواندن/تبدیل داده · self-host; integration credentials separately | Node-RED |
| 145 [MCP Reference Filesystem Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | O:reference stdio Node | خواندن فایل در مسیر allowlist · local process and directory scopes | PowerShell read-only |

برای کشف ناشر و نسخه از [Official MCP Registry](https://registry.modelcontextprotocol.io/)، [سرورهای مرجع MCP](https://github.com/modelcontextprotocol/servers)، [GitHub MCP Registry](https://github.com/mcp) و [MCP Inspector](https://github.com/modelcontextprotocol/inspector) استفاده شود. ثبت در دایرکتوری به معنی ممیزی مجوز، نگهداری، دسترسی حساب یا اعتبار annotation ابزار نیست. Playwright و Chrome DevTools روی Node/stdio و مرورگر اجرا می‌شوند. Browser MCP افزونه و runtime محلی دارد. برای APIهای ساده، HTTPS مستقیم یا UI رسمی بدیل کم‌وابستگی است.

## D — سرویس‌های مرورگری رایگان

- **پژوهش و شواهد** Google، Bing، GitHub، MDN، arXiv، Google Trends، Wayback و Open Library.
- **اسناد و همکاری** Microsoft 365 Web، Google Docs/Sheets/Slides، Notion، Trello، Linear، Slack. ورود به حساب و داده خصوصی تابع Scope است.
- **گرافیک و رسانه** Photopea، Canva، Adobe Express، Clipchamp و PDF24. طرح‌های premium و محدودیت export را از قابلیت پایه جدا بخوان. شرایط upload و پردازش فایل مشتری باید روشن باشد.
- **UI در کنار API متری یا محدود** Google/Bing Search، OpenCorporates، eBay، Figma و Vercel. برای جست‌وجوی موردی یا خواندن داشبورد ارزش دارند. مجوز استفاده برنامه‌ای و بازنشر تابع Terms است.
- **API-free** Browser داخلی برای صفحه عمومی و JS. HTTP، RSS و دانلود dataset رسمی برای خروجی ساختاری. CLI/SDK محلی برای پردازش فایل. HTTP عمومی در صورت نیاز از rate limit، cache و شرایط منبع پیروی کند.

## E — توسعه رایگان

GitHub و رجیستری‌های PyPI/npm برای کد و metadata، MDN و Context7 برای مستندات، GitHub.dev و CodePen برای مرور/ویرایش سبک، Codespaces/Colab/Kaggle برای compute مشروط به quota. GitHub Actions برای خواندن CI در scope مجاز و OSV/NVD برای بررسی دفاعی dependency. ظرفیت cloud و دسترسی کد خصوصی برای هر حساب مستقل‌اند.

## F — قابلیت‌های تخصصی

| کار | مسیر کم‌هزینه | محدودیت تعیین‌کننده |
|---|---|---|
| کندل، سری زمانی و آمار | Kraken/Coinbase، World Bank، FRED | تاریخچه، کندل جاری و حق بازنشر |
| صوت، گفتار، ترجمه | Whisper/Vosk، Piper، LibreTranslate | کیفیت فارسی، مدل زبان، CPU و مجوز |
| PDF و ویدئو | PDF.js، Tesseract، OCRmyPDF، FFmpeg | OCR برای اسکن، codec و حجم فایل |
| نقشه و داده | QGIS، Natural Earth، Nominatim/Overpass | سقف نرخ، مختصات حساس و ODbL |
| تحلیل و شرکت | Google Trends، Search Console، GLEIF، Open Food Facts | property مجاز، شرایط بازنشر، محدودیت دادهٔ تجاری |
| امنیت دفاعی | OSV، NVD، Trivy | تطبیق اکوسیستم و تازگی advisory |
| گردش‌کار | RSS، Node-RED، Telegram Bot API | scope کانال و اثر بیرونی هر عملیات |

## G — گزینه‌های اول هر حوزه

| حوزه | نامزدهای اول پژوهشی | تعداد رکورد |
| --- | --- | --- |
| جست‌وجوی وب و پژوهش | DuckDuckGo، SearXNG، Tavily/Exa مشروط به احراز شرایط | 13 |
| مرورگر، CDP و RPA | OpenMausBot Browser، Playwright، Chrome DevTools MCP | 9 |
| استخراج، پایش و RSS | FreshRSS/Miniflux، Jina Reader، Firecrawl | 6 |
| توسعه، Git و مستندات | MDN، GitHub، Context7، PyPI/npm | 7 |
| IDE و اجرای آنلاین | GitHub.dev، CodePen، Colab/Kaggle برای Python | 6 |
| Google Workspace | Gmail و Drive/Sheets با حساب مجاز، REST با Scope خواندن | 7 |
| Microsoft Productivity | Microsoft 365 Web، Outlook و OneDrive، Graph برای خواندن ساختاری | 4 |
| مدیریت پروژه و دانش | Notion، Joplin، Linear | 5 |
| پایگاه داده و ذخیره | SQLite، DuckDB، Neon یا Supabase به شرط نیاز به سرویس راه‌دور | 5 |
| Cloud و پایش | GitHub Pages، Cloudflare Workers، Render، UptimeRobot | 7 |
| استنتاج هوش مصنوعی | AI Horde، OpenRouter، Hugging Face Hub؛ اجرای inference مشروط به حساب و مجوز | 6 |
| گرافیک و تصویر | Photopea، GIMP، Figma برای مشاهده طرح | 8 |
| ویدئو | FFmpeg، HandBrake، Clipchamp | 5 |
| صوت، گفتار و ترجمه | Vosk، Whisper، Piper، LibreTranslate | 5 |
| PDF، OCR و تبدیل | PDF.js، Tesseract، LibreOffice | 5 |
| پژوهش دانشگاهی | arXiv، Crossref، Europe PMC، OpenAlex | 7 |
| بازار و اقتصاد | Kraken و World Bank؛ CoinGecko برای کشف دارایی | 6 |
| نقشه و GIS | Natural Earth، QGIS، Nominatim برای lookup کم‌حجم | 4 |
| امنیت دفاعی | OSV، GitHub Advisory Database، NVD | 4 |
| بازاریابی، SEO و تحلیل | Google Trends، Search Console، Matomo | 5 |
| کالا و شرکت | Open Food Facts، GLEIF، eBay برای مرور دستی | 4 |
| ارتباط و گردش‌کار | Telegram Bot API با رضایت، Slack با Scope، Node-RED | 5 |
| داده عمومی و آمار | World Bank/EU data، Wikidata، Open-Meteo برای مصرف مجاز | 5 |
| ویندوز و مدیریت سیستم | PowerShell، Sysinternals | 4 |
| ابزارها و استانداردهای MCP | MCP Registry، MCP Inspector، Agent Skills | 4 |
| آرشیو و منابع باز | Wayback Machine، Wikimedia Commons، Open Library | 5 |

## H — مسیرهای OpenMausBot 0.1.152

| مسیر | سازوکار و محدودیت |
|---|---|
| Browser داخلی | ابزار همراه میزبان برای URL رسمی و snapshot. گردش‌کار هر سرویس و دسترسی نشست زنده UNVERIFIED. |
| HTTP/RSS/SDK | endpoint یا فید رسمی از ابزار شبکهٔ مجاز Codex. مسیر CLI با Python/Node/PowerShell در صورت دسترسی مجاز. شبکهٔ هر بات UNVERIFIED. |
| Remote MCP | Plugins → MCP servers → Add server، URL رسمی Streamable HTTP یا SSE در صورت مستندبودن، سپس Bot access. تعریف server می‌تواند برای بات‌های مجاز مشترک باشد. quota و credential مشترک تابع ارائه‌دهنده‌اند. |
| Local MCP | همان بخش با command/stdio و runtime سازگار Windows. یک تعریف مشترک به معنی یک پردازهٔ مشترک بین turnها نیست. هزینهٔ واقعی RAM UNKNOWN. |
| Google Workspace MCP | Developer Preview با Scope محصول. از ۱۱ نوامبر ۲۰۲۶ الزام علامت‌گذاری OAuth client به‌عنوان agentic اعلام شده. سازگاری OAuth نسخهٔ نصب‌شده UNVERIFIED. UI و REST مسیرهای مستقل‌اند. |
| GitHub / Notion / Linear | endpoint رسمی و OAuth یا credential محدود. GitHub read-only و toolsets در صورت پشتیبانی مسیر. دسترسی به workspace یا repo خصوصی از مجوز حساب می‌آید. |
| Figma و Vercel | Figma سهمیهٔ MCP وابسته به seat/plan. Vercel ممکن است فقط client تأییدشده را بپذیرد. سازگاری OpenMausBot تأیید نشده. |

[مستند OpenMausBot](https://github.com/milind-soni/OpenMausBot/blob/main/docs/custom-mcp-servers.md) · [یادداشت‌های Workspace](https://developers.google.com/workspace/release-notes). افزونهٔ ChatGPT یا کارت نمایش‌داده‌شده در میزبان، معادل دسترسی مؤثر همان ابزار برای بات نیست.

## I — سهمیه و ایران

| وضعیت | نمونه و معنی |
|---|---|
| عمومی بدون کلید | arXiv، Crossref، World Bank، OSV، Kraken و GLEIF. rate limit، حقوق محتوا و دسترسی از ایران جداگانه بررسی شود. |
| دوره‌ای بدون کارت اعلام‌شده | Tavily، Exa، Firecrawl و SerpApi. استفاده حساب ایران احراز نشده. |
| اعتبار همراه کارت یا billing | Brave و Parallel API، همچنین Cloudflare R2 در مسیر billing. مبلغ hold، cap و overage مستقل‌اند. |
| اعتبار شروع | Serper، SearchAPI.io، توکن آغازین Jina و دوره آزمایشی Railway. طرح Free دوره‌ای Railway در ردیف خودش تفکیک شده است. |
| مدرک منطقه‌ای | ایران در فهرست Gemini API نیست. GitHub مجوز اعلام‌شده برای ارائه خدمات ابری به توسعه‌دهندگان ایران دارد. شرایط محصول و billing مستقل است. |
| بدیل مستقل از حساب ابری | RSS عمومی، SQLite/DuckDB، Tesseract/GIMP و اجرای محلی. دسترسی دانلود و Terms منبع همچنان برقرار است. |

واحدهای credit، request، token، result، browser-hour و storage متفاوت‌اند. شرایط کارت، reset، هزینه اضافه، eligibility، حق استفاده تجاری و حق بازنشر برای همهٔ نامزدها به‌طور کامل اثبات نشده‌اند. مقدار مجهول در گزارش **UNKNOWN/DENY** برای فعال‌سازی است.

## J — پوشش و موارد باز

- **151 گزینهٔ یکتا در ۲۶ حوزه** · 77 VERIFIED · 68 PARTIALLY VERIFIED · 6 UNVERIFIED.
- برچسب‌های هم‌پوشان · F0: 39 · F1: 38 · F2: 7 · F3: 48 · F4: 72 · P: 1 · U: 10. یک رکورد P برای Google Custom Search JSON API ثبت شد. Bing Search API بازنشسته است و Bing UI به‌عنوان قابلیت مستقل در کاتالوگ ماند.
- **UNVERIFIED** Marginalia Search، DOAJ، Alpha Vantage، Natural Earth، Wikimedia Commons، Openverse.
- کمبود شواهد بیشتر در API رایگان ویدئوی حرفه‌ای، قیمت انبوه کالا، API شبکه اجتماعی و عرضه تجاری حساب‌محور برای ایران است. release، runtime footprint، کارت، entitlement و شرایط تجاری تعدادی از نامزدها نیز باز مانده‌اند.
- منابع پایه · [گزارش اولیه](https://chatgpt.com/library?file_id=libfile_7b3b86ae30148191a0a81819428d55f5&account_id=personal) · [Operating Memory](https://app.notion.com/p/3edc8c684690814a9707cb880534f462) · [Tool Governance](https://app.notion.com/p/3edc8c68469081cc90abdd5183f1bdb1) · [پژوهش مستقل استنتاج مدل در GitHub](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/06-tests-and-evidence/provider-research/DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md).
- هیچ اتصال، نصب، خرید، ساخت حساب، تغییر سیستم یا پایلوت انجام نشد.

