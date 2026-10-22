# KYNXA H0 — Windows user RAM after restart (2026-10-22)

User-supplied, read-only PowerShell report; not collected by assistant:
- AvailableRAM_GiB: 2.55
- CommitUsed_GiB: 3.37
- ChatGPTProcesses: 0

History: initial RAM available 0.99 GiB; after closing ChatGPT Desktop 1.79 GiB; post-restart 2.55 GiB. Compared to prior observation the free RAM increased by 0.76 GiB; against first reading it rose by 1.56 GiB. Earlier commit use 9.58 GiB, now 3.37 GiB. These measurements alone cannot attribute changes to one process.

Status: user-observed memory preflight improved. KYNXA installer not run and KYNXA resource use not measured. Prior ZIP SHA matched publisher-provided digest, but extracted installer is unsigned and publisher did not report an actual installation test of v1.7.0. Next: scan extracted installer with Microsoft Defender and review the result before any installation decision. Do not bypass Defender warnings. No new approvals for Windows tools, file access or external accounts. Architecture remains unselected.

Task: TASK-0021; comparison queue: KYNXA #1, goose #2.
