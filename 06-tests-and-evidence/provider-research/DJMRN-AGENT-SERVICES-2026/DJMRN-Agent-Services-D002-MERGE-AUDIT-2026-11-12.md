# DJMRN — Agent Services 252 + Discovery 002 research merge

**Date:** 2026-11-12  
**Status:** RESEARCH ONLY; not a list of verified free/working MCP connections.  
**Current canonical dataset:** [DJMRN-Agent-Services-MASTER-2026.csv](DJMRN-Agent-Services-MASTER-2026.csv)  
**Base snapshot:** `b9981687afeb00c4f665b3f7e527297fcfbbedda` / Git blob `76a9ce3fd871fb5ce5a76b598a69b77031e1e5e7`.

## Exact reconciliation

| Type | Count |
|---|---:|
| Existing baseline (unchanged first 27 fields) | 252 |
| Recovery original research candidates | 171 |
| D002 partial-evidence potential-new candidates imported | 163 |
| D002 evidence-insufficient candidates imported as UNVERIFIED | 7 |
| D002 RequestBin duplicate excluded | 1 |
| Baseline-seed duplicates excluded (GitLab, Bitbucket etc.) | 12 |
| Unidentified clue «تیگر زو» excluded pending identity | 1 |
| D002 recovered checkpoint source records including exclusions | 184 |
| **Canonical research master rows** | **422** |
| **Original columns preserved** | **27** |
| **D002 raw fields preserved with D002__ prefix** | **47** |
| **Additional tracking columns** | **3** |
| **Canonical column total** | **77** |
| **Original canonical categories retained** | **26** |
| **New categories introduced** | **2** |
| **Canonical categories total** | **28** |

Original 252 records are preserved without altering their first 27 cells. Their new columns are empty to avoid inventing D002 data. All 170 new records retain **all** source D002 fields with a prefixed namespace, plus a projection into the original 27-column schema. Two new categories are analytical classifications for: (27) job/freelance opportunities and (28) authentication/access control. Original D002 A–L umbrella labels remain in `D002__service_category`.

**Deduplication:** first-pass case/spacing-normalized name and official website domain checks on 170 import candidates found **zero direct baseline matches** and **170 unique candidate names**; Work marked 13 entries CONFIRMED DUPLICATE, and 1 identity clue was set aside. *Deeper alias/corporate family relationship remains reviewable.* Some rows represent paid-only, trial-only, local-software-only, restricted automated-use, or unverified services. No candidate was asserted to be operationally free just by import.

## Preservation and provenance

- [Frozen 252 baseline CSV](DJMRN-Agent-Services-MASTER-252-SNAPSHOT-2026-11-12.csv) — exact original Git blob reference, not rewritten.
- [Recovery checkpoint CSV (184 records)](DJMRN-Discovery-002-Checkpoint.csv) — parser-normalized CSV copy retaining all 47 source fields; original uploaded byte-level source SHA-256: `f95729707857ca43d8a07979253a0056b062acff49e727e325972114eee5247b`.
- [Recovery checkpoint Markdown](DJMRN-Discovery-002-Checkpoint.md) — originally uploaded source SHA-256: `82ed944f28ef03c4a3d85b72dba947bad90131adfdd7be634fd0884498963554`.
- [Excluded 14 rows](DJMRN-Discovery-002-EXCLUSIONS-2026-11-12.csv) — 13 known duplicates and unverified «تیگر زو», separately preserved without inflating master.
- [Original Work 151 CSV](DJMRN-Free-Agent-Services-2026.csv) and [original report](DJMRN-Free-Agent-Services-2026.md), unchanged.
- [ChatGPT 101 additions](CHATGPT-APPS-DISCOVERY-2026-11-12.csv), unchanged.

Note: The CSV file-reading bridge normalizes numeric display (e.g. `1` may be rendered as `1.0`) and serializes CSV again, so the archival CSV should be treated as **semantically faithful**, not claimed byte-identical to the uploaded source. The original source bytes remain in the user's conversation attachment, referenced by its SHA-256 above. The original source Markdown is also retained here as read.

## Free-first and use gates

**UNKNOWN cost = UNKNOWN/DENY.** No registrations, MCP installations, OAuth connections, credit consumption, payments, deployments or OpenMausBot tests were executed. `verified` at row level records the status of source research, not account/geography/operational verification. This master is the **single research catalog** for upcoming Work continuation; point future prompts to it and ask Work to exclude all 422 names, aliases, domains and product identities before claiming NEW.
