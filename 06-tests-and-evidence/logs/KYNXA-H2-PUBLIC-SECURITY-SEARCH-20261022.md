# KYNXA H2 — Targeted public security report and installer reputation review

Date of search: **2026-10-22**. **User instruction:** Search whether KYNXA has publicly reported security problems, then advance their guided installer trial if no credible reports are found. **Authority:** user personally chooses whether to proceed despite SmartScreen; no assistant access to device.

## Actual independent searches (not a code audit)
Web searches in English and Chinese for exact identifiers `KYNXA`, `jinpeng900/KYNXA`, `KYNXA-1.7.0-windows-x64-setup`, malware/virus/backdoor/security/vulnerability/Windows EXE and official release ZIP SHA256. Also inspected live GitHub repository metadata and GitHub Issues API:
- Repo https://github.com/jinpeng900/KYNXA created **2026-09-05**, at check **6 stars, 4 forks, 0 open issues**.
- `https://api.github.com/repos/jinpeng900/KYNXA/issues?state=all&per_page=100` returned **6 entries, all Pull Requests**, none a security incident issue. This does NOT show private reports, undisclosed flaws or prove clean security.
- Searches returned **no corroborated, public KYNXA-specific malware or reported exploitable-vulnerability finding**. Results mentioning malware were mostly about unrelated software and cannot be attributed to KYNXA.
- Public repository-specific advisory API query was **blocked by connector URL allowlist**, therefore cannot claim an independently exhaustive list of KYNXA's repository advisories from that endpoint. Global GitHub advisory indexing/search was reviewed but no KYNXA-specific item surfaced.

## Evidence and remaining uncertainties
- Original KYNXA v1.7.0 release, https://github.com/jinpeng900/KYNXA/releases/tag/v1.7.0, publicly released **2026-10-22** with user verified ZIP digest `d2e16a8b17de8e86672ff12226d4aa6719f5b4d1ffd61a910e6b333af0fa973b`. KYNXA release says installer **not actually installation-tested and not production signed**.
- User's first attempt to execute the extracted EXE raised Windows Defender SmartScreen **"Windows protected your PC" / unrecognized app**; this warning alone does not prove the binary is malicious. Microsoft's app reputation documentation: https://learn.microsoft.com/windows/apps/package-and-deploy/smartscreen-reputation explains new/unsigned binaries may have no reputation and show that warning.
- Earlier user-provided Defender full scan screenshot reported zero detected threats but was not a file-specific trusted safety or static-analysis report.
- Brand-new release and thin independent adoption means **absence of public reports is weak evidence of safety**. ZIP digest matches publisher, not an independent trust validation or proof binary corresponds to source.
- KYNXA is designed to include Windows shell/tools/browser integrations, so untrusted executable exposure is materially greater than a text-only desktop viewer.

## User-governed next action
**Search conclusion:** `NO_CREDIBLE_PUBLIC_KYNXA_SPECIFIC_REPORT_FOUND_AS_OF_SEARCH`, **NOT** `SECURITY_CLEARED`. User wishes to move forward. Informed, voluntary per-file SmartScreen override may be chosen by user using **More info > Run anyway**; this does not require globally disabling antivirus, Windows security or changing group policy. If an explicit malware finding, unexpected elevation, unusual behavior or altered target executable appears, STOP. The installer wizard should be inspected *before Install*, opt out of optional Qwen/model download and auto startup, do not connect sensitive accounts or approve broad file/shell tools. Assistant did NOT execute installer, did NOT see wizard and did NOT benchmark RAM. No model/stack selection; D-005 OPEN.

Related records: [SmartScreen screen](KYNXA-H2-SMARTSCREEN-USER-BLOCK-20261022.md), [prior Defender scan](KYNXA-H1-DEFENDER-FULL-SCAN-USER-20261022.md), [evaluation plan](../../03-architecture-and-tools/READY-MADE-HOST-EVALUATION-QUEUE-20261022.md).
