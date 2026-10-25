# OmniRoute Provider Gate v3 — real user Windows offline analysis

Date: 2026-10-25. Mission: DJMRN-OMNIROUTE-PROVIDER-GATE-V3-20261025.

## Provenance and scope

User pasted the console output in this conversation after running the delivered script through `powershell.exe -NoProfile -ExecutionPolicy Bypass -File ... -Mode AnalyzeExisting`. Evidence is **USER-REPORTED REAL WINDOWS OFFLINE RUN**, not independently retrieved device files. Exact PowerShell/CLR versions were not included in the pasted output; do not claim independent Windows PowerShell 5.1 compatibility certification. The complete AnalyzeExisting path did execute successfully according to this console evidence. Network mode, C# HTTPS transport and inference were not exercised by this user run.

```text
DJMRN_PROVIDER_GATE_V3=3.0.0
MODE=AnalyzeExisting; RUN_STATUS=COMPLETE; PROVIDERS=375
QUEUE_A=0; QUEUE_B=158; QUEUE_C=40; QUEUE_D=0; QUEUE_E=149; PENDING_EVIDENCE=28
NEW_UNIQUE_URL_TESTS=0; IMPORTED_ROWS=977; HTTP_ROWS=885
INFERENCE=NOT_TESTED; FREE_ACCOUNT_ELIGIBILITY=NOT_VERIFIED; NO_KEYS_NO_POST_NO_BILLING
WARNINGS=0; INPUT=DJMRN-DEEP-375-20261025-042141
SEND=12_COPY_SUMMARY_TO_CHAT.txt and optionally 01_ALL_375_PROVIDERS.csv + 02_ALL_API_ENDPOINT_TESTS.csv
OUTPUT: <USER_DESKTOP>\DJMRN-PROVIDER-GATE-V3-20261025-140557-971
```

The output folder timestamp is the literal user-reported folder label; timezone was not separately measured. Windows username and absolute personal path have been replaced with `<USER_DESKTOP>` for public-repository privacy. No substantive counters were changed.

## Interpretation

| Queue | Providers | Interpretation |
|---|---:|---|
| A | 0 | No independently verified account/free/eligibility gates recorded; not proof no free services exist |
| B | 158 | Follow-up candidates for endpoint/signup/auth/free-model verification |
| C | 40 | HTTP policy/region/WAF/rate/redirect/server or conflicting-path review |
| D | 0 | No repeated-network-failure classification established by this offline mode; not universal reachability |
| E | 149 | Special integration or no established fixed public API in pinned sources |
| PENDING_EVIDENCE | 28 | Insufficient evidence; preserve unknown |
| Total | 375 | All catalog identities retained |

977 endpoint rows were imported, 885 endpoint rows show HTTP responses. These are not unique reachable providers, not 885 inference engines and not successful completions. There were zero new URL tests and zero reported warnings. Do not merge these v3 totals with earlier v2 counts as if they had the same denominator.

## Missing source files and next action

The original v2 pair and the newly generated v3 CSV/JSON files still reside only on the user's Windows machine. **No actual per-provider result rows have been received or inspected in Work.** The numeric summary is all that is known. Never substitute the packaged synthetic sample files for these missing real records.

Next: obtain `08_OMNIROUTE_CONNECTION_QUEUE.csv` and `02_ALL_API_ENDPOINT_TESTS.csv` from the reported v3 output folder, or provide one offline read-only PowerShell text export when attachments are inconvenient. Then analyze all actual candidates and verify official free/account/model/billing/region conditions. No additional network scan is the current next step. No provider activation, paid call, account changes or operational failover authorized by this archive request.

## Related artifacts

- [Provider Gate v3 archive index](../tools/omniroute-iran-direct-check/provider-gate-v3/INDEX.md)
- [Earlier 817-URL v2 user evidence](OMNIROUTE-375-DEEP-AUDIT-V2-USER-RUN-20261025.md)
- [Canonical CURRENT](../../07-operations-and-continuity/CURRENT-STATUS.md)
