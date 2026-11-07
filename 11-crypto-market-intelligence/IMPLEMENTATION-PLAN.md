# DJMRN Crypto Intelligence — Practical Implementation Plan
Date: 2026-11-06 | Mission: DJMRN-CRYPTO-MARKET-001
Status: APPROVED PLAN, NOT INSTALLED. Progress authority: ../07-operations-and-continuity/CURRENT-STATUS.md

## Product objective
Build an autonomous, headless, multi-source research and opportunity discovery system for cryptocurrencies. Detect potentially undervalued projects with actual adoption and growth, evaluate project credibility, and generate evidence-based risk-aware entry/exit scenarios or NO ENTRY. Low unit token price does not mean cheap valuation. No guaranteed return and no live orders.

## Data dimensions
1. Exchange markets: OHLCV, volume, volatility, order-book liquidity, spread, slippage, listing changes.
2. Historical context: point-in-time price and fundamental data, past event reactions, market regimes, strategy tests, survivorship and leakage safeguards.
3. Fundamental: utility, active users, fees/revenue, TVL quality, token value capture, market cap, FDV, emissions, unlocks, governance and treasury.
4. Competitors: sector peers, relative growth, substitution, competitive advantage, comparable valuation.
5. On-chain: activity, holders, concentration, flows, contract risks and data limitations.
6. News/events: primary-source announcements, hacks, regulation, token unlocks, sentiment with source and publication time.
7. Parallel markets: BTC/ETH, equities/ETFs, rates, USD, bonds, gold, silver, oil and liquidity; distinguish correlation from causation.
8. Project credibility: issuer/team, chain/contract, audit and exploit history, liquidity, manipulability, custody and redemption.
9. Tokenized equities/RWA: rights versus synthetic price exposure, issuer, oracle, custody, redemption and legal constraints.
10. Quant and AI: baseline models, regime analysis, ML, walk-forward and out-of-sample evaluation; tool-using AI may request read-only analysis of shortlisted opportunities, not replace deterministic risk checks.

## Candidate module inventory (evaluate, do not bulk-install)
- Freqtrade/FreqAI: first trial for public exchange data, historical testing and optional ML.
- CCXT + Python + SQLite: simpler alternative if Freqtrade unsuitable.
- onchain-research-desk and DefiLlama: fundamental, valuation and competitor research candidates.
- SignalDesk: independent opportunity-scanning and reporting candidate; maturity, licensing and costs unverified.
- TradingAgents and FinRobot: AI research patterns/candidates, only if simpler evidence synthesis is insufficient.
- Qlib / Backtesting.py: optional quantitative evaluation.
- Fincept Terminal / Superalgos: comprehensive alternatives, not required installations.
- TradingView: optional external alert source; check plan, webhook availability, safe delivery and costs. Not the canonical source of data.
- Codex or approved cloud model: optional read-only tool caller on difficult events, not a permanently running agent per asset.

## Integration design
Begin as a modular Python application with SQLite, raw-source evidence, timestamps, explicit asset identity and reproducible reports. Prefer documented CLI/API/file export of third-party tools. One data owner per field; tool outputs are evidence, not automatically truth. Avoid microservices, heavy dashboards and multiple agents unless measurements demonstrate necessity. VPN remains user-controlled; validate connectivity while running, not via a separate hardware preflight.

## Sequential delivery and acceptance
P0: Verify official Freqtrade installation instructions, license, Windows dependencies, public-data workflow and reversible install path. Ask explicit approval for installation. No hardware benchmark gate.
P1: Install first candidate in isolated environment; retrieve historical and recent public data for 3–10 pairs, persist source/time/market data, handle errors and verify repeatable output. No trading API keys or orders. If unsuitable, trial CCXT.
P2: Produce a real fundamental and competitor report for one protocol and two peers. Require dated evidence for revenue, tokenomics, market cap/FDV, liquidity and credibility; mark missing data UNKNOWN.
P3: Run a simple baseline and one quantitative method with time-ordered evaluation, fees, slippage and realistic risk. Generate conditional entry zone, targets, invalidation, horizon and abstention.
P4: Integrate official news, macro and parallel-market evidence, then trial one AI tool-using analyst on shortlisted cases. Measure whether AI adds useful evidence versus deterministic baseline; verify no fabricated sources.
P5: Run background incremental scans with SQLite state, alerts, retry, dedup, logging, VPN/network recovery and paper outcome tracking.
P6: Add autonomous new-token discovery, safety screening and gradual coverage from 10 to 25 to 60 to 100 assets based on measured quality and resources. Add tokenized assets only where evidence and legal context are sufficient.
P7: Separate proposal and explicit approval before any real-money or exchange-account actions.

## First concrete user action
Start P0 with Freqtrade official install documentation; prepare one Windows PowerShell isolated-install command and one public market data command. After approval, user runs it and returns actual output. Do not require hardware benchmarking before installation. If blocked, choose CCXT fallback. After first real data flow, proceed to P2 fundamental work.

## Opportunity report contract
Asset identity, market, observation timestamp, source and publication timestamp, freshness, project legitimacy, fundamentals, peers, technical signals, news, macro, model version, validation evidence, upside/downside scenarios, entry zone, targets, invalidation, liquidity, costs, risk/reward, counterarguments, uncertainty, decision (WATCH/CANDIDATE/NO_ENTRY/INSUFFICIENT_DATA), and observed outcome.

## Controls
Free-first; unknown API costs DENY; verify official licensing and quotas. No secrets, paid activation, trading orders, production deployment or sensitive changes without approval. Every stage is DONE only with real input/output, tests, failure handling, reproducible state and useful result.

---

## DJMRN Entry/Exit — Five mandatory evidence dimensions (user roadmap, 2026-11-08)

**Record type:** USER-DEFINED ROADMAP / REQUIREMENTS — **not implemented, backtested as a complete system, validated, deployed, or authorized for real trading**. This is a component of the existing DJMRN crypto market intelligence roadmap, **not a second operational status authority**. Canonical project progress remains [CURRENT-STATUS.md](../07-operations-and-continuity/CURRENT-STATUS.md).

**هدف:** سامانهٔ نهایی برای هر موقعیت بالقوهٔ خرید، فروش/خروج یا «عدم معامله»، **هر پنج محور زیر** را بررسی کند و شواهد مثبت، منفی، نامعلوم و تناقض‌ها را کنار هم بگذارد. اندیکاتور به‌تنهایی مجوز معامله نیست. وجود چند سیگنال حمایتی هم الزاماً به معنای ورود نیست؛ موانع سخت ریسک می‌توانند تصمیم را رد کنند. **خروج اضطراری/کنترل ضرر هرگز به‌خاطر ناکامل‌بودن امتیازهای تأییدی به تعویق نیفتد.**

### پنج محور ضروری (تعریف نیازمندی، نه ادعای قابلیت عملیاتی)

| شناسه | محور لازم | ورودی‌ها و زیرقابلیت‌هایی که باید تکمیل شوند | خروجی مورد انتظار برای ورود و خروج | وضعیت |
|---|---|---|---|---|
| **D1** | **Price Action / پرایس اکشن** | حمایت/مقاومت و واکنش قیمت به سطح؛ شکست معتبر/جعلی و برگشت به سطح (retest)؛ پولبک؛ کندل‌ها و الگوهای برگشتی/ادامه‌دهنده؛ زمان‌بندی شکست و ابطال | محدوده‌های ورود/خروج، نقطه ابطال، دلیل و زمان سیگنال، شاهد کندلی/قیمتی | **REQUIRED / INCOMPLETE** |
| **D2** | **اندیکاتورها و مدل‌های تکنیکال** | HMA, SMA, EMA, WMA, VWMA, DEMA, TEMA, RSI, MACD, ATR, Volume و سایر اندیکاتورهای موجود؛ تنظیم دوره‌ها؛ چندتایم‌فریم؛ مدل تکی و ترکیبی؛ قواعد ورود و خروج مستقل | تأیید/رد روند و مومنتوم، زمان و قیمت سیگنال، تنظیمات نسخه‌دار، خطاهای کاذب و ناسازگاری‌ها | **REQUIRED / PARTIAL-RESEARCH** |
| **D3** | **تحلیل ساختاری، الگویی و تصویری** | HH/HL/LH/LL؛ BOS/CHoCH؛ ساختار روند در تایم‌فریم بالاتر؛ نواحی عرضه/تقاضا و نقدینگی/شکار استاپ؛ الگوهای هندسی و تصویری از جمله دو سقف/دو کف، سر و شانه، مثلث، پرچم، کنج؛ تحلیل تصویری AI فقط در صورت ارزش افزودهٔ اثبات‌شده | ساختار و فاز بازار، نقاط چرخش و ناحیه‌های حساس، سطح اطمینان *کالیبره‌شده در صورت وجود*، دلیل رد یا تأیید ساختار | **REQUIRED / INCOMPLETE** |
| **D4** | **اخبار و فاندامنتال** | اخبار رسمی و زمان انتشار، رویدادهای اقتصاد کلان، نرخ‌ها/نقدینگی و بازارهای مرتبط، عوامل بنیادی/درون‌زنجیره‌ای و رویدادهای اختصاصی ارز، کیفیت منبع و تازگی خبر | جهت/شدت/ابهام اثر رویداد، هشدار ریسک خبری، تأیید یا حق وتوی ورود؛ شواهد زمان‌مند برای خروج و تغییر شرایط | **REQUIRED / NOT INTEGRATED** |
| **D5** | **موقعیت قیمت در دامنهٔ یک‌ساله و ریسک بازار** | سقف و کف **غلتان ۳۶۵روزه/۱۲ماهه** با مرجع صرافی و واحد مشخص؛ نسبت جایگاه قیمت در بازه، فاصله تا سقف و کف، دامنه نوسان سالانه، نوسان جاری، فاز بازار، افت احتمالی، حد ضرر، نسبت سود به زیان و افق نگهداری | امتیاز ریسک مستقل برای ورود و خروج؛ تشخیص خرید نزدیک مقاومت/سقف، فروش نزدیک حمایت/کف؛ محدودیت اندازه موقعیت، ابطال یا NO-TRADE | **REQUIRED / PROPOSAL** |

**مرزبندی بدون دوباره‌شماری:** D1 قواعد قیمتی و رویدادهای قابل اجرای کندلی/سطحی را تعریف می‌کند؛ D3 ساختار زمینه‌ای چندمقیاسی و تشخیص الگوهای پیچیده یا تصویری را ارزیابی می‌کند. یک شکست قیمت یا یک الگوی واحد نباید صرفاً چون در هر دو دسته دیده می‌شود **دو رأی مستقل** بگیرد. D5 جدا از تأیید تکنیکال است و می‌تواند ورود را از نظر ریسک رد کند.

### اتصال به امتیازدهی قبلی و تصمیم نهایی

- **رکورد موجود:** [فرضیهٔ اولیهٔ سه‌محوری BTC و امتیاز ۴۰/۲۰/۴۰](../07-operations-and-continuity/CURRENT-STATUS.md) — **۴۰ امتیاز** دامنه/رفتار تاریخی بازار (حالا **D5**)، **۲۰ امتیاز** اخبار/فاندامنتال (**D4**)، **۴۰ امتیاز** سیگنال‌های تکنیکال که اکنون بین **D1 + D2 + D3** باید بر اساس آزمون تقسیم شود. این تقسیم در حال حاضر **تعیین نشده**؛ امتیاز مستقل پنج محور نباید به‌طور ناخواسته مجموع را بیش از ۱۰۰ کند.
- **آستانهٔ مثالی:** «حداقل **۷۰ از ۱۰۰**» فقط یک **مثالِ قابل تنظیم و نیازمند اعتبارسنجی** است؛ **۷۰ امتیاز = ۷۰٪ احتمال موفقیت یا سود تضمینی نیست**. وزن‌ها، آستانه‌ها و سخت‌گیری هر محور تا زمان آزمون و تصویب نهایی **پیشنهادی** هستند. منظور «تکمیل پنج محور» قابلیت ارزیابی هر پنج حوزه است، نه این‌که همه سیگنال‌ها همیشه هم‌جهت باشند.
- **قرارداد ورودی:** شناسه دارایی و صرافی/بازار، داده OHLCV معتبر، زمان UTC و زمان دسترسی هر شاهد، تایم‌فریم‌ها، افق معامله، قوانین هر محور، وضعیت تازه/نامعلوم/متناقض، هزینه، اندازه/ریسک مجاز.
- **قرارداد خروج هر محور:** `BUY_SUPPORT / SELL_SUPPORT / NEUTRAL / VETO / UNKNOWN`، شواهد/منشأ و زمان، نسخهٔ قاعده/مدل، نواحی قیمت و نقطهٔ ابطال در صورت وجود؛ خروجی AI به‌تنهایی **دلیل قطعی یا احتمال کالیبره‌شده** نیست.
- **تصمیم یکپارچه:** موتور قطعی و قابل بازپخش با هویت سیگنال، وابستگی‌ها و وزن‌های معلوم، نظرها را بدون دوباره‌شماری ترکیب می‌کند. برای **ورود**: پوشش هر پنج محور، کف کیفیت داده، بررسی veto و سپس امتیاز لازم. `UNKNOWN` حیاتی، عدم توافق مهم، نقدینگی/نرخ خطای غیرمجاز یا ریسک بیش از حد → `WAIT / NO-TRADE`. برای **خروج**: قوانین حفاظت سرمایه/حد ضرر اولویت دارند؛ خروج بر اساس تضعیف ساختار، تغییر رژیم، سطح هدف یا تشدید ریسک می‌تواند مستقل از رأی ورود فعال شود. تصمیم‌ها `ENTER / EXIT / HOLD / WATCH / NO-TRADE` فقط در حالت پژوهشی/شبیه‌سازی تا تصویب مجزای اجرای واقعی ارائه شوند.
- **درصد سالانه:** نسبت سقف/کف تاریخیِ یک سال می‌تواند برای تحلیل موقعیت و ظرفیت نوسان استفاده شود، اما **«۷۰٪ دامنهٔ تاریخی» یک مقدار ثابت جهانی، احتمال سود یا حد سود تضمینی نیست**. بازه هر لحظه به‌روز شود؛ بازهٔ یک‌ساله فقط از داده‌هایی محاسبه شود که در زمان صدور سیگنال واقعاً در دسترس بوده‌اند.

### ترتیب تکمیل و معیار پذیرش

- [ ] **F1 — قرارداد مشترک:** تعریف دقیق «ورود صحیح»، «خروج صحیح»، سیگنال کاذب، تأخیر تشخیص نقطهٔ چرخش، drawdown، افق زمانی و سنجه‌ها؛ ثبت نمونه‌های قابل بازبینی. دامنهٔ شش اندیکاتور پایه و قیمت BTC را قبل از توسعهٔ فراگیر ثابت و آزمایش کنیم.
- [ ] **F2 — بازیابی قابلیت موجود:** ممیزی اندیکاتور/الگوی از پیش موجود در OpenTerminalUI، APIها، داده و تنظیمات؛ **Reuse/Extend** به جای نصب سرویس یا عامل مجزا. تمایز قابلیت نمایشی از مسیر واقعی تولید سیگنال و معامله روشن شود.
- [ ] **F3 — پیاده‌سازی محدود هر محور:** یک ورودی واقعی BTC با محاسبهٔ مستقل، نتایج قابل توضیح و قابل بازپخش؛ برای AI تصویری ابتدا گزینهٔ بدون مدل و سپس مدل مستقیم/یک ایجنت دارای ابزار بررسی شود، نه شبکهٔ چندایجنت پیش‌فرض.
- [ ] **F4 — اعتبارسنجی زمانی:** سال آموزش و آزمون جدا، walk-forward/دادهٔ مستقل، عدم استفاده از کندل‌های آینده (خصوصاً تأیید pivot)، رویداد خبری با timestamp انتشار و منع leakage، هزینه/اسپرد/لغزش، مقایسهٔ baseline و ارزیابی جداگانهٔ ورود **و** خروج. آستانه و وزن‌ها براساس شواهد تنظیم و روی دادهٔ دیده‌نشده آزموده شوند.
- [ ] **F5 — ترکیب و کنترل ریسک:** آزمون تک‌محوری در برابر همهٔ پنج محور و حذفِ تک‌تک آنها (ablation)، پوشش داده، هم‌بستگی رأی‌ها، veto و عدم معامله؛ خروج اضطراری نیازمند کسب حداقل امتیاز ورود نباشد.
- [ ] **F6 — عملیاتی‌شدن تدریجی:** وضعیت پایدار، گزارش، خطا و recovery، پایش حافظه/هزینه در لپ‌تاپ ۸GB، ذخیره قابل بازیابی تنظیمات، alert و paper-trading؛ اتصال سفارش واقعی، provider پولی، کلید صرافی یا فعال‌سازی ایجنت حساس **فقط با پیشنهاد اثر و مجوز مستقل**.

**معیار DONE برای این زیرنقشه:** هر پنج حوزه برای یک دارایی واقعی داده تازه و مستند دریافت کرده، شواهد و رد/پذیرش تولید کنند؛ امتیاز/قواعد ورود و خروج قابل‌بازتولید باشند؛ کیفیت خارج از نمونه و خطرات اندازه‌گیری شوند؛ حالت NO-TRADE و مسیر خروج محافظتی آزمون شود؛ مسیر ذخیره/بازیابی و نظارت کار کند. **فعلاً فقط تعریف نیازمندی و نقشه‌راه ثبت شده است؛ هیچ آزمون جدید، اجرا، نصب، مدل تصویری یا سفارش معاملاتی انجام نشده است.**
