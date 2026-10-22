# KYNXA H2 — Windows Defender SmartScreen warning before installer launch

Date: 2026-10-22. Origin: user-provided screenshot of Windows UI. Exact repository: `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`. **Evidence is screenshot reported by user; no assistant Windows access.**

## What was actually observed
- User attempted to start extracted `KYNXA-1.7.0-windows-x64-setup.exe` after a Defender full scan with 0 detections.
- Blue Windows SmartScreen dialog: **"Windows protected your PC"**, **"Microsoft Defender SmartScreen prevented an unrecognized app from starting. Running this app might put your PC at risk."**
- Visible actions: **More info** and **Don't run**. Screenshot does not show the installer wizard, user click result, "Run anyway" or actual installation.
- Previous independently inspected publisher's official v1.7.0 release stated production code signing not configured and **installer itself not installation-tested**. User reported `Get-AuthenticodeSignature` as **NotSigned**, and downloaded release ZIP SHA256 equal to the publisher asset digest. Full Windows Defender scan 0 detections is not a file-specific assurance, malware-free certificate or a SmartScreen override.
- Previous user Windows read-only baseline: 8 GiB installed physical DIMMs, OS-visible 5.88 GiB; free RAM post-restart 2.55 GiB; ChatGPT Desktop process count 0. KYNXA memory/runtime not measured.

## Response and boundaries
- Advise user to click **Don't run**, **not** bypass SmartScreen or approve unexpected elevation. SmartScreen warning is a trust/reputation gate; not proof the EXE is malicious, but absence of trust and no demonstrated installation testing means an unchecked direct-run on a working device has avoidable risk.
- Next: pursue source/publisher verification or isolated testing, request signed/reproducible release or publisher installation validation; compare second candidate goose when appropriate. Don't install a background memory manager or tweak pagefile because installer launch did not occur.
- **Test status:** `H2_SMARTSCREEN_WARNING_OBSERVED / LAUNCH_BLOCKED / INSTALL_NOT_RUN`. No assistant-run installation, no user-reported success/failure click, no KYNXA runtime or model, no app settings or file permissions changed, no D-005 stack adoption, no G3B guard changes.

## Associated evidence
[KYNXA H1 Windows Defender full scan user observation](KYNXA-H1-DEFENDER-FULL-SCAN-USER-20261022.md) · [KYNXA evaluation queue](../../03-architecture-and-tools/READY-MADE-HOST-EVALUATION-QUEUE-20261022.md).
