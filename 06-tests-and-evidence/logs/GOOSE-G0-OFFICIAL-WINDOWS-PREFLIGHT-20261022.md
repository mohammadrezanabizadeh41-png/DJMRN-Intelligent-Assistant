# DJMRN host candidate #2 — goose: Windows Desktop preflight, NOT installed

**Date:** 2026-10-22. **Scope:** begin candidate #2 after KYNXA H3 PARK/HOLD. No new Windows install/download/run by assistant or user observed in this step. Evidence from official goose GitHub REST latest-release API and goose installation docs, plus canonical DJMRN host queue and verified Windows installed-engine inventory.

## Verified official release, NOT a guessed download
- Official repository: https://github.com/aaif-goose/goose
- Official latest stable **as checked 2026-10-22:** `v1.55.0`, published **2026-10-16 16:58:21Z**; https://github.com/aaif-goose/goose/releases/tag/v1.55.0
- Windows x64 Desktop **non-CUDA** archive: `Goose-win32-x64.zip`, publisher GitHub asset size **246,032,962 bytes**, SHA-256 digest **`4a10e547730832afc2fb13d1c3c4e60b0332ce3e49fd3793cb04259206054c0c`**, URL https://github.com/aaif-goose/goose/releases/download/v1.55.0/Goose-win32-x64.zip .
- Another Windows CLI archive, not chosen for desktop-first user: `goose-x86_64-pc-windows-msvc.zip`, size 76,483,830 bytes; archive is not the desktop package. CUDA Windows desktop archive `Goose-win32-x64-cuda.zip` 418,762,332 bytes; **not preferred for AMD Vega iGPU**. A publisher digest is evidence of source consistency, not independent signed binary safety or code trust.
- Official installation page https://goose.vcorp.ai/docs/getting-started/installation/ says Windows desktop: download ZIP, unzip, run executable. **Do not run installation scripts or WinGet just to see the GUI**. User authorization, Windows warnings, Defender and SHA match first.
- goose is Desktop+CLI/API and agent tooling over MCP, with permission controls according to official https://block.github.io/goose/ . Its desktop executable **is not a local LLM weight**; does **not** establish a working, free model at install time. Requires a configured LLM provider/model; existing old Jan / Ollama endpoints in [inventory](../../07-operations-and-continuity/LOCAL-ENGINE-AND-MODEL-PATH-REGISTER.md) do not prove actual service/inference available today. Do NOT invent a free permanent API or start paid accounts.
- Local on-device **Gemma3 1B** may make basic text but reliable agent tool calling remains **NOT TESTED**. User laptop physical 8 GiB, Windows usable ~5.88 GiB; CPU-only desktop first, avoid concurrent 4B+ loads and heavy extensions. Upfront criteria: *no per-day PowerShell/manual engine starts*, one working Persian chat after a one-time authorized GUI setup, meaningful approval-bound tool smoke only after chat works, no sustained swapping. If impossible, park goose quickly rather than repeat KYNXA long troubleshooting.

## Official workflow proposed for user (NOT_EXECUTED)
1. Consult permanent machine-readable inventory (all known local GGUFs, apps, endpoints, with actual-vs-inferred labels) **BEFORE any new installed-program search**: [Markdown registry](../../07-operations-and-continuity/LOCAL-ENGINE-AND-MODEL-PATH-REGISTER.md), [JSON registry](../../07-operations-and-continuity/LOCAL-ENGINE-AND-MODEL-PATH-REGISTER.json). KYNXA remains installed but parked; do not remove model files or app.
2. User downloads **only** `Goose-win32-x64.zip` from the verified official v1.55.0 release and may hash-check if user wishes; pause at Windows SmartScreen or antivirus warnings; no forced bypass.
3. Unzip and run Desktop only after opt-in; take screenshot of provider/model setup options **before** linking any cloud account / API key, installing MCP extensions or granting folders/shell permissions.
4. If startup/setup requires an unsupported, paid or manually serviced model, issue simple stop/go decision and return to core project. User wants a ready-made chat-first assistant, not custom long-running daemon plumbing.

**Status:** GOOSE-G0 OFFICIAL_RELEASE_RESEARCH_PASS / WINDOWS_DOWNLOAD_NOT_RUN / INSTALL_NOT_RUN / INFERENCE_NOT_RUN / D-005 OPEN / G3B GUARD CLOSED.
