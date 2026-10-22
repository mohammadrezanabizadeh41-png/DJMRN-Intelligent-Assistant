# KYNXA H0 — ChatGPT Desktop manually closed and RAM improved (user observation)
**Date:** 2026-10-22. **Evidence source:** user-pasted read-only PowerShell stdout. **No remote Windows actions by coordinator.**

## Observed results
- User manually closed Windows ChatGPT Desktop following GUI startup/exit guidance; read-only `Get-Process -Name ChatGPT` returned **ChatGPT_Processes = 0**.
- Windows `Win32_OperatingSystem.FreePhysicalMemory` converted to GiB returned **AvailableRAM_GiB = 1.79**.
- Previous directly observed baseline: **0.99 GiB** available; difference **+0.80 GiB**. This is a before/after temporal observation, not controlled proof that all of the delta was exclusively released by ChatGPT.
- Prior device snapshot established **8.00 GiB installed**, **5.88 GiB OS-visible**. No new post-close committed memory/process table was provided.

## Interpretation, boundaries and action
- H0 remains **PARTIAL**, showing user could improve memory headroom by closing an unneeded foreground app; KYNXA setup/application/model still **NOT_RUN**. Approximately 1.79 GiB free is a plausible starting snapshot for **further inspection**, not evidence of KYNXA's minimum or suitability and not an authorization to install untested/unsigned EXE.
- User suggested rebooting to see if additional RAM frees, and proposed future assistant resource manager. **Reboot NOT_RUN**, before/after restart measurements NOT_RUN. Reboot may free some resources but is not guaranteed; if tested, save work and check ChatGPT remains closed/disabled and then recheck read-only available RAM and committed bytes. No pagefile changes, memory cleaners or automatic process termination.
- **Resource management requirement candidate, not adopted design:** Evaluate native KYNXA 1.7 existing resource admission / coordinator and local model lifecycle first; avoid building or adding a RAM-optimizer without proof. Direct original implementation: https://github.com/jinpeng900/KYNXA/blob/main/apps/agent-core/src/resources/admission.rs and https://github.com/jinpeng900/KYNXA/blob/main/apps/agent-core/src/resources/coordination.rs ; older version-scoped documentation https://github.com/jinpeng900/KYNXA/blob/main/docs/architecture/local-models.md (1.5 series, not verified v1.7 runtime). Favor one local model at a time, on-demand loads, no surprise background launches, queue-based jobs and strict user approvals. The existence of code/docs does NOT establish Windows real runtime or DJMRN integrations.
- **Security still independently unresolved:** KYNXA v1.7.0 installer EXE `NotSigned`, publisher explicitly reports installation not run/tested. Matching publisher ZIP SHA-256 is not safety assurance. Do not recommend bypassing Defender/SmartScreen. H2 installation pending informed user approval and provenance/safety review.
- No install, system configuration change, process kill, cloud account connection, model launch, new manager or KYNXA/Goose benchmark by coordinator. Existing G3B and CAP-006 guards unaffected; D-005 stays **OPEN**.

Links: [prior H0 DIMM/process snapshot](KYNXA-H0-USER-WIN11-RAM-PROCESSES-20261022.md), [current evaluation queue](../../03-architecture-and-tools/READY-MADE-HOST-EVALUATION-QUEUE-20261022.md).
