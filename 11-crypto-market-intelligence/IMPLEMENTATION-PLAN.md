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
