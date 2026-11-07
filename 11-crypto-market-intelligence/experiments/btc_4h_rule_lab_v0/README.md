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
