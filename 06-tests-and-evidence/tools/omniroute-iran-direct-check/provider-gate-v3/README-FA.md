# راهنمای اجرای Provider Gate v3

این ابزار ۳۷۵ شناسهٔ OmniRoute 3.8.52 را نگه می‌دارد. فایل PS1 مستقل است؛ CSV، Python، Node، PowerShell 7، نصب یا Administrator لازم ندارد. داده‌های نسخهٔ ثابت داخل فایل فشرده و با SHA256 کنترل شده‌اند. کد کمکی C# داخل همان فایل با امکانات داخلی Windows PowerShell کامپایل می‌شود؛ در رایانه‌ای که سیاست سازمانی Add-Type را منع کرده باشد، آزمون شبکه و SelfTest قابل اجرا نیست، ولی تحلیل آفلاین به آن نیاز ندارد.

وضعیت تحویل: کد اجرا و با ورودی مصنوعی در Linux / PowerShell 7.4.6 آزموده شده است. اجرای واقعی Windows PowerShell 5.1 و اینترنت دستگاه شما هنوز NOT_RUN است. این بسته تأیید نهایی رایگان بودن یا اجازهٔ استفاده از همهٔ سرویس‌ها نیست.

## اجرای فعلی پیشنهادی: فقط تحلیل قبلی، بدون اینترنت

فایل `Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1` را در Downloads ذخیره کنید. PowerShell معمولی ویندوز را باز کنید و این **یک دستور کامل** را اجرا کنید:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode AnalyzeExisting
```

Bypass فقط برای همان فرایند است؛ تنظیم دائمی ExecutionPolicy یا Registry تغییر نمی‌کند. اگر فایل داخل پوشهٔ استخراج ZIP قرار دارد، مسیر پس از `-File` را به محل واقعی همان فایل تغییر دهید. فایل ZIP را داخل خودش اجرا نکنید.

ابزار در Desktop واقعی ویندوز، Desktop معمولی و Desktopهای OneDrive، پوشه‌های `DJMRN-DEEP-375-*` را جست‌وجو می‌کند؛ درون پوشه‌های شخصی دیگر پیمایش نمی‌کند. آخرین پوشهٔ معتبر حاوی هر دو CSV را با زمان اصلاح پوشه انتخاب می‌کند. ۳۷۵ شناسه، نبود تکرار، ستون‌ها، HTTP و تطبیق آدرس‌ها کنترل می‌شوند. اگر ورودی پیدا نشود یا خراب باشد، گزارش شواهد ناکافی ساخته می‌شود و **اسکن شبکه خودکار آغاز نمی‌شود**.

برای انتخاب دقیق خروجی اجرای شناخته‌شده:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode AnalyzeExisting -InputDirectory "$env:USERPROFILE\Desktop\DJMRN-DEEP-375-20261025-042141"
```

اگر Desktop در OneDrive است، محل واقعی پوشه را به `-InputDirectory` بدهید. دو فایل ورودی v2 عبارت‌اند از `01_ALL_ADDRESSES_AND_REASONS.csv` و `02_ALL_375_PROVIDER_DECISIONS.csv`. ورودی صریح همچنین می‌تواند پوشهٔ خروجی v3 حاوی `10_FULL_AUDIT_RESULTS.json` با همین DatasetSHA256 باشد.

## حالت‌های دیگر

آزمون داخلی کاملاً آفلاین:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -SelfTest
```

بازآزمایی محدودِ فقط URLهای قبلاً بدون HTTP، به‌علاوه سه کنترل مشخص:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode RetestFailed -InputDirectory "$env:USERPROFILE\Desktop\DJMRN-DEEP-375-20261025-042141" -TimeoutSeconds 6 -RetryCount 1
```

کنترل‌ها: `/v1/models` رسمی LLM7 و UncloseAI و `/api/v1/models` رسمی OpenRouter. پاسخ حداقل دو کنترل لازم است تا عدم پاسخ مکرر مسیرهای آزموده‌شده به صف D برسد. شکست کنترل‌ها مساوی اثبات قطع اینترنت نیست. اگر هیچ URL بدون HTTP موجود نباشد، کنترلی نیز درخواست نمی‌شود. ردیف‌های unvetted یا NOT_TESTED جزو بازآزمایی نیستند.

اسکن کاملِ صریح؛ این حالت مرور قبلی را تکرار می‌کند و مقصدهای رسمیِ تکمیلی را نیز می‌آزماید:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode FullNetworkAudit -TimeoutSeconds 6 -RetryCount 1
```

فهرست شامل ۱۰۸۸ ردیف مقصد و ۸۸۷ URL یکتای دارای منشأ رسمی واجد اسکن است؛ ۴۱ ردیف curated قدیمی فاقد تأیید مستقل مسیر، فقط برای واردکردن شواهد حفظ شده‌اند. تعداد درخواست واقعی ممکن است کمتر باشد: URLهای مشترک یک بار آزموده می‌شوند؛ مقصد ناامن/پارامتری رد می‌شود؛ پس از ۴۲۹ بقیهٔ مسیرهای همان host در همان اجرا متوقف می‌شوند. این اعداد تعداد Provider یا مدل مستقل نیستند.

هم‌زمانی عمداً **یک** است تا رفتار شبکه و مصرف محدود بماند. `TimeoutSeconds` سقف **هر مرحله** DNS/TCP/TLS/خواندن header است، نه کل اجرای یک URL. حداکثر یک IP از هر خانواده امتحان می‌شود و تلاش موفق ممکن است پیش از خانوادهٔ دوم خاتمه یابد. یک تلاش می‌تواند تا حدود هفت برابر این مقدار طول بکشد؛ با retry بیشتر می‌شود. اسکن کامل روی شبکهٔ کند ممکن است طولانی باشد. TLS فقط 1.2 و HTTP/1.1 است؛ عدم پاسخ اثبات انسداد یا عدم پشتیبانی روش‌های دیگر نیست.

Checkpoint/ادامه: از ابتدا یک پوشهٔ خروجی ثابت **خالی** تعیین کنید:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode FullNetworkAudit -OutputDirectory "$env:USERPROFILE\Desktop\DJMRN-GATE-V3-RUN" -TimeoutSeconds 6 -RetryCount 1
```

پس از توقف، همان دستور و پارامترها با `-Resume`:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode FullNetworkAudit -OutputDirectory "$env:USERPROFILE\Desktop\DJMRN-GATE-V3-RUN" -TimeoutSeconds 6 -RetryCount 1 -Resume
```

حالت، داده، timeout، retry و hash ورودی باید یکسان بمانند. هر URL کامل‌شده checkpoint می‌شود؛ نسخهٔ قبلی `.bak` برای خرابی نوشتن حفظ می‌شود. درخواست نیمه‌تمام ممکن است در ادامه دوباره انجام شود. پس از Ctrl+C در صورت امکان گزارش جزئی ساخته می‌شود؛ بستن اجباری پنجره یا قطع برق تضمین اجرای finally ندارد. در آن حالت Resume گزارش را بازسازی می‌کند.

تولید دوبارهٔ صف‌ها بدون هیچ درخواست:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\Downloads\Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1" -Mode ExportShortlist -InputDirectory "$env:USERPROFILE\Desktop\DJMRN-GATE-V3-RUN"
```

## نتایج و ارسال بدون عکس

پوشه‌ای با نام `DJMRN-PROVIDER-GATE-V3-...` روی Desktop ساخته می‌شود. اگر Desktop در محیط غیرعادی مشخص نباشد، محل فعلی استفاده می‌شود و مسیر در کنسول چاپ می‌شود.

| فایل | کاربرد |
|---|---|
| 01_ALL_375_PROVIDERS.csv | وضعیت جداگانهٔ شبکه و onboarding هر ۳۷۵ شناسه |
| 02_ALL_API_ENDPOINT_TESTS.csv | همهٔ مقصدها، شامل مسیر API، host، سایت و مقصد آزمون‌نشده |
| 03_REACHABLE_API_CANDIDATES.csv | نامزدهای دارای پاسخ قابل پیگیری؛ نه فهرست قابل استفاده |
| 04_AUTH_OR_SIGNUP_PENDING.csv | صف B |
| 05_POLICY_REGION_OR_WAF_REVIEW.csv | صف C |
| 06_NETWORK_UNAVAILABLE.csv | فقط صف D با شرایط سخت‌گیرانه |
| 07_FREE_TIER_VERIFICATION.csv | هزینه/سهمیه/کارت/منطقه/منبع؛ UNKNOWNها حفظ می‌شوند |
| 08_OMNIROUTE_CONNECTION_QUEUE.csv | ترتیب بررسی، نوع اتصال، مدل‌های ثبت‌شده و اقدام بعدی |
| 09_DIAGNOSTIC_REASON_COUNTS.csv | شمارش دلیل‌ها برحسب نوع مقصد؛ نه Provider یکتا |
| 10_FULL_AUDIT_RESULTS.json | داده کامل، ورودی تاریخی، metadata و hashها |
| 11_PERSIAN_EXECUTIVE_REPORT.md | گزارش فارسی و تعداد دقیق صف‌ها |
| 12_COPY_SUMMARY_TO_CHAT.txt | چند خط آمادهٔ کپی در چت |

خطوط بین `COPY TO CHAT` و `END` را مستقیم کپی کنید. یا برای پوشهٔ واقعی خروجی:

```powershell
Get-Content -LiteralPath "$env:USERPROFILE\Desktop\نام-واقعی-پوشه-خروجی\12_COPY_SUMMARY_TO_CHAT.txt" -Encoding UTF8
```

برای تحلیل کامل‌تر، فایل‌های 01 و 02 را ضمیمه کنید. ابزار فقط دادهٔ مقصدهای عمومی را خروجی می‌دهد و arbitrary columns، ErrorDetail خام، header حساس یا body را وارد گزارش نمی‌کند. فایل‌هایی که خودتان به آن‌ها اطلاعات حساب اضافه کرده‌اید برای ارسال مناسب نیستند.

## معنی صف و اولویت

A تنها پس از تأیید مستقل eligibility حساب، مدل رایگان، نبود کارت و hard stop ممکن است؛ در دادهٔ این تحویل **هیچ حسابی تأیید نشده است**. B پیگیری مسیر/ثبت‌نام/کلید/مدل؛ C بررسی سیاست، منطقه، WAF، redirect، سهمیه یا سرور؛ D عدم پاسخ مکرر در مسیر آزموده‌شده با کنترل؛ E خارج از اتصال مستقیم یا فاقد مسیر عمومی ثابت در منبع نسخه. `PENDING_EVIDENCE` یک وضعیت افزودهٔ صادقانه است تا نبود شواهد به B یا D تبدیل نشود؛ جمع پنج صف و این وضعیت دقیقاً ۳۷۵ است.

`ReviewPriority` ترتیب **بررسی** است، نه نمرهٔ هوش مدل: ۰ gateهای A؛ ۱۰ پاسخ + سرنخ رسمی طرح رایگان؛ ۲۰ پاسخ نیازمند تحقیق؛ ۵۰ شواهد ناکافی؛ ۶۰ حل خطا؛ ۷۰ بازبینی شبکه؛ ۸۰ مانع کارت/صورتحساب؛ ۹۰ integration جدا. وجود مدل در registry نه رایگان بودن آن را ثابت می‌کند و نه کیفیت/قابلیت آن را.

۴۰۱/۴۰۵ باقی می‌مانند؛ ۴۰۴ و redirect «مسیر تأییدنشده» هستند. ۴۰۳ منشأ قطعی ندارد. بدنه خوانده نمی‌شود و WAF/منطقه در نبود شواهد مستقل UNKNOWN می‌ماند. ۴۵۱ محدودیت اعلامی پاسخ‌دهنده است، نه اثبات هویت Origin. هیچ درخواست POST inference یا حتی تست موفقیت POST انجام نمی‌شود.

## مرز ایمنی و محدودیت‌ها

- کلاینت مستقیمِ داخل فرایند دارای `UseProxy=false` ثابت است؛ به proxy سیستم مراجعه نمی‌کند. برای جلوگیری از DNS rebinding، TCP را به IP عمومیِ همان پاسخ DNS pin می‌کند و SNI/اعتبارسنجی TLS را با hostname واقعی انجام می‌دهد. IP خصوصی/loopback/link-local/CGNAT و پاسخ مختلط عمومی‌ـخصوصی رد می‌شوند. هیچ redirect، مسیر login، Cookie یا Authorization دنبال/ارسال نمی‌شود.
- این روش نبود VPN/TUN، transparent proxy، ISP middlebox، CDN/WAF یا دست‌کاری trust store را ثابت نمی‌کند. سیستم‌عامل ممکن است برای اعتبارسنجی زنجیره/ابطال گواهی تماس‌های خود را انجام دهد؛ این کلاینت callback پذیرش گواهی دلخواه ندارد.
- ۳۷۵ ادغام لزوماً ۳۷۵ موتور LLM نیستند. OAuth، Web Cookie، Local، Search، Audio و CLIها مسیر پژوهشی جدا دارند. Cloudflare به account ID نیاز دارد و base `/accounts` inference کامل نیست.
- quota/حقوق تجاری/کارت/منطقه برای تمام ۳۷۵ سرویس مستقلاً تکمیل نشده‌اند. تحقیق رسمی منتخب در RESEARCH-RECEIPT-FA.md و matrix مشخص است؛ بقیه UNKNOWN و فاقد مجوز فعال‌سازی‌اند. بدون key نمی‌توان سهمیه باقی‌ماندهٔ حساب را دانست.
- GET بدون auth ممکن است نتیجه‌ای متفاوت از POST مجاز بدهد. هویت Origin و inference واقعی، eligibility ایرانی و اتصال OmniRoute در این ابزار اثبات نمی‌شوند.
- فایل ورودی v2 زمان هر درخواست ندارد؛ زمان فایل فقط منشأ جانبی است. اسکریپت نتیجهٔ گذشته را اندازه‌گیری امروز جا نمی‌زند.
- با Windows PowerShell 5.1 طراحی شده، ولی Parser واقعی 5.1، .NET Framework، trust store ویندوز و اینترنت واقعی شما هنوز باید محلی آزموده شوند. هیچ نتیجهٔ synthetic به معنی کارکرد در ایران نیست.

## فایل‌های توسعه و آزمون

`Test-Gate-Fixtures.ps1` کلاینت مصنوعی **بدون شبکه** دارد و باید در یک PowerShell جدا اجرا شود؛ در همان فرایند نباید پس از آن اسکن واقعی انجام داد. این فایل برای بازبینی توسعه‌دهنده است؛ اجرای عادی فقط فایل اصلی را می‌خواهد. `DirectHttps.cs` همان متن کلاینت تعبیه‌شده در PS1 است، نه وابستگی خارجی. `VALIDATION-RESULTS.json` نتایج واقعی محیط Work و پوشهٔ `SYNTHETIC-SAMPLE-OUTPUT` نمونهٔ ساختگی است؛ هیچ‌کدام خروجی اینترنت شما نیستند.
