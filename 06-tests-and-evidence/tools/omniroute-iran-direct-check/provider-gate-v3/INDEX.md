# Provider Gate v3 — recoverable source, research, tests and real user handoff

**Latest checkpoint: USER-REPORTED Windows AnalyzeExisting COMPLETE, all 375 identities retained; no new network tests.** [Real user evidence](../../../logs/OMNIROUTE-PROVIDER-GATE-V3-USER-ANALYZE-20261025.md).

## Start here for the next assistant

1. Read project CURRENT and the real user evidence above.
2. Real counts: A=0, B=158, C=40, D=0, E=149, PENDING_EVIDENCE=28; imported rows=977; HTTP rows=885; new requests=0; warnings=0.
3. Request the user's `08_OMNIROUTE_CONNECTION_QUEUE.csv` and `02_ALL_API_ENDPOINT_TESTS.csv`, or one offline text extraction. Those device files are **not yet present in GitHub or Work**. Do not start another full scan or fabricate the names of 158 B candidates from summary counts.
4. Keep the two source CSVs from the old run, the pinned source catalog and the newly created outputs distinct. No inference, eligible free account, approved provider connection or failover is established.

## Preserved deliverables

| Artifact | Meaning |
|---|---|
| [Executable PS1](Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1) | Original delivered self-contained v3.0.0; default offline AnalyzeExisting; explicit FullNetworkAudit, RetestFailed, ExportShortlist, SelfTest |
| [Persian instructions](README-FA.md) | Original delivered commands, limits, output schema and safety boundaries |
| [Research receipt](RESEARCH-RECEIPT-FA.md) | Original three-source receipts; research commercially PARTIAL; captured original project/upstream HEADs |
| [Notion read receipt](NOTION-READ-RECEIPT.json) / [Git source manifest](SOURCE-MANIFEST.json) | Exact observed source versions, page dates and blob SHAs |
| [Pinned dataset](PINNED-DATASET.json) | 375 IDs; 1088 target rows; 887 unique vetted URL strings; 41 historical curated rows without independent path corroboration |
| [Endpoint provenance](ENDPOINT-PROVENANCE.csv) / [Candidate matrix](MERGED-CANDIDATE-MATRIX.csv) | Versioned static source mappings and explicit UNKNOWN commercial/model gates; not actual device results |
| [Test report](TEST-REPORT-FA.md) / [Validation JSON](VALIDATION-RESULTS.json) | Linux PowerShell 7.4.6: 52 internal assertions + 42 integration checks PASS, zero real network requests; C# language-version-5 compilation and PS7 parser PASS |
| [Synthetic harness](Test-Gate-Fixtures.ps1) / [transport](DirectHttps.cs) | Reviewable fixtures and the transport source embedded in the executable |
| [Synthetic sample directory](SYNTHETIC-SAMPLE-OUTPUT/) | Index to all 12 original generated example outputs retained byte-for-byte inside the original ZIP; clearly SYNTHETIC ONLY, never real Iranian ISP evidence |
| [User console](USER-CONSOLE-SUMMARY.txt) / [user summary JSON](USER-RUN-SUMMARY.json) | Exactly the pasted numeric result, sanitized output path; not the missing row-level data |
| [Delivery checksums](SHA256SUMS.txt) | Original ZIP member checksums retained unchanged |
| build_gate.py / gate-template.ps1 / run_validation.py | Original Work development recipes/layout; optional developer material, not Windows-user dependencies |

## Historical status correction, without rewriting original receipts

The original research/test reports state that real Windows execution was NOT_RUN and no GitHub write had occurred **at delivery time**. Preserve those original receipts as historical. The later user run now establishes that the offline AnalyzeExisting path ran on their Windows device and completed. It does not exercise HTTPS transport, report exact PowerShell/CLR versions, prove all network modes on Windows 5.1, verify inference or resolve free/account gates. This archive is the later GitHub persistence action expressly requested by the user; original 'no GitHub write' statements do not describe the current archive state.

No WQ/WA has been invented. Earlier mission item 14/REPOSITORY-LOCK limited unsolicited research writes; the user's subsequent explicit instruction to save all of this work in this project authorizes **this scoped archive plus continuity links**. It does not amend the general lock, alter architecture, approve provider activation or modify Notion.

## Downloadable original package

[Original delivered ZIP](https://chatgpt.com/library?file_id=libfile_1b2a1de0d3d4819195c1950e31cd4e94&account_id=personal), 410935 bytes; SHA256 `8c0a00d5f1ba1647375101b13ac4eea6501ce1c0ac7c0361e987b3ef734a8bf4`. This link resolves only for the owning account; the original executable, source data, research and tests are also directly readable here. [Exact original ZIP is retained in GitHub as well](DJMRN-OmniRoute-Provider-Gate-v3-20261025.zip); bulky synthetic output members remain inside it rather than being duplicated as expanded Git files. A checksum/readback proves artifact retention, not successful inference or an eligibility approval.
