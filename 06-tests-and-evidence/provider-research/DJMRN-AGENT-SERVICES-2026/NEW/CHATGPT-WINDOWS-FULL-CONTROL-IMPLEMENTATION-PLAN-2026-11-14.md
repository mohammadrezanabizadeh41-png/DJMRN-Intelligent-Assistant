# DJMRN — NEW — ChatGPT ↔ Windows / Browser / Coding: Operational Implementation Plan

**Date:** 2026-11-14  
**Status:** PARTIAL IMPLEMENTATION — 19 downloads + 19 Windows shortcuts verified; CLI/GUI installation attempted, blockers tracked in section J; full same-chat operation NOT yet verified  
**Repository branch:** main. This is a new document in the NEW subfolder, not a new Git branch.  
**Purpose:** Resume and implement the minimum adequate toolset so the existing ordinary ChatGPT conversation can control the user's authorized Windows PC, browser, coding workflow and compatible desktop apps.
**Parent discovery catalog:** [19 ChatGPT connection, Windows, Browser and MCP tools](../CHATGPT-CONNECTION-WINDOWS-BROWSER-MCP-TOOLS-2026-11-14.md). This parent research list stays unchanged.

> This document preserves the preceding report's tool selection, priorities, execution order, real test acceptance criteria and alternatives. It is a proposed action plan, not evidence of installation, working visual control, unlimited access, entitlement to Custom MCP, or approval for sensitive operations.

## A. Required capability and non-goals

**Target:** the same ChatGPT chat issues tasks; can observe Windows screenshots/UI, click/drag/type/scroll/switch windows, navigate Chrome/Edge and fill harmless forms, code and test websites, run local apps, and where technically supported interact with graphics software and games. Actions must return observable results to this chat and support stop/retry/recovery.

**Not the goal:** install 19 overlapping programs; create another agent team/IDE by default; bypass ChatGPT tool entitlements, provider terms or billing; disable Windows protections; install everything before the first test. Installing an MCP server locally does not by itself make it directly callable from ChatGPT. A compatible authenticated transport/host or a simple local CLI adapter reachable through the already connected remote bridge must actually work.

## B. Selected stack and roles

| Priority | Software | Role | Selection | Official source |
|---|---|---|---|---|
| P0 | Remote Desktop Commander | EXISTING remote executor: files, PowerShell/terminal, processes, scripts and test results from this chat | KEEP. Already connected, do not reinstall or duplicate | https://desktopcommander.app/ |
| P1 | Windows-MCP (CursorTouch) | Windows UI: screenshots/snapshots, mouse, keyboard, scroll, app focus and switching | FIRST new visual control candidate; must prove same-chat control via reachable local adapter | https://github.com/CursorTouch/Windows-MCP |
| P2 | Microsoft Playwright MCP / Playwright | Browser tabs, DOM/accessibility, form actions, screenshots, repeatable browser tests | SECOND new candidate; use direct CLI if less complex than full MCP bridging | https://github.com/microsoft/playwright-mcp |
| P3 | Chrome DevTools MCP/CLI | Console, Network, performance and professional website debugging | OPTIONAL, only when relevant web-debugging tasks exist | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| Existing | Python, Node.js/npm, uv, Git, VS Code, Codex CLI | Coding, execution, builds, tests | Previously detected on Windows PATH; no default reinstall | Existing device tools |

**Minimal core = Remote Desktop Commander + Windows-MCP + Playwright.** Chrome DevTools is an on-demand specialist, not a duplicate browser agent.

**Alternatives only if there is a real unmet capability:** 
- [OpenDesk](https://github.com/vitalops/opendesk) instead of Windows-MCP if GUI capability fails.
- [Browser MCP](https://github.com/BrowserMCP/mcp) if Playwright cannot access the needed owner-authorized browser context reliably.
- [Windows Commander MCP](https://github.com/exalsch/windows-commander-mcp) for a specific Windows administration tool gap only.
- [Backboard Desktop](https://github.com/Backboard-io/Backboard-Desktop) is an independent agent IDE, not an automatic extension of this chat; consider only if ordinary ChatGPT plus tools cannot perform an important programming workflow.
- [Chat On Steroids](https://github.com/totec448-spec/chat-on-steroids) may be evaluated later for an all-in-one interface, but full Custom MCP support and compatibility with the current ChatGPT plan are UNVERIFIED. It is not a reliable bypass of Codex/Work entitlement.
- gptme, Browser Use, chrome-use, chatgpt-use, Web GPT Agent, MCP Plugins With ChatGPT Web, codex-browser-bridge, Yep Anywhere and ChatGPT Desktop Community remain research/alternative items in the parent 19-tool catalog; no default installation.

## C. Exact integration design (proposal, not tested)

1. ChatGPT (current conversation) sends a supported tool request to existing Remote Desktop Commander.
2. Remote Desktop Commander executes a local script/command on the authorized Windows session.
3. The local command uses Windows-MCP through a real local MCP client/adapter, **or** a simpler directly callable Windows UI automation interface when MCP overhead is unnecessary.
4. Browser commands use Playwright CLI/client, or Playwright MCP via the same verified local adapter.
5. Diagnostics use Chrome DevTools CLI/MCP only when needed.
6. Return screenshot/DOM, exit code, test result or other non-sensitive observation back to ChatGPT. Model assesses result before next action.

**Important:** no assumption of automatic MCP discovery, no invented Remote Desktop Commander tool capability, and no assertion that an MCP server installed on Windows can be added directly to all ChatGPT subscription tiers. If the bridge cannot transfer or invoke a new tool, the step is BLOCKED until a tested compatible local client/adapter exists. Prefer deterministic direct scripts over new servers for simple tasks.

Keep interfaces local/loopback by default; don't expose an unauthenticated control port. Treat screenshots, web content and files as untrusted; never put browser session cookies, credentials or private client files in chat or this publicly visible repository.

## D. Step-by-step order with real I/O, gates and success tests

### S0 — Read-only readiness (START HERE NEXT TIME)

Before any download: check the existing remote connection, Windows version, RAM/process headroom, browser environment, actual available tools in this ChatGPT session, relevant official project releases, Windows compatibility, license, maintenance, dependency versions, install size, cost and current quotas; identify required permissions and uninstall/rollback paths.

Existing evidence from the immediately preceding conversation (not a new test by this document): remote device was online; Python launcher, Node/npm, Git, uv, VS Code, Codex CLI were on PATH. The tested Python environment did not detect pyautogui, mss, Pillow, Playwright, pywinauto, selenium or win32gui. Do NOT install these all automatically: choose only proven dependencies.

**Pass:** identify minimal free installation/test command, allowed folders and process boundaries, expected resource use, exact rollback; no unknown-cost paid action or unapproved permission change.

### S1 — Windows visual pilot (FIRST real missing capability)

Tool: Windows-MCP, or a simpler Windows UI automation adapter reached via existing remote command tool.

1. Capture a fresh Windows desktop screenshot or structured UI snapshot and make result accessible in this chat.
2. Use a harmless test program such as Notepad/Calculator: open it, focus and switch window.
3. Perform a click, typed innocuous text, scroll and if applicable a controlled drag.
4. Capture a second screenshot/snapshot and compare to the intended state.
5. Test an expected failure: missing/unfocused window, wrong resolution, disconnected tool, timeout or locked/elevated desktop; demonstrate stop and recovery.

**PASS only if:** same ChatGPT conversation → connected remote bridge → local visual action → verified screenshot/observable result. Otherwise mark BLOCKED/FAIL, report which hop failed, and trial the simpler direct automation fallback rather than claim success.

**Limits to record:** DPI scaling, multiple monitors, background/minimized windows, elevated/UAC secure desktop, GPU full-screen apps, keyboard layouts, latency. No silent privilege escalation.

### S2 — Browser automation pilot (SECOND)

Tool: Microsoft Playwright (prefer simplest working direct CLI; MCP only if necessary).

1. Launch an isolated disposable Chrome/Edge test context, not owner's primary logged-in browser.
2. Open a harmless public demo page; read current URL/title/DOM and screenshot.
3. Click links/buttons, type sample text into a test form, navigate and switch tabs.
4. Confirm visible result and handle timeout, dynamic page changes, popup/new tab and error.
5. Only if required later, examine the official Playwright extension approach to operate the owner's existing authenticated profile with deliberate permission. Do not export passwords, cookies or tokens.

**PASS:** current chat issued and verified all browser actions, including resulting URL/title/DOM/screenshot. Sending real proposals, messages or payments needs separate action-level approval.

### S3 — Code, website and debugging pilot (THIRD)

Tools: existing Python/Node/Git/VS Code through Remote Desktop Commander, Playwright for browser test, Chrome DevTools if actual error investigation calls for it.

1. Create a small project in an agreed isolated workspace.
2. Edit source files with current chat tools; run a local build/test and inspect errors/exit codes.
3. Start local development server; visit site with Playwright and test one user interaction.
4. If a website bug occurs, examine Console/Network using DevTools or ordinary browser diagnostics.
5. Fix error, rerun tests, verify result visually, terminate server cleanly, and verify restart.

**PASS:** actual source, repeatable build/test, working browser UI, observable error handling, clean stop/recovery. Git push, production deployment, release/merge or publication require task-specific approval.

### S4 — Windows apps, graphics, game compatibility (FOURTH, per application)

After S1-S3, separately test opening/focusing an authorized application, menus, file dialogs, screenshots, mouse/keyboard. For graphics and games check GPU rendering, full-screen/direct input, input latency, anti-cheat and accessibility limits. **Do not promise arbitrary games can be played by an agent**; neither unlimited control nor real-time gameplay is guaranteed. No anti-cheat bypass, no UAC/security bypass.

### S5 — Convenience and measured reliability (FIFTH, conditional)

Only after evidence of repeated useful operation: create one minimal start/stop script (with approval), configure bounded retries/timeouts, process cleanup, simple logs appropriate to the actual task and a known reconnect route. Respect 8GB-laptop resource limits; avoid duplicate resident agents, daemons, queue services or extra IDEs unless measurements show a need.

## E. Acceptance / evidence matrix

| Capability | Evidence required | Status now |
|---|---|---|
| Existing Windows file/terminal remote tool | command and observed response | OBSERVED in preceding conversation |
| Windows screenshot visible to this chat | real screenshot/result inspectable here | NOT TESTED |
| Click/keyboard/drag/window switch | harmless action plus before/after validation | NOT TESTED |
| Browser control, multiple tabs and form actions | repeatable isolated browser flow with URL/DOM/screenshot | NOT TESTED |
| Real Chrome logged-in profile | explicit opt-in and isolated compatibility test | NOT TESTED / OPTIONAL |
| Local coding and website with working UI | real files, build/test, browser verification | NOT TESTED END-TO-END |
| Chrome DevTools error diagnosis | actual console/network problem investigated | NOT TESTED / OPTIONAL |
| Desktop graphics / game control | per-app evidence with recorded limitations | NOT TESTED / OPTIONAL |
| Restart/recovery | clean stop, reconnect and no orphan processes | NOT TESTED |
| Current ChatGPT plan compatibility with Custom MCP | official plan docs and test, where relevant | UNVERIFIED |

No capability is DONE just because a package was installed, a server started, or a process printed success. Require end-to-end usable value in this conversation, verification, failure handling, safety and resource awareness.

## F. Download order / install instructions for the NEXT execution session

**No download, installation, tool activation or privileged change is authorized by saving this plan.**

1. Read this file and linked 19-tool list; re-verify official Windows-MCP and Playwright requirements/current releases at execution time.
2. Preserve the already-connected Desktop Commander; run S0 only.
3. After an explicit execution instruction and review of impacts, install/test the smallest Windows-MCP path for S1.
4. After S1 passes, install/test the smallest compatible Playwright path for S2.
5. If professional web-debugging actually needs it, add Chrome DevTools in S3.
6. Consider OpenDesk or Browser MCP as **replacement** if respective primary tool fails, not parallel installs.
7. Consider Backboard Desktop only as a **separate optional workflow**, not as a prerequisite for this chat to code.
8. Stop on unknown nonzero spend, billing/overage, excessive permissions, environment corruption or incompatible connection; report precise blocker and rollback.

## G. Authorization, constraints and authority

- **Free-first:** free/open source does not imply free hosted inference or unrestricted quota. Verify costs, licenses, current free limits, credit consumption, card requirement and overage. UNKNOWN COST = DENY.
- **Security:** owner seeks wide capabilities but Windows Firewall, Defender, UAC, Secure Boot and account protections do not need disabling. Prefer least privilege, test profiles, clear scopes and immediate stop/disconnect. Consequential operations require explicit approval.
- **No secret export:** do not send credentials, cookies, tokens, account IDs, private customer contents or sensitive device details to this public GitHub repo.
- **Authority:** GitHub canonical source and code, Notion approved architecture/decisions, current Windows runtime execution, ChatGPT reasoning/tool orchestration. This is a static new proposed plan, **not** a new rolling progress tracker or enacted architecture. Ongoing project status remains in the existing CURRENT-STATUS.md only when the owner specifically requests a status update.
- **No unauthorized external action:** no payments, sensitive permission grants, deletion, publication, deployment, messages, proposals or account changes solely from this plan.

## H. Resume instruction

**NEXT USER COMMAND EXPECTED:** authorize a concrete S0/S1 action after reviewing this plan. Start with S0 read-only checks and one reversible Windows visual test; don't install the whole stack in one batch. Advance S1 → S2 → S3 → S4 → S5 only when each prior stage has verified real I/O in this same ChatGPT conversation. Keep this file as the single static execution plan in NEW; do not create further redundant plan files.

**Archive action only:** this GitHub document does NOT mean any Windows software was downloaded, installed, activated, connected, tested, or granted new rights.


---

## I. Owner-authorized 19-file installation register — 2026-11-14

**Authority / intent:** Owner explicitly requested this exact 19-file set to be installed sequentially, tested where feasible, and given Windows shortcuts where an interactive launcher exists. This updates the **existing NEW execution plan**, not the historical 19-tool discovery catalog.

**Download audit:** 19/19 local download artifacts verified on DJMRN Windows staging area in the preceding run. This does **NOT** imply 19 separate installable applications: five are packaged CLI libraries, two are browser extensions, one is source-only, and several are portable programs or GUI installers. Installation, compatibility and ChatGPT connection have different acceptance gates.

| # | Software/artifact | Delivery | State at registration | Next installation/verification task |
|---:|---|---|---|---|
| 01 | Windows-MCP | Python wheel | Downloaded; isolated venv executable present | Verify import, CLI/help, visual MCP transport; create on-demand shortcut |
| 02 | Playwright MCP | npm package | Downloaded; local npm executable present | Verify CLI, isolated non-authenticated browser run; launcher shortcut |
| 03 | Chrome DevTools MCP | npm package | Downloaded; local npm executable present | Verify CLI and browser compatibility; launcher shortcut |
| 04 | OpenDesk | Python wheel | Downloaded; isolated venv interpreter present | Verify installed module/CLI and GUI transport; shortcut if invocable |
| 05 | Backboard Desktop | Pinned GitHub source ZIP | Downloaded; source only; no installed Windows app observed | Inspect build/install prerequisites; resource/cost gate before building VS Code-sized app |
| 06 | Chat On Steroids | Windows x64 installer | Downloaded; not installed | Review installer/signature/Windows Defender; user-scoped installation if safe; shortcut |
| 07 | Chat On Steroids browser extension | ZIP extension | Downloaded; not activated | Extract staged extension; browser permission grants require separate owner action |
| 08 | Windows Commander MCP | Windows ZIP | Downloaded; portable EXE extracted | Check .NET runtime, CLI, safe execution; launcher shortcut |
| 09 | chatgpt-use | Windows ZIP | Downloaded; portable EXE extracted | Verify --help and tool requirements; only launch locally after terms/privacy review |
| 10 | MCP Plugins With ChatGPT Web | GitHub source ZIP | Downloaded; npm dependencies installed | Inspect build scripts; build if safe; launcher, no authenticated Chrome access |
| 11 | Browser MCP | GitHub source ZIP | Downloaded; pnpm dependencies installed | Inspect build scripts; build if safe; extension remains disabled until permission review |
| 12 | codex-browser-bridge | Windows EXE | Downloaded; portable file staged | Verify CLI/help and setup; create on-demand shortcut |
| 13 | Browser Use | Python wheel | Downloaded; isolated venv installed | Verify import/CLI, optional browser dependencies, no cloud billing |
| 14 | chrome-use | Windows archive | Downloaded; portable EXE extracted | Verify CLI/help, shortcut; no account automation without review |
| 15 | gptme | Windows x64 installer | Downloaded; not installed | Review signature/Defender; user-scope install and shortcut where safe |
| 16 | ChatGPT Desktop Community | Windows x64 installer | Downloaded; not installed | Review installer; user-scope install and shortcut; do not migrate credentials |
| 17 | Yep Anywhere | Windows x64 installer | Downloaded; not installed | Review installer; user-scope install and shortcut; no external agent connections |
| 18 | Web GPT Agent | Windows x64 installer | Downloaded; not installed | Review installer; user-scope install and shortcut; no ChatGPT account takeover |
| 19 | Web GPT Agent browser extension | ZIP extension | Downloaded; not activated | Extract staged extension; owner approval needed for Chrome permissions |

### Required install sequence and acceptance

1. **Before each change:** verify provenance/official source and SHA where published; inspect executable signature/Defender results, free use and dependencies; do not force elevation/disable UAC or Defender; install per-user/in isolated directories if possible. If an installer needs privileged rights, unexpected account access or provider billing, **stop that item, record blocker**, and continue other independent items.
2. **Installed means:** executable/module is present and verified via version/help/import or a smoke test; browser extension staging does not equal browser-activated; source extraction does not equal compiled app. The user asked for full installation; differentiate VERIFIED/INSTALLED, PARTIAL/EXTRACTED, BLOCKED and NOT-STARTED rather than asserting success.
3. **Shortcuts:** add only useful on-demand shortcuts to the Windows Desktop, preferably inside one `DJMRN ChatGPT Tools` folder. For MCP servers/CLI tools use explicitly named `Launch ...` shortcuts or documentation; never start 19 persistent agents automatically. For extensions, keep setup documentation and unpacked files until browser permissions are reviewed.
4. **Validation:** no secrets/passwords/cookies transferred; do not log in to ChatGPT Web through automation until account/platform terms are reviewed; no paid credits or new remote exposing ports; report local state honestly.
5. **Continuity:** this is the current user-authorized installation checklist. Return to the S0–S5 end-to-end operating tests in the same file afterward. The connected remote desktop transport may have quota, so installing local MCP tools alone is not a replacement for an authorized bridge into this conversation.

**At registration:** the initial tool inventory confirmed 19/19 files exist, and these already installed/staged executables were detected: Windows-MCP, OpenDesk, Browser Use, Playwright MCP, Chrome DevTools MCP, Windows Commander MCP, chatgpt-use, chrome-use and codex-browser-bridge. GUI installer execution and real browser/session integration **not yet confirmed**. Exact completed work to be verified from the Windows machine before claiming a completed item.


---

## J. Verified Windows installation results — 2026-11-14 (supersedes previous NOT YET INSTALLED statements)

**User authorization:** after the archival registration in section I, the owner explicitly instructed sequential installation of all 19 downloaded artifacts, and Windows shortcuts for later use. The subsequent actions were carried out on the authorized local laptop via the already-connected remote bridge. No account/session authorization, payments, production deployment, or global security policy changes were authorized or performed.

**Evidence summary:** 19/19 source download files verified by size and recorded hash; 19/19 numbered Windows shortcuts created in a single Desktop folder named `DJMRN ChatGPT Tools`; local evidence files `GUI-INSTALL-RESULTS.csv`, `CLI-VALIDATION.csv`, and the two download-queue CSVs remain in `Desktop\DJMRN-ChatGPT-Downloads`. The new Windows shortcuts folder contains `README-STATUS.txt` reflecting real states and blockers. A shortcut is **not** independent proof of a runnable application.

| # | Item | Verified result | Real evidence / remaining action |
|---:|---|---|---|
| 01 | Windows-MCP | **INSTALLED, EXECUTION BLOCKED** | Python virtual environment and `windows-mcp.exe` exist, but `--help` returned Windows Application Control WinError 4551; use signed/approved distribution or scoped policy review, not blanket security disabling |
| 02 | Microsoft Playwright MCP | **INSTALLED; CLI HELP PASS** | Local npm executable exists, `--help` exit 0; a later no-account local browser pilot passed via the preinstalled remote executor (section K); MCP bridge still not connected |
| 03 | Chrome DevTools MCP | **INSTALLED; CLI HELP PASS** | npm executable exists, `--help` exit 0; Chrome debugging end-to-end not yet tested |
| 04 | OpenDesk | **INSTALLED; CLI HELP PASS** | Python venv and `opendesk.exe` exist, `--help` exit 0; a later memory-only screenshot using OpenDesk's installed mss dependency passed (section K); OpenDesk MCP and real mouse control not yet tested |
| 05 | Backboard Desktop | **SOURCE ONLY / BUILD BLOCKED** | Official pinned source ZIP valid; no verified native release binary in prior GitHub releases; Bun absent; full source extraction via Windows tar encountered unsupported symlink fixture; no runnable desktop build; existing 8 GB RAM is a constraint |
| 06 | Chat On Steroids | **GUI INSTALLER BLOCKED** | Official download validated; silent per-user launch rejected by Windows Code Integrity / Application Control; event ID 3077 observed; not installed |
| 07 | Chat On Steroids extension | **UNPACKED / NOT ENABLED** | Chrome extension ZIP extracted, manifest located; browser permissions not granted |
| 08 | Windows Commander MCP | **PORTABLE STAGED / RUNTIME ERROR** | official ZIP unpacked with `WindowsCommander.McpServer.exe`; `--help` produced `System.IO.FileLoadException`; contemporary Code Integrity 3077 events reported DLL blocking |
| 09 | chatgpt-use | **PORTABLE STAGED / EXECUTION BLOCKED** | Windows ZIP extracted; `--help` returned WinError 4551; no logged-in ChatGPT web session accessed |
| 10 | MCP Plugins With ChatGPT Web | **BUILD PASS / NOT CONNECTED** | npm dependencies installed; TypeScript `tsc` build succeeded and `dist/index.js` exists; no browser/ChatGPT account permission set |
| 11 | Browser MCP | **BUILD PASS / EXTENSION STAGED** | pnpm dependencies installed; `pnpm -r build` produced MCP server `dist/index.js` and Chrome MV3 extension; no browser permissions granted |
| 12 | codex-browser-bridge | **PORTABLE STAGED / EXECUTION BLOCKED** | official EXE present; `--help` returned WinError 4551; no browser bridge established |
| 13 | Browser Use | **INSTALLED; CLI HELP PASS** | isolated Python venv has `browser-use.exe`; `--help` exit 0; no billable/browser cloud provider used |
| 14 | chrome-use | **PORTABLE READY; CLI HELP PASS** | official Windows archive extracted, `chrome-use.exe --help` exit 0; no ChatGPT Web session accessed |
| 15 | gptme Desktop | **GUI INSTALLED / REGISTRY VERIFIED** | silent install exit 0; Windows uninstall registration gptme 0.36.0 and app EXE existence verified; no model account connected |
| 16 | ChatGPT Desktop Community | **GUI INSTALLER BLOCKED** | download verified but silent install rejected by Windows Application Control; not installed |
| 17 | Yep Anywhere | **GUI INSTALLED / REGISTRY VERIFIED** | signed installer, exit 0, Windows uninstall registration YepAnywhere 0.10.0 and app EXE verified; no agent connection configured |
| 18 | Web GPT Agent | **GUI INSTALLED / REGISTRY VERIFIED** | silent install exit 0, Windows uninstall registration Web GPT Agent 2.3.1 and EXE verified; no account/session connected |
| 19 | Web GPT Agent extension | **UNPACKED / NOT ENABLED** | browser extension ZIP extracted with manifest; Chrome permissions not granted |

### Result categories (mutually exclusive)

- **3 native GUI applications installed:** gptme, Yep Anywhere, Web GPT Agent (first-run sign-in/functional use not tested).
- **5 tools pass safe CLI-help smoke test:** Playwright MCP, Chrome DevTools MCP, OpenDesk, Browser Use and chrome-use. CLI success is not an end-to-end integration test.
- **2 source tools compiled locally but are not browser/account connected:** MCP Plugins With ChatGPT Web and Browser MCP.
- **2 browser extensions staged but not activated:** Chat On Steroids and Web GPT Agent extensions.
- **6 blocked or runtime-failing executables/installers:** Windows-MCP, Chat On Steroids, Windows Commander MCP, chatgpt-use, codex-browser-bridge, ChatGPT Desktop Community. Windows Code Integrity/App Control events were observed; do not claim these are fully usable.
- **1 source-only app not fully installed:** Backboard Desktop. Full build requires a separately justified Windows toolchain and resource plan, or a verified official Windows binary.

**Controls:** Microsoft Defender real-time protection was observed active, and targeted scans of five GUI installers completed without scan command errors (not a security guarantee). No global App Control rule, UAC, Firewall, Secure Boot, Chrome extension permission or account security setting was relaxed. Installed apps were not given access to private provider accounts or authentication tokens. No 19-tool autostart policy was created.

### Remaining next-action gates, ordered by user value

1. **Prioritize operational same-chat value:** use the already-connected Remote Desktop Commander + **runnable OpenDesk** to attempt a harmless visual screenshot/window pilot, then runnable Playwright CLI for isolated browser workflow. Do not wait for blocked parallel tools; record real I/O and errors.
2. **Blocked tools:** ask owner for separate, narrowly scoped review/authorization to use an OS-approved signed release or per-application code-integrity allow rule, with clear risks and rollback. Do not silently bypass/disable Windows Application Control.
3. **Backboard:** identify a verifiable official Windows installer from the publisher (desktop page: https://bbstudio.io/app/desktop), or plan a resource-bounded Code-OSS source build if official binary cannot be confirmed; cannot claim compiled/install success yet.
4. **Extensions:** request specific owner consent to enable the unpacked extensions in Chrome and review exactly what sites/data they can access. Do not auto-install permission-sensitive extensions.
5. **End-to-end confirmation:** after compatible connection, validate screenshot/click/keyboard, browser DOM/forms, code build/tests, browser DevTools, stop/recovery, all in this existing ChatGPT conversation. Only then consider this overall desktop control capability OPERATIONAL/DONE.

**This section is the verified latest state.** Older sections above describe the earlier proposal/registration state and are historical for those statements. No additional parallel GitHub installation tracker was created.


---

## K. Safe real-I/O smoke tests after installation — 2026-11-14

**Scope:** user-authorized installation smoke checks using existing Remote Desktop Commander to execute small local scripts. No authenticated website, password, cookies, paid provider, browser extension permission or persistent agent configuration was used.

- **Browser actual I/O: PASS.** Playwright Core from the installed Microsoft Playwright MCP dependency launched installed Microsoft Edge in a temporary headless browser session, opened a self-contained local `data:` test page, clicked a harmless button, confirmed the rendered text changed to `clicked`, captured a screenshot in memory and shut down cleanly. Script exit code 0. No external web request or sign-in.
- **Windows screenshot primitive: PASS.** `mss` available in OpenDesk's isolated Python environment acquired an in-memory desktop screenshot, returned only monitor count, dimensions and a short SHA256 digest. Script exit code 0. Screenshot bytes were **not** sent to ChatGPT, persisted to GitHub or saved as a new image.
- **Limitations:** These pilots validate the current chat → existing remote command bridge → local browser/screen primitives → returned result. They do **not** validate direct ChatGPT Custom MCP availability, Windows-MCP execution (still Code Integrity blocked), OpenDesk's own MCP protocol, keyboard/mouse events on a real desktop window, user login, or any app's subscription/quota compatibility.
- **Local evidence:** `Desktop\DJMRN-ChatGPT-Downloads\validate-browser.cjs` and `validate-screen.py` contain the test source; stdout returned `PLAYWRIGHT_REAL_IO result=clicked` and `OPENDESK_SCREENSHOT_CAPTURE_PASS` with zero exit codes. Only non-sensitive proof is recorded here.

**Resume:** choose OpenDesk's operational computer-use interface and an approved local bridge path for a visible app click test (S1), then use Playwright to validate a browser automation end-to-end from this chat (S2). Do not modify Windows Application Control or add sensitive browser permissions without separately scoped proposal and owner approval.


---

## L. Local Codex/MCP fallback and isolated browser permissions — 2026-11-14

**Goal / owner authorization:** Prepare independent **ChatGPT Desktop/Codex LOCAL** access to existing authorized Windows/browser tools, in case connected Remote Desktop Commander remote-tool quota is exhausted; grant the browser agent extensions enough permissions in separate operational browser profiles. User explicitly requested installation/connection/permissions; **no service billing or public exposure authorized**.

### VERIFIED completed on DJMRN-LAPTOP

- Read-only check of the installed Codex environment showed an existing `~/.codex/config.toml` with native `node_repl`, `cua_repl`, `uivision` and bundled computer-use/browser plugin entries. Preserved existing configuration; made a local, SHA256-verified backup before modification. No authentication values were printed or committed.
- Using the **official** `codex mcp add ... -- <stdio server>` CLI, **five** local MCP integrations were registered successfully and verified using `codex mcp list --json`: `djmrn_windows_mcp`, `djmrn_opendesk`, `djmrn_windows_commander`, `djmrn_playwright`, `djmrn_chrome_devtools`. All were reported enabled; authentication and model inference were not invoked. Existing Codex MCPs remain configured.
- Created a private **personal local plugin marketplace** `djmrn-local-tools` and packaged plugin `djmrn-desktop-control` v0.1.0, with a compatible Codex local `.codex-plugin/plugin.json` and local stdio `.mcp.json` for Windows-MCP, Windows Commander MCP, Playwright MCP and Chrome DevTools MCP. JSON validation passed; marketplace installed via `codex plugin marketplace add`; plugin installed via `codex plugin add djmrn-desktop-control@djmrn-local-tools --json`, with verified local cache contents. The plugin is local-only, points to software already installed on the owner’s PC, is not shared or published, and has no API credentials.
- Created **three separate one-click agent-browser shortcuts** in Desktop’s `DJMRN ChatGPT Tools/Agent Browsers` subfolder, each launching Microsoft Edge with a unique persistent profile and its respective unpacked Manifest V3 extension: Browser MCP v2.2.3, Chat On Steroids v2.1.53, Web GPT Agent v2.3.1. Shortcut target and extension/profile flags verified. These use the broad tab/debugger/host permissions declared in the extension manifests **only within the dedicated profiles**. No cookies, sessions or saved profiles were copied from ordinary Chrome/Edge, and optional cookie access was not silently granted. Each extension had earlier passed a service-worker activation test in a disposable no-login profile. Do not assume the persistent-profile launcher is authenticated or has permission to modify the user’s normal Chrome session.
- Remote Desktop Commander remains **online** and its account reported **62% remote tool calls left** at check time. This is a snapshot, not a promise of future quota.
- Prior turn verified Windows-MCP, Windows Commander MCP and OpenDesk tool enumeration through a local MCP client; screenshot and Calculator UI Automation `2 + 2 = 4`, plus an isolated Playwright Edge page click and screenshot, were observed. The local alternative means a user-run Codex/Work task on the authorized PC can use local MCP tools **without consuming Remote Desktop Commander as a transport for that task**, subject to user’s existing Codex/Work access and tool-approval policies.

### LIMITATIONS — do not claim fixed

- **This existing ordinary mobile/remote ChatGPT conversation does not automatically acquire these locally registered tools.** OpenAI’s plugin docs say local stdio MCP plugins run in supported **ChatGPT Desktop local tasks**, not in web/mobile chats. Full custom remote MCP modify/write access currently has plan and workspace entitlement requirements; a Windows stdio server or Chrome Web extension does not bypass them.
- OpenAI’s documented **local Work sync** may let eligible, enabled workspaces continue a newly started desktop-local Work task on mobile. Its rollout/workspace entitlement and current account settings are **UNVERIFIED**; old chats and Codex tasks are not automatically converted. Thus, **independent same-thread mobile control when Commander quota reaches zero remains UNVERIFIED / NOT IMPLEMENTED**.
- The Plugin Creator entry was surfaced for the user to install/enable directly in ChatGPT. A suggestion does not install it, and no subsequent connection confirmation was observed.
- Local plugin may only appear in supported ChatGPT Desktop plugin surfaces after client reload/restart and selection/installation by the user; Codex CLI plugin installation was verified but **ChatGPT Desktop Work tool invocation was not**.
- Avoid keeping all 5 optional MCP servers running at once on the 8 GB laptop; register tools for on-demand use. Do not expose an unauthenticated Windows-MCP or Windows Commander endpoint to the internet, share screenshots/credentials, relax security globally, or initiate paid API calls. Existing ability to start local tools is distinct from permission to send messages, spend money, publish code or change account settings.

### Next concrete tests

1. On the local ChatGPT Desktop app, open Plugins and check whether the personal source `DJMRN Local Tools` and `djmrn-desktop-control` are selectable in a fresh local Work/Codex task; run an innocuous read-only `list windows` then a disposable Calculator test and inspect result. Restart client only after checking for running tasks.
2. Evaluate the account’s Work/Cloud local-sync and `Control this PC` pairing status in official UI. If unavailable, use **Codex local** as the independent execution path, not a falsely promised Android same-thread connector.
3. For authenticated browsing, choose an agent-specific Edge profile and explicitly sign in only where needed, reviewing extension permissions and third-party terms first. Never copy existing Chrome cookies/session data automatically.
4. Evaluate a vetted hosted/secure tunnel only if account entitlements actually allow remote **write** tools and free limits are verified; otherwise STOP rather than build a risky exposed bridge.
5. After end-to-end local Work/Codex validation, mark the status **OPERATIONAL**; until then this is **Codex-configured and locally smoke-tested; native ChatGPT Desktop integration awaits validation**.

**Official references:** [OpenAI Plugins](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt); [Connecting custom MCP](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt); [Local Work sync](https://help.openai.com/en/articles/20001548-agent-security-and-local-work-sync-in-chatgpt); [Package local plugins](https://developers.openai.com/plugins/build/plugins); [Codex MCP](https://developers.openai.com/learn/docs-mcp).


---

## M. Private DJMRN ChatGPT plugin and tested independent local execution packaging — 2026-11-14

**Objective and authority:** Owner explicitly authorized broad browser extension permissions and establishing a direct local ChatGPT Desktop/Codex integration before the Remote Desktop Commander quota ends. This section is an updated implementation/verification record, not a claim of browser/mobile same-thread access.

### Private plugin registered in ChatGPT

- OpenAI **Plugin Creator** was connected in this conversation and successfully created a **PRIVATE, USER-scoped** plugin `djmrn-windows-local` **v0.1.0**, using the portable `plugin.json` + `mcp.json` local STDIO format. This differs from the earlier `djmrn-desktop-control` local Codex plugin and is a separately selected candidate, **not** an additional remote authority.
- Bundle defines four on-demand local MCP backends: `djmrn_windows_commander`, `djmrn_opendesk`, `djmrn_windows_mcp`, `djmrn_playwright`. The bundled Node.js `server/launch.mjs` only launches the known locally installed executable from the owner desktop and pipes stdio; **no public listener, secret or paid model required**.
- Private plugin creation success is verified by the Plugin Creator release/metadata response. **It has NOT been proven installed/selected inside the user's ChatGPT Desktop local Work conversation**, nor in this mobile/web thread. The user must select the plugin and run a fresh local Work tool call where supported; some plans and local-host policies can block full write tools. Do not mark direct remote ChatGPT connection DONE.

### Installed local plugin and Codex compatibility

- The same plugin source was placed at `~/.agents/plugins/plugins/djmrn-windows-local/`; the personal marketplace manifest `~/.agents/plugins/marketplace.json` now has `djmrn-local-marketplace` entry and was written as UTF-8 **without BOM** after an initial malformed BOM was detected and corrected.
- `codex plugin add djmrn-windows-local@djmrn-local-marketplace --json` returned successful installation; cached at `~/.codex/plugins/cache/djmrn-local-marketplace/djmrn-windows-local/0.1.0/`. Node launcher syntax check exited 0.
- Independent local `server/launch.mjs` + MCP initialization/list-tools smoke tests passed for **Windows Commander (57 tools)**, **OpenDesk (22)**, and **Windows-MCP (21)**. Prior Playwright isolated browser click/screenshot test had passed; bundled Playwright launcher remains configured but a separate plugin-hosted Playwright call was not yet run.
- Previous Codex `djmrn-desktop-control@djmrn-local-tools` remains **installed/enabled**, and the older five `djmrn_*` MCP server identities were detected enabled by Codex. No other plugin or Codex configuration was deleted. Running both overlapping sets at once is not advised on the 8 GB laptop. The new local plugin is an alternative; consolidate only after a verified replacement test.

### Owner-authorized browser extension readiness (isolated profiles)

- Created and tested **three persistent, separate Microsoft Edge profiles** under `Desktop/DJMRN-ChatGPT-Downloads/browser-profiles/`: `browser-mcp` v2.2.3, `chat-on-steroids` v2.1.53, `web-gpt-agent` v2.3.1. For each, a real Edge browser started, the Manifest V3 extension background service worker was observed, and the browser exited cleanly.
- Created three named launch-on-demand shortcuts in `Desktop/DJMRN ChatGPT Tools/` for the above profiles. The extension's declared broad site/debugger/tabs permissions apply in its own testing/working profile. These do **not** silently install the extension into the user's personal Chrome profile or copy cookies, passwords or existing sessions.
- Earlier `DJMRN ChatGPT Tools/Agent Browsers/` shortcuts use other isolated profile directories; those were found and preserved. This duplication is **UNRECONCILED** and should be evaluated before scaling/launching both sets. Keep one preferred launcher per integration after an explicit reversible consolidation decision.

### Remote bridge and supported fallback boundary

- The Remote Desktop Commander account reported **62% remote calls remaining at one snapshot**; this may change. The already-connected remote service remains the transport for **this mobile chat**.
- **Documented OpenAI constraints:** local STDIO MCP plugins work in supported ChatGPT Desktop **local** tasks, not automatically in mobile/web threads. Custom **remote** MCP full write support has plan/workspace restrictions, and remote ChatGPT cannot directly call localhost. OpenAI local Work sync is a separate feature requiring workspace/rollout eligibility and applies to **new desktop-created tasks only**; entitlement **UNVERIFIED** for this account.
- Current truly quota-independent fallback: open **ChatGPT Desktop Work** (if eligible and local plugin install succeeds) or **Codex local task** on the Windows computer, where MCP processes launch locally. This is **not** proof that the current mobile chat will continue controlling Windows without the Remote Desktop Commander app.
- No public tunnel, account token extraction, API billing, unknown credit consumption, or browser cookie export was used. Installation and isolated permissions authorized by user do not authorize bypass of platform entitlements or silent consequential external actions.

### Latest NEXT gate

1. In ChatGPT Desktop, verify the new private plugin and/or installed local `djmrn-desktop-control` appears in Plugins for a new **local Work** thread; perform a read-only `list_windows` and an approved test Calc click without calling Remote Desktop Commander. Confirm with observable result and check quota unchanged.
2. Verify whether the current account has an enabled **local Work sync** permission; if absent, mobile continuity remains unavailable. Do not guess.
3. Test `djmrn_playwright` through the installed local plugin and choose a single production browser-extension launcher/profile after reviewing permission scope; avoid keeping three browsers/MCP clients running continuously.
4. After true independent local Work/ChatGPT success, update the architecture authority in Notion and this GitHub test result to `OPERATIONAL` and retire redundant bridges only with separate approval.

**Sources:** [OpenAI desktop-only plugins](https://developers.openai.com/plugins/deploy/desktop-only), [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt), [Custom MCP in ChatGPT](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt), [local Work sync](https://help.openai.com/en/articles/20001548-agent-security-and-local-work-sync-in-chatgpt), [packaging local plugins](https://developers.openai.com/plugins/build/plugins).
