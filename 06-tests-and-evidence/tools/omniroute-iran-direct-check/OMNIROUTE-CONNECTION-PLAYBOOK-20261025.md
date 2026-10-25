# DJMRN — دفتر شماره‌دار پیگیری اتصال ۳۷۵ Provider به OmniRoute

**تاریخ تهیه:** 2026-10-25 · **وضعیت:** CURRENT *connection-candidate tracking plan* (نه اتصال انجام‌شده) · **نسخه OmniRoute:** `v3.8.52` · **Authority:** GitHub project evidence; no live account/inference proof.

> این سند **فهرست اجرایی پیگیری** است. «HTTP پاسخ داده» مساوی «مدل کار می‌کند»، «ایران مجاز است»، «رایگان است» یا «به OmniRoute متصل شده» نیست. هیچ Provider در زمان تهیه این لیست با کلید واقعی فعال نشده است. همهٔ ۳۷۵ شناسه یک شماره پایدار در snapshot حاضر دارند و در [CSV مکمل](OMNIROUTE-PROVIDER-CONNECTION-TRACKER-20261025.csv) قابل فیلتر و به‌روزرسانی وضعیت هستند.

## هدف و نحوه استفاده

۱. از ردیف **001** آغاز کن، وضعیت همان Provider را در `OmniProxy → Providers` ببین؛ اگر شیوه No-auth / ثبت‌نام / OAuth خاصی لازم بود طبق مستند رسمی انجام بده، نه با حدس endpoint.
۲. برای ردیف‌های دارای API Key، ابتدا طرح **$0 واقعی**، عدم کارت/خرید/overage، دسترسی مجاز حساب از ایران و مدل مشخص رایگان را احراز کن؛ سپس صرفاً همان مدل را در allowlist اضافه کن. برای ردیف‌های no-auth نیز ToS و کارکرد واقعی را تأیید کن.
۳. به محض موفقیت ثبت کن: `OnboardingProgress=CONNECTED_VERIFIED_FREE` **فقط بعد از یک inference واقعی صفرهزینه و پاسخ صحیح از طریق OmniRoute**؛ قبل از آن `KEY_OBTAINED`, `CONFIGURED_NOT_VERIFIED`, `BLOCKED_ACCOUNT`, `NOT_FREE` یا `PARKED` را ثبت کن. هرگز API key، رمز یا کوکی را در GitHub وارد نکن.
۴. اگر سهمیه پایان یافت، مسیر جایگزین **فقط از ردیف‌های verified free** قابل انتخاب است. این سند به خودی خود مسیریابی یا Failover خودکار را فعال نمی‌کند.
۵. آزمون‌های دسته‌جمعی شبکه **تکرار نشوند**؛ تصمیم به پیگیری از داده‌های ذخیره‌شده گرفته می‌شود. کد 401/405 به معنی HTTP پاسخ‌داده و نامزد پیگیری است؛ 403 به معنی رد دسترسی نامشخص، 451 نشانه محدودیت قانونی اعلام‌شده و HTTP=0 فعلاً پارک است.

## آمار و دامنه شاهد

| منبع آزمایش واقعی کاربر | نتیجه |
|---|---|
| اسکن اولیه 51 مسیر API | 48 پاسخ HTTP و 3 بی‌پاسخ، بدون inference |
| اسکن Deep v2 | 817 URL یکتا؛ 247/280 پاسخ GET از مسیر واقعی API؛ 251/280 پاسخ host |
| Gate v3 offline AnalyzeExisting | 375 Provider، imported=977، HTTP rows=885؛ A=0/B=158/C=40/D=0/E=149/PENDING_EVIDENCE=28؛ **بدون آزمایش جدید شبکه** |
| تازه‌ترین Inline PowerShell | 314 آدرس یکتا؛ 375 شناسه؛ A=10، B_AUTH=101، B_HTTP=72، C_DENIED=54، C_OTHER=12، D_NO_HTTP=37، E_NO_FIXED_API=89 |

**تفاوت مهم:** اعداد Gate v3 با دسته‌بندی جدید یکسان تعریف نشده‌اند؛ تعداد 158 را به 158 نام حدسی تبدیل نکرده‌ایم. از خروجی Gate v3 فقط آمار جمعی موجود است، چون CSVهای شخصی ویندوز در مخزن آپلود نشده‌اند. ردیف‌های این دفتر از **۲۸۶ سطر دقیق ثبت‌شده Inline** و **۸۹ شناسه باقی‌مانده در فهرست رسمی** ساخته شده‌اند. وب‌سایتِ قابل دسترسی به‌جای API استفاده نشده است.

### تفکیک و تعداد صف‌های واقعی این دفتر

| صف پیگیری | تعداد |
|---|---:|
| `P01_KEYLESS_HTTP_CANDIDATES` | 5 |
| `P02_PUBLIC_MODEL_CATALOG` | 10 |
| `P03_API_AUTH_OR_METHOD` | 82 |
| `P04_API_OTHER_HTTP` | 57 |
| `P05_SPECIAL_HTTP_CONNECTORS` | 28 |
| `R06_ACCESS_DENIED_REVIEW` | 53 |
| `R07_OTHER_HTTP_REVIEW` | 12 |
| `H06_NO_HTTP_NOW` | 37 |
| `H07_OFFICIAL_REGION_HOLD` | 2 |
| `H08_NO_FIXED_PUBLIC_API` | 89 |
| **جمع کل** | **375** |

**P01→P02→P03→P04:** صف‌های واجد اولویت پیگیری اتصال. **P05:** نیازمند روش اتصال ویژه، نه لزوماً API استاندارد. **R06/R07:** HTTP وجود دارد ولی محدودیت/اشکال هنوز رفع نشده. **H06:** بدون پاسخ HTTP در آزمایش تازه؛ کنار گذاشته‌شده از اقدام جاری. **H07:** محدودیت رسمی منطقه‌ای؛ کنار گذاشته‌شده از اتصال در ایران. **H08:** منبع ثابت API نداریم و نمی‌توان مسدودبودن را نتیجه گرفت.

## راهنمای وضعیت‌های تجاری که از منابع رسمی تا 25 اکتبر تأیید شده‌اند

| Provider | شواهد طرح رایگان | شرط اتصال |
|---|---|---|
| Requesty | [Free $0 / 200 درخواست روزانه / بدون کارت](https://www.requesty.ai/pricing) | فقط **مدل‌های free**؛ مسیر GET فهرست 200 بود |
| LLM7 | [Free token تا 100k توکن در 24h](https://llm7.io/) | از dashboard، مدل دارای مجوز Free؛ عدم استفاده از Pro/paid |
| Hugging Face | [Free user monthly $0.10 credit](https://huggingface.co/docs/inference-providers/pricing) | هزینه هر مدل را پیش از call بررسی؛ خرید credit انجام نشود |
| OpenRouter | [Free 50 req/day / 25+ free models](https://openrouter.ai/pricing/) | در آخرین scan 403؛ فقط بررسی شرایط دسترسی و free models |
| Cloudflare Workers AI | [Free 10,000 neurons/day](https://developers.cloudflare.com/workers-ai/platform/pricing/) | بعضی مدل‌ها پولی‌اند؛ REST و حساب فعلاً 403/400 |
| LLM7 anonymous | **طبق شرایط فعلی API token صادرشده الزامی است** | بدون توکن را Free بدون حساب معرفی نکن |
| AI Horde, UncloseAI, Pollinations و باقی | برچسب `No-auth` یا `Free` در catalog به‌تنهایی اثبات حساب رایگان نیست | احراز ToS و اینکه کدام مدل با همین روش واقعاً کار می‌کند |

برای `openai` و `gemini`، با وجود پاسخ HTTP، دسترسی از ایران در فهرست رسمی پشتیبانی‌شده نیست: [OpenAI](https://help.openai.com/en/articles/5347006-openai-api-supported-countries-and-territories) و [Gemini](https://ai.google.dev/gemini-api/docs/available-regions). این دو در **H07** هستند، نه صف حساب‌سازی.

## اختلافات مشاهده‌شده که نباید موجب حذف اشتباه شوند

- **SambaNova:** در اسکن 51 تایی `TIMEOUT` و در اسکن جدیدتر `/models=200` و `inference GET=405`؛ آخرین شاهد قوی‌تر است؛ در P02 نگهداری می‌شود.
- **OpenRouter:** در اسکن 51 تایی فهرست مدل‌ها `200` و در اسکن جدیدتر `403`؛ وضعیت **متعارض/متغیر**، نه قطعی فیلتر/قابل استفاده.
- **Groq:** اسکن 51 تایی `403`، میزبان در اسکن v2 `200`، و در آخرین مسیر مشخص `403`؛ داشبورد برای کاربر باز نشد. در R06 نگه داشته شود.
- **UncloseAI:** در فهرست رسمی No-auth، اما `/v1/models=401` در اینترنت کاربر؛ فعلاً آماده استفاده بدون حساب نیست.
- **LLM7:** میزبان root در v2 `404`، اما `/v1/models=200` و dashboard `200` دیده شده‌اند؛ root 404 به معنای خرابی API نیست.
- **Jina:** `451` روی مسیر تست‌شده؛ برای صف اتصال فعلی کنار گذاشته شده، بدون ادعای مسدودبودن همه محصولات.

## فهرست سراسری شماره‌دار — تمام ۳۷۵ Provider و وضعیت آزمون

شماره‌های زیر مطابق ستون `Sequence` در CSV هستند؛ `NOT_CONNECTED` برای همه وضعیت شروع است. ستون HTTP دقیقاً از latest user-pasted Inline result آمده؛ زمان، روش و مسیرهای دقیق در اسناد منبع هستند. برای صف P04، 404 گاهی مربوط به GET روی مسیر POST-only یا path خاص است: **این موارد فقط HTTP پاسخ داده‌اند، نه inference موفق.**


### P01_KEYLESS_HTTP_CANDIDATES (5)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 001 | `aihorde` — AI Horde | `API_ROUTE:405` | OFFICIAL CATALOG ANONYMOUS KEY؛ No-auth اسمی | پیگیری مسیر بدون ورود مستقل؛ نوع وب/روش OmniRoute و 401 را بررسی کن |
| 002 | `uncloseai` — UncloseAI | `API_ROUTE:401,SOURCE_REGISTRY_MODELS:401` | CATALOG NOAUTH CLAIM CONFLICTS 401؛ No-auth اسمی | پیگیری مسیر بدون ورود مستقل؛ نوع وب/روش OmniRoute و 401 را بررسی کن |
| 003 | `duckduckgo-web` — DuckDuckGo AI Chat | `API_ROUTE:400` | رایگان: UNKNOWN؛ No-auth اسمی | پیگیری مسیر بدون ورود مستقل؛ نوع وب/روش OmniRoute و 401 را بررسی کن |
| 004 | `cloudflare-playground` — Cloudflare AI Playground | `API_ROUTE:200` | رایگان: UNKNOWN؛ No-auth اسمی | پیگیری مسیر بدون ورود مستقل؛ نوع وب/روش OmniRoute و 401 را بررسی کن |
| 005 | `veoaifree-web` — Veo AI Free | `API_ROUTE:400` | رایگان: UNKNOWN؛ No-auth اسمی | پیگیری مسیر بدون ورود مستقل؛ نوع وب/روش OmniRoute و 401 را بررسی کن |

### P02_PUBLIC_MODEL_CATALOG (10)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 006 | `requesty` — Requesty | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | OFFICIAL FREE 200 RPD NO CARD؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 007 | `llm7` — LLM7.io | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | OFFICIAL FREE 100K TOKENS DAY؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 008 | `modelscope` — ModelScope | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 009 | `huggingface` — HuggingFace | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | OFFICIAL FREE CREDIT 0.10 USD MONTH؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 010 | `sambanova` — SambaNova | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `TIMEOUT`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 011 | `deepinfra` — DeepInfra | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 012 | `novita` — Novita AI | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 013 | `openference-api` — Openference API | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 014 | `venice` — Venice.ai | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |
| 015 | `aimlapi` — AI/ML API | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | رایگان: UNKNOWN؛ API Key | ثبت‌نام اختیاری/لازم؛ فقط مدل دارای قیمت صفر؛ اتصال آزمایشی در OmniRoute |

### P03_API_AUTH_OR_METHOD (82)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 016 | `logfare` — Logfare | `API_ROUTE:405` | CATALOG FREE KEY UNVERIFIED؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 017 | `qwen-cloud` — Qwen Cloud | `API_ROUTE:400,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 018 | `zai` — Z.AI | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 019 | `bigmodel` — BigModel.cn (Zhipu) | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 020 | `glm` — GLM Coding | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 021 | `siliconflow` — SiliconFlow | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 022 | `mistral` — Mistral | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 023 | `deepseek` — DeepSeek | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 024 | `together` — Together AI | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 025 | `hyperbolic` — Hyperbolic | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 026 | `cerebras` — Cerebras | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 027 | `minimax` — Minimax Coding | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 028 | `minimax-cn` — Minimax (China) | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 029 | `nebius` — Nebius AI | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 030 | `longcat` — LongCat AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 031 | `anthropic` — Anthropic | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 032 | `alibaba` — Alibaba Cloud Model Studio | `API_ROUTE:400,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 033 | `api-airforce` — Api.airforce | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 034 | `arcee-ai` — Arcee AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 035 | `auriko` — Auriko | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 036 | `bai` — b.ai | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 037 | `baichuan` — Baichuan | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 038 | `baidu` — Baidu (ERNIE) | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 039 | `bailian-coding-plan` — Alibaba Token Plan | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 040 | `bazaarlink` — BazaarLink | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 041 | `byteplus` — BytePlus ModelArk | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 042 | `cheaperinference` — Cheaper Inference | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 043 | `cloudcode-one` — CloudCode.ONE | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 044 | `clova-studio` — Naver CLOVA Studio | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 045 | `codestral` — Codestral | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 046 | `deepai` — DeepAI | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 047 | `dgrid` — DGrid | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 048 | `digitalocean` — DigitalOcean | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 049 | `dit` — DIT.ai | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 050 | `free-ai` — Free.ai | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 051 | `freeaiapikey` — FreeAIAPIKey | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 052 | `glm-cn` — GLM Coding (China) | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 053 | `glmt` — GLM Thinking | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 054 | `greenpt` — GreenPT | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 055 | `helyxai` — Helyx AI | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 056 | `iflytek` — iFlytek Spark | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 057 | `internlm` — InternLM (Intern-S1) | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 058 | `kenari` — Kenari | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 059 | `leonardo` — Leonardo AI | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 060 | `liquid` — Liquid AI | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 061 | `literouter` — LiteRouter | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 062 | `llm-kiwi` — LLM.Kiwi | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 063 | `meganova-ai` — MegaNova AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 064 | `meta-llama` — Meta Llama API | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 065 | `mnn-ai` — MNN AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 066 | `morph` — Morph | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 067 | `naga-ac` — Naga.ac | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 068 | `naga-ai` — Naga AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 069 | `nan` — NaN.Builders | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 070 | `nara` — NaraRouter | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 071 | `nube` — Nube.sh | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 072 | `ofoxai` — OfoxAI | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 073 | `openvecta` — OpenVecta | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 074 | `poe` — Poe | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 075 | `qianfan` — Baidu Qianfan | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 076 | `qwen-cloud-token-plan` — Qwen Cloud Token Plan | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 077 | `regolo` — Regolo AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 078 | `sarvam` — Sarvam AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 079 | `scaleway` — Scaleway AI | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 080 | `sealion` — SEA-LION | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 081 | `sparkdesk` — SparkDesk | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 082 | `speka` — Speka AI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 083 | `stepfun` — StepFun | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 084 | `sumopod` — SumoPod | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 085 | `synthetic` — Synthetic | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 086 | `tokenmarket` — Token Market | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 087 | `typhoon` — Typhoon | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 088 | `udio` — Udio | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 089 | `unorouter` — UnoRouter | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 090 | `upstage` — Upstage | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 091 | `vercel-ai-gateway` — Vercel AI Gateway | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 092 | `volcengine-agent-plan` — Volcengine Ark Agent Plan | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 093 | `volcengine-coding-plan` — Volcengine Ark Coding Plan | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 094 | `wafer` — Wafer AI | `API_ROUTE:401` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 095 | `xai` — xAI (Grok) | `API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 096 | `yi` — Yi (01.AI) | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |
| 097 | `zerolimitai` — ZeroLimitAI | `API_ROUTE:405` | رایگان: UNKNOWN؛ API Key | API پاسخ 401/405 داشته؛ نیاز به کلید/روش صحیح و طرح رایگان را بررسی کن |

### P04_API_OTHER_HTTP (57)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 098 | `pollinations` — Pollinations AI | `API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200` (قدیم: `200`) | PUBLIC MODEL CATALOG ONLY؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 099 | `cloudflare-ai` — Cloudflare Workers AI | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:400` (قدیم: `400`) | OFFICIAL FREE 10000 NEURONS DAY؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 100 | `opencode-zen` — OpenCode Zen | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 101 | `opencode-go` — OpenCode Go | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 102 | `xiaomi-mimo` — Xiaomi MiMo | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 103 | `agentrouter` — AgentRouter | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 104 | `agnes` — Agnes AI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 105 | `agnes-cn` — Agnes AI (China) | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 106 | `alibaba-cn` — Alibaba (China) | `API_ROUTE:400` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 107 | `ant-ling` — Ant Ling / Ring (inclusionAI) | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 108 | `apmix` — Apmix | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 109 | `beatapi` — BeatAPI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 110 | `bluesminds` — BluesMinds | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 111 | `charm-hyper` — Charm Hyper | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 112 | `chenzk` — Chenzk API | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 113 | `command-code` — Command Code | `API_ROUTE:200` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 114 | `dahl` — Dahl | `API_ROUTE:200` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 115 | `daoxe` — DaoXE | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 116 | `demonroute` — Demon Route | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 117 | `dify` — Dify | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 118 | `dxnt` — DXNT / DX Token | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 119 | `featherless-ai` — Featherless AI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 120 | `freebuff` — Freebuff | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 121 | `freetheai` — FreeTheAi | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 122 | `friendliai` — FriendliAI | `API_ROUTE:400` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 123 | `g4f-groq` — g4f.space — Groq | `API_ROUTE:429` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 124 | `g4f-nvidia` — g4f.space — NVIDIA | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 125 | `gitlawb` — Gitlawb Opengateway (MiMo) | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 126 | `gitlawb-gmi` — Gitlawb Opengateway (GMI Cloud) | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 127 | `hcnsec` — Huancheng Public API | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 128 | `helixmind` — HelixMind | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 129 | `heroku` — Heroku AI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 130 | `ideogram` — Ideogram | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 131 | `inference-net` — Inference.net | `API_ROUTE:400` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 132 | `kie` — KIE.AI | `API_ROUTE:200` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 133 | `navy` — NavyAI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 134 | `nlpcloud` — NLP Cloud | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 135 | `oneminai` — 1min.AI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 136 | `onomeo` — onomeo | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 137 | `openadapter` — OpenAdapter | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 138 | `opper` — Opper | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 139 | `poixe-ai` — Poixe AI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 140 | `publicai` — PublicAI | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 141 | `seekai` — SeekAi | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 142 | `sensenova` — SenseNova | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 143 | `stability-ai` — Stability AI | `CURATED_PUBLIC_DISCOVERY:404` (قدیم: `404`) | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 144 | `token-kiosk` — Token Kiosk | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 145 | `tokenreply` — TokenReply | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 146 | `tokenrouter` — TokenRouter | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 147 | `unifically` — Unifically | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 148 | `v0-vercel` — v0 (Vercel) | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 149 | `xiaomi-mimo-token-plan` — Xiaomi MiMo Token Plan | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 150 | `xkiro` — xKiro | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 151 | `y-api` — Y-API | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 152 | `yolo-auto` — Yolo-Auto | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 153 | `zenmux` — ZenMux | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |
| 154 | `zylo-api` — Zylo API | `API_ROUTE:404` | رایگان: UNKNOWN؛ API Key | پاسخ HTTP دیگر؛ ابتدا endpoint واقعی/مدل رایگان را در مستند رسمی روشن کن |

### P05_SPECIAL_HTTP_CONNECTORS (28)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 155 | `adapta-web` — Adapta.org (Adapta One Web) | `API_ROUTE:401` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 156 | `assemblyai` — AssemblyAI | `CURATED_PUBLIC_DISCOVERY:404` (قدیم: `404`) | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 157 | `chatplayground` — ChatPlayground | `API_ROUTE:401` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 158 | `claude` — Claude Code | `API_ROUTE:405` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 159 | `codebuddy-cn` — CodeBuddy CN | `API_ROUTE:401` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 160 | `codex` — OpenAI Codex | `API_ROUTE:405` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 161 | `deepseek-web` — DeepSeek Web | `API_ROUTE:200` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 162 | `ghe-copilot` — GitHub Enterprise Copilot | `API_ROUTE:405` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 163 | `github` — GitHub Copilot | `API_ROUTE:405` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 164 | `grok-cli` — Grok Build | `API_ROUTE:405` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 165 | `grok-web` — Grok Web (Subscription) | `API_ROUTE:401` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 166 | `inner-ai` — Inner.ai (Subscription) | `API_ROUTE:405` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 167 | `kiro` — Kiro AI | `API_ROUTE:404` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 168 | `maxai` — MaxAI | `API_ROUTE:200` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 169 | `muse-code` — Muse Code (Meta) | `API_ROUTE:401` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 170 | `notrack-web` — NoTrack Web (Free) | `API_ROUTE:405` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 171 | `openference` — Openference | `API_ROUTE:401` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 172 | `perplexity-web` — Perplexity Web (Pro/Max) | `API_ROUTE:405` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 173 | `promptql` — PromptQL (Unofficial/Experimental) | `API_ROUTE:200` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 174 | `qoder` — Qoder | `API_ROUTE:401` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 175 | `syntx` — SYNTX.ai (Unofficial/Experimental) | `API_ROUTE:404` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 176 | `t3-web` — t3.chat (Pro/Free) | `API_ROUTE:429` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 177 | `tinycms-web` — TinyCMS Web (Free/Sub) | `API_ROUTE:404` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 178 | `xai-oauth` — xAI OAuth (Grok) | `API_ROUTE:405` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 179 | `yuanbao-web` — Tencent Yuanbao (Free) | `API_ROUTE:404` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 180 | `zai-web` — Z.ai Web | `API_ROUTE:200` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 181 | `zed-hosted` — Zed Hosted Models | `API_ROUTE:404` | رایگان: UNKNOWN؛ OAuth | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |
| 182 | `zenmux-free` — ZenMux Free (Web) | `API_ROUTE:404` | رایگان: UNKNOWN؛ Web session | OAuth/Web/Audio/Connector خاص؛ API استاندارد مستقیماً اثبات نشده |

### R06_ACCESS_DENIED_REVIEW (53)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 183 | `openrouter` — OpenRouter | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `200`) | OFFICIAL FREE 50 RPD؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 184 | `groq` — Groq | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 185 | `nvidia` — NVIDIA NIM | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 186 | `fireworks` — Fireworks AI | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 187 | `chutes` — Chutes.ai | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 188 | `cohere` — Cohere | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 189 | `kimi` — Kimi (Legacy Moonshot API) | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 190 | `moonshot` — Kimi | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 191 | `ollama-cloud` — Ollama Cloud | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 192 | `perplexity` — Perplexity | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `404`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 193 | `jina-ai` — Jina AI (Foundation API) | `CURATED_PUBLIC_DISCOVERY:451` (قدیم: `451`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 194 | `jina-reader` — Jina Reader (r.jina.ai) | `CURATED_PUBLIC_DISCOVERY:451` (قدیم: `451`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 195 | `ai21` — AI21 Labs | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 196 | `baseten` — Baseten | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 197 | `blackbox` — Blackbox AI | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 198 | `blackbox-web` — Blackbox Web (Subscription) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 199 | `bytez` — Bytez | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 200 | `chatgpt-web` — ChatGPT Web (Clean Room) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 201 | `chatgpt-web-codex` — ChatGPT Web (Codex) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 202 | `claude-web` — Claude Web | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 203 | `cline` — Cline | `API_ROUTE:403` | رایگان: UNKNOWN؛ OAuth | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 204 | `clinepass` — ClinePass | `API_ROUTE:403` | رایگان: UNKNOWN؛ OAuth | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 205 | `conol-web` — Conol (Unofficial/Experimental) | `API_ROUTE:451` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 206 | `cursor` — Cursor IDE | `API_ROUTE:403` | رایگان: UNKNOWN؛ OAuth | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 207 | `cursor-api` — Cursor API | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 208 | `electronhub` — Electron Hub | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 209 | `elevenlabs` — ElevenLabs | `CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 210 | `factory` — Factory | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 211 | `fastrouter` — FastRouter | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 212 | `gemini-web` — Gemini Web (Free) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 213 | `hyperagent` — HyperAgent (Unofficial/Experimental) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 214 | `inception` — Inception | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 215 | `kilo-gateway` — Kilo Gateway | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 216 | `kilocode` — Kilo Code | `API_ROUTE:403` | رایگان: UNKNOWN؛ OAuth | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 217 | `kimi-coding` — Kimi Code CLI | `API_ROUTE:403` | رایگان: UNKNOWN؛ OAuth | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 218 | `kimi-coding-apikey` — Kimi Code API Key | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 219 | `kimi-web` — Kimi Web | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 220 | `llmgateway` — LLM Gateway | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 221 | `lmarena` — Arena (Free) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 222 | `nanogpt` — NanoGPT | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 223 | `nous-research` — Nous Research | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 224 | `perplexity-agent` — Perplexity Agent | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 225 | `plamo` — PLaMo | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 226 | `poolside` — Poolside | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 227 | `reka` — Reka | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 228 | `routeway` — Routeway | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 229 | `twinmind` — Twinmind (Unofficial/Experimental) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 230 | `uc` — UC (uncensored.com) | `API_ROUTE:403` | رایگان: UNKNOWN؛ Web session | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 231 | `uc-direct` — UC Direct (uncensored.com) | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 232 | `vertex` — Vertex AI | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 233 | `void-ai` — Void AI | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 234 | `wandb` — Weights & Biases Inference | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |
| 235 | `writer` — Writer | `API_ROUTE:403` | رایگان: UNKNOWN؛ API Key | 403 یا 451؛ علت WAF/سیاست/منطقه نامعلوم؛ فعلاً فعال نکن |

### R07_OTHER_HTTP_REVIEW (12)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 236 | `chat-oripe` — Chat Oripe | `API_ROUTE:530` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 237 | `chatanywhere` — ChatAnywhere | `API_ROUTE:302` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 238 | `coze` — Coze | `API_ROUTE:503` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 239 | `crof` — CrofAI | `API_ROUTE:302` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 240 | `doubao-web` — Dola Web (ByteDance) | `API_ROUTE:503` | رایگان: UNKNOWN؛ Web session | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 241 | `freeinference` — FreeInference | `API_ROUTE:502` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 242 | `huggingchat` — HuggingChat (Free) | `API_ROUTE:302` | رایگان: UNKNOWN؛ Web session | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 243 | `orcarouter` — OrcaRouter | `API_ROUTE:301` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 244 | `pioneer` — Pioneer AI | `API_ROUTE:410` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 245 | `tabitoken` — TabiToken | `API_ROUTE:500` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 246 | `trae` — Trae | `API_ROUTE:503` | رایگان: UNKNOWN؛ OAuth | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |
| 247 | `x5lab` — X5Lab | `API_ROUTE:530` | رایگان: UNKNOWN؛ API Key | 3xx/5xx یا خطای دیگر؛ فعلاً فعال نکن |

### H06_NO_HTTP_NOW (37)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 248 | `agy` — Antigravity CLI | `API_ROUTE:0` | رایگان: UNKNOWN؛ OAuth | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 249 | `ainative` — AINative Studio | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 250 | `aion` — Aion Labs | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 251 | `antigravity` — Antigravity | `API_ROUTE:0` | رایگان: UNKNOWN؛ OAuth | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 252 | `anyapi` — AnyAPI AI | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 253 | `codebuddy-intl` — CodeBuddy Intl | `API_ROUTE:0` | رایگان: UNKNOWN؛ OAuth | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 254 | `databricks` — Databricks | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 255 | `devin-desktop` — Devin Desktop | `API_ROUTE:0` | رایگان: UNKNOWN؛ OAuth | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 256 | `doubao` — Doubao | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 257 | `eurouter` — EURouter | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 258 | `fal-ai` — Fal.ai | `CURATED_PUBLIC_DISCOVERY:0` (قدیم: `TIMEOUT`) | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 259 | `freemodel-dev` — FreeModel.dev | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 260 | `g4f-gemini` — g4f.space — Gemini | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 261 | `g4f-ollama` — g4f.space — Ollama | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 262 | `g4f-pollinations` — g4f.space — Pollinations | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 263 | `galadriel` — Galadriel | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 264 | `gigachat` — GigaChat (Sber) | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 265 | `gitlab-duo` — GitLab Duo | `API_ROUTE:0` | رایگان: UNKNOWN؛ OAuth | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 266 | `haiper` — Haiper | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 267 | `lambda-ai` — Lambda AI | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 268 | `llamagate` — LlamaGate | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 269 | `lyceum` — Lyceum | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 270 | `maritalk` — Maritalk | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 271 | `mixlayer` — Mixlayer | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 272 | `modal` — Modal | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 273 | `monsterapi` — MonsterAPI | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 274 | `muse-spark-web` — Muse Spark Web (Meta AI) | `API_ROUTE:0` | رایگان: UNKNOWN؛ Web session | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 275 | `notion-web` — Notion AI Web (Unofficial/Experimental) | `API_ROUTE:0` | رایگان: UNKNOWN؛ Web session | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 276 | `nscale` — nScale | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 277 | `ovhcloud` — OVHcloud AI | `API_ROUTE:0,CURATED_PUBLIC_DISCOVERY:0` (قدیم: `TIMEOUT`) | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 278 | `predibase` — Predibase | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 279 | `qiniu` — Qiniu | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 280 | `tencent` — Tencent Hunyuan | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 281 | `tencent-aistudio-web` — Tencent AI Studio (Free) | `API_ROUTE:0` | رایگان: UNKNOWN؛ Web session | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 282 | `vertex-partner` — Vertex AI Partners | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 283 | `volcengine` — Volcengine | `API_ROUTE:0` | رایگان: UNKNOWN؛ API Key | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |
| 284 | `workbuddy` — WorkBuddy | `API_ROUTE:0` | رایگان: UNKNOWN؛ OAuth | در آزمون اخیر HTTP=0؛ پارک بدون تست جدید |

### H07_OFFICIAL_REGION_HOLD (2)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 285 | `gemini` — Gemini (Google AI Studio) | `API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403` (قدیم: `403`) | رایگان: UNKNOWN؛ API Key | محدودیت رسمی ارائه API از ایران؛ از صف اتصال حذف شود |
| 286 | `openai` — OpenAI | `API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401` (قدیم: `401`) | رایگان: UNKNOWN؛ API Key | محدودیت رسمی ارائه API از ایران؛ از صف اتصال حذف شود |

### H08_NO_FIXED_PUBLIC_API (89)

| شماره | Provider — نام داخلی | آخرین پاسخ GET روی دستگاه | رایگان / نیازمندی | قدم بعدی |
|---:|---|---|---|---|
| 287 | `360ai` — 360 AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 288 | `9router` — 9router | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 289 | `adobe-firefly` — Adobe Firefly (Image/Video) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ Web session | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 290 | `amazon-q` — Amazon Q | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ OAuth | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 291 | `anysearch-search` — AnySearch | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 292 | `auggie` — Augment (Auggie CLI) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ No-auth اسمی | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 293 | `auto` — Auto (Zero-Config) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 294 | `aws-polly` — AWS Polly | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 295 | `azure-ai` — Azure AI Foundry | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 296 | `azure-openai` — Azure OpenAI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 297 | `bedrock` — Amazon Bedrock | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 298 | `black-forest-labs` — Black Forest Labs | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 299 | `brave-search` — Brave Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 300 | `cartesia` — Cartesia | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 301 | `clarifai` — Clarifai | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 302 | `cliproxyapi` — CLIProxyAPI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 303 | `codex-app-server` — OpenAI Codex (App-Server) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ No-auth اسمی | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 304 | `codex-cloud` — Codex Cloud | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 305 | `comfyui` — ComfyUI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 306 | `context7` — Context7 (library docs) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 307 | `copilot-m365-web` — Microsoft 365 Copilot (BizChat) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ Web session | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 308 | `copilot-web` — Microsoft Copilot Web | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ Web session | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 309 | `datarobot` — DataRobot | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 310 | `deepgram` — Deepgram | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 311 | `devin` — Devin | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 312 | `devin-cli` — Devin CLI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ OAuth | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 313 | `devin-cli-agentic` — Devin CLI Agentic Bridge | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ No-auth اسمی | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 314 | `docker-model-runner` — Docker Model Runner | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 315 | `empower` — Empower | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 316 | `exa-search` — Exa Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 317 | `fenayai` — FenayAI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 318 | `firecrawl` — Firecrawl | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 319 | `fishaudio` — Fish Audio | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 320 | `getgoapi` — GoAPI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 321 | `gitlab` — GitLab Duo PAT | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 322 | `gladia` — Gladia | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 323 | `google-pse-search` — Google Programmable Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 324 | `inworld` — Inworld | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 325 | `jules` — Google Jules | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 326 | `laozhang` — LaoZhang AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 327 | `lemonade` — Lemonade Server | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 328 | `linkup-search` — Linkup Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 329 | `llama-cpp` — llama.cpp | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 330 | `llamafile` — Llamafile | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 331 | `lm-studio` — LM Studio | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 332 | `magnific` — Magnific | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 333 | `mixedbread` — Mixedbread AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 334 | `mlx-gemma` — MLX Gemma 26B | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 335 | `mlx-qwen` — MLX Qwen 3.8 27B | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 336 | `nimble-search` — Nimble Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 337 | `nomic` — Nomic | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 338 | `oci` — OCI Generative AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 339 | `ollama-local` — Ollama | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 340 | `ollama-search` — Ollama Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 341 | `oobabooga` — oobabooga | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 342 | `parallel-search` — Parallel Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 343 | `perplexity-search` — Perplexity Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 344 | `piapi` — PiAPI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 345 | `playht` — PlayHT | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 346 | `poe-web` — Poe Web (Subscription) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ Web session | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 347 | `recraft` — Recraft | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 348 | `rev-ai` — Rev AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 349 | `runwayml` — Runway | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 350 | `sap` — SAP Generative AI Hub | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 351 | `sdwebui` — SD WebUI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 352 | `searchapi-search` — SearchAPI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 353 | `searxng-search` — SearXNG Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 354 | `segmind` — Segmind | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 355 | `serper-search` — Serper Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 356 | `snowflake` — Snowflake Cortex | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 357 | `soniox` — Soniox | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 358 | `speechmatics` — Speechmatics | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SERVICE_SPECIFIC | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 359 | `tavily-search` — Tavily Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 360 | `thebai` — TheB.AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 361 | `tinyfish` — TinyFish Fetch | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 362 | `topaz` — Topaz | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 363 | `triton` — NVIDIA Triton | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 364 | `typesafe` — TypeSafe AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 365 | `v0-vercel-web` — v0 Vercel Web (Code Gen) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ Web session | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 366 | `venice-web` — Venice Web (Privacy) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ Web session | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 367 | `vllm` — vLLM | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 368 | `voyage-ai` — Voyage AI | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 369 | `watsonx` — IBM watsonx.ai Gateway | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ API Key | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 370 | `x-search` — X Search (Grok) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 371 | `xinference` — XInference | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ LOCAL | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 372 | `xquik-search` — Xquik X Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 373 | `youcom-search` — You.com Search | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ SPECIAL_OR_UNKNOWN | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 374 | `zcode` — ZCode (GLM Coding Plan) | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ No-auth اسمی | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |
| 375 | `zed` — Zed IDE | `بدون مسیر ثابت در گزارش` | رایگان: UNKNOWN؛ OAuth | در منبع موجود API عمومی ثابت شناسایی نشده؛ شبکه نامعلوم |

## منابع دقیق و ضمانت عدم جعل شواهد

- [فهرست رسمی snapshot 375 Provider](OmniRoute_v3.8.52_375_providers.csv) و [280 مسیر upstream](OmniRoute_v3.8.52_upstream_api_snapshot.csv) و [54 مسیر تکمیلی](OmniRoute_v3.8.52_api_discovery_additions.csv).
- [گزارش مستقیم 314 آدرس با متن 286 سطر و 89 ردیف بی‌نشانی](../../logs/OMNIROUTE-DIRECT-314-URLS-MODEL-CATALOG-USER-RUN-20261025.md).
- [نتایج 51 API](../../logs/OMNIROUTE-375-IRAN-ISP-USER-RUN-20261025.md)، [Deep v2 817 URL](../../logs/OMNIROUTE-375-DEEP-AUDIT-V2-USER-RUN-20261025.md)، [Gate v3 offline](../../logs/OMNIROUTE-PROVIDER-GATE-V3-USER-ANALYZE-20261025.md).
- اصل روش: هر عنوان `USER WINDOWS OBSERVATION` از متن خروجی کاربر بازنویسی شده و **نه دسترسی زنده به فایل‌های Desktop و نه اتصال API دارای کلید** در این اقدام رخ داده است.

**Next concrete action: ردیف 001 از P01، سپس دقیقاً ردیف بعدی؛ در صورت نداشتن مسیر واقعی یا منع قانونی، وضعیت را PARKED کن و ادامه بده.**
