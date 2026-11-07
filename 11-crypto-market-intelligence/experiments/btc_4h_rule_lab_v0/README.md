# DJMRN BTC/USD 4H — Rule Strategy Laboratory v0

**Status:** Experimental / unmerged branch / read-only research. No live exchange connection, no trade placement, no new plugins, no background jobs, no paid compute.

## What is working

- Input: previously saved Bitstamp BTC/USD two-year, four-hour, gap-free OHLCV CSV (4,380 completed bars). SHA256 is verified **before** any evaluation.
- Six technical rule families: SMA trend, EMA trend, MACD, RSI mean reversion, Bollinger mean reversion, and high/low breakout.
- Twelve predeclared parameter variants in `config.json` (two per family); parameters can be edited and rerun without editing Python.
- Non-ML pilot: the term **model** means a deterministic technical decision rule and parameters, not a trained LLM or neural network.
- Chronological train 2,190 candles (first 12 months) and untouched holdout 2,190 candles (last 12 months). First 100 training candles excluded as warm-up for comparison.
- Parameter selection only uses training data, score = train net return minus 0.5 × maximum drawdown; a model needs ≥4 completed trades for eligibility. Locked holdout used once to report initial results, not for selecting parameters.
- Signal at the **close of bar t**, orders simulated at the **OPEN of bar t+1**. Long/flat; no leverage or shorts.
- Exploratory cost assumption: 10 bps exchange fee + 5 bps slippage **per side**. This is not a verified Bitstamp fee schedule.
- Reports include trade win rate, trade count, net return, maximum drawdown, exposure, and after-cost buy-and-hold comparison.
- `selftest.py` checks data continuity, rule causality/no future leakage, nonnegative effect of transaction costs, and 12-month split.

## Actual pilot execution on DJMRN laptop (2026-11-07)

| Strategy | Holdout net return | Trade win rate | Trades | Max drawdown |
|---|---:|---:|---:|---:|
| Bollinger | -3.532% | 75.00% | 36 | 32.108% |
| Breakout | -6.423% | 33.33% | 12 | 19.501% |
| EMA | -43.294% | 21.65% | 97 | 44.089% |
| MACD | -39.454% | 22.06% | 68 | 39.770% |
| RSI | -16.519% | 75.00% | 16 | 29.233% |
| SMA | -21.310% | 22.73% | 44 | 28.888% |

Buy-and-hold comparator (same holdout and cost convention): **-24.602%**. Even a 75% trade win rate does **not** imply a profitable strategy. None of these six strategies achieved a positive net holdout return. Do not treat these ranks as proven or optimized trading signals.

First-run output: [`first_run_results.json`](first_run_results.json) (actual laptop execution). Quality checks: `SELFTEST=PASS; CHECKS=36`.

## Run locally from repository root (Python >= 3.10; standard library only)

PowerShell (one command):

```powershell
python 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/run.py --csv 11-crypto-market-intelligence/data/BTC-USD_4h_Bitstamp_2y_2026-11-07_complete_4h.csv --config 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/config.json --output btc_4h_rule_lab_results.json
```

Self-test:

```powershell
python 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/selftest.py --csv 11-crypto-market-intelligence/data/BTC-USD_4h_Bitstamp_2y_2026-11-07_complete_4h.csv --config 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/config.json
```

Everything is reproducible and can also run headless from an existing Python interpreter. On the laptop, the test ran against the existing local CSV and OpenTerminalUI's isolated Python runtime; OpenTerminalUI source and settings were not modified.

## Important limits and next tests

- The six rules are deliberately simple. Do not infer predictive precision or calibrated probabilities of 70% from trade-win percentages.
- No news, contemporaneous fundamental data, economic releases, annual-range 40/20/40 weighting, multi-timeframe agreement, dynamic target/stop, or risk gates are included yet.
- A holdout result may be exploratory evidence only; further repeated iterations require a *new* untouched forward window or walk-forward evaluation to avoid selecting on the test set.
- The market price of the eventual execution venue, trading costs, spreads, liquidity and market regime may differ from Bitstamp historical values.
- Next minimal test: improve risk exits and independent validation without retuning on the already inspected holdout; then test second timeframe and historical event data with point-in-time timestamp proof.

## Tools and cost

- **Existing connected GitHub plugin:** needed for branch, code versioning and read-back. No additional plugin is required.
- **Existing Remote Desktop Commander:** runs local tests on the authorized laptop, no new runtime installed.
- **GitHub Actions NOT enabled or triggered.** A private-repository runner consumes a plan allowance and can incur extra charges after allowances. The user's account quota, overage prevention, repo workflow policy and manual-run approval are not verified; no cloud execution is authorized at this stage.
- Do not publish, merge, schedule, enable workflows, connect brokerage accounts or execute trades without separate authorization.

**Authority:** project code and experimental result files in this isolated GitHub branch; only the main GitHub CURRENT-STATUS.md is the durable operational status ledger if the user later requests recording a milestone.

---

## V1 — HMA-centered multi-indicator and multi-timeframe study

**Status: experimental branch only.** The original v0 SMA/EMA/RSI etc baseline remains intact for comparison. V1 was executed on the actual DJMRN laptop using the same SHA-checked 4,380 Bitstamp BTC/USD completed 4H candles; no live trades, no installed packages, no GitHub Actions, no LLM and no OpenTerminalUI source modifications.

### Working artifacts

- [hma_multiconfirm_v1.py](hma_multiconfirm_v1.py): 12 technical *families*, 46 initial parameter variants, including four HMA-specific entry types and independent RSI, MACD, Donchian, Bollinger, volume+HMA, Supertrend and Keltner conditions.
- [hma_multiconfirm_v1_results.json](hma_multiconfirm_v1_results.json): actual deterministic output from completed first run.
- [audit_hma_v1.py](audit_hma_v1.py) and [audit_hma_v1_results.json](audit_hma_v1_results.json): train-only exit-period selection, votes=2/3/4 sensitivity, and HMA slope-turn periodicity on 4H/12H/1D derived from fully completed 4H bars.
- [test_hma_v1.py](test_hma_v1.py): causality/prefix regression suite; **210/210 checks PASS**. The original v0 36-check self-test also passed.
- Source HMA formula: [Alan Hull, original author](https://alanhull.com/the-hull-moving-average/); mathematical WMA double-half minus full, smoothed by sqrt period using integer truncation. HMA is responsive, **not guaranteed profitable**.

### Chronological setup and interpretation

- 2024-11-07 to 2025-11-07: select each rule's parameters using **training-only** 5% upside-before-5% stop within 30 days, with at least 16 eligible samples; **not** select using the last-year 20%/50% target outcomes.
- 2025-11-07 to 2026-11-07: fixed holdout year. Forward targets are 20% within 180 completed 4H bars (~30 days) before a hypothetical 10% stop, and 50% within 360 or 540 completed 4H bars (~60 or 90 days) before a 10% stop. At most one event per family per 24h; any event too close to the end is censored from that target's denominator. Simultaneous high/low target and stop in a candle counts as stop (conservative).
- For independent trade simulation: entry at the next 4H open, 20% target, 10% hard stop, 8% trailing stop using **previous completed candles' highs**, HMA downslope exit executed at next bar open, maximum 30-day holding time, with 10 bps fees + 5 bps slippage per side (experimental assumptions).
- 12H and daily HMA regimes are calculated only from **completed 12H/daily UTC candles** and projected forward; no unclosed higher-timeframe bars. No 1H study, no fundamental/news inputs, no 40/20/40 score, no calibrated probabilities, no auto-trading.

### Selected HMA parameter results (selected by first-year research criterion only)

| HMA slope-turn timeframe | Training-selected HMA period | Event count on holdout | Held-out 20% in 30d, before 10% stop |
|---|---:|---:|---:|
| 4H | 34 bars (=136 hours) | 72 | 9.52% of 63 eligible |
| 12H | 34 bars (=408 hours) | 27 | 8.00% of 25 eligible |
| 1D | 16 bars (=16 days) | 24 | 9.09% of 22 eligible |

The model count is **not** trade count; multiple events can overlap a single open trade. Short-period 4H HMA-9 produced 195 held-out events (much noisier/faster), while 4H HMA-34 produced 72 and HMA-89 produced 43. Annual signal cadence is tunable but frequency alone proves nothing.

### What happens when model votes overlap?

The five independent families were **frozen using training quality only**: RSI oversold rebound, Keltner breakout, HMA pullback, HMA price cross, HMA dual. A confluence event requires N different families firing within the last <=12 hours, rising **completed** 12H HMA16 and daily HMA20 trend confirmations, and minimum 1-day re-arm.

| Required distinct votes | Train-year events | Held-out-year events | Training-selected exit HMA period | Test trades | Test net return | Test trade win rate | Test 20%-30d target hits |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2/5 | 41 | 36 | 55 | 22 | -6.90% | 27.27% | 4/36 |
| 3/5 | 26 | 23 | 55 | 14 | -5.18% | 21.43% | 2/23 |
| 4/5 | 7 | 7 | 16 | 7 | +13.30% | 71.43% | 0/7 |

Exit-HMA variants 16, 21, 34, 55, 89 were compared **only on the train period** before their holdout returns were computed. Critical: the 4/5 case has **just seven trades**; its positive net total has no statistically convincing success evidence, and neither its 20%-30d objective nor 50%-90d objective was hit. Do not use as a live policy. The “2/5” path is not categorically inferior in all conditions; the held-out sample itself is one market regime.

**Baseline feasibility:** unconditional start once daily across the test year yielded ~9.25% 20%-within-30d before 10% stop (335 eligible starts), and **0%** 50%-within-90d before 10% stop (275 eligible). These are overlapping horizons, **not independent probability trials**, and venue, fee, timing and stop conventions matter. Selection/test leakage can occur if results here are repeatedly retuned against the same holdout. Need fresh forward data or further independent regimes.

### Reproduce with existing Python, no plugin required

Run from the repo root:

```powershell
python 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/hma_multiconfirm_v1.py --csv 11-crypto-market-intelligence/data/BTC-USD_4h_Bitstamp_2y_2026-11-07_complete_4h.csv --output btc_hma_v1.json
python 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/audit_hma_v1.py --csv 11-crypto-market-intelligence/data/BTC-USD_4h_Bitstamp_2y_2026-11-07_complete_4h.csv --output btc_hma_timing_v1.json
python 11-crypto-market-intelligence/experiments/btc_4h_rule_lab_v0/test_hma_v1.py --csv 11-crypto-market-intelligence/data/BTC-USD_4h_Bitstamp_2y_2026-11-07_complete_4h.csv
```

**Next candidate work, not yet implemented:** genuinely independent entry quality/exit risk evaluation, regime-stratified tests, news/fundamental history with point-in-time provenance, annual high/low position score, portfolio-level drawdown, multiple hypotheses testing and independent future-date validation. The previously proposed 40% technical + 40% historical behavior + 20% fundamentals remains a **proposal**, not trained or mathematically calibrated.

