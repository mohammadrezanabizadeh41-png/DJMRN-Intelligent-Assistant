# گزارش بازسازی و تطبیق DJMRN

## منشأ خط مبنا

۱. [Source A، نتایج مثبت ۱۶۰تایی](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/06-tests-and-evidence/provider-research/DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md): عدد ۲۵۲ در عنوان به دامنهٔ تحقیق اشاره دارد. جدول مثبت شامل ۱۶۰ شناسه است و به تنهایی خط مبنای کامل نیست.

۲. [کاتالوگ کامل ۲۵۲ API-key](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/06-tests-and-evidence/provider-research/OMNIROUTE-252-APIKEY-PROVIDER-CATALOG-V3852-20261030.md): ۲۵۲ ردیف، ۲۵۲ شناسه یکتا، شماره‌های ۱ تا ۲۵۲؛ blob SHA: `943fca04aa487db9db8348f99d5bc9e2850d990f`. نتیجه `BASELINE_COMPLETE`.

۳. [CURRENT-STATUS](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/07-operations-and-continuity/CURRENT-STATUS.md): فقط بخش `DJMRN-FREE-API-R08-USER-APPROVAL-20261031` مبنای تصمیم است، نه snapshotهای تاریخی R07 و قبل. ۱۳۷ تأیید، ۲۳ حذف، اشتراک صفر. blob SHA: `1573797f224a211e59e9b2447239d08cfe85835b`.

۴. [کاتالوگ وسیع‌تر ۳۷۵تایی](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/06-tests-and-evidence/tools/omniroute-iran-direct-check/OmniRoute_v3.8.52_375_providers.csv): blob SHA: `90e600e1f4e3f31a25e2ecf6ab6cb71241079d07`. هر ۲۵۲ شناسه در آن پیدا شد. دامنه و alias استخراج‌شده از این کاتالوگ، بازتأیید امروز مالکیت دامنه نیست.

۵. دو سند زندهٔ `DJMRN — Persistent Operating Memory` و `DJMRN — Tool Governance & Architecture Intelligence` پیش از کشف مطالعه شدند؛ شناسه‌های Notion به ترتیب `3edc8c68-4690-814a-9707-cb880534f462` و `3edc8c68-4690-81cc-90ab-dd5183f1bdb1`. این مأموریت مستقل، هیچ نوشتنی در منابع زنده انجام نمی‌دهد.

## روش و نتیجه

تطبیق exact ID با تمام ۲۵۲ و ۳۷۵ ردیف انجام شد. سپس نام، alias، hostname، شرکت مادر و محصول/API با شواهد عمومی بررسی شد. تطبیق دامنه قرینهٔ هویت است، نه حکم ادغام شرکت‌ها. ۳۹ ردیف MAIN هیچ exact ID مشترکی با هیچ‌یک از دو کاتالوگ ندارند. شواهد هویت نامطمئن به HOLD منتقل شدند. این نتیجه نبودن در اسناد بازیابی‌شده را نشان می‌دهد؛ غیبت از هر مکالمه یا هر رکورد تاریخی دیگر DJMRN اثبات نشده است.

۱۵ ردیف زیر بیرون از ۲۵۲، اما از پیش در ۳۷۵ شناخته شده‌اند و در کشف تازه شمرده نمی‌شوند:

`deepgram, assemblyai, speechmatics, cartesia, elevenlabs, fishaudio, gladia, exa-search, tavily-search, parallel-search, youcom-search, inworld, aihorde, firecrawl, soniox`

۲۳ مورد حذف‌شدهٔ کاربر در فایل مستقل `04-EXCLUDED-23.csv` حفظ شده‌اند. هیچ‌یک در MAIN نیستند. هیچ تصمیمی دوباره ارزیابی یا تغییر داده نشد. ۹۲ شناسهٔ دیگر خط مبنای ۲۵۲ خارج از مجموعهٔ ۱۶۰ تصمیم مثبت هستند؛ این وضعیت مساوی «حذف کاربر» نیست.

## موارد مهم هویت

| مورد | تصمیم تطبیق | دلیل و محدودیت |
|---|---|---|
| Codiv / TypeSafe / Jev | NEW_DISTINCT_API_PRODUCT | سازگاری wire یا مدل مشترک، برابری endpoint را ثابت نمی‌کند؛ API در api.codiv.ai است. شرکت حقوقی مستقل UNKNOWN. |
| BharatRouter / Krutrim | محصول یک گروه | محصول متمایز، شرکت مادر مشترک؛ دو گرنت مستقل یا دو شرکت شمرده نشوند. Krutrim در HOLD است. |
| Sail computer/systems/industries | یک ردیف | aliasهای یک خدمت؛ چند ارائه‌دهنده ساخته نشد. |
| Infron / OneRouter | یک ردیف مشروط به پرداخت | endpoint مرتبط llm.onerouter.pro و حداقل موجودی، دلیل کشف رایگان تازه نیست. |
| LlamaParse / LlamaCloud | یک محصول/سهمیه | دو بار شمرده نشده است. |
| Moondream / Prime | HOLD | مهاجرت/تملک و تناقض قیمت؛ استقلال یا گرنت قدیمی فرض نشده است. |
| SmarToken | نامزد با هشدار | thesmartoken.com با smartoken.com یا smartokenx.com بدون مدرک ادغام نشده است. |
| GonkaBroker | UNCERTAIN_IDENTITY | docs.gonkabroker.com و دامنه‌های مشابه به طور خودکار یکی نیستند. |
| Naga AI / Naga AC و Kimi / Moonshot در baseline | حفظ شناسه‌های جدا | شناسه‌های فنی متفاوت به‌علت شباهت شرکت ادغام نشدند. |

## معنی دسته‌ها و IDها

`MAIN`: پیشنهاد رایگان عمومی برای نامزد تازهٔ واجد بررسی. `HOLD`: هویت، entitlement یا قیمت/فعال بودن نامشخص. `KNOWN_OUTSIDE_252`: از قبل در پروژه. `PAYMENT_CONDITIONAL`: پرداخت شرط استفاده. `OUT_OF_SCOPE`: compute خام.

`NEW_PROVIDER` در داده به معنی هویت خدمت در اسناد مقایسه‌شده است؛ ثبت حقوقی مستقل تأیید نشده است. IDهای تازهٔ MAIN شناسه‌های پیشنهادی همین پژوهش هستند، نه نام داخلی صادرشده از ارائه‌دهنده یا شناسهٔ از قبل پذیرفتهٔ Gateway. فیلد `ID_Provenance` این تمایز را نگه می‌دارد. `ALREADY_IN_BASELINE` و `PREVIOUSLY_EXCLUDED` در CSV خط مبنا قابل تشخیص‌اند؛ در مخزن کشف تازه حضور ندارند.

پیشنهاد رایگان جدید برای شرکت موجود تنها وقتی با تاریخ رسمی روشن باشد گزارش می‌شود. هیچ پایش کامل تغییرات هر ۲۵۲ سرویس انجام نشده است. تغییر Fish S2.1 و Firecrawl در فهرست شناخته‌شده، دلیل افزودن دوبارهٔ شرکت نیست.
