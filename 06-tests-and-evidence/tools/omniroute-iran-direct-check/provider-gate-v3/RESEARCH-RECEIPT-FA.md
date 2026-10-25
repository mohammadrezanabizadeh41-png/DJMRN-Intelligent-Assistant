# رسید پژوهش و گزارش فنی Provider Gate v3

شناسه: DJMRN-OMNIROUTE-PROVIDER-GATE-V3-20261025 — تاریخ: ۲۵ اکتبر ۲۰۲۶.

**وضعیت: IMPLEMENTED / TESTED-SYNTHETIC؛ پژوهش تجاری و eligibility = PARTIAL؛ Windows PowerShell 5.1 و اینترنت کاربر = NOT_RUN.** کد اجرایی کامل تحویل شده است؛ این وضعیت به معنی تأیید استفادهٔ عملیاتی از Providerها نیست. هیچ فایل GitHub یا Notion تغییر نکرده است. WQ/WA متناظر در درخواست تعیین نشده؛ شناسه یا مسیر فرضی ساخته نشده است. Commit: NONE؛ readback ثبت گزارش: NOT_APPLICABLE.

## APPLIED_LIBRARY_READ_RECEIPT

هر پنج صفحهٔ درخواستی با اتصال Notion واقعاً fetch شدند. متن کامل صفحات دریافت شد؛ سیاست‌های جاری، checkpointها و بخش‌های مرتبط با API، مدل ابری، سهمیه، authority و مجوز مرور شدند. **ادعای مطالعهٔ موشکافانهٔ تمام تاریخچهٔ چندمیلیون‌کاراکتری یا همهٔ صفحات فرزند نداریم.** جزئیات قابل بازبینی در `NOTION-READ-RECEIPT.json` است.

| سند | نسخه/زمان و مشاهده |
|---|---|
| [Persistent Operating Memory](https://app.notion.com/p/3edc8c684690814a9707cb880534f462) | آخرین ویرایش برگشتی 2026-10-20T16:48:30.778Z؛ 70,457 کاراکتر؛ free-first، permission و تفاوت تحقیق/اجرا |
| [Tool Governance](https://app.notion.com/p/3edc8c68469081cc90abdd5183f1bdb1) | 2026-10-17T16:40:34.103Z؛ 62,776 کاراکتر؛ Need→Capability→Existing→Verify و عدم duplicate authority |
| [Applied Capability Index](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f) | v0.48؛ 2026-10-20T17:01:05.277Z؛ 652,008 کاراکتر؛ ۱۷ شاخه، سرنخ‌های Groq/OpenRouter/Workers AI/HF؛ اطلاعات تاریخی رایگان بودن، مجوز روز نیست |
| [Applied Mission](https://app.notion.com/p/3fdc8c6846908167a77feab9564dc66d) | 2026-10-20T17:08:47.939Z؛ 237,155 کاراکتر؛ شاخهٔ پژوهشی از پروژهٔ اجرای دستیار جداست |
| [General Discovery](https://app.notion.com/p/3fbc8c684690817d8c94cce0bfaa1a59) | Discovery054 / CURRENT v52 / TECH-20261018-213-GX؛ 2026-10-18T15:00:07.265Z؛ 1,384,259 کاراکتر؛ هفت ستون/۳۰ خانواده؛ research≠activation |

فیلد native verification صفحات `unverified` بود؛ این فیلد را با نقش canonical تعیین‌شده توسط کاربر خلط نکردیم. محتوای زنده قابل دریافت بود. سیاست اختصاصی `SOURCES-AND-AUTHORITY.md` برای همین مخزن بر عبارات تاریخی عام مقدم است؛ هیچ همگام‌سازی خودکار Notion انجام نشد.

## PROJECT_REPOSITORY_READ_RECEIPT

- هویت از ابزار GitHub: `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`، repository ID `1427268660`، default branch `main`. مخزن در مشاهدهٔ فعلی public بود؛ اسناد قدیمی که private می‌گویند تاریخی‌اند.
- HEAD خوانده‌شده و clone فقط‌خواندنی: `505330b455385c384f2143f6a35ca96dadb26806`.
- همهٔ فایل‌های درخواست‌شده، سه CSV، دو اسکریپت، دستورالعمل‌ها و لاگ اجرای واقعی از همین revision خوانده/پردازش شدند. `SOURCE-MANIFEST.json` برای **هر فایل** HEAD، Git blob SHA، مسیر و تعداد بایت دارد؛ SHA ساختگی استفاده نشده است.
- REPOSITORY-LOCK blob: `231778be56580deedcd1d5c0c5de54bc093552fc`. این سند تنها پاسخ متناظر WA موجود را مجاز می‌داند؛ این تحویل هیچ write به مخزن ندارد.
- دادهٔ واقعی موجود: گزارش متنی user-run شامل ۳۷۵ Provider، ۲۸۰ route، ۵۴ addition و ۸۱۷ URL؛ 341/363 سایت، 251/280 API host و 247/280 API route GET پاسخ داده‌اند. این اعداد از **لاگ canonical کاربر** است، نه اجرای Work یا تعداد مدل قابل استفاده.
- دو CSV اصلی Desktop در Work موجود نبودند و سطرهای واقعی‌شان مشاهده نشد. آمار صف‌های واقعی عمداً اعلام نشده است. اسکریپت آن‌ها را محلی پیدا و وارد می‌کند؛ fixtureهای تحویل کاملاً مصنوعی‌اند.

## INDEPENDENT_SEARCH_RECEIPT

نسخهٔ رسمی `release/v3.8.52` جداگانه از `cheaper-inference/OmniRoute` خوانده شد؛ HEAD واقعی آن: `c754707d0edf250107a386168d4e324f51b24135`. Provider Reference، FREE_TIERS، RESILIENCE_GUIDE، snapshot translate-path، constants و همهٔ فایل‌های registry/index به‌صورت محلی خوانده و برای استخراج فیلدهای ثابت پردازش شدند؛ برای موارد منتخب کدها مستقیماً بازبینی شدند. hash دقیق همه در SOURCE-MANIFEST است. FREE_TIERS خود شامل اصلاحات تاریخی و تقریب‌های بودجه است؛ آن را سند قیمت فعلی هر vendor فرض نکردیم.

تطبیق واقعی داده: ۳۷۵ شناسهٔ یکتا، ۲۸۰ route CSV منطبق با مقدار URL در snapshot، ۵۴ addition. endpointهای literal رسمی stream/nonStream و modelsUrlها به‌صورت مستقل استخراج شدند. آدرس پارامتری Snowflake حذف شد؛ هیچ `/models` حدسی تولید نشد. ۱۰۸۸ ردیف مقصد، ۸۸۷ URL یکتای دارای منشأ رسمی واجد اسکن و ۴۱ ردیف curated تاریخی بدون corroboration مستقل مسیر، در دادهٔ نهایی ثبت است. این اعداد با ۸۱۷ اجرای قبلی یکسان نیستند، زیرا پوشش source تکمیل شده؛ پیش‌فرض آن‌ها را دوباره درخواست نمی‌کند.

تحقیق وب مستقل با دو موتور جست‌وجو و صفحات رسمی vendor انجام شد. موارد زیر خلاصهٔ **Fact منتشرشده / Unknown** هستند؛ نه تأیید حساب کاربر. منبع/تاریخ در dataset و matrix نیز هست.

| نامزد | نتیجهٔ رسمی قابل اتکا و فاصلهٔ باقی‌مانده |
|---|---|
| LLM7 | [Limits](https://docs.llm7.io/limits): Free token برای متن ۱۰۰هزار input+output در ۲۴ ساعت rolling؛ ۱ درخواست/ثانیه، ۶۰/دقیقه و ۲۵۰/ساعت. [Models API](https://docs.llm7.io/guides/models-api) Free را به turbo محدود می‌کند؛ Pro و usage-based را رایگان فرض نکنید. کارت، ایران و حقوق کاربرد واقعی کامل تأیید نشده‌اند. عدد ۵میلیون/روز در OmniRoute تاریخی است. |
| OpenRouter | [Pricing](https://openrouter.ai/pricing): Free API، ۵۰ درخواست/روز و ۲۰/دقیقه؛ فقط مدل واقعاً free. شارژ ۱۰دلاری این مأموریت را مجاز نمی‌کند. [Models endpoint](https://openrouter.ai/docs/api-reference/models/get-models) مسیر رسمی را تأیید می‌کند. eligibility ایران/حساب و hard stop واقعی این کاربر UNKNOWN. |
| UncloseAI | [Inference topology](https://uncloseai.com/inference.html) مدل چرخشی و `/v1/models` را توضیح می‌دهد؛ [Terms](https://www.uncloseai.com/terms-of-use.html) خدمات رایگان را توصیف می‌کند. نتیجهٔ ۴۰۱ واقعی کاربر حفظ می‌شود؛ No-auth بودن روی اینترنت او ثابت نیست. quota و account/region gate UNKNOWN. |
| Cloudflare AI | [Pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/): Workers Free روزانه ۱۰هزار Neuron، reset ساعت 00:00 UTC و توقف در سقف؛ Paid overage دارد. بعضی مدل‌ها payment می‌خواهند؛ free tag registry کافی نیست. endpoint inference وابسته به account ID است؛ base `/accounts` را completion نمی‌نامیم. eligibility حساب ایرانی UNKNOWN. |
| Groq | [Rate limits](https://console.groq.com/docs/rate-limits): برای gpt-oss-20b/120b نمونهٔ Free برابر ۳۰ RPM، هزار RPD، ۸هزار TPM و ۲۰۰هزار TPD؛ محدودیت organization مشترک و مدل‌محور است. [Models](https://console.groq.com/docs/models) منبع شناسهٔ روز است؛ مدل‌های قدیمی ممکن است بازنشسته/Enterprise شده باشند. دسترسی console/مسیر و eligibility این کاربر نامعلوم. |
| Hugging Face | [Pricing](https://huggingface.co/docs/inference-providers/pricing): صفحهٔ فعلی برای Free Users اعتبار ماهانه‌ای نشان نمی‌دهد؛ PRO و Team اعتبار وابسته به اشتراک دارند. این با یادداشت قدیمی Notion دربارهٔ $0.10 تعارض زمانی دارد. برای همین API hosted، رایگان پایدار تأیید نشد؛ Spaces و self-hosting محصولات جدا هستند. |
| Cerebras | [Pricing](https://www.cerebras.ai/pricing) و [account billing](https://inference-docs.cerebras.ai/console/account-billing): اعتبار یک‌بارهٔ ۵دلار پس از payment method، انقضای ۳۰روزه؛ در این مأموریت گزینهٔ بدون کارت نیست. |
| Together | [Credits](https://docs.together.ai/docs/billing-credits): free trial فعلی ندارد؛ خرید اولیهٔ حداقل ۱۵دلار لازم است. از اتصال رایگان عملیاتی کنار گذاشته شود؛ مشاهدهٔ شبکه حفظ می‌شود. |
| Fireworks | [Billing](https://docs.fireworks.ai/faq-new/billing-pricing/how-does-billing-and-credit-usage-work): prepaid و اطلاعات پرداخت؛ Auto Reload می‌تواند خرید کند. grant رایگان مستقل برای این حساب ثابت نشد. Fire Pass شرطی و غیرتولیدی، معادل API رایگان عمومی نیست. |
| NVIDIA | [NIM FAQ](https://docs.api.nvidia.com/nim/docs/product): دسترسی Developer Program برای prototype/research/development/testing؛ این مجوز تولید تجاری دائمی یا quota عددی ثابت نیست. ایران و شرایط حساب UNKNOWN. |
| DeepSeek | [Pricing](https://api-docs.deepseek.com/quick_start/pricing): inference توکن‌محور و کسر از topped-up/granted balance؛ grant به معنی سهمیهٔ رایگان تجدیدپذیر نیست. API با chat وب رایگان یکی نیست. |
| SiliconFlow | [Rate limits](https://docs.siliconflow.com/en/userguide/rate-limits/rate-limit-and-upgradation): free modelها و محدودیت حساب/مدل جدا دارند. مدل زندهٔ مشخص با هر دو قیمت صفر لازم است؛ flagshipهای دارای قیمت و اعتبار ثبت‌نام، رایگان دائمی فرض نشدند. |
| Z.AI | [Pricing](https://docs.z.ai/guides/overview/pricing) مدل‌های اصلی پولی را نشان می‌دهد؛ [GLM-4.5](https://docs.z.ai/guides/llm/glm-4.5) Flash را free معرفی می‌کند. سازگاری endpoint/حساب/منطقه و محدودیت مدل باید جدا تعیین شود؛ free cache یا کمپین paid-plan مساوی inference رایگان نیست. |
| Pollinations | [سایت رسمی](https://pollinations.ai/) و [Terms](https://pollinations.ai/terms): Pollen و پاداش Quest مطرح‌اند. استخراج [API docs](https://gen.pollinations.ai/docs) در این محیط محتوای کافی نداد؛ anonymous inference/سهمیهٔ تجدیدپذیر تأیید نشد و با توضیح قدیمی registry خلط نشد. |
| SambaNova | [Rate limits](https://docs.sambanova.ai/docs/en/models/rate-limits): Free بدون payment method و Developer با payment method؛ سقف ۲۰میلیون توکن روزانهٔ Developer را سهمیهٔ Free ننامید. مقدار واقعی Free/region/حساب نیازمند پیگیری است. |
| Openference / openference-api | [Pricing](https://openference.com/pricing)، [Models API](https://docs.openference.com/api-reference/models): استخراج صفحهٔ قیمت کامل نبود. Free جاری به‌طور مستقل ثابت نشد. OAuth و API-key دو ادغام یک سرویس‌اند، نه دو سهمیهٔ مستقل. |
| ModelScope | registry و FREE_TIERS منبع upstream برای مسیر و سرنخ gate هویت منطقه‌ای‌اند؛ جست‌وجوی رسمی vendor نتیجهٔ کافی برای عدد quota/KYC روز نداد. وضعیت UNKNOWN؛ ۲۰۰ روی میزبان جای eligibility را نمی‌گیرد. |
| OVHcloud | registry رسمی OmniRoute optional auth و ۲ درخواست/دقیقه/IP/model را ادعا می‌کند؛ در جست‌وجوی مستقیم vendor شاهد روز کافی برای شرایط همهٔ gateها تثبیت نشد. ادعای upstream از vendor verification جداست؛ reset واقعی کاربر حفظ می‌شود. |

۱۹ رکورد ادغام در dataset بررسی مستقل منتخب/تلاش مستند دارند؛ این **۱۹ طرح رایگان تأییدشده نیست**. برای سایر رکوردها policy/pricing/region/capabilities به‌صورت UNKNOWN حفظ شده‌اند. به‌خصوص همهٔ نامزدهای reachable احتمالی در CSV واقعی کاربر هنوز شناخته نشده‌اند؛ پس ادعای تکمیل بررسی تجاری همهٔ reachableها ممکن نیست. بازکردن ۳۷۵ root یا ارسال inference برای «پرکردن جدول» انجام نشده است.

## تصمیم اجرایی و گزینهٔ ساده‌تر

Fact: ابزار v2 روی کامپیوتر کاربر قبلاً census داده است. Judgment: ساده‌ترین مسیر مفید، تحلیل آفلاین همان دو CSV و تکمیل provenance است. گزینهٔ تکرار ۸۱۷ درخواست پیش‌فرض رد شد؛ گزینهٔ یک toolkit خارجی نیز نصب/وابستگی غیرضروری ایجاد می‌کرد. اسکریپت deterministic با state محلی و شبکهٔ GET صریح انتخاب شد؛ این انتخاب فقط ابزار آزمایش است و معماری روتر/Agent/Failover را تغییر نمی‌دهد.

تحلیل مستقل دو محور دارد: NetworkStatus از شواهد endpoint و OnboardingStatus از هزینه/حساب/منطقه؛ ۴۰۱ و ۴۰۵ حذف نمی‌شوند. مسیر واقعی نسبت به API host اولویت دارد؛ هر تعارض ۴۰۳/۴۲۹/۴۵۱/redirect/5xx برای بازبینی حفظ می‌شود. A بدون account proof قابل کسب نیست. `PENDING_EVIDENCE` افزوده شد تا شکست گذرا یا نبود شاهد به‌زور در A–E جا داده نشود. امتیاز هوش مدل از اسم مدل یا تعداد parameter جعل نشده است.

## آزمون و حدود آن

`VALIDATION-RESULTS.json` شمار دقیق assertionها و نتایج آخرین اجرای واقعی را دارد. آزمون‌ها شامل Parser در PowerShell 7.4.6، کامپایل کلاینت با C# language version 5، HTTP taxonomy، CSV fixture و ۳۷۵ شناسه، no-endpoint preservation، خروجی ۱۲فایلی/JSON/CSV، عدم خروج sentinelهای حساس، اجرای کامل شبکه با transport مصنوعی بدون socket، قطع شبیه‌سازی‌شده و Resume، backup خراب، Export آفلاین، ورودی مفقود/خراب، URLهای خصوصی و عدم Queue A/D کاذب‌اند. خطای اولیهٔ mock compiler و template Snowflake در توسعه کشف و اصلاح شد؛ PASS نهایی جایگزین پنهان‌کردن آن‌ها نیست.

این تست‌ها اجرای واقعی Windows 5.1، .NET Framework reference assemblies، Administrator-free behavior روی ویندوز، DNS/TCP/TLS/reset واقعی، IPv6 واقعی، قطع فیزیکی اینترنت، trust store ویندوز، اثبات Origin، eligibility حساب ایرانی یا inference عملی را پوشش نمی‌دهند: **NOT_RUN**. نگاشت خطا و mock transport شبیه‌سازی‌اند، نه بازتولید اختلال واقعی شبکه. بستهٔ portable PowerShell فقط در محیط توسعه برای آزمون استفاده شد؛ prerequisite دستگاه کاربر نیست.

هیچ درخواست inference، حساب، secret، upgrade، payment، Windows/network setting، provider activation یا failover واقعی انجام نشد. خواندن منابع رسمی عمومی و دریافت source/runtime آزمون در محیط Work با مصرف API مدل پولی خلط نمی‌شود. نسخهٔ قابل بازبینی و راه اجرای محلی تحویل شده؛ تکمیل معیار عملیاتی نیازمند اجرای خود کاربر و تحلیل CSV واقعی است.
