# پروتکل دریافت و تبدیل پژوهش به دانش قابل استفاده

## مسیرهای ورود
1. **متن ارسالی کاربر از پژوهش قبلی:** متن را **به‌عنوان raw user-supplied** با منشأ/تاریخ/عنوان (اگر داده شده) در `inbox/SRC-####-[slug].md` ثبت کن، در صورت حساسیت پیش از commit sanitize. نقل‌قول بلند/متن شخص ثالث را با رعایت حقوق نشر/اجازه منتشر نکن؛ در موارد نامشخص به جای بازنشر کامل، بخش مجاز و لینک اصل منبع را نگهدار.
2. **Notion Applied/General:** شاخه، عنوان، نسخهٔ دیده‌شده، URL و fragment/provenance را یادداشت کن؛ فقط بخش مرتبط را به زبان خود برای پروژه استخراج کن و به Notion لینک بده؛ نسخهٔ قدیمی را واقعیت امروز فرض نکن.
3. **Work:** [04-work-research-bridge](../04-work-research-bridge/README.md) را بخوان؛ WQ/WA واقعی و `reviews/WQ####.md` باید مستقل بازبینی شوند. Work مالک raw response است؛ هماهنگ‌کننده مدخل KB را می‌سازد؛ **Work به‌صورت خودکار دانشنامه یا decision register را ویرایش نمی‌کند**.
4. **جست‌وجوی مستقیم و اسناد رسمی:** exact URL، ناشر، release/version، observed_at و بخش پشتیبان ادعا را ثبت کن. search engine فقط مسیر کشف است، نه منبع اعتبار.
5. **کد/آزمایش واقعی:** فایل repo، commit، Test ID، خروجی sanitized و تاریخ دستگاه را بگذار؛ نتیجه را از user report با independently verified جدا کن.

## مراحل پذیرش یک ورودی
**RECEIVE → CHECK ACCESS/SAFETY → RAW ARCHIVE (if appropriate) → SOURCE REGISTER → DEDUPE/ALIAS → ATOMIC FACT EXTRACTION → OFFICIAL/PRIMARY VERIFICATION → RELEVANCE TO DJMRN → KNOWLEDGE ENTRY → INDEX/LINKS → OPEN GAPS → READBACK.**

- یک منبع جدید لزوماً مدخل دانش ارزشمند نیست. اگر نامرتبط، منسوخ، ناامن یا duplicate بود، ورودی و علت تصمیم را بدون ارتقای ادعا ثبت کن.
- هر گزاره باید برچسب `FACT / CLAIM / INFERENCE / HYPOTHESIS / UNKNOWN` داشته باشد و با فیلد `supported_by` به منبع دقیق وصل باشد. اگر چند منبع تعارض دارند `CONFLICT` ثبت کن؛ میانگین/انتخاب حدسی نکن.
- پیش از ورود در دستهٔ architecture، «چرا برای این دستگاه و این کاربرد مهم است؟» و «چه چیزی هنوز آزمایش نشده؟» را پاسخ بده.
- **Original research may be useful even without verification** اما تا منبع اصلی/آزمون تأیید نشود با `CURATED-UNVERIFIED` باقی بماند؛ ایده را با اجرای تأییدشده اشتباه نگیر.
- **نتیجهٔ مقایسه در KB** به معنی `SELECTED` نیست. گزینه‌های متضاد را حفظ کن؛ تصمیم‌های واقعی با شماره `D-` در [Decision Register](../02-project-management/DECISION-REGISTER.md) و کد/تست در 05/06 ثبت شوند.

## کنترل بروزرسانی، اصلاح و supersession
- در هر مدخل `observed_at`, `checked_at`, `review_due` و `source_version` را در صورت موجود بودن نگهدار. اطلاعات ناپایدار مانند pricing/releases/legal/region با تاریخ منقضی می‌شود؛ revalidate **در لحظه تصمیم**.
- اگر گزاره رد شد، مدخل را پاک نکن؛ `SUPERSEDED/CONTRADICTED` و لینک نسخهٔ اصلاحی و دلیل بیفزا. فایل خام اولیه تغییر نکند مگر redaction/حقوق انتشار نیاز باشد.
- شناسهٔ جدید بعد از بررسی `INDEX`, `SOURCE-REGISTER` و مسیر واقعی repo؛ شکست/ابهام GitHub write = fetch قبل از retry، بدون overwrite.
- انتهای کار: دقیقاً مسیر/commit readback verified + تعداد source/KB + شکاف‌های باز + وضعیت بدون نصب را در CHANGELOG / در صورت اهمیت CURRENT ثبت کن.

## قرارداد مخصوص متن بعدی کاربر
**اکنون هنوز متن پژوهش قبلی دریافت نشده.** بعد از دریافت آن، اصل مجاز را با label `USER-SUPPLIED / UNVERIFIED-PENDING-REVIEW` ثبت می‌کنیم، نکته‌های متمایز را دسته‌بندی، ارزش فنی/محدودیت/تعارض را بررسی، و سپس مدخل‌ها و لینک‌های معماری می‌سازیم. لازم نیست برای دریافت نمونهٔ بعدی WQ0001 ساخته شود؛ Work فقط برای شکاف پژوهشی واقعی بعد از intake مورد استفاده است.
