# DJMRN — Crypto Market Intelligence | پروژه رمز ارز
**Mission ID:** DJMRN-CRYPTO-MARKET-001  
**Status:** PLANNED / RESEARCH COMPLETE IN PART / NO INSTALLATION / NO LIVE TRADING  
**Date:** 2026-11-06  
**Canonical progress and next action:** [CURRENT-STATUS.md](../07-operations-and-continuity/CURRENT-STATUS.md). This file is the topical product specification, research synthesis and staged acceptance plan, NOT a second daily status log.

## 1. هدف واقعی و غیرقابل‌تقلیل
یک تحلیلگر مالی هوشمند و همیشه‌فعال هنگام روشن‌بودن رایانه، ابتدا برای رمزارز و بعد در صورت تأمین داده معتبر برای سایر بازارها. سیستم باید *خودش* دارایی‌های تازه و فرصت‌های مناسب را پیدا کند، حدود ۱۰۰ بازار را پایش کند، داده قیمت/حجم/نقدینگی، تکنیکال، فاندامنتال، توکنومیک، داده درون‌زنجیره، اخبار رسمی و اقتصاد کلان را ترکیب کند، مدل‌ها و استراتژی‌های متفاوت را با داده تاریخی و جدید ارزیابی کند، فرصت‌ها را رتبه‌بندی کند و محدوده احتمالی ورود/خروج، حد ابطال، هدف، ریسک، زمان و شواهد را گزارش دهد. صرف داشبورد/چارت/اندیکاتور یا الزام کاربر به تحلیل دستی ۱۰۰ بازار **مردود** است.

تنظیمات کاربر: بازارها، watchlist و کشف آزاد، تایم‌فریم‌های 15m/1H/4H/1D، افق نگهداری مستقل (مثلاً چهار روز)، اهداف سود، سقف ریسک/افت، دفعات تحلیل، کیفیت هشدار و آستانه رتبه‌بندی. پیش‌بینی قطعیت نیست؛ «ارزان» بودن توکن به معنای قیمت واحد پایین نیست؛ ارزش بازار/FDV/عرضه/درآمد/کاربرد/رقبا و ریسک unlock باید بررسی شوند.

## 2. محیط، هزینه و ایمنی
Windows 11؛ AMD Ryzen 5 3500U؛ RAM کل ۸GB؛ بودجه هدف برای سامانه ۳–۴GB (اندازه‌گیری‌نشده). حجم دیسک اولویت محدودکننده نیست. مدل ابری رایگان/اعتبار رایگانِ تأییدشده در صورت نیاز؛ مدل محلی سنگین پیش‌فرض نیست. Free-first و UNKNOWN cost = DENY. هیچ API دارای overage/پرداخت، نصب، اتصال حساب حساس، کلید صرافی، سفارش واقعی یا انتشار عمومی بدون بررسی و مجوز مستقل. فازهای نخست read-only، backtest و dry-run/paper؛ سرمایه‌گذاری واقعی هدف نهایی کاربر است اما اجرای واقعی به تصمیم و مجوز جداگانه، کنترل امنیتی و آزمون نیاز دارد. هیچ بازده یا نقطه ورود «امن» تضمین نمی‌شود.

## 3. یافته‌های Work (گزارش ارائه‌شده توسط کاربر، 2026-11-06)
پژوهش Work مسیر مشروط **Freqtrade + FreqUI + لایه پژوهش سبک + SQLite + AI ابری اختیاری** را برای حلقه زنده پیشنهاد داده است؛ این **انتخاب قطعی نیست**، چون هسته Freqtrade به‌تنهایی تحلیلگر بنیادی/خبری خودکار و شکارچی فرصت نیست.
- Freqtrade: داده کریپتو، فهرست پویا، اندیکاتور، بک‌تست، dry-run و پایش؛ FreqUI نمایش وضعیت. امکان RemotePairList و کانال WebSocket analyzed_df به‌عنوان گزینه اتصال، نیازمند آزمون نسخه و محیط.
- لایه پژوهش پیشنهادی، محصول آماده مستقل نیست؛ باید فقط برای شکاف اثبات‌شده نوشته شود: هویت دارایی، کیفیت و تازگی داده، خبر، بنیادی، تحلیل ترکیبی، رتبه‌بندی، هشدار و حافظه.
- SQLite برای state پژوهش/هشدار؛ هسته مالک داده معاملاتی آزمایشی خودش؛ لایه پژوهش مالک شواهد و تحلیل. مدل زبانی فقط از شواهد موجود تحلیل/توضیح دهد؛ محاسبات عددی و ریسک deterministic و قابل آزمون باشند.
- مسیرهای رقیب: Superalgos (یکپارچه بصری، اما هوشمندی بنیادی آماده تأیید نشده)، Fincept Terminal (ترمینال چندبازاری؛ پوشش واقعی خودکار باید بررسی شود)، Gunbot Quant (شرایط مجوز/قیمت باید بررسی شود)، OctoBot، و مسیر سفارشی CCXT + Backtesting.py + SQLite.
- محدودیت‌های گزارش Work: RAM واقعی UNKNOWN؛ Binance از محیط پژوهش HTTP 451، Kraken timeout، Coinbase historical پاسخ داده ولی سازگاری Freqtrade نامعلوم؛ اینها آزمون لپ‌تاپ نیستند. CoinGecko Public و Demo سهمیه متفاوت دارند؛ DefiLlama/Coin Metrics Community محدودیت داده؛ RSS خبر تأخیر دارد؛ Alpaca Basic پوشش محدود IEX و Massive Basic داده EOD؛ پوشش زنده رایگان همه بازارها اثبات نشده.
- آزمون‌های backtest باید کارمزد، لغزش، spread، gap و داده تاریخی point-in-time را لحاظ کنند؛ خبر/بنیادی امروز را نمی‌توان به گذشته تزریق کرد. برای خبر و بنیادی از امروز first_seen ذخیره شود؛ داده‌های vintage مثل ALFRED برای آزمون تاریخی مهم‌اند.
- پیشنهاد Work: شروع با BTC ETH SOL AVAX NEAR SUI APT LINK AAVE UNI مشروط به پشتیبانی منبع، سپس ۱۰→۲۵→۶۰→۱۰۰.
- اهداف آزمایشی پیشنهادی (نه نتایج واقعی): p95 RAM حدود ۳.۵GB، peak ≤۴GB، پوشش کندل ≥۹۹٪ در بازه معتبر، تأخیر پردازش داخلی p95 ≤۲ ثانیه، بازیابی هدف ≤۵ دقیقه پس از backfill، منشأ قابل ردیابی برای همه خروجی‌ها، صفر سفارش واقعی.
- گزارش Work مدعی مقایسه ۳ مسیر، ۱۶ مسیر داده، ۱۲ نقش و ۵۳ منبع است؛ فایل‌های کامل گزارش/بسته شواهد در این گفتگو ارائه نشده‌اند. این خلاصه بر متن چسبانده‌شده کاربر تکیه دارد؛ **بازبینی مستقل همه ۵۳ منبع و کد انجام نشده**.

## 4. کاوش GitHub: نامزدها، نه ابزارهای تأییدشده
برای **تحلیل خودکار و پژوهش**: [TradingAgents](https://github.com/TauricResearch/TradingAgents)، [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot)، [Qlib](https://github.com/microsoft/qlib)، [FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading)، [Freqtrade/FreqAI](https://github.com/freqtrade/freqtrade).
سرنخ‌های تکمیلیِ نیازمند بررسی دقیق مخزن/مجوز/تست/نگهداری: [ProofAlpha](https://github.com/search?q=ProofAlpha&type=repositories)، [Alpha Research Engine](https://github.com/search?q=Alpha+Research+Engine&type=repositories)، [OpenQnt](https://github.com/sinatooor/openqnt) (مجوز open-source بودن **تأیید نشده**)، [Axiom](https://github.com/srossitto79/axiom)، [Trading Research Agents](https://github.com/BijectiveLabs/trading-research-agents)، [AutoResearch Strategy](https://github.com/nhocconan/AutoResearch-based-Trading-Strategy-Generation-and-Testing)، [AutoPilotPM](https://github.com/recogardtech/AutoPilotPM). فهرست‌های کشف: [awesome-agentic-trading](https://github.com/orangejustin/awesome-agentic-trading) و [awesome-finance-agents](https://github.com/aowang-ai/awesome-finance-agents). وجود README یا ادعای agent، اثبات عملکرد، سازگاری ویندوز، مجوز یا سودآوری نیست.
**تصمیم باز:** انتخاب یک موتور تحلیلی اصلی + حداکثر یک جایگزین بر اساس آزمون واقعی؛ هیچ موتور هوشمندی هنوز تأیید یا نصب نشده است.

## 5. معماری هدف حداقلی، مشروط به اثبات
منابع عمومی داده بازار/خبر/بنیادی → دریافت افزایشی و بررسی کیفیت/هویت → موتور بازار زنده (نامزد Freqtrade) + موتور تحلیل هوشمند (TBD، ابتدا single agent/direct model یا مدل کمی) → رتبه‌بندی مستند، محاسبه قطعی ریسک و ورود/خروج → SQLite و هشدار/داشبورد. تاریخچه حجیم روی دیسک؛ پنجره‌های محدود در RAM؛ orderbook فقط برای نامزدهای نهایی؛ AI فقط برای تغییرهای معنادار؛ عدم نیاز پیش‌فرض به Redis/Postgres، microservices، GPU یا چند Agent. هر بخش قرارداد I/O و مالک state روشن داشته باشد. پس از قطعی، backfill و fresh-check قبل از هشدار؛ هشدار تکراری و stale ممنوع.

## 6. نقشه راه اجرایی با دروازه پذیرش
| Stage | کار | خروجی قابل اثبات | Gate |
|---|---|---|---|
| S0 | بررسی عمیق GitHub و شواهد Work؛ مقایسه موتورهای هوشمند، مجوز، داده، هزینه، امنیت، Windows و failure modes | ماتریس انتخاب با یک موتور اصلی/جایگزین، طرح کوچک‌ترین vertical | بدون نصب و بدون ادعای عملکرد |
| S1 | baseline سیستم، آزمون دسترسی منابع و انتخاب روش نصب Windows (native/WSL2/Docker)؛ نصب فقط با مجوز بعدی | log RAM/CPU، اتصال واقعی، یک بک‌تست تکرارپذیر، FreqUI در صورت انتخاب | بدون کلید معامله؛ سقف RAM بررسی شود |
| S2 | یک حلقه واقعی ۱۰ دارایی با state و تحلیلگر هوشمند منتخب | گزارش خودکار فنی+بنیادی+خبر با source/time و رتبه‌بندی | بدون تحلیل دستی هر دارایی؛ بدون اعداد ساختگی |
| S3 | مدل‌های پایه و پیش‌بینی، مقایسه چند روش و Walk-forward | نتایج OOS، baseline، هزینه/لغزش/افت، رد مدل نامعتبر | عدم انتخاب صرفاً براساس سود تاریخی |
| S4 | کشف فرصت فراتر از watchlist، ناحیه ورود/خروج و ابطال، هشدار مستند | فرصت رتبه‌بندی‌شده و paper alerts؛ backfill/restart/dedup | stale/هویت مبهم → no signal |
| S5 | پایش چند هفته‌ای و افزایش ۱۰→۲۵→۶۰→۱۰۰ | نرخ خطا/false alert، کیفیت فرصت، RAM و latency برای هر مرحله | گسترش فقط پس از پاس |
| S6 | ارزیابی امکان استفاده برای سرمایه‌گذاری واقعی | پیشنهاد کنترل ریسک/حقوق دسترسی و human approval | معامله واقعی فقط با تصمیم و مجوز مستقل |

**گام بعدی مشخص:** S0 — بازبینی مستقل ۴–۶ موتور تحلیلگر/پیش‌بینی GitHub، صحت مجوز، وجود کد و تست، نگهداری، پوشش اخبار/بنیادی/کریپتو، و انتخاب کوچک‌ترین ترکیب واقعاً خودکار. قبل از نصب باید مشخص شود آیا Freqtrade + یک موتور هوشمند کافی است یا گزینه all-in-one واقعی بهتری وجود دارد.

## 7. قرارداد گزارش فرصت و آزمون
هر پیشنهاد باید asset ID و chain/exchange، زمان داده و زمان دریافت، منابع قابل بازتولید، تایم‌فریم و افق، شرایط ورود، بازه قیمت پیشنهادی (در صورت کفایت داده)، stop/invalidation، target، risk/reward پس از هزینه، دلایل فنی/بنیادی/خبر، ریسک نقدینگی و unlock، مدل/نسخه/روش آزمون، confidence فقط اگر کالیبره، و status «WATCH / CANDIDATE / INVALIDATED / EXPIRED» داشته باشد. در نبود داده کافی، نتیجه «NO SIGNAL»؛ نه توصیه ساختگی. ارزیابی: walk-forward، point-in-time، OOS، regime، leakage، benchmark، paper forward results، latency، alert precision، drawdown، failure/recovery و هزینه.

## 8. مراجع و منشأ
- گزارش Work کاربر در چت 2026-11-06، خلاصه «مسیر پیشنهادی Freqtrade + لایه پژوهش سبک»، با اشاره به گزارش اصلی ۵۳ منبع؛ پیوست کامل هنوز در این جلسه در دسترس نیست.
- پژوهش/گفتگوهای DJMRN درباره Superalgos، Fincept، OctoBot، Freqtrade، TradingAgents، FinRobot، Qlib، FreqAI و سایر مخازن؛ وضعیتشان CANDIDATE/UNVERIFIED مگر خلافش با کد/آزمون ثابت شود.
- مستندات رسمی: https://www.freqtrade.io/en/stable/ ، https://github.com/freqtrade/freqtrade ، https://github.com/microsoft/qlib ، https://github.com/TauricResearch/TradingAgents ، https://defillama.com/ ، https://docs.coingecko.com/ .
- Authority: GitHub source/code/tests؛ همین فایل فقط مشخصات موضوعی؛ **CURRENT-STATUS.md تنها مرجع جاری پیشرفت و اقدام بعدی**. هیچ ثبت روزانه موازی یا تغییر Notion خودکار.
