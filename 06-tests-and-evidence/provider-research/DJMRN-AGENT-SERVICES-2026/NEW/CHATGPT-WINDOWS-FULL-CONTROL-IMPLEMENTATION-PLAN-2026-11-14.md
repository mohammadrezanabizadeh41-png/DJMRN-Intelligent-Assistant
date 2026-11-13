# DJMRN — NEW — ChatGPT ↔ Windows / Browser / Coding: Operational Implementation Plan

**Date:** 2026-11-14  
**Status:** PROPOSED / NOT YET IMPLEMENTED  
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
