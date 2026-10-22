# KYNXA H2 — Installer wizard observed before installation

**Date:** 2026-10-22. **Source:** user screenshot from their Windows 11 desktop; only what is visible is reported. **Coordinator did not operate device or installer.**

## Observed wizard
- Window title: `Setup - KYNXA version 1.7.0`.
- Installer displays `6 GB RAM detected - a suitable model is selected`; this is approximately the **5.88 GiB usable** previously measured, while installed DIMMs total **8.00 GiB**.
- Optional local chat model listed `Qwen3 1.7B Q8_0`, approximately **1.7 GB** download, **8 GB RAM recommended**; critical **Download and enable checkbox is unchecked**. A selected model name inside a disabled field does NOT mean download/activation is enabled.
- Application, Data, User tools locations default under the user's per-profile **LocalAppData/Programs/KYNXA** folder, with no absolute personal user pathname retained here.
- Language English. Desktop shortcut checkbox checked. Wizard reports approximately **120.4 GiB free at application location** (wizard observation, not new PowerShell disk audit).
- Buttons `Install` and `Cancel` visible. Screenshot does not establish Install click, completion, runtime service startup, autostart entry, model download or actual KYNXA RAM footprint.

## Guidance / scope
- User explicitly requested progressing to an informed guided trial after a public security incident search. KYNXA v1.7.0 is still an **unsigned and publisher-install-untested** build. Previous SmartScreen override by user is evidenced by now-visible wizard; this alone does not establish trust.
- Coordinator reviewed options and advised **leave optional model unchecked**; keep default current-user paths, English, shortcut optional; user may now choose **Install**. Do not approve unusual extra elevation, cloud sign-in, broad file or shell tool access or any model download. If unexpected UAC/warning/error appears, stop and show screenshot. No global Defender shutdown.
- Test target: **no-model host startup idle**; after completion, user should measure available memory, CPU and program process tree. Prevent unrequested indexing of real personal directories or account linking.
- Status: `H2_WIZARD_VISUALLY_VERIFIED / INSTALL_BUTTON_USER_INSTRUCTED / INSTALL_SUCCESS_NOT_OBSERVED`. No installation result from user yet. `TASK-0021`, KYNXA candidate #1, goose #2, D-005 global stack OPEN, previous G3B file guard closed.

Related: [user risk search](KYNXA-H2-PUBLIC-SECURITY-SEARCH-20261022.md), [installer trust warning](KYNXA-H2-SMARTSCREEN-USER-BLOCK-20261022.md).
