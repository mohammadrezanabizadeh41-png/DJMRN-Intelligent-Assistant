# DJMRN — Ready-Made Windows Assistant Host Evaluation Queue

**Date:** 2026-10-22. **User intent:** prefer real ready-made assistant products over building duplicate chat, agent, memory and local-model infrastructure from scratch. **Decision scope:** USER-REQUESTED EVALUATION ORDER ONLY, NOT HOST/STACK ADOPTION; this document authorizes neither installation nor tool access. **Canonical repo:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, branch `main`.

## Ordered candidates (requested order)

1. **KYNXA — first to inspect/benchmark.** Official repo: https://github.com/jinpeng900/KYNXA . Current inspected **v1.7.0**, 2026-10-22 release: https://github.com/jinpeng900/KYNXA/releases/tag/v1.7.0 . For ordinary Windows x64 setup, the ONLY required release download is https://github.com/jinpeng900/KYNXA/releases/download/v1.7.0/KYNXA-1.7.0-windows-x64-setup.zip ; 1,348,688,758 bytes; publisher's GitHub-asset SHA-256 `d2e16a8b17de8e86672ff12226d4aa6719f5b4d1ffd61a910e6b333af0fa973b`. Second `resources.zip` is for source builders and NOT needed for ordinary setup. The setup ZIP contains the installer EXE plus the base runtime, browser, E5 retrieval model and tools; optional conversational models are separate. Developer SDKs are not required for an end user. **Vendor explicitly states installer was compiled but NOT installation-tested and production signing is NOT configured.** The SHA is publisher-provided, not an independent authenticity proof. Review installer behavior and never bypass antivirus/SmartScreen/approval to run it.
2. **goose — second comparison target.** Official project: https://github.com/aaif-goose/goose . Current inspected desktop release `v1.55.0` (2026-10-16), official downloads: https://github.com/aaif-goose/goose/releases . UI, MCP, permission options and local Ollama are available by project documentation; not a verified DJMRN file boundary.

## Available historic device evidence (NOT a fresh reading)

- Lenovo Windows 11 Pro x64, Ryzen 5 3500U, RAM 8 GiB physically installed, historically ~5.88 GiB OS-visible because of hardware reservation. Earlier available memory snapshots ranged ~1.73 to 3 GiB under different loads. These are historical, not today's baseline and NOT an app benchmark.
- Do NOT repeat old generic D0 diagnostics just to re-establish known hardware; use a small fresh read-only baseline immediately before this particular performance experiment if user chooses.
- Disk/download size is not a measurement of peak working-set or memory footprint. Bundled E5/Chromium and background indexing can affect memory. No measured KYNXA idle/peak on this Windows device exists.

## Stage gates and report contract

- **H0 / PENDING USER-DEVICE READOUT:** Capture Windows-installed, OS-visible and available GiB, pagefile allocation, C: free GiB and running-app baseline in a read-only, no-admin, no-install PowerShell/CIM command. No personal file access, process command lines, secrets or logs uploaded. User provides sanitized output. If headroom looks poor, postpone installing and prefer alternate/lightweight testing.
- **H1 / NOT_RUN:** User download of KYNXA installer ZIP only; compare `Get-FileHash -Algorithm SHA256` against publisher digest and check Microsoft Defender warning; NO automatic install, code-signing bypass, execution-policy bypass or privilege elevation. A matching hash is insufficient to establish safety.
- **H2 / NOT_APPROVED, NOT_RUN:** Only after explicit, separate agreement about installer scope and provenance: controlled installer/launch, document installation location, observed consent/Windows warnings, running idle CPU/RAM and Windows available RAM; leave web accounts, plugins, auto-download chat models, unrestricted shell and personal folders DISABLED. Stop if risky prompts or unexplained activity occur.
- **H3 / NOT_RUN:** Opt-in separate local-model loading and Persian chat benchmarks if memory headroom allows, one model at a time. Compare no-model idle memory to loaded-model peaks, swapping, responsiveness, disk impact and graceful stop. Benchmark/selection is NOT inferred from ZIP size.
- **H4 / NOT_RUN:** If appropriate and separately authorized, confined two-fictional-file document tool flow with user-visible approvals, provenance verification, outside-manifest denial; no existing G3B test or CAP-006/guard status is invalidated by choosing a host.
- **H5 / NOT_RUN:** Compare goose under equivalent conditions and choose READY-MADE DIRECT / EXTENSION / COMPONENT REUSE / NO FIT based on evidence. No Fork until justified.

**Acceptance / stop indicators:** OS remains responsive, Windows available RAM is not exhausted, no sustained harmful paging, no unapproved installs/network/account/file operations; Persian chat and permitted tool calling demonstrated, not claimed. A provisional 1 GiB available-RAM floor at desktop idle may be used as a caution trigger, **not** as a validated threshold. Record exact Windows version, app version, idle/peak, test inputs, outputs and failure reasons. All stages currently `NOT_RUN`.

## Authority and continuity

Read [PROJECT-RULES](../PROJECT-RULES.md), [CURRENT](../07-operations-and-continuity/CURRENT-STATUS.md), [TASK-REGISTER](../02-project-management/TASK-REGISTER.md), [WORK-JOURNAL](../07-operations-and-continuity/WORK-JOURNAL.md) and relevant [TEST-REGISTER](../06-tests-and-evidence/TEST-REGISTER.md) before recording runtime results. D-005 global stack remains **NOT DECIDED**, G3/G3B fail-closed status remains unchanged. Applied/General library and Notion Tool Governance remain independent authorities for discovery and policy.
