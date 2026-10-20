# Historical evidence summary — 2026-10-17 .. 2026-10-19
**Primary source:** [original Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3). این خلاصه فقط بخش‌های مربوط به پروژهٔ جدید را با boundary دقیق منتقل می‌کند و جایگزین raw console output نیست.

## Python/SQLite
Python 3.14.7 and sqlite3 3.50.4 user-run tests; FTS5 compiled True and in-memory virtual table creation passed. SQLite3.50.4 vulnerable/concurrent WAL behavior must not be assumed safe under untested workload. Historical Research Architect CLI `init/inspect/index/search/packet` on local synthetic corpus works as reported, but not part of chosen greenfield implementation.

## Jan and inference
Jan Desktop localhost local model API catalog passed. Jan Agent nightly `0.8.6-64` installed and constrained read-only pilot reported one file read; user compared SHA-256 of target, unchanged. No proof of full tool trace, browser/website actions, sandbox boundaries or production security. Gemma3 4B had Vulkan OOM in some settings and Jinja role alternation errors, yet simple API eventually succeeded. Gemma3 12B CPU test slow; LM Studio Gemma4 E4B load stalled. Different scenarios ≠ unconditional incompatibility.

## P1-A simulated durability/receipt
Source 2026-10-19 user pasted PowerShell output, **P1-A RESULT: PASS / Python exit 0**, sandbox folder under AppData/Local for synthetic-only test. One-shot local sqlite DELETE journal/synchronous EXTRA, quick_check ok; exactly 20 incoming IDs, 15 accepted jobs and 5 duplicates; simulated subprocess exit before COMMIT -> no receipt then accepted replay; after COMMIT before ACK -> durable receipt reused; conflicting payload same logical key rejected. **Limit:** Assistant did NOT independently open actual Windows JSON/DB bytes or rerun local machine test; no authenticated website, email, model, externally sent message, or full power-loss resilience verified.

## Resource readings
Detailed RAM/commit/hardware observations under `01-system-inventory/resource-observations.md`, tied to Oct17/19 measurement. P1-A measured P0 baseline, **not peak full system under P1-A**.

## Next test proof requirements
Test ID, user authorization, context, anonymized inputs, config/model version, expected/actual, actual output path/commit/hash if available, resource readings, failure injection, restart proof, rollback, risks, remaining uncertainties. Never declare the real assistant done because synthetic tests passed.
