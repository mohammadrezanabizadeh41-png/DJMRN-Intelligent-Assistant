# KYNXA H0 — Second Windows RAM, memory commit and process snapshot (USER-REPORTED)

**Observed:** 2026-10-22. **Device:** User's own Windows 11 laptop. **Evidence level:** USER-PASTED PS OUTPUT; coordinator did not run code on Windows. No private machine identifiers, command lines, service details, user paths, credentials or private files retained.

## Exact reported observations

| Field | Reported value |
|---|---:|
| Installed DIMM RAM, sum `Win32_PhysicalMemory.Capacity` | **8.00 GiB** |
| OS-visible usable RAM, `Win32_OperatingSystem.TotalVisibleMemorySize` | **5.88 GiB** |
| RAM available, `Win32_OperatingSystem.FreePhysicalMemory` | **0.99 GiB** |
| Estimated hardware-reserved gap from rounded figures | ~2.12 GiB |
| Committed bytes | **9.58 GiB** |
| Commit limit | **11.66 GiB** |
| Pagefile allocated | **5.78 GiB** |

Top 15 group-by-name `Get-Process` **WorkingSet64 sums (MiB, rounded)**: chrome 11 processes/1495; ChatGPT 13/966; svchost 82/953; explorer 1/264; Memory Compression 1/242; msedgewebview2 6/205; MsMpEng 1/196; conhost 27/181; node_repl 12/113; RuntimeBroker 5/104; codex 2/98; node 13/97; powershell 1/89; WindowsTerminal 1/86; WmiPrvSE 3/84.

**Corrections and interpretation:** Prior ambiguous `RAM_Physical_GB=5.88` was the computer's OS-visible memory, NOT installed DIMM capacity; this Win32_PhysicalMemory reading resolves total physical installed RAM = 8.0 GiB. Chrome and ChatGPT account for ~2461 MiB **grouped working-set readings**, not necessarily 2461 MiB reclaimable private physical RAM: shared resident pages can be counted more than once. Never sum them to infer exact free memory after closing. Approximately 82.2% of commit limit was already committed. These are a single moment's observation; not a sustained swap/latency measurement or KYNXA resource benchmark.

**Safety/context:** Earlier H1 user-reported ZIP digest matched official KYNXA v1.7.0, extracted EXE `NotSigned`; vendor did not independently attest installer run/signature. This test made **no system changes**, did not install/run EXE, scan antivirus, or invoke KYNXA/model/Jan/Goose. No process closure observed or conducted. Do NOT automatically terminate `svchost`, `MsMpEng`, Memory Compression, Windows services or developer processes; only user-selected nonessential foreground applications can be closed normally after saving work.

**Assessment:** H0 `OBSERVED_LOW_HEADROOM`, ~0.99 GiB available while KYNXA NOT INSTALLED. Insufficient evidence for safe/responsive KYNXA test; pause setup. Proposed next: user closes optional duplicated browser/ChatGPT UI and otherwise unused foreground apps through their normal UI, then runs a short **read-only** Available GiB/Committed GiB snapshot. Treat >=1.5–2.0 GiB available only as a **provisional candidate testing target**, not a vendor minimum or safety guarantee. An unsigned, vendor-unverified installer retains its separate integrity/trust gate independent of RAM. If RAM headroom cannot improve without disrupting user work, continue lighter host evaluation or offline inspection instead.

**Related prior evidence:** [Download/hash/first RAM reading](KYNXA-H0-USER-WIN11-PREFLIGHT-20261022.md); [Host evaluation queue](../../03-architecture-and-tools/READY-MADE-HOST-EVALUATION-QUEUE-20261022.md). **D-005 OPEN, CAP-006 and G3B unchanged.**
