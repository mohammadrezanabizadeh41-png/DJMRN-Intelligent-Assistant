# KYNXA H2 — User-reported completed installer and first real UI launch

**Date:** 2026-10-22. **Evidence:** User-supplied Windows screenshot and Persian message **"نصب شد"** (installed). The assistant has **no remote execution/session on the laptop** and did not independently test files/processes.

## Observed user screenshot
- A running maximized **KYNXA** window, with visible Work, Chat, Knowledge, Connections, Scheduled tasks, Skills, Models, Recent, Projects and Tasks navigation.
- Main composer: "Describe what you'd like to work on...", **Ask for approval**, **Select model**. Empty model selection is visually consistent with no model selected but does **not** prove that no model is downloaded/loaded.
- The window is genuine visible evidence of a successful **installer completed and GUI launched by the user**, not proof of gateway readiness, working inference, agent permissions enforcement, persistence, network isolation, file sandbox, low-RAM suitability or model installation.
- Prior installer UI screenshot had optional local model **Download and enable checkbox unchecked**; user has not reported a subsequent toggle or download.

## Previous hard evidence / issues
- Before installation, Windows 11 machine had 8.00GiB installed RAM, 5.88GiB OS-visible, last available 2.55GiB after restart; committed 3.37GiB. **No post-install or KYNXA-process memory observation yet.**
- Downloaded official v1.7.0 ZIP matched publisher SHA-256; extracted installer was **NotSigned**, SmartScreen warned unrecognized app, Defender full scan indicated 0 detected threats. Publisher admitted installer had not been installation-tested. User explicitly chose informed installation despite unsigned new-release risk.
- The user's actual installed version is inferred from their v1.7.0 Setup screenshot plus newly open KYNXA UI, not independently inspected by binaries.

## State and next test
**H2_USER-REPORTED_INSTALL_AND_GUI-LAUNCH_PASS**, **H2_IDLE_RESOURCE_BENCHMARK_NOT_RUN**, **H3_LOCAL_MODEL_NOT_RUN**. Host/global technology **D-005 remains OPEN**. G3B security guard unchanged and fail closed. User requested prioritizing KYNXA #1, goose #2; **no decision to adopt KYNXA as DJMRN core**.

Next user action: keep the main application window open, do not choose/download a model, do not enable Skills/Connections/Tools or index personal files, preserve **Ask for approval**, and run an isolated read-only PowerShell snapshot of OS available RAM/committed bytes plus KYNXA name/descendant process working sets. Report output without private paths or command lines. One point-in-time working-set sum is not a complete idle/peak/proportional RAM or CPU benchmark; comparison against before-install RAM is indicative only because other app load/time may differ.
