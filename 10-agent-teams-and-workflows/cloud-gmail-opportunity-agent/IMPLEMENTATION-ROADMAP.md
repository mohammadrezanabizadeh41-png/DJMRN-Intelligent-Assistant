# DJMRN — نقشه راه عملی ساخت ایجنت ابری Gmail، پیگیری کار و پورتفولیو

**Project:** DJMRN-CLOUD-GMAIL-OPPORTUNITY-001
**Date / research snapshot:** 2026-11-12
**Scope:** Google-first cloud opportunity assistant + approved portfolio + future Windows agent-team integration
**Status:** EXECUTION ROADMAP APPROVED FOR DOCUMENTATION ONLY / NO PROVIDER OR GMAIL ACTIVATION
**Execution priority:** Next DJMRN project; this document is the numbered work plan, not a separate daily status ledger.
**Canonical progress:** ../../07-operations-and-continuity/CURRENT-STATUS.md
**Companion project specification:** README.md
**No secrets or personal content in this public GitHub project.**

## هدف نهایی و تعریف نتیجه قابل‌استفاده

در نبود لپ‌تاپ، در زمان‌بندی‌های محدود و بدون هزینه، فرصت‌های کاری از Gmail و بعداً منابع مجاز عمومی کشف شوند؛ از نظر مهارت، نوع پروژه، بودجه، دورکاری، امکان پرداخت و محدودیت حقوقی ارزیابی شوند؛ با پورتفولیوی تأییدشده تطبیق یابند؛ پیش‌نویس پیشنهاد فارسی/انگلیسی و یادآوری پیگیری تولید شود؛ و نتیجه مستند و قابل بازیابی به کاربر برسد. ارسال واقعی، مذاکرات و درخواست‌های سایت‌ها فقط بعد از عبور از دروازه مجوز انجام شود.

**حداقل خروجی موفق نسخه اول (MVP):** یک مأموریت Gmail واقعی و محدود به‌صورت خواندنی اجرا شود، پیام‌های مربوط به فرصت‌ها بدون تغییر mailbox دسته‌بندی شوند، نتیجه مرتبط با شناسه/لینک منبع ارائه شود، موارد تکراری حذف شوند، مدل برای ایمیل خصوصی فراخوانی نشود، یک گزارش قابل‌اقدام فارسی تحویل شود و سیستم در خطاهای OAuth/Quota/VPN درست متوقف یا بازیابی شود. مرحله بعدی ساخت Draft جداگانه تأیید می‌شود.

**این نقشه راه اجازه انجام مراحل نیست؛ هر مرحله مستقل بررسی و اقدام حساس جداگانه تأیید می‌شود.** ثبت‌نام، نصب، فعال‌سازی Gmail/Google OAuth، کلیدها، ارسال، انتشار، اتصال ارائه‌دهنده جدید، تغییر Trigger/DB/Automations و هزینه بدون مجوز ممنوع.

## اصل انتخاب فناوری و ترتیب عملی

| نقش | گزینه اولیه برای بررسی | چرا / شرط تغییر |
|---|---|---|
| اجرای ابری دوره‌ای | Google Apps Script (V8) time-driven trigger | سبک؛ بدون لپ‌تاپ همیشه روشن؛ نیازمند مجوز Gmail و محدودیت زمان/سهمیه |
| دسترسی به Gmail | Advanced Gmail Service/Gmail API با OAuth محدود | API رسمی؛ مجوز فقط خواندن در پایلوت؛ Gemini API key جای آن نیست |
| شناسایی و فیلتر | کد قطعی JS قبل از LLM | هزینه صفر و خطای کمتر؛ شرایط و محرمانگی قابل بازرسی |
| مدل تحلیل | Gemini API موجود؛ مدل سبک منتخب و Free واقعی | فقط متن عمومی/غیرحساس با شرایط مجاز؛ RPM/TPM/RPD پروژه باید بررسی شوند |
| پورتفولیو | فهرست تأییدشده + اصل فایل در Drive/مخزن مالک مناسب | GitHub فقط فایل‌ها/لینک‌های عمومیِ مجاز؛ عدم افشای رزومه خصوصی |
| ذخیره وضعیت عملیاتی | انتخاب فقط یک محل پس از آزمون: ساده در Google یا Neon موجود | هیچ حالت موازی/دو authority؛ Gmail مرجع پیام و Draft است |
| ارتباط با کاربر | گزارش فارسی/لینک‌های مرور و بعداً اعلان مصوب | گزارش‌های موجود ChatGPT نباید دوباره‌کاری تولید کنند |
| تیم پیشرفته | Google ADK 2.0 (در صورت مزیت اثبات‌شده) | چارچوب ایجنت نه هاست رایگان؛ اتصال Gmail Toolset و scope باید ممیزی شود |
| ایجنت‌های ویندوز | MausBot/OpenMausBot موجود | خروجی Cloud را فقط پس از روشن شدن دستگاه Pull کند |
| ابزارهای جایگزین | Activepieces Free، Neon Functions، Cloudflare Workers، Make، n8n Community | فقط اگر یک نیاز مشخص توسط Google-first پوشش داده نشود؛ هزینه و سهمیه تازه تأیید شود |

**سهمیه مرجع در تاریخ پژوهش (برای حساب Gmail عادی، نه ضمانت حساب واقعی):** Apps Script اجرای Trigger در مجموع ۹۰ دقیقه/روز؛ ۶ دقیقه/اجرا؛ ایمیل read/write غیر از send تا ۲۰٬۰۰۰ عملیات/روز؛ URL Fetch تا ۲۰٬۰۰۰ فراخوانی/روز؛ Properties Store حداکثر ۵۰۰KB و هر value حداکثر ۹KB. Google ممکن است این سقف‌ها را تغییر دهد. سهمیه Gemini جداگانه و در سطح پروژه است، نه در سطح API Key؛ Free Tier فقط برخی مدل‌ها را پشتیبانی می‌کند. بررسی زنده AI Studio و شرایط منطقه‌ای پیش‌شرط مدل است.

### معماری هدف پیشنهادی، نه استقرار قطعی

زمان‌بند مجاز Google → دریافت حداقلی Gmail (OAuth) → طبقه‌بندی قطعی/حذف تکراری → بررسی قابلیت و تطبیق پورتفولیو → فراخوانی Gemini فقط برای محتوای عمومی مجاز → نتیجه/وضعیت در تنها state store منتخب → گزارش انسانی → (در فاز بعد) Draft با تأیید → پیگیری پاسخ‌ها → همگام‌سازی خروجی با MausBot هنگام آنلاین شدن لپ‌تاپ.

Gmail مالک پیام/Thread/Draft است؛ GitHub مالک کد/تست/نقشه؛ Notion مالک تصمیم معماری نهایی؛ یک پایگاه‌داده منتخب مالک job state. متن محرمانه Gmail به Google Gemini **Unpaid**، سرویس مدل دیگر یا مخزن GitHub ارسال نشود. سرویس Apps Script و Gemini هر دو متعلق به Google باشند، انتقال داده را خودکار مجاز نمی‌کند.

## فاز R0 — آماده‌سازی پروژه و انتخاب یک وظیفه واقعی (نقطه شروع بعدی)

**اقدامات به ترتیب:**
1. بازخوانی همین README و همین ROADMAP و تک‌محل CURRENT-STATUS؛ بررسی سابقه پیشنهاد محلی DJMRN-EMAIL-OPPORTUNITY-AUTOMATION-001 و پروژه Opportunity Hunter؛ عدم راه‌اندازی سامانه چهارم بدون تصمیم درباره سه گزارش تکراری Gmail ChatGPT موجود.
2. تعیین یک مأموریت کوچک و قابل سنجش: مثال «شناسایی ۱۰ فرصت مناسب در ۲۴ ساعت گذشته از ایمیل‌های اعلان کار و ساخت گزارش فارسی بدون ارسال». نوع پروژه فریلنس/قراردادی، ریموت، حداقل بودجه/پرداخت، حساسیت مهلت و شرایط قبول/رد باید به تأیید کاربر برسد.
3. بررسی صرفاً خواندنیِ دسترس‌پذیری Google AI Studio، project tier، فهرست مدل‌های رایگان قابل استفاده، RPM/TPM/RPD و نیاز به فعال‌بودن billing. **کلید واقعی خوانده، درخواست، کپی یا در GitHub درج نشود.**
4. بررسی موجودی Google Apps Script/Cloud project و Gmail API/Consent فقط در محدوده مجاز؛ بدون ایجاد برنامه، Scope یا OAuth جدید. شرایط حساب مصرف‌کننده، منطقه، محرمانگی، کاربری شخصی/تجاری و هزینه پنهان را مستند و با صاحب حساب تأیید کن.
5. تصمیم اولیه درباره پورتفولیو و محل اصلی job state، بدون ایجاد پایگاه‌داده جدید.

**خروجی:** صورت‌مسئله یک‌صفحه‌ای؛ ماتریس ظرفیت/مجوز/هزینه واقعی؛ فهرست استفاده مجدد؛ و مجوزهای لازم برای R1 تا R3.
**PASS:** یک use case دقیق و بدون تداخل، مشخص بودن داده‌های مجاز و سقف هزینه صفر، بدون تغییر حساب. **STOP:** هزینه ناشناخته، مجوز Gmail نامعتبر، حریم خصوصی حل‌نشده یا عدم انطباق منطقه.

## فاز R1 — پورتفولیو و مدارک آماده ارسال، قبل از مدل و پیشنهاد

**کارهای اصلی:**
1. فهرست خدمات واقعی قابل تحویل را از سابقه‌های موجود بازبینی کن: وب/فروشگاه، Python/API/اتوماسیون، AI و ابزارها، گرافیک/ویدئو، اکسل/داده، محتوا، پشتیبانی Windows در صورت مرتبط بودن. مهارت یا نتیجه انجام‌نشده ادعا نشود.
2. فهرست منبع نمونه‌کارهای سابق را بساز (آدرس‌ها/فایل‌ها **UNVERIFIED until found**): ویدئوی نمونه «Ursala/Orsola» از Text-3 دسکتاپ؛ HTML فروشگاهی/نمونه «خانه جوانه»؛ هر نمونه کد قابل نمایش موجود در GitHub؛ نمونه تحلیل/اتوماسیون با داده ساختگی. لینک‌های عمومی فقط بعد از تأیید مالکیت، دسترسی، حق انتشار و بازشدن واقعی پذیرفته شوند.
3. یک «portfolio manifest» با ستون‌های نوع کار، مهارت اثبات‌شده، توضیح کوتاه FA/EN، لینک مجاز، تصویر/فایل منبع، حقوق نشر/اجازه، تاریخ آزمون، میزان آمادگی، دسته فرصت و وضعیت APPROVED/PRIVATE/UNVERIFIED بساز. **این سند شامل اطلاعات شخصی، شماره تماس/نشانی محرمانه یا فایل اصلی مشتری نشود.**
4. قالب رزومه/معرفی مستقل فارسی و انگلیسی، نسخه‌های تخصصی و پاسخ کوتاه/بلند به کارفرما را آماده کن؛ **نام، تجربه، پرداخت/زمان‌بندی و لینک‌ها فقط بر اساس تأیید کاربر**.
5. سیاست انتخاب نمونه برای هر آگهی: تنها ۱–۳ نمونه مرتبط، بدون ادعای ساخت سیستم منتشرنشده یا دستاورد مشتری که مجاز به افشا نیست.
6. نگهداری فایل‌های نمونه و رزومه: Drive برای مدیا/فایل‌های قابل ارائه در صورت تأیید؛ GitHub برای کد عمومی مجاز؛ در pipeline فقط ارجاع به asset ID و وضعیت انتشار؛ بدون بارگذاری خودکار اسناد شخصی در سرویس‌های AI.

**خروجی:** Portfolio Manifest تأییدشده، حداقل ۲ بسته معرفی تخصصی FA/EN، یک متن اصلی شرایط همکاری، راهنمای موارد ممنوع در پیشنهاد.
**PASS:** هر نمونه لینک واقعاً کار کند، اجازه انتشار داشته باشد و با مهارت/فرصت مرتبط باشد. **STOP:** نمونه نامعتبر یا اطلاعات محرمانه/حق نشر نامعلوم. انتشار یا اتصال Drive نیازمند approval مستقل.

## فاز R2 — طراحی قرارداد داده و شبیه‌ساز بدون حساب واقعی

1. از APIهای موجود و کدهای Opportunity Hunter قرارداد مشترک ورودی/خروجی را استخراج و reuse کن؛ ابتدا قرارداد ساده در کد و تست، نه ساخت registry/queue framework جدید.
2. فیلدهای کمینه Opportunity: شناسه منبع/پیام/thread، زمان مشاهده، نوع آگهی، URL، دسته مهارت، سقف/کف بودجه اگر معلوم، ریموت/محدودیت، deadline، fit reason، سطح اطمینان، وضعیت، next_action و timestamps.
3. برای هر فرصت کلید یکتا source + externalID یا messageID و dedup با historyId Gmail تعریف کن. داده متنی پیام فقط در Gmail بماند؛ در job state حداکثر خلاصه پالایش‌شده/ارجاع.
4. وضعیت‌ها: NEW → FILTERED → QUALIFIED/REJECTED/REVIEW → REPORT_READY → DRAFT_REQUESTED → DRAFT_READY → HUMAN_APPROVAL → SENT_BY_HUMAN → WAIT_REPLY → REPLIED/FOLLOW_UP_DUE → CLOSED. ERROR, RATE_LIMITED, PRIVACY_BLOCKED و AUTH_REVOKED حالت‌های مستقل‌اند. فازهای بدون مجوز به حالت send نباید برسند.
5. ۱۰–۲۰ ایمیل و آگهی ساختگی شامل اعلان واقعی‌نما، کلاه‌برداری، لینک خراب، تکرار، محدودیت کشور و پیام حاوی prompt injection بساز؛ از داده شخصی استفاده نشود.
6. قواعد تشخیص نوع اعلان، fit و انتخاب نمونه‌کار را به‌صورت pure deterministic functions با تست‌های مصنوعی بساز. مبدأ/دلیل تصمیم حفظ شود.
7. آزمون offline: دو اجرای تکراری باید خروجی تکراری نسازند؛ «متن پیام» نباید اجازه ارسال، تغییر دسترسی یا درخواست رمز ایجاد کند.

**خروجی:** قرارداد قابل آزمون، ماژول فیلتر، state machine، تست و نمونه گزارش فارسی.
**PASS:** تست‌های طبقه‌بندی و idempotency، ۰ ارسال، ۰ درخواست API و ۰ استفاده از داده واقعی.

## فاز R3 — نمونه اجرایی ابری Apps Script با داده ساختگی

1. تنها بعد از تأیید، یک Apps Script آزمایشی جدا از حساب‌های production ایجاد و کد ساده R2 را وارد کن.
2. ابتدا تابع دستی دریافت ۱۰ رویداد ساختگی و گزارش خروجی بساز؛ نه Gmail API، نه Gemini، نه هیچ Trigger فعال.
3. محدودیت زمان اجرا، خطا، ذخیره حداقلی cursor و فرصت‌های تکراری را اندازه‌گیری کن؛ log را از محتوای شخصی پاک کن.
4. بعداً با مجوز مستقل یک زمان‌بندی آزمایشی کوتاه، مثلاً یک یا دو اجرای محدود، با stop switch بررسی کن؛ از همین‌جا به‌بعد هر Cron فعال، خودش یک اقدام زمان‌بندی‌شده است.
5. Google Apps Script installable triggers تحت حساب سازنده اجرا می‌شوند، ممکن است دقیقاً در دقیقه اعلام‌شده اجرا نشوند و Runtime کل روز سقف دارد؛ برای SLA سخت مناسب نیست.

**خروجی:** اجرای ابری تستی قابل بازبینی بدون روشن بودن لپ‌تاپ.
**PASS:** نتیجه قابل‌تکرار، گزارش اجرا/خطا، ۰ داده خصوصی و ۰ هزینه؛ توقف/غیرفعال‌سازی واقعی قابل آزمون.

## فاز R4 — Gmail اتصال OAuth حداقلی و پایلوت فقط‌خواندنی

**گیت مجوز:** دسترسی به Gmail یا Consent، حتی اگر همان حساب قبلی باشد، باید برای این برنامه و Scopeهای دقیق تأیید شود.

1. از Gmail API Advanced Service / مسیر رسمی OAuth استفاده کن، نه رمز عبور، OTP، ذخیره کوکی یا key Gemini برای ورود Gmail. خواندن بدنه نیازمند gmail.readonly (Restricted) است؛ metadata-only scope فقط header/label را می‌دهد و **Gmail API search parameter q با gmail.metadata قابل استفاده نیست**؛ بنابراین طرح فیلتر انتخابی باید مطابق Scope واقعی اصلاح شود.
2. قبل از هر Scope در سند مجوز مشخص کن چه می‌خوانیم و کجا نگه می‌داریم. Audit الزامات Google OAuth restricted scope، استثنائات personal-use/testing و امکان نیاز به security assessment؛ فعال‌کردن سرویس شخصی را به‌طور خودکار «بدون مجوز» یا «بدون الزام ارزیابی» فرض نکن.
3. از یک بازه کوچک و allowlist محدود شروع کن: مثلاً ۵ تا ۱۰ ایمیل مرتبط کاری، label/فرستنده و تاریخ مشخص، فقط پس از تأیید؛ بدون علامت‌گذاری read، جابه‌جایی، حذف، Draft یا ارسال.
4. داده پیام در Gmail بماند. فقط شناسه/زمان/تگ/نتیجه تصمیم در state store مجاز ذخیره شود. اگر بدنه برای تصمیم لازم است، دسترسی in-memory محدود؛ هیچ انتقال به سرویس AI رایگان در این مرحله.
5. بعد از اولین full sync محدود، historyId ثبت و برای ادامه از history.list استفاده شود. historyId قدیمی ممکن است 404 بدهد؛ fallback bounded resync، بدون تکرار پیام.
6. با سه ChatGPT automations موجود تطبیق بده؛ منبع گزارش تکراری/مالک واحد هر فرآیند باید مشخص شود؛ هیچ Automation قبلی بدون مجوز تغییر نکند.

**خروجی:** گزارش ۵–۱۰ ایمیل واقعی در محدوده مجاز همراه شناسه/دلیل، بدون افشای محتوا در logs.
**PASS:** عدم تغییر Gmail، dedup، OAuth revocation → توقف امن، 429 → backoff، history 404 → sync محدود.

## فاز R5 — امتیازدهی و تحلیل محدود با Gemini Free

1. تأیید فعال بودن Free Tier حساب/پروژه موجود و اینکه مدل منتخب در منطقه و شرایط رسمی مجاز است؛ بررسی quota از AI Studio (RPM/TPM/RPD)، سقف روزانه برای همین workflow و عدم billing/overage.
2. قبل از هر مدل یک فیلتر «PUBLIC_SHAREABLE» بگذار: تنها متن آگهی عمومی/مجاز، بدون نام یا اطلاعات شناسایی شخصی، اطلاعات نامه خصوصی، پیوست، شماره تماس/حساب/رزومه شخصی. موارد محرمانه با قواعد deterministic یا review انسانی، بدون ارسال به unpaid Gemini.
3. قرارداد prompt ساختاریافته: fit score، دلایل با ارجاع، شواهد کافی/ناکافی، خطرها، دسته پیشنهادی از R1 و JSON schema؛ هیچ ادعای ناشی از مدل evidence نیست.
4. کم‌مصرف‌ترین مدل مجاز را با نمونه‌های ساختگی/عمومی آزمایش کن؛ خروجی ۲ مدل فقط اگر تفاوت قابل‌ارزیابی یا نیاز واقعی وجود دارد. نرخ و تعداد call را ثبت کن؛ با 429 و حریم خصوصی معیوب fail closed.
5. سیستم بدون مدل باید همچنان نسخه حداقلی فرصت‌های واجدشرایط را گزارش دهد.

**خروجی:** گزارش امتیازدار و مستند فرصت‌های عمومی + مقایسه دقت/هزینه/تاخیر در مقابل فیلتر قطعی.
**PASS:** کیفیت بهترِ قابل اندازه‌گیری، داده مجاز، بدون کلید در log، سقف رایگان محقق. **STOP:** حریم خصوصی نامشخص یا هزینه غیرصفر.

## فاز R6 — ساخت پیشنهاد/رزومه متناسب و Gmail Draft

**گیت جدید:** این مرحله WRITE روی Gmail است و نیازمند مجوز gmail.compose جدا از خواندن؛ این scope می‌تواند عملیات ارسال هم پوشش دهد، بنابراین **ابزار ارسال نباید در کد یا در اختیار ایجنت باشد**. استفاده از gmail.send نیز تنها در مرحله مجاز بعدی ممکن است.

1. برای هر فرصت QUALIFIED در portfolio manifest بهترین نمونه‌ها، متن معرفی، تعهدات مجاز و پرسش‌های لازم را انتخاب کن. ساخت متن می‌تواند template-based باشد؛ مدل فقط برای متن عمومی مجاز استفاده شود.
2. پیش‌نویس در ابتدا فقط داخل خود برنامه و بدون Gmail Draft واقعی تولید شود، با QA منبع و بررسی فارسی/انگلیسی.
3. بعد از مجوز، Gmail drafts.create را با MIME صحیح، threadId، Subject و References/In-Reply-To سازگار برای پاسخ به رشته قبلی آزمایش کن؛ اگر thread پیوست نیست، ایمیل جدید نساخته/ارسال نکن تا کاربر تصمیم بگیرد.
4. قبل از هر Gmail Draft دوم، وضعیت همان job و draft ID را بخوان؛ به ازای یک opportunity یک draft تأییدشده حفظ شود؛ duplicate drafts ممنوع.
5. ارسال پیشنهاد، دعوت جلسه، قیمت‌گذاری، تعهد، فایل پیوست و مذاکره حساس به طور پیش‌فرض MANUAL_APPROVAL باشد.

**خروجی:** یک پیش‌نویس Gmail صحیح و آماده تصمیم انسانی؛ لینک فرصت + منابع نمونه‌کار و چرایی تناسب.
**PASS:** ۰ ارسال ناخواسته، ۰ ادعای غیرواقعی، thread درست و بازرسی انسانی.

## فاز R7 — پیگیری جواب کارفرما و اطلاع‌رسانی

1. threadIDهای پیگیری را با Gmail API بررسی کن؛ پاسخ جدید واقعی را از پیام خودکار/بازگشت خطا جدا کن.
2. اعلان کوتاه فارسی ایجاد کن: کارفرما، درخواست، موعد، مرحله، متن پیشنهادی برای پاسخ و لینک thread. داده محرمانه در کانال اعلان بدون اجازه منتشر نشود.
3. برای موارد بدون پاسخ، next_followup_at با سیاست تعداد دفعات، فاصله و opt-out ثبت شود؛ spam و تکرار ممنوع.
4. فقط Draft پیگیری بساز، ارسال خودکار را فعلاً مسدود نگه دار. ارسال خودکار تنها در یک پیشنهاد مجوز جدا با مخاطبان/قالب/حدود دقیق و kill switch قابل بحث است.
5. در صورت لغو دسترسی، پایان پروژه یا اعلام عدم تمایل طرف مقابل، همه پیگیری‌های بعدی متوقف شوند.

**خروجی:** وضعیت هر مکاتبه به‌روز و یک اعلان قابل اقدام برای کاربر.
**PASS:** پاسخ جدید از قلم نیفتد؛ دوباره یادآوری بیجا نشود؛ هیچ ارسال بدون approval.

## فاز R8 — توسعه سایت‌ها و فرصت‌های عمومی، از کارنامه موجود

1. جریان «ورود از ایمیل → سایت» قبلاً فقط برای این پنج پلتفرم در DJMRN تعیین شده: Creativepool، Joberz (هویت/دامنه دقیق تأیید شود)، Voice123، LinkedIn، iEstekhdam. بقیه سایت‌ها در گردش‌کار مستقل کشف عمومی Opportunity Hunter بررسی می‌شوند.
2. برای هر سایت ابتدا Terms/robots/API/RSS و دسترسی واقعی/رایگان ارسال پیشنهاد را بررسی کن؛ ادعاهای ۲۰۲۶ درباره اپلای رایگان باید دوباره تأیید شوند.
3. عمومی/بدون ورود: API یا RSS و پایش با cron؛ ورود/درخواست کارفرما: فقط با OAuth یا نشست مجاز و approve، بدون ذخیره رمز، CAPTCHA bypass، KYC bypass یا ارسال خودکار گسترده.
4. هر درخواست فقط یک owner و jobID، با مدل/رزومه مناسب R1 و check واقعی confirmation after submit.
5. از data store و پورتفولیوی فازهای قبلی reuse کن؛ crawler/API gateway دوم بدون نیاز اثبات‌شده نساز.

**خروجی:** یک سایت منتخب با فیلتر درست و خروجی پیش‌نویس مرتبط؛ درخواست/ارسال تا approval متوقف.
**PASS:** لینک واقعی، قوانین سایت رعایت شود، صفر پیشنهاد نامجاز.

## فاز R9 — Google ADK 2.0: ارزیابی عملی و ارتقا فقط در صورت مزیت

**Google ADK فراموش نشود؛ اما برای نسخه اول الزام نصب نیست.** شامل agent/tool orchestration، graph-based/dynamic/collaborative workflows، evaluator و Google Apps Toolsets برای Gmail، Calendar، Sheets، Docs. مدل Gemini جداگانه و با API/سهمیه مستقل است؛ ADK یک Cloud رایگان آماده یا scheduler نیست.

1. پس از R4–R7 تنها اگر مسئله واقعی حل‌نشده پیدا شد (مثل نیاز به بازبینی مستقل یا گردش‌کار پیچیده چندسایته)، ADK Python 2.0 را در محیط غیرحساس با داده ساختگی آزمایش کن؛ با یک coordinator + یک reviewer، نه هفت ایجنت مقیم.
2. **گیت امنیتی مهم:** GmailToolset آماده در ADK Python بر اساس docs ممکن است به‌طور پیش‌فرض scope بسیار وسیع https://mail.google.com/ بخواهد؛ tool_filter صرفاً ابزار قابل‌فراخوانی را محدود می‌کند، **Scope را محدود نمی‌کند**. راه ادغام least-privilege مثل OAuth جداگانه و function-tool wrapper بر Gmail API بررسی شود. بدون رفع این گیت، اتصال ADK به Gmail واقعی DENY.
3. لاگ‌ها و ترسیم جریان داده را با نمونه بدون PII تست کن؛ ایمیل دریافتی untrusted است و نباید از طریق prompt دسترسی دیگر ابزارها یا ارسال را باز کند.
4. اجرای ابری ADK می‌تواند در Cloud Run یا میزبان دیگر باشد، اما **Cloud Run free usage = تعهد هزینه صفر نیست**. نیاز به billing/IAM/secret manager/egress/scheduler و overage باید رسمی و با حساب واقعی تأیید شود؛ Unknown cost=DENY.
5. معیار مقایسه: درصد تشخیص درست، کیفیت Draft، مدیریت خرابی، زمان پردازش و تعداد token/API calls، سطح دسترسی و نگهداری در مقایسه با Apps Script ساده.
6. اگر بهبود معنادار و هزینه صفر تأیید نشد، **ADK در نقش ON_DEMAND** باقی می‌ماند و سیستم Google Apps Script ادامه می‌یابد.

**خروجی:** گزارش قابل سنجش ADK vs Apps Script و توصیه KEEP/INTEGRATE/DEFER؛ نه مهاجرت بدون مجوز.
**PASS:** نیاز واقعی، ابزار کم‌دسترسی، بدون داده حساس و هزینه، و کیفیت بهتر؛ در غیر این صورت DEFER.

## فاز R10 — همکاری ابری و دسکتاپ، مقاوم در برابر خاموشی/VPN

1. فقط پس از اینکه Cloud مستقلاً خروجی مفید و durable state اثبات کرد، یک API/adapter کم‌مجوز برای Windows MausBot در نظر بگیر.
2. Cloud وظایف محدود و ساختاریافته را انجام دهد و نتیجه را با شناسه و زمان در **همان** محل state مورد تأیید ذخیره کند. لپ‌تاپ وقتی آنلاین شد با اتصال خروجی امن Pull، ack/idempotency، و در صورت لزوم درخواست کمک agent تخصصی انجام دهد.
3. هیچ پورتی روی Windows برای دسترسی inbound باز نشود؛ VPN/proxy local تغییر کند نباید jobهای Cloud متوقف شوند. اما eligibility و network-policy سرور ابری تضمین‌شده نیست.
4. مقاومت: restart، duplicate event، تغییر token، 429، timeout، webhook missed، conflict between cloud and local owners، sync-after-days.
5. سنجش مصرف واقعی و ارزش: فرصت‌های واجدشرایط، نرخ تبدیل به مذاکره، draftهای تأییدشده، کیفیت پاسخ کارفرما، هزینه و مصرف quota.

**خروجی:** مسیر end-to-end Cloud (laptop off) → persisted result → online Windows acknowledgment.
**PASS:** بدون تکرار/افشای داده/هزینه و با امکان توقف/بازیابی.

## ترتیب اجرایی کوتاه و فهرست گیت‌های Approval

| ترتیب | اولین اقدام مجاز در آن گیت | مجوز موردنیاز | معیار خروج |
|---|---|---|---|
| 0 | ممیزی read-only Google API availability و سه Gmail automation | فقط‌خواندنی در محدوده موجود | روشن شدن scope، free quota، تداخل و داده مجاز |
| 1 | تکمیل پورتفولیو و قالب‌های پاسخ بدون انتشار خودکار | بررسی و تأیید نمونه/رزومه | دارایی قابل استناد و قابل‌استفاده |
| 2 | نوشتن/تست کد با داده ساختگی | approval ساخت source در مخزن | تست dedup/filter/report PASS |
| 3 | ایجاد محیط آزمایشی Apps Script بدون Gmail | approval ایجاد/تنظیم محیط | synthetic cloud run PASS |
| 4 | اتصال Gmail read-only محدود | OAuth/Scope + موافقت برای خواندن پیام واقعی | ۵–۱۰ پیام مرتبط، صفر side effect |
| 5 | اتصال Gemini فقط برای آگهی‌های عمومی | تأیید Free Tier/داده/مدل | نتیجه بهتر و مصرف صفر |
| 6 | ساخت Gmail Draft | مجوز WRITE محدود | draft صحیح، صفر send |
| 7 | پیگیری پاسخ و گزارش | مجوز Trigger و سیاست پیگیری | reply watcher بدون duplicate |
| 8 | اتصال سایت‌های کاری | مجوز مستقل هر سایت/اکانت | فرصت واقعی، بدون ارسال نامجاز |
| 9 | ارزیابی ADK 2.0 | تأیید آزمون کم‌دسترسی و هزینه صفر | برتری سنجیده یا DEFER |
| 10 | هماهنگی با MausBot و deploy | approval security/deploy/state migration | real I/O + recovery + observable value |

## تست‌های الزام‌آور و کنترل هزینه/امنیت

- **Secrets:** Gemini API Key پیشاپیش نزد کاربر است ولی نباید در پیام، GitHub، log، Portfolio یا خروجی مدل درج شود. نگهداری در مکان runtime-specific با محدودیت دسترسی و rollback؛ برای Gmail OAuth هیچ رمز/OTP/cookie مستقیم گرفته نشود.
- **OAuth:** gmail.metadata و gmail.readonly از نظر گوگل Restricted هستند؛ gmail.compose نیز Restricted؛ gmail.send Sensitive؛ mail.google.com بسیار گسترده و غیرقابل قبول برای MVP. انتقال داده محدودشده به سرور ثالث ممکن است نیازمند ممیزی امنیتی باشد؛ وضعیت personal-use exception باید طبق docs بررسی شود، نه حدس.
- **Privacy:** Gemini Unpaid ورودی/خروجی را ممکن است برای بهبود محصولات استفاده کند و بازبین انسانی داشته باشد. اطلاعات شخصی/محرمانه/متن کامل Gmail و مشخصات خصوصی کارفرما به آن فرستاده نمی‌شود.
- **Quota:** وضعیت واقعی RPM/TPM/RPD را از AI Studio و نرخ refresh و reset بگیر. قبل از هر فراخوانی check budget، توقف در quota/price anomaly، بدون automatic top-up، بدون charge یا paid fallback.
- **Model quality:** prompt injection و hallucination، false positive/false negative، فریب آگهی، محتوای حساس، لینک‌های مشکوک، تداخل ده‌ها اتوماسیون و اشتباه در thread reply تست شوند.
- **Reliability:** Timeout + retry with jitter/backoff، per-message idempotency، safe cursor resync، kill switch، هشدار failure، ثبت provenance و استفاده از داده تازه؛ monitor logs metadata only.
- **Definition of DONE:** مدرک real I/O، ذخیره پایدار، آزمون، نظارت، مالکیت داده، امنیت، بازگشت‌پذیری، هزینه صفر تأییدشده، کمک واقعی به دریافت پروژه. یک ماژول/نسخه/پرونده به تنهایی DONE نیست.

## راهنمای ادامه در پنجره یا ایجنت جدید

**شروع کار:** فایل همین ROADMAP و README پروژه و ابتدای CURRENT-STATUS را از مخزن اصلی/شاخه main بخوان. سپس تنها گیت بعدیِ صریحاً مجاز را بررسی کن. هر بار مورد انجام‌شده را با واقعیت GitHub/Google/Gmail مستقل verify کن؛ هیچ موفقیت آزمایش/اجرا را از متن پلان استنباط نکن. مسیر پیشرفت فقط CURRENT-STATUS است؛ فایل نقشه راه برای ترتیب و قرارداد کار ثابت می‌ماند و با تصمیم رسمی بعدی نسخه‌دار می‌شود. Notion برای rationale/تصمیم معماری پذیرش‌یافته و یک کانون حقیقت باقی بماند؛ این سند صرفاً SPEC/PROPOSAL است.

**نخستین مأموریت اجرایی که بعداً می‌توان به تیم سپرد:**
«R0 را فقط به‌صورت READ-ONLY اجرا کن: اسناد موجود، وضعیت سه اتوماسیون Gmail، Google Apps Script/Gmail OAuth و Free Tier Gemini را بررسی کن. هیچ API Key یا رمز نخواه، هیچ حساب/API/Trigger/Scope ایجاد نکن، هیچ Gmail خصوصی نخوان و هیچ هزینه‌ای ایجاد نکن. یک پیشنهاد R1/R2 با معیار قبول/رد و درخواست مجوز گیت بعد بده.»

## منابع رسمی مبنای تصمیم (بازبینی 2026-11-12)

- Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas
- Apps Script time triggers: https://developers.google.com/apps-script/guides/triggers/installable
- Advanced Gmail service: https://developers.google.com/apps-script/advanced/gmail
- Gmail OAuth scopes & restricted permissions: https://developers.google.com/workspace/gmail/api/auth/scopes
- Gmail messages.list query (metadata restriction): https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- Gmail synchronization/history error: https://developers.google.com/workspace/gmail/api/guides/sync
- Gmail threading reply rules: https://developers.google.com/workspace/gmail/api/guides/threads
- Gmail Drafts: https://developers.google.com/workspace/gmail/api/guides/drafts
- Gemini pricing/free tier: https://ai.google.dev/gemini-api/docs/pricing
- Gemini rate limits: https://ai.google.dev/gemini-api/docs/rate-limits
- Gemini Unpaid privacy: https://ai.google.dev/gemini-api/terms
- Google ADK 2.0: https://adk.dev/2.0/
- ADK Google Apps Toolsets and default Gmail scope warning: https://adk.dev/integrations/google-api-toolsets/
- Google OAuth restricted-scope verification/exceptions: https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification
