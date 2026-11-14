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

### Follow-up: direct ChatGPT Desktop UI verification (2026-11-14)

- Launched the **official ChatGPT Windows Desktop** app and, via UI Automation, navigated to `Plugins → Installed`. The **private DJMRN Windows Local** plugin was visibly listed as installed in this native app (not only in Codex CLI). Opened its detail page and verified version **0.1.0** and **MCP servers 4** with each server's UI toggle **On**: `Djmrn_opendesk`, `Djmrn_playwright`, `Djmrn_windows_commander`, `Djmrn_windows_mcp`. The detail page describes the owner’s plugin as cloud-hosted metadata; its MCP backends still need the supported local executor and cannot be presumed reachable over the internet.
- `Try now` was invoked from the plugin page and the app returned to a **Codex-mode** chat UI with composer. A local chat-initiated model/tool invocation independent from Remote Desktop Commander **has not been demonstrated**, so overall remote fallback status stays **PENDING**. No model prompt was sent, no external paid usage occurred.
- The local Node plugin launcher (from its installed Codex cached source, invoked through a standalone client) independently initialized/listed tools: Windows Commander **57**, OpenDesk **22**, Windows-MCP **21**. This proves the installed plugin launcher and local STDIO transports work on the PC; it does not prove same existing mobile thread access.
- Three additional dedicated agent Edge profiles and three launch-on-demand shortcuts under `Desktop/DJMRN ChatGPT Tools` were verified with each MV3 extension service worker active. The older `Agent Browsers` folder has separate profile locations and remains available but **overlaps**. No authenticated sessions were copied into either set.
- The Remote Desktop Commander quota snapshot was **62% remaining**, not current guaranteed future availability; the existing remote connection was used only for setup/inspection. An unsupported custom host/tunnel or self-install into this same mobile chat must not be claimed operational.
- **Next acceptance test (user's Windows desktop):** in a *fresh local ChatGPT Desktop/Codex/Work task*, run an innocuous MCP `list_windows` call to `djmrn_windows_commander`, check its displayed tool output, and confirm Remote Desktop Commander call allowance did not decrease during that specific local task. Then verify (not infer) whether local Work sync is enabled for the account and any mobile continuation originates from that eligible desktop Work task.


---

## N. FIRST INDEPENDENT LOCAL CHATGPT DESKTOP WORK MCP SUCCESS — 2026-11-14

**VERIFIED — scope-specific OPERATIONAL achievement:** This section supersedes prior statements in L/M that the native ChatGPT Desktop Work integration was not tested. The owner explicitly authorized preparing a quota-independent local alternative and testing it.

- Using the real signed **ChatGPT Windows Desktop app**, visited `Plugins → Installed → DJMRN Windows Local` and verified the plugin detail page: v0.1.0, four configured MCP servers and **all four toggles On**, with Read/Write capabilities displayed.
- Invoked **Try now**, entered ChatGPT mode with **Work** selected (UI toggle `On`) and selected execution locality **`On your computer — This chat stays on this computer`** rather than Cloud. The composer showed `DJMRN Windows Local` already attached.
- Sent a deliberately read-only Work prompt requesting a **single `djmrn_windows_commander` MCP `list_windows` tool call** with no titles, paths, screenshots, accounts, API usage or personal data returned. The UI displayed tool permission prompt `Allow the djmrn_windows_commander MCP server to run tool "list_windows"?`. The prompt subsequently disappeared; the local Work conversation itself reported the final tool result exactly **`Succeeded. 7 windows returned.`**, confirming real tool execution from **ChatGPT Desktop local Work**. A later UI verification again showed `Succeeded. 7 windows returned.` and the task completed (Worked for 54s). The test was local and did not require the Remote Desktop Commander transport within the Work task; we nevertheless used Remote Desktop Commander remotely to observe/control the Windows UI during setup/testing.
- **Evidence strength:** Direct native GUI inspection + plugin toggles + native Work task's final tool result, not merely CLI `--help` or source build. Tool permission handling is still subject to ChatGPT/Work policy; future commands may ask for approval. No claim of unlimited quota, privileged app control, auto-approval for unsafe actions or mobile/web same-thread native MCP access.

**NOW:** `ChatGPT Desktop local Work -> DJMRN Windows Local plugin -> djmrn_windows_commander -> list_windows` = **PASS / OPERATIONAL for this specific read-only local tool call**. Other three MCP backends separately pass local STDIO initialization (57/22/21 tools), and isolated Playwright is tested; they are not yet all proven called by a native Work agent. The Remote Desktop Commander alternate transport is **not required for future eligible tasks created and run locally on the laptop**, but **the currently open mobile/web conversation** has **no proven automatic bridge or quota-independent remote continuation**; native local Work sync eligibility and mobile continuation remain `UNVERIFIED`.

**Follow-up:** Preserve the original Desktop Commander connection as emergency remote access; use this tested local Work pathway on the laptop. If remote continuity from phone is needed, first verify Work local-sync for this account and test continuing the *new desktop-originated task* from the mobile UI. Avoid tunnels, exposing desktop control ports, authenticating extensions against the user's full private browser, or payment/overage until approval and verification.


---

## O. Codex Remote Android-to-Windows troubleshooting — 2026-11-14

**Diagnostic classification:** Owner reports that previously paired mobile Codex Remote can no longer start/access the desktop. This is the **Codex Remote / Control this PC** feature, not the local plugin itself. The user's exact current mobile error was **not** available to read during this investigation. Therefore mark root-cause identification **PROBABLE, UNVERIFIED** until a mobile-initiated attempt is reproduced.

**Read-only host checks, performed on the authorized PC:**

- Official ChatGPT Desktop host running/responding, Windows app package version `26.1111.2228.0`, network Wi-Fi up, DNS for `chatgpt.com`, `auth.openai.com`, `api.openai.com` succeeded; `https://chatgpt.com` HTTP 200. A generic PowerShell HEAD to `auth.openai.com` returned 403; this is **not evidence** the installed ChatGPT app authentication or Remote WebSocket is blocked.
- Desktop `Settings → Connections → Control this PC`: `Allow connections` **On**, `Keep this PC awake` **On**. An already authorized Android phone was shown in the paired devices list with an exceptionally recent `Last connected` timestamp (~1 minute at capture). **Pairing is not missing**, and a recent relay/control-plane touch happened, but actual task start success is not implied. Do not revoke or re-pair routinely.
- Desktop `Settings → Computer use`: `Toggle Computer Use` **On**, Excel/Word live control toggles On. This setting alone cannot prove the mobile Codex Remote task path is successful.
- The app processes had established TCP sessions (including HTTPS 443), Windows Firewall profiles enabled with no observed custom outbound block, system proxy enabled. The existing Remote Desktop Commander independent bridge was also online. VPN/proxy WebSocket behavior remains an alternate hypothesis, not confirmed.
- Existing two previously approved Codex local project folders (an earlier dated `new-chat` and `DJMRN-Remote-Workspace`) both exist and have exact-case `trust_level="trusted"` entries in `~/.codex/config.toml`. In contrast, multiple newly generated projectless folders under `Documents/Codex/2026-11-14/` — including `new-chat`, `new-chat-2` — have **no explicit trust entry**. This matches a known Android→Windows Codex Remote failure after successful pairing when initiating a **new No project chat**. We did not add a broad trust rule or change account/security permissions.
- Official relevant guidance: [Codex Remote connections](https://learn.chatgpt.com/docs/remote-connections), [Codex mobile](https://learn.chatgpt.com/docs/mobile); independent failure cases: [Windows projectless trust #39855](https://github.com/openai/codex/issues/39855), [case-sensitive Windows trust #40002](https://github.com/openai/codex/issues/40002), [remote message queue stale #41708](https://github.com/openai/codex/issues/41708). These are community bug reports, not proof this specific phone encountered the same error.

**Shortest non-destructive validation sequence:** On mobile open **Codex / Remote** (not an ordinary cloud Work thread), choose the existing paired Windows host and explicitly select the already trusted `DJMRN-Remote-Workspace` instead of `No project`. Start a harmless read-only instruction; if it works, isolate projectless trust as failure. If creating a No-project chat, try **Read only** for a diagnostic rather than assigning trust to every auto-generated folder. If mobile cannot even see the host, inspect account/workspace and mobile UI/version; the host was paired and enabled at this snapshot. If connection still fails with a trusted project, capture the exact Android error and time; investigate proxy/VPN-specific real-time signaling or an OpenAI Remote regression. Do not disable firewall/UAC, reset the whole app, revoke pairing, expose ports or modify trusted paths without more evidence and explicit scoped approval.

**Result:** Windows host/paired device healthy at the control-plane level; **new project trust failure is most plausible demonstrated local configuration gap**, but reproduction from Android is still required. **Not fixed/NOT DONE** for mobile remote use until the remote task actually executes and shows results.


---

## P. Codex Android project picker loading: host registration repaired — 2026-11-14

**New evidence:** User supplied screenshot of ChatGPT Android Codex `Choose Project` menu with only `No project` and a persistent `Loading recent projects...`. The failure occurs **before** a specific project trust check or tool permission gate. Prior projectless trust hypothesis (section O) alone did not explain this UI. The user had not supplied an Android post-fix screenshot yet.

**Host inspection:** In the official Windows ChatGPT Desktop app (26.1111.2228.0), switch to **Codex**: the **Projects sidebar itself showed `No projects`** despite the existing filesystem folder `C:\Users\Mrn7206\Documents\Codex\DJMRN-Remote-Workspace` and older `trust_level="trusted"` configuration. Desktop app running/responsive, Windows Control this PC enabled, paired Android device present, recent connection observed, Wi-Fi/DNS/HTTPS reachable. Read-only `codex doctor --network-only --summary --ascii` returned **4 ok / 0 warn / 0 fail**, including **Responses WebSocket HTTP 101**, so general network/socket connectivity is healthy. One `Refresh` UI action on the paired devices page was briefly disabled; no pairing/reset action performed.

**Local non-destructive correction performed:** Through native Codex Desktop UI `Projects → Add new project`, entered display name **DJMRN Remote Workspace**; selected the **preexisting** exact folder `C:\Users\Mrn7206\Documents\Codex\DJMRN-Remote-Workspace` using the native Windows `Select Project Root` folder picker; confirmed source folder before pressing **Create project**. Native UI then replaced `No projects` with `DJMRN Remote Workspace` and showed `Start new chat in DJMRN Remote Workspace`, proving local project registration is restored. **The original folder and its file content were not changed.** No Codex model task was submitted or credits spent to register the project.

**Status:** **HOST_PROJECT_REGISTRATION_REPAIRED / ANDROID_REMOTE_SYNC_UNVERIFIED**. Mobile Codex may need refreshing/reopening (not reinstalling or revoking device) to reload project list; actual Android list update needs a user screenshot or a mobile-initiated task result. If phone still shows perpetual spinner despite now-populated desktop projects, the remaining fault is likely **Android project-list cache, app-server remote synchronization, or service bug** rather than missing local folder, and must be diagnosed from phone version/connection state and narrow remote diagnostics. Do not assign blanket trust to all newly generated paths, disable Firewall/Defender, delete mobile storage or re-pair the phone without evidence.

**External issue evidence (not proof of exact user bug):** Official Codex issue [Windows/Android Remote picker stale #44582](https://github.com/openai/codex/issues/44582); official [Remote connections](https://learn.chatgpt.com/docs/remote-connections) and [Codex on mobile](https://learn.chatgpt.com/docs/mobile).


---

## Q. Browser-open remote bridge research and Commander quota fallback — 2026-11-14

**User goal:** With Chrome/Edge on the laptop and ChatGPT web page open, find a free-first method for **this existing mobile ChatGPT conversation** to use local Windows tools without consuming Remote Desktop Commander. Also reassess already installed 19 artifacts versus a real remote endpoint. **Research/proposal only, no new provider, tunnel, remote server, security permission, or billable service activated.**

### Verified snapshot

- Remote Desktop Commander `who_am_i` live reported **remote_calls_left_pct = 60** (40% consumed). `DJMRN-LAPTOP` **Online**, agent version `0.3.2`. Service exposes a percentage, **not** an exact count of calls. Source: connected Remote Desktop Commander account API, same conversation.
- Existing chat context: ChatGPT Desktop Work `On your computer` used the private `DJMRN Windows Local` plugin to complete `djmrn_windows_commander.list_windows` with result `Succeeded. 7 windows returned.` This is independent **local task execution**, not proof of mobile/browser same-thread remote access. Codex Remote Android project picker still failed to load projects after host project registration; remain UNVERIFIED.
- Actual connected Browser plugin call from **this mobile chat** failed with `Browser access requires the originating browser context. Open ChatGPT in the browser with the connected extension and try again.` Therefore ChatGPT's browser-tab reader **does not** currently see the PC's browser tabs from this thread. Browser must be origin-connected.

### Candidate transports and boundaries

| Mechanism / evidence | Existing installed desktop tools reused | Same-mobile-chat path | Cost/availability gate | Assessment |
|---|---|---|---|---|
| Official ChatGPT Chrome/Edge extension + ChatGPT web / Desktop | Existing browser/profile/Chrome tabs | **Not automatically**: browser control requires correct originating browser session and account permissions; does not expose whole Windows desktop | Existing subscription permissions, no new provider budget evidenced | Strong **local-origin browser** route, NOT replacement for mobile-to-Windows full-device bridge |
| ChatGPT Desktop local Work + `DJMRN Windows Local` | Windows Commander/OpenDesk/Windows-MCP/Playwright | **Local on PC tested**; mobile continuation via *new* locally-originated Work tasks requires optional Local Work Sync rollout and workspace permissions. The old current mobile chat does not migrate. | Local Work Sync eligibility UNVERIFIED | Best **already-working fallback** when operating ChatGPT on PC |
| OpenAI Secure MCP Tunnel (`openai/tunnel-client`, official) | Any compatible existing local stdio MCP, with scoped permission proxy | **Architecturally correct**: OpenAI-hosted authenticated outbound HTTPS tunnel connects private host to ChatGPT custom remote MCP | Requires Platform `tunnel_id`, runtime API key and org/workspace Tunnels roles; **pricing/overage and account remote write entitlement UNKNOWN => DENY deployment** | Best candidate for **genuine remote MCP**, not yet available/installed; no inbound port necessary |
| `Mirochill/browser-pilot` (GitHub Cloudflare Worker + Chrome MV3 extension + OAuth) | Chrome tabs only; not the installed local Windows Commander | Potential web remote browser MCP, **author explicitly says mobile ChatGPT not validated** | Cloudflare Workers + KV + SQLite Durable Objects have a limited Free tier, but ChatGPT custom MCP write permissions remain workspace-gated; highly young project, 1 commit/0 stars at inspection | Research alternative only, not an established Windows desktop replacement |
| `Officially-aditya/browserControl` (remote HTTPS/OAuth + extension WSS) | Existing Chrome browser session only | Remote browser MCP in architecture; cannot control full Windows/apps | Relay/free usage and security review unverified | Alternative to Browser Pilot with the same remote MCP entitlement boundary |
| `Draivix/chatgpt-gateway` or `DrA1ex/chatgpt-bridge` (logged-in chatgpt.com tab automation) | Uses signed-in ChatGPT browser tab as an unofficial message client | Exposes/automates **ChatGPT UI or messages**, does NOT register OS tools in this remote thread or act as authenticated remote MCP | Reliability, terms, security and account/session risk unverified | **Do not treat as a quota-free same-chat desktop control solution** |
| Other 19 local executables/GUI agents (`OpenDesk`, Windows-MCP, Windows Commander, Browser MCP, Playwright, codex-browser-bridge, Chat On Steroids, Backboard, gptme, etc.) | Locally installed/tested | No standalone internet relay from a mobile ChatGPT thread unless paired with **separate supported transport and entitlement** | No external model/provider billing assumed | Local execution layer only, **not** 19 alternative remote conduits |

**Official sources:**
- https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app
- https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt (full custom web MCP currently Business/Enterprise/Edu; plan/workspace-specific gating)
- https://help.openai.com/en/articles/20001548-agent-security-and-local-work-sync-in-chatgpt (new desktop-originated local Work tasks; member/workspace rollout)
- https://developers.openai.com/api/docs/guides/secure-mcp-tunnels
- https://github.com/openai/tunnel-client/releases (Windows build with checksum files; no installation authorized by this research)
- https://github.com/Mirochill/browser-pilot
- https://github.com/Officially-aditya/browserControl
- https://developers.cloudflare.com/workers/platform/pricing/ (Workers free 100,000 requests/day; KV + SQLite Durable Objects free tier within limits)

**Recommendation, not action:** (1) Preserve remaining Commander quota for high-value diagnosis/management. (2) Use verified ChatGPT Desktop local Work/Codex for on-PC Windows and coding tasks. (3) To regain mobile remote access, first check existing account's Local Work Sync access; if unsupported, check **official Secure MCP Tunnel entitlement and zero-overage pricing** before asking authorization to create any Platform credentials, tunnel, or plugin. If not accessible, **STOP for same-chat mobile remote**, rather than deploying a risky unvetted third-party relay or pretending that opening ChatGPT web creates a local tool bridge.

**Current decision:** no new installs, charges or remote listeners; this is a technology/availability discovery. **Status: fallback-local PROVEN; fallback-mobile SAME CHAT UNVERIFIED.**


### 2026-11-14 follow-up: verified permission, quotas, licenses and setup gates

**Research-only.** Inspected current official Secure MCP Tunnel documentation, official GitHub tunnel-client README/releases, direct GitHub source README for `Mirochill/browser-pilot` and `Officially-aditya/browserControl`, Cloudflare Durable Objects Free pricing and OpenAI ChatGPT custom-MCP plan/permission help. No deployment, browser permission change, tunnel, token or charge made.

| Dimension | Official Secure MCP Tunnel | Browser Pilot | browserControl |
|---|---|---|---|
| Scope | Private **Windows MCP**, browser or file tools exposed to supported product | Chrome tabs only, no arbitrary Windows UI/files | Existing Chrome tabs only, no arbitrary Windows UI/files |
| Working transport | Outbound HTTPS `api.openai.com:443` → OpenAI-hosted tunnel → private stdio/HTTP MCP; Platform tunnel ID + runtime API key | Self-host Cloudflare Workers/KV/SQLite Durable Object + GitHub OAuth + MV3 Chrome extension/CDP | Local stdio/loopback OR hosted HTTPS OAuth/WSS relay (author-operated Railway endpoint) + Chrome extension/CDP; selfhosting possible with persistent state and relay secrets |
| Current mobile-chat availability | **UNVERIFIED/BLOCKED by entitlement** for full write MCP on current personal plan; ChatGPT custom MCP connections created on web, not mobile | **NOT VALIDATED** for ChatGPT mobile per project author; ChatGPT custom MCP entitlement remains independent | Remote MCP-compatible agent supported by project, but **not demonstrated inside this existing mobile ChatGPT chat**; entitlement remains |
| Official service/software costs | Client source/release public, no explicit tunnel per-call/free pricing stated in official tunnel doc; Platform key/role required, API usage could bill if Responses API used; **cost UNKNOWN -> DENY** until account billing controls and feature access confirmed | No extra AI API key required for project; Cloudflare Workers Free includes SQLite Durable Objects with hard daily caps. Actual Workers/KV/DO usage and all service permissions require preflight verification | Project README claims MIT but root LICENSE file was not found by GitHub fetch; hosted Relay price/uptime/privacy terms **UNVERIFIED**; self-host hosting/Redis costs unknown |
| Security controls | Workspace + Platform RBAC; outbound-only; bound server permissions; operational health; default 600 MCP req/min, max 10 MiB serialized payload, 120 s request deadline | GitHub OAuth allowlist, 6-character pairing, 2-hour browser session, 30-day device token; global signed-in tabs readable, heuristic sensitive action controls; no desktop/clipboard/file-upload APIs; root LICENSE not found and README has no explicit project license → rights **UNVERIFIED** | OAuth PKCE, per-device relay credentials, pause/tab leases, URLs limited to HTTP(S); hosted relay carries screenshots/browser commands and accesses signed-in pages; security trust and hosted terms need assessment |
| Maturity/test evidence | Official OpenAI repository latest inspected release v0.0.20 (2026-11-06), Windows amd64/arm64 release assets and SHA256SUMS | README version 0.2.3, describes 257 **mostly mocked** checks and limited native Chrome probes; no mobile end-to-end | README documents local and remote real Chrome canaries; source code public, claims MIT; no confirmed mobile ChatGPT test |

**Formal finding:** Secure MCP Tunnel is the strongest **OS-wide bridge architecture**, but not a confirmed viable feature for this ChatGPT mobile plan. As of the reviewed 2026 Help Center article, full custom MCP on ChatGPT web is Business/Enterprise/Edu, Pro supports read/fetch only, and **creating custom MCP connections from mobile is unsupported**. Do not infer that the inability to *create* on mobile proves already-created tools never work in mobile; that specifically remains untested. Tunnel does not expand ChatGPT entitlements.

**Preference:** Continue using already-proven local `DJMRN Windows Local` / Work for PC-side tool operations. If a *supported* ChatGPT workspace/Platform tunnel permission and zero-overage billing become confirmed, prototype official tunnel with a single harmless read-only MCP `list_windows` instead of all 57 filesystem/UI operations. For browser-only fallback, `browserControl` has clearer local/remote architecture and a hosted relay but greater third-party session risk; `Browser Pilot` demands selfhosting setup and has unverified software license. Neither solves Android mobile same-chat privilege bottleneck today.

**Source URLs:**
- https://developers.openai.com/api/docs/guides/secure-mcp-tunnels
- https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt
- https://github.com/openai/tunnel-client/releases
- https://github.com/Mirochill/browser-pilot/blob/main/README.md
- https://github.com/Officially-aditya/browserControl/blob/main/README.md
- https://developers.cloudflare.com/durable-objects/platform/pricing/


---

## R. Chat On Steroids local zero-paid setup — 2026-11-14

**Action approved:** User requested completion of all free/local Chat On Steroids settings after authenticating to ChatGPT in an isolated Edge browser, explicitly excluding any paid settings, API/Platform billing, credit usage or tunnel cost. Execution on the authorized Windows device was done via existing Remote Desktop Commander; no external ChatGPT API calls were made.

**Observed and VERIFIED on PC:**

- **Chat On Steroids v2.1.53** Windows GUI open at `Settings → Setup`, app remains `Not connected` to Core plugin. Existing isolated Edge profile `Desktop/DJMRN-ChatGPT-Downloads/browser-profiles/chat-on-steroids` loaded the v2.1.53 MV3 extension; ChatGPT authenticated under the owner's account in this dedicated profile. Setup advanced to Step 2/7 after pairing.
- Selected exactly the preexisting, empty local `C:\Users\Mrn7206\Documents\Codex\DJMRN-Remote-Workspace` folder in the OS picker. CoS registered share identity `/djmrn-remote-workspace` and `Settings → Workspace` confirmed exactly **one shared folder** and matching Windows absolute path. No user files were copied; the preexisting directory was empty and no `.git` repo existed.
- Access wizard `Full access` was already selected; all four categories `Look at files`, `Change files`, `Browser and desktop control`, `Run programs` were On. `Sub-agent tools` was On. This is a capability scope *within the authorized CoS app*, **not yet a successful tool call from ChatGPT**. `Save a checkpoint before each turn's first edit` changed **Off → On**; snapshots are temporary and are not a substitute for backup/testing.
- CoS `Settings → Agents & automation → Browser & history`: reports **`browser extension 2.1.53 connected and provisioned`** and **`browser wake channel (browser) authenticated`**, plus `Disconnect browser` button. Model discovery initially timed out; a single Refresh resulted in **`Available in your ChatGPT account — checked [local time]`**, i.e. free browser UI-based model discovery passed. No model/API inference was initiated.
- Corrected dangerous inherited browser-tool authorizations: `Allow unattributed calls` **On → Off**; `Trust only selected chats` **Off → On**. This avoids using full Windows tools from unidentified/untrusted chats. New CoS chats will need individual trust before desktop tool actions. Do not switch these back for ease.
- Low-RAM/no-unrequested-usage controls: `Automatically recover unfinished answers` On→Off; `Background chats` On→Off; `Open tabs only when asked` Off→On; `End background processes of workers asleep for more than 30 minutes` Off→On. `Browser bridge port` left at Auto, `Local control API` Off and `Allow actions` Off, no broad local HTTP listener, auto-start unconfigured. This 8 GB laptop had <1 GB free at some snapshots, so avoid unattended multi-agent runs.
- Inspected `Settings → Setup → Tunnel` and expanded optional Desktop control. **Core and Desktop are separate ChatGPT MCP plugins/tunnels**; Desktop asks for a second tunnel ID. **No OpenAI Platform tunnel, no restricted API key, no custom remote ChatGPT MCP plugin, no paid provider, no Cloudflare relay was created or activated.** Tunnel and API key stages intentionally STOPPED, as price/entitlement unknown under Free First.
- The program was left on **Setup → Tunnel** with banner **`Not connected`**. It must NOT be described as a functional replacement for Remote Desktop Commander from this existing mobile ChatGPT chat. Local browser pairing/permission setup is completed; remote Core/desktop MCP transport is not.

**Security/authority:** User directly completed OAuth/sign-in; no passwords, OTPs, cookies, session tokens, API keys or screenshots containing them were saved to GitHub/Notion. The extension can observe/automate ChatGPT page content locally according to the developer's own responsible-use notice, and this browser interface is not an official public API. Keep it in the dedicated Edge profile and only use user-trusted chats.

**Future gate:** Verify user has supported custom ChatGPT MCP entitlements, official Platform tunnel access and clear zero-overage pricing before proposing a read-only Core tunnel test. Never create Platform credentials or connect by bypassing plan/workspace capabilities. Do not enable extra desktop tunnel as a shortcut. Existing ChatGPT Desktop local Work and Windows Commander MCP remain the proven zero-additional-provider execution path.

**Upstream reference:** https://github.com/totec448-spec/chat-on-steroids/blob/main/docs/setup.md and https://github.com/totec448-spec/chat-on-steroids/blob/main/README.md.


### CoS follow-up: Plus web custom MCP UI and free Cloudflare transport preflight — 2026-11-14

**Owner directive:** Continue Chat On Steroids *in ordinary ChatGPT*, with no paid/provider-billing steps. This is a continuation of section R; do not confuse with local ChatGPT Desktop Work/Codex.

- Through the owner's **already signed-in, isolated Edge ChatGPT web** session, navigated to `Plugins → Add → Add custom MCP server` via UI Automation. The menu item was **enabled** and the modal opened. It offers `Server URL` and `Tunnel` connection choices; selecting `Tunnel` exposes an editable `Tunnel ID` input. `Create as a plugin` was **disabled** with no valid server ID or URL. This is **direct UI evidence on Plus** that the add-MCP form is visible, **not** evidence that write/action tools or tunneled custom MCP are authorized for the plan or accepted for remote access. Official Help Center still describes full MCP write beta as Business/Enterprise/Edu; avoid overclaiming.
- CoS `Open Tunnels` opens OpenAI Platform in Google Chrome. The Platform page showed **`Sign up or login with an OpenAI account`**, i.e. **not signed in to Platform in that browser**. No account sign-in, Platform tunnel, project, API key, payment method, billing action, or paid model execution was performed.
- Local package audit showed CoS 2.1.53 includes `resources/tunnel/tunnel-client.exe` (CLI `--version` = `0.0.20+c2144...`, exit 0) and `cloudflared.exe` (CLI `--version` = `2026.10.2`, exit 0). Both were checked by SHA256 locally but Windows Authenticode was `NotSigned`; this does not verify publisher signatures or the remote platform service itself. The executables were **NOT** started as remotely reachable tunnels.
- Per official [CoS setup](https://github.com/totec448-spec/chat-on-steroids/blob/main/docs/setup.md), `Tunnel → API key → Connect → ChatGPT` require either (a) OpenAI Secure MCP Tunnel with Platform tunnel ID and Restricted API key, or (b) custom HTTPS/Cloudflare quick tunnel and a matching ChatGPT custom MCP plugin. Official [Cloudflare Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/) confirms **free, no-account**, ephemeral `*.trycloudflare.com` endpoints. Such URLs are publicly reachable by anyone who knows them, and Cloudflare's optional email OTP protection **requires an interactive browser** and therefore cannot authenticate typical noninteractive MCP requests. CoS uses a secret path but that is still internet publication of a Windows control surface.
- **Safe completion limit:** existing CoS browser wake authenticated, a single shared workspace folder, safety settings and checkpoints from R remain; `Not connected` Core MCP is still displayed. No external tunnel was launched because owner consent to free-only settings does not on its own authorize publication of full Windows control through a public URL, and the platform authorization for normal-chat tool execution is not demonstrated. Need a **scoped external exposure approval** and verified custom MCP entitlement (or stop). No bypass of plan permissions, hidden API billing, or migration to Work/Codex.

**Next acceptance test if explicitly approved:** test a **read-only single tool** (e.g. harmless status/list-windows output only) with a temporary separately restricted sandbox endpoint, observe a genuine call from ordinary ChatGPT web, and immediately stop/revoke tunnel afterward. Do not expose the current Full-access CoS/real browser sessions as first test. If ChatGPT write-capable MCP is blocked, do not expand the tunnel or switch identities to circumvent entitlement.

**Status:** LOCAL_BROWSING_PAIRED / WEB_CUSTOM_MCP_FORM_VISIBLE / TUNNEL_UNACTIVATED / MOBILE-SAME-CHAT_REMOTE_CONTROL_UNVERIFIED.


---

## S. Cloudflare Quick Tunnel no-account MCP pilot and cleanup — 2026-11-14

**User authorization:** explicitly approved temporary free Cloudflare Quick Tunnel pilot; asked if a separate email can be used instead of two older potentially insecure Cloudflare/VPN-related email accounts. **Official Cloudflare Quick Tunnel requires NO account, email, domain, payment card, or API key.** Existing accounts were not touched. User restricted paid actions; none performed.

**Server created and locally verified:** A separate isolated Python MCP v2.3.0 Streamable HTTP server (`Desktop/DJMRN-ChatGPT-Downloads/cos-readonly-tunnel-probe.py`) was bound **only to 127.0.0.1:18677**, `json_response=True`, `stateless_http=True`, max request body 65536, eight max sessions, DNS rebinding protection enabled, known exact allowed hosts and ChatGPT allowed Origins. It exposed **exactly one harmless static tool** `djmrn_connection_probe`, returning a fixed success message; absolutely no file, process, shell, desktop, browser, account or credential access. `initialize`, `tools/list`, and `tools/call` all returned local HTTP 200 with expected JSON-RPC bodies. No Chat On Steroids Full-access endpoint was exposed.

**Free Cloudflare Quick Tunnel test:** Used already bundled `Chat On Steroids/resources/tunnel/cloudflared.exe` 2026.10.2 with command equivalent to `cloudflared tunnel --url http://127.0.0.1:18677 --no-autoupdate`. Cloudflare issued an ephemeral `*.trycloudflare.com` URL. The first tunnel defaulted to QUIC and all UDP/QUIC egress prechecks failed with timeouts, public HTTP 530. Restarted with `--protocol http2`, Cloudflare HTTP2 outbound edge registered a tunnel connection, but an external MCP POST returned HTTP **502 Bad Gateway** and a later GET 530. Logs recorded repeated `Error shutting down control stream: client disconnected`, despite a healthy local MCP server. Proxy and bypass-proxy curl tests both returned HTTP 530. Thus this network cannot presently deliver a stable quick-tunnel connection; **NO successful public MCP handshake**.

**Protocol-debug lesson:** MCP Python 2 DNS rebinding protection uses **exact hostname allowlists**; the attempted `*.trycloudflare.com` wildcard returned HTTP 421 `Misdirected Request` in a direct Host-header simulation. Updated the isolated server's `allowed_hosts` to the **specific temporary trycloudflare.com hostname** (with and without port wildcard), then locally reproduced HTTP 200 under the simulated public Host. This eliminated an independent protocol-level configuration error; external 502/530 remained a distinct Cloudflare edge connectivity failure. Do not disable DNS rebinding protection globally, and do not assume broad subdomain wildcard is supported.

**Cleanup verified:** Stopped the pilot `cloudflared.exe` PID 8948 and test MCP `python.exe` PID 8832 after verifying each executable's identity and command-line target. `Get-NetTCPConnection -LocalPort 18677 -State Listen` returned **0 listeners**, and a process query returned **0 pilot processes**. Both ephemeral public URLs consequently expire. No public listener, full-access service, or paid setup remains. Test scripts and logs exist locally for future diagnosis; they contain no user credentials and should not be committed publicly.

**Current status:** `LOCAL_MCP_TEST=PASS`; `PUBLIC_CLOUDFLARE_QUICK_TUNNEL=FAIL(network 502/530)`; `NORMAL_CHATGPT_CHAT_TOOL=NOT_CONNECTED`; `ACCOUNT_EMAIL_OR_BILLING_CHANGE=NONE`; `PUBLIC_EXPOSURE=CLOSED`. No ChatGPT custom MCP plugin was created because the publicly reachable endpoint was not stable. The installed private `DJMRN Windows Local` plugin and already verified on-PC Work path remain unaffected.

**Official references:** https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/ ; https://py.sdk.modelcontextprotocol.io/troubleshooting/ ; https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt. If another network/VPN route is tested, use the same read-only server first; a successful tunnel alone does not prove Plus mobile custom MCP permissions or native write-tool access.


---

## T. Cloudflare after Windows firewall prompt permission — second isolated retest

**Trigger:** User reported granting Windows a network access permission prompt for Cloudflared and explicitly requested a free tunnel retest. Changes to firewall were **not** made by the assistant. Scope remained the previously approved *read-only, single-static-tool* internet test.

**Read-only Windows verification:** Existing Windows Defender Firewall rule list now showed two enabled **Inbound Allow** rules named `cloudflared.exe`; all Windows firewall profiles remain enabled. Note that Cloudflare Quick Tunnel is **outbound-initiated**, so merely granting inbound allowance does not guarantee working edge connectivity.

**Retest procedure:** Reused the existing isolated `cos-readonly-tunnel-probe.py` via its Python MCP v2 environment. Bound only `127.0.0.1:18677`; verified local JSON-RPC `tools/list` HTTP 200 and **exactly one** capability `djmrn_connection_probe`, whose result is constant and cannot read/write Windows, browser, files, credentials or processes. Reused CoS-bundled `cloudflared.exe` with temporary no-account Quick Tunnel, `--protocol http2`, `--http-host-header 127.0.0.1:18677`, `--no-autoupdate`, and an ephemeral generated `trycloudflare.com` hostname. No DNS rebinding protection was disabled, no credentials or third-party account added, and no paid provider activated.

**Observed outcome:** The HTTP2 edge transport registered successfully (`protocol=http2`, Cloudflare fra03); the network precheck reported `hard_fail=false`. Nonetheless public POST requests to the temporary `/mcp` endpoint did **NOT** yield usable MCP JSON-RPC responses: one connection-level failure (no HTTP status), then Cloudflare HTTP **502**, then HTTP **530**. Cloudflared log at 2026-11-14T02:00:23Z: `failed to serve incoming request ... Error shutting down control stream: context canceled`, followed by edge reconnect attempts. Thus `LOCAL_MCP_PASS / CLOUD_EDGE_CONNECTED_INTERMITTENTLY / PUBLIC_MCP_FAIL`. Inbound Windows rule was not the sole original blocker.

**Cleanup and residuals:** Inline PowerShell `try/finally` stopped only the two known pilot child processes after identity verification. Confirmed zero listeners on TCP 18677 and no leftover pilot cloudflared or Python processes. No full-access Chat On Steroids service was published; its login and scoped workspace were not changed. A `.ps1` file attempt was blocked by existing Windows PowerShell ExecutionPolicy, which was **not** modified; the same legitimate console commands were run directly and completed. Retest local logs remain in `Desktop/DJMRN-ChatGPT-Downloads/` for debugging; no secrets or public hostname committed.

**Next decision:** Do not retry by weakening Windows Firewall, disabling security policy or exposing the full Windows controller. If further remote access is needed, test only this same isolated read-only MCP probe on a **different reliable VPN/network route** or evaluate an approved official tunnel. It is still not proven that ordinary mobile ChatGPT Plus can invoke a custom remote MCP tool; first obtain reliable remote transport. User-facing conclusion: permission alone did not fix the 502/530 problem; remote fallback remains **NOT OPERATIONAL**.


---

## U. Browser-only CoS route examined on live Windows UI — no remote MCP bypass

**User asked:** Return to browser settings to avoid tunnel / API / Cloudflare / alternative remote-relay steps while retaining goal of same ordinary ChatGPT mobile thread directly calling Windows tools.

**Live GUI evidence (2026-11-14):** On the connected Windows laptop, `Chat On Steroids → Settings → Setup → Browser` displayed `Signed in. ChatGPT is connected.` and the two choices `In Chat On Steroids — Use the app's built-in browser` and `In your browser — Use Edge and your existing profile`. The browser extension remains paired; these choices affect **where ordinary ChatGPT chat renders / interacts with the browser**, not network access from OpenAI's remote MCP tool execution to local Windows.

`Settings → Setup → Tunnel → Advanced → METHOD` ComboBox was directly expanded using Windows UI Automation and returned exactly: `OpenAI Secure MCP Tunnel (recommended)`, `Cloudflare quick tunnel`, `Local only - I run my own tunnel`. The third mode explicitly presupposes a separately supplied external tunnel; it is **not** a standalone browser-only bridge usable from ChatGPT mobile. The CoS UI still reads `Not connected` for Core. The developer's official setup documentation mandates completing `Tunnel → API key → Connect → ChatGPT`, then registering the Core plugin before full Windows/file/terminal tools can be invoked.

**Finding:** The installed browser extension can support ChatGPT UI communication / login locally but there is **no documented or observed browser-only configuration** that makes this same mobile ChatGPT chat call local desktop MCP without a reachable registered MCP transport or other supported remote bridge. Using `In Chat On Steroids` built-in browser instead of Edge does not remove that gate. Do not misrepresent a paired browser session as an operating remote control connection, and do not attempt unsafe scraping/DOM automation to bypass ChatGPT platform MCP permissions.

**Action/side effects:** Read-only inspection of live GUI / expansion of dropdown; METHOD preserved unchanged on `OpenAI Secure MCP Tunnel`. Browser step left showing successful account login. No new tunnel, public port, key, app/plugin, API charges, or chat turn was initiated.

**Source:** https://github.com/totec448-spec/chat-on-steroids/blob/main/docs/setup.md . Same-mobile-thread access remains through the already connected Remote Desktop Commander while quota is available; alternate local Work can use independently tested plugins on the PC but it is not the user-requested mobile ordinary chat route.


---

## V. User-requested installed-tool connectivity audit — live 2026-11-14

**Question:** Are all software/extension artifacts originally downloaded to give ChatGPT more Windows/browser/coding capabilities fully connected, usable from this *existing ordinary mobile chat*, and performing the originally recorded roles?

**Direct live read-only inspection:** Read authoritative Notion DJMRN Operating Memory and Tool Governance, original 19-tool discovery report, this execution plan, current Windows Desktop shortcuts, registry, process list, CLI validation CSV, Codex MCP list, isolated extension shortcut paths/manifests, Browser and plugin endpoint availability. No new installs, tool permissions, secrets, model calls, Work tasks, external tunnels or bills.

### Numbering and current states

- The parent catalog contains **19 distinct researched services**, including pre-existing Remote Desktop Commander and cloud-only TinyFish. The separate user-authorized **19 downloaded artifacts** are *not* identical to that parent list; the artifact set includes three browser extensions and source/CLI packages. There are **19 numbered Windows desktop shortcuts** plus **3 isolated-Edge browser shortcuts**, i.e. **22 present .lnk** files, **all with target paths existing**. Shortcut presence is not a functional test.
- Windows Installed Applications registry currently confirms **6 native GUI installs**: Backboard Studio 3.1.27, Chat On Steroids 2.1.53, gptme 0.36.0, ChatGPT Desktop Community 0.2.1, YepAnywhere 0.10.0, Web GPT Agent 2.3.1. They were not running in this audit and were not loaded together (8 GB RAM). The previous `README-STATUS.txt` correctly records later installation superseding earlier Section J Code Integrity blocks, but its "extensions not active" line is historical: all 3 isolated Edge profiles/shortcuts were subsequently provisioned and smoke-tested; **currently all isolated browser profiles had zero Edge processes**.
- Existing local code and CLI artifacts remain present: Windows-MCP 0.8.9, Playwright MCP 0.0.85, Chrome DevTools MCP 1.13.0, OpenDesk 0.3.0, Windows Commander MCP 0.1.1, chatgpt-use 0.0.12, built MCP Plugins ChatGPT Web, built Browser MCP plus extension 2.2.3, codex-browser-bridge 2.0.0, Browser Use 1.0.4 and chrome-use 1.5.291. Historic CLI-VALIDATION.csv lists nine safe `--help` or timeout checks; historical metadata is NOT proof of new live sessions. Current desktop link target existence checked for each.
- Isolated Edge shortcut `--user-data-dir` and `--load-extension` arguments and unpacked manifest versions verified directly: Browser MCP 2.2.3 (7 declared permissions), Chat On Steroids 2.1.53 (6), Web GPT Agent 2.3.1 (5). No isolated agent browser running during audit. CoS owner previously authenticated ChatGPT inside isolated Edge and paired the extension; CoS GUI was closed at owner's explicit request and its Core status remained `Not connected` because no working tunnel/plugin was registered. Browser MCP and Web GPT Agent do not have a verified authenticated end-to-end normal-chat session.
- Current Windows Codex CLI `codex mcp list --json` returned 13 entries: **five named DJMRN stdio MCP servers enabled** (`djmrn_windows_mcp`, `djmrn_opendesk`, `djmrn_windows_commander`, `djmrn_playwright`, `djmrn_chrome_devtools`); additional `browser`, `cua_repl`, `devtools`, `node_repl`, `uivision`, `wincommander`, `windows` enabled, and `codex_app` disabled. This proves configured/active toggle, **not proof that each backend can run every tool or is exposed to this mobile conversation**.
- Prior *same-day real I/O* verified local MCP enumeration: Windows-MCP **21** tools plus screenshot, Windows Commander **57** tools plus Calculator UIA `2+2=4`, OpenDesk **22** tools plus desktop capture primitive; Playwright separate Edge page click/screenshot pass. Chrome DevTools MCP only CLI/help checked, no real Chrome DevTools debugging acceptance test. Backboard/gptme/ChatGPT Desktop Community/Yep Anywhere/Web GPT Agent/chatgpt-use/chrome-use/codex-browser-bridge/Browser Use/MCP Plugins ChatGPT Web/Browser MCP have no demonstrated standalone remote link into this ordinary mobile chat.
- Prior native *ChatGPT Desktop local Work* real execution of private `DJMRN Windows Local` plugin called `djmrn_windows_commander.list_windows` and returned **`Succeeded. 7 windows returned.`** The plugin has four locally enabled MCP toggles in native Desktop; this is a **supported local Work task**, not the user's requested same-mobile-thread independent Windows tool bridge, nor a guarantee all MCP endpoints were used inside Work.
- **Current-chat connector evidence:** `mcp__Browser__list_tabs({})` **rejected** with `Browser access requires the originating browser context. Open ChatGPT in the browser with the connected extension and try again.` `Plugin_Management.get_app_permissions({app_id:"DJMRN Windows Local"})` returned **`not_installed` for the current ChatGPT plugin context**, despite separately proven Desktop Work local installation. There is **no callable `DJMRN Windows Local` / local Windows-MCP namespace** in tools available to this mobile chat. The direct, operating ordinary-chat host-to-Windows route remains Remote Desktop Commander.
- Desktop Commander agent 0.3.2 **Online** on authorized laptop; current read-only quota check `remote_calls_left_pct=59` (59% left; exact call count not returned), and direct `start_process` executed real PowerShell audits. TinyFish app tools are technically available in this chat but they control **provider cloud browser**, not local authenticated Windows/Chrome; usage prices/credits for charged operations not pre-approved.
- Live security checks: Defender Antivirus ON, real-time protection ON, Windows Firewall domain/private/public ON. Previous explicit Smart App Control OFF persists as recorded historical state (not re-toggled in this audit). No external tunnel, pilot server, or CoS GUI was running. User's 8 GB device had ~1.6 GB free at one check; avoid loading GUI/agent stacks simultaneously.

### Acceptance classification and recommended next steps

| Function / original user goal | Evidence | Current completion |
|---|---|---|
| This mobile chat can read files and run authorized Windows shell tasks | Existing Remote Desktop Commander remote calls | **OPERATIONAL while Commander online/quota remaining** |
| Windows screenshots/UI automation on laptop | Windows-MCP/Windows Commander/OpenDesk local smoke tests via Commander | **INDIRECT FUNCTIONAL; not independent direct connector** |
| Browser automation | Playwright isolated Edge test pass; Browser MCP extension staged separately | **INDIRECT isolated-browser pilot; real account sessions and direct browser-origin this chat blocked** |
| Chrome console/network debugging | Chrome DevTools MCP CLI present/enabled in Codex | **CONFIGURED, END-TO-END NOT TESTED** |
| Local ChatGPT Desktop Work uses Windows MCP | Native local Work list_windows 7 windows | **OPERATIONAL for one read-only Work task; not same mobile chat** |
| Same mobile ordinary chat uses Windows MCP without Commander | No working remote tunnel/remote normal-chat MCP app; current-chat plugin not installed; Browser origin mismatch | **BLOCKED / NOT OPERATIONAL** |
| Independent GUI hosts / agents: Backboard, gptme, Community, Yep Anywhere, Web GPT Agent | Native Windows installs and shortcuts; no independent provider/agent session verified | **INSTALLED ONLY / NOT OPERATIONAL FOR ORIGINAL GOAL** |
| Browser bridges and CLI variants: CoS, Browser MCP, chatgpt-use, MCP Plugins, codex-browser-bridge, Browser Use, chrome-use | Local installation, builds, isolated profiles, CoS browser pairing, safe CLI help | **PARTIAL / NOT CONNECTED TO THIS THREAD** |

**Decision:** Keep only the current verified Commander connection for mobile ordinary-chat Windows actions; local Work/MCP is a tested but different-mode fallback. Do not claim 19/19 agents are attached or assert all Windows capabilities are granted. Do not restart CoS against user's prior closure instruction, authorize full browser session access, upgrade, install duplicate plugins or start paid API/tunnels without a separately verified need and explicit consent. Future effort should test each actual independent transport with an innocuous single read-only tool and test direct mobile entitlement before adopting any complex architecture.


---

## W. DJMRN desktop development capabilities and Codex-free execution alternatives — 2026-11-14

**User directive:** Save verified new Windows desktop capabilities in the existing DJMRN GitHub implementation report, then distinguish tools that can perform Codex-like work without consuming the Codex usage bucket. This records capability/evidence only; no paid provider, API key, deployment or account migration is authorized.

### A. Verified live local environment

- Authorized Windows laptop, 8 GiB RAM. At last inspection approximately 1.4 GiB physical memory free, so use one working agent/app at a time.
- Command availability tested directly on laptop in this chat: Node.js **v24.22.1**, npm **v11.19.1**, Python launcher **3.14.7**, Git **2.55.0.windows.5**, and VS Code CLI. A pre-existing workspace folder under Documents/Codex/DJMRN-Remote-Workspace exists; no site was built during that inventory.
- Existing Remote Desktop Commander is the **only verified independent transport from THIS ordinary ChatGPT mobile conversation to Windows**; the latest separate account check in section V found **59% of remote tool calls remaining** (a snapshot, no exact count).
- Previously confirmed real local I/O: Playwright launched a sandboxed Edge data page, clicked a button, verified changed text and screenshot; Windows-MCP enumerated **21** tools and captured screenshot, Windows Commander enumerated **57** tools and invoked Calculator 2+2=4, OpenDesk enumerated **22** tools and captured the screen primitive. These were mediated by Commander/local MCP clients, not new direct mobile plug-ins.
- Five named DJMRN local MCP integrations remain enabled in the Codex configuration: windows_mcp, opendesk, windows_commander, playwright, chrome_devtools. This is configuration evidence only. Separately, the native ChatGPT Desktop **local Work** plug-in already completed one real window-list action returning 7 windows; that achievement is a different execution/quota mode.

### B. Capability to value and acceptance boundaries

| Customer-facing task | What this conversation can do through existing Commander + local scripts | Proof/status |
|---|---|---|
| Persian RTL landing, portfolio, business site, mobile responsive site | Write HTML/CSS/JS, assets and content; make project files; serve locally; iteratively refine UI | **READY/FEASIBLE**, full website end-to-end acceptance not yet performed |
| React/Vite/Next.js interactive site | Scaffold components, navigation, forms, state, responsive styles, tests and production build | **READY/FEASIBLE**, framework setup/build must be tested per project |
| E-commerce website demo | Product catalog/filter UI, cart and checkout prototype, accessibility/mobile UX | **FRONTEND FEASIBLE**; live orders, identity/payment processing, inventory, tax and security NOT verified |
| Python/Node software and REST APIs | Code and test automations, APIs, CSV/JSON/SQLite processing, scripts | **LOCAL CODE EXECUTION AVAILABLE**; database/deployment requires separate setup |
| Browser UI testing | Playwright navigation, input/click, screenshots, assertions and regression tests | **REAL isolated Edge click/screenshot already PASSED**; no authenticated account/browser automation assumed |
| Website debugging | Inspect build/test errors, Git diffs; Chrome DevTools MCP is installed for console/network inspection | **Build/CLI ready**; direct DevTools debugging smoke test still pending |
| Windows files and GUI tools | Read/write scoped files, run commands, inspect windows/screenshots, UI Automation | **MCP local pilots passed**, but this chat uses Commander quota as transport |
| Deploy/production/real customer handling | Hosting, DNS, TLS, auth, secrets, backups, monitoring, payment gateways | **NOT PROVEN/NOT AUTHORIZED** until vendor/cost/security verification, tests and owner approval |

**Minimal verified development workflow without running Codex:** Ordinary ChatGPT conversation drafts and reviews project code -> existing Commander writes it on the authorized PC and executes Node/Python/Git -> Playwright tests a separate browser -> the assistant evaluates returned test evidence and fixes failures. It uses ordinary ChatGPT chat limits + **Commander independent tool-call quota**, NOT the Codex CLI or local Work agent usage. Do not call this unrestricted or model-free: planning here is done by ChatGPT.

### C. Downloaded software versus actual Codex quota independence

| Tool / installed group | What it adds | Inference and Codex quota distinction | DJMRN deployment status |
|---|---|---|---|
| **Node, Python, Git + Playwright + Chrome DevTools** | Deterministic web building, scripts, testing and debugging; no autonomous agent required | **No Codex agent/inference call** when directly executed. Chat and Commander can have distinct quotas. | Local runtime tools present; Playwright real isolated-browser test PASS, DevTools actual debug NOT YET TESTED |
| **Windows-MCP / Windows Commander MCP / OpenDesk** | Visual/Windows/file/process hands for an authorized AI host | Tools do **not inherently invoke a paid model or Codex**; the chosen calling host/model determines the quota | Local MCP enumeration and harmless real I/O PASS; ordinary mobile chat direct link absent |
| **gptme 0.36.0** | Model-agnostic terminal/coding agent; potential independent Codex alternative | **Critical:** gptme official docs state ChatGPT Plus/Pro openai-subscription provider uses the **Codex backend endpoint**, so do not assume it avoids Codex usage. Use independently verified-free model/provider (e.g. eligible Gemini or OpenRouter free tier) or a genuinely local small model instead, subject to 8 GiB RAM and fresh rate/cost review. | GUI installed; no verified live agent/model+code success on user's PC |
| **Backboard Studio 3.1.27** | All-in-one coding IDE/agent host, diffs, model routing, browser/computer tools | BYOS ChatGPT subscription or hosted model does **not** prove separate-from-Codex quota. A verified free independent model route may be possible, but costs/entitlement UNKNOWN. | App installed; user provider & full independent execution UNVERIFIED; heavy GUI requires RAM budget |
| **Browser Use 1.0.4** | Specialist agent to run browsers using a chosen LLM | Open-source runner may use independently verified free/locally hosted models; hosted browser/agent functions can cost extra. Plain Playwright is cheaper/simpler for deterministic tests. | CLI passes help; real autonomous agent+free provider NOT VERIFIED |
| **chatgpt-use 0.0.12 + chrome-use 1.5.291** | Experimental local ChatGPT-web-driven coding/harness and Chrome UI control | Project author describes driving logged-in ordinary ChatGPT web instead of Codex usage, but this consumes **ChatGPT chat rate/usage**, is fragile, and provider Terms may prohibit programmatic output extraction; no guaranteed compliance or stable unlimited execution. If Codex remains the outer harness for planning, it may still consume Codex. | Binary help PASSED; no authenticated browser account/task agent acceptance test; no automated auth granted |
| **Web GPT Agent 2.3.1 / Chat On Steroids 2.1.53 / MCP Plugins With ChatGPT Web** | Web ChatGPT and MCP/local file/browser tool bridges | Claimed web-chat model usage rather than Codex agent quota requires real supported integration and terms review. **Their local installation does not create direct remote connectivity**; CoS and Web GPT Agent require a configured MCP path/tunnel. | GUI/builds available; CoS Edge browser login/extension paired but **Core NOT CONNECTED**; app closed at owner's request |
| **Browser MCP** | Real tab/browser actions for a local compatible MCP host | Not itself an LLM. Another model or ordinary chat host must issue actions; not a direct quota bypass. | Server/isolated MV3 extension built, not live connected to mobile-chat |
| **Yep Anywhere 0.10.0** | Mobile/web interface supervising Codex and Claude Code sessions | **Does not eliminate Codex quota** if its backing agent is Codex. Alternative provider options must be separately verified. | GUI installed; no authenticated remote agent acceptance test |
| **ChatGPT Desktop Community 0.2.1** | Community GUI on official codex app-server | **Not an independent Codex quota bypass** when Codex is the backend. | GUI installed only |
| **codex-browser-bridge 2.0.0** | Browser pipe tools between compatible local clients | Browser connector, not model; does not itself eliminate model or agent quota | Binary help PASS; real pipe integration not tested |
| **TinyFish connected cloud browser** | Online browser agent provider (not local Windows desktop) | Provider's own quota/price, UNKNOWN for new heavy operations; no spending approved | Plugin available, not a locally downloaded PC controller |

**Recommendation under DJMRN free-first / simplest adequate policy:** For an actual paid client website or portfolio sample, start with **ordinary chat + Commander + Node/Python/Git + Playwright**, because this has the most real I/O evidence and does not need Codex. For a genuinely independent automated coding-agent host, trial **one** of gptme or Backboard with a **verified separate free-model provider**, with one small bounded test, and measure model quota, task completion, RAM and browser/tool security. Do not select gptme openai-subscription for the explicit objective of preserving Codex quota without independent provider-usage verification. Do not run 6 IDE/agents at once or add new infra just to increase installed tool count.

**Boundaries:** No new ChatGPT API spend, Codex/Work agent call, provider key/OAuth session, production deployment, merge, security-permission expansion, external tunnel, public port or paid tier was initiated in this capability register. Free software does not guarantee free inference. The screenshots, cookies, passwords and credentials of real user/customer accounts remain outside AI tool flows unless explicitly and securely approved.

**Canonical sources:** Earlier evidence in sections J–V of this exact report; original 19-tool discovery list; official [gptme provider docs](https://gptme.org/docs/providers.html), [gptme supported providers](https://gptme.org/docs/providers-supported.html), [Backboard README](https://github.com/Backboard-io/Backboard-Desktop), [Browser Use README](https://github.com/browser-use/browser-use), [chatgpt-use README](https://github.com/leeguooooo/chatgpt-use), [Web GPT Agent README](https://github.com/dbc-hbin/web-gpt-agent), [Yep Anywhere README](https://github.com/kzahel/yepanywhere), [ChatGPT Desktop Community README](https://github.com/Ninot1Quyi/chatgpt-desktop-community).
