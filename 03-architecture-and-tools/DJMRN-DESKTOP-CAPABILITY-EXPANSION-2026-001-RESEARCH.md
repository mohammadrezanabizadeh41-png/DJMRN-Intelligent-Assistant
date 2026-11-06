# DJMRN — Advanced ChatGPT Desktop Control & Automation Ecosystem Discovery
Mission: DJMRN-DESKTOP-CAPABILITY-EXPANSION-2026-001  
Research date: 2026-11-06  
Status: RESEARCH COMPLETE (user-supplied Work report); INDEPENDENT VERIFICATION PARTIAL; IMPLEMENTATION NOT AUTHORIZED.

> This is a structured archival synthesis of the detailed Work report supplied by the user in chat on 2026-11-06, not a verbatim transcription or independently re-run verification of all cited official sources. Claims labeled VERIFIED-LOCAL were reported by Work; this assistant independently confirmed only that Remote Desktop Commander listed DJMRN-LAPTOP online, app v0.3.1. Full original Work text remains in the source conversation. No tool installations or Windows modifications were performed in this registration.

## Executive decision
Start with existing Remote Desktop Commander + Windows PowerShell/CIM + on-demand Codex CLI. First inspect availability of native Computer Use, then evaluate exactly one GUI path (winapp CLI or restricted Windows-MCP) and one browser path (existing Ui.Vision, then Playwright if necessary). Do not build a new multi-agent orchestration layer for this purpose without measured need.

## Reported local inventory (Work evidence, not independently retested here)
- Windows 11 Pro build 26300; Ryzen 5 3500U; installed RAM 8 GiB, OS usable ~5.88 GiB, snapshot free ~1.67 GiB; CPU snapshot 45%.
- Remote Desktop Commander 0.3.1, process RSS snapshot ~76.55 MB (not total bridge overhead).
- PowerShell 5.1.26100.9711, Node 24.22.1, Python launcher 3.14.7, Codex CLI 0.166.0.
- Installed-package observations: OpenAI.Codex 26.1027.3384.0, OpenClaw 2026.10.9, OpenAgents 1.1.9, OmniRoute 3.8.52, Ui.Vision Desktop 2.1.43.
- Port 20128 and 18789 not listening at sampling time; 20809 listening. This is not conclusive provider/agent health evidence.
- playwright, browser-use, pywinauto, psutil and APScheduler not found in checked default Python interpreter; virtual environments and Node packages not excluded.
- Native Work Computer Use availability, Ui.Vision browser extension/MCP and exact subscription entitlements remain UNKNOWN.

## Capability boundaries
| Surface | Confirmed/reported ability | Gap |
|---|---|---|
| Remote Desktop Commander | terminal, file operations, process listing, long-running sessions | no dedicated native click/type/live screenshot tool in observed tool set |
| PowerShell/CIM | process/resource/port/Windows diagnostics | cannot by itself guarantee GUI semantics |
| Codex CLI | local CLI installed, on-demand tasks feasible | current task/session ownership, quota, app-server integration need verification |
| Work cloud browser | cloud browser operations | not automatically local Chrome session |
| Native Computer Use | Windows support documented by Work | actual account/desktop availability unverified |
| Local MCP | STDIO/local HTTP integrations possible in suitable hosts | cloud cannot directly reach laptop localhost |
| Scheduler | Windows Task Scheduler available | durable monitoring/recovery requires explicit workflow state |

## Tool discovery matrix (Work research candidate pool)
| Category | Candidates | Proposed role |
|---|---|---|
| Existing shell/system | Remote Desktop Commander, local Desktop Commander, PowerShell/CIM, Task Scheduler, OpenSSH, Sysinternals | direct execution/observation |
| Windows GUI | native Computer Use, Microsoft winapp CLI, Windows-MCP, pywinauto, AutoHotkey, FlaUI, PyAutoGUI, Power Automate Desktop | one targeted GUI bridge |
| Browser | Ui.Vision MCP/XModules, Playwright CLI/MCP, Chrome DevTools MCP/CLI, Browser MCP, Browser Use | one browser controller, session-safe |
| Codex/agents | Codex CLI/app-server, OpenAgents Launcher, OpenClaw | reuse, on-demand; no new team by default |
| Durable workflow | Windows Task Scheduler, APScheduler, WinSW, Dagu, Node-RED, n8n, Activepieces, Windmill | only when actual persistence/complexity requires |
| MCP plumbing | FastMCP, mcp-proxy, Windows MCP/ODR | adapter/transport; not automatic security |
| Advanced GUI agents | Microsoft UFO, Agent S, UI-TARS Desktop | conditional/defer; model cost/compatibility unknown |
| Process library | psutil | optional only when built-in diagnostics insufficient |

All pricing, free quotas, permissions, licenses, releases and version compatibility must be verified from primary sources immediately before adoption. Work reported Commander Remote public free quota 10,000 calls/month and a public Pro price $20/month; account entitlement, overage behavior and remaining credits are NOT verified here. Unknown cost = DENY activation.

## Tiering
- **Tier 1:** existing Commander, PowerShell/CIM, Python/Node, Git, Codex on demand, Task Scheduler when approved.
- **Tier 2:** inspect native Computer Use; test winapp CLI or restricted Windows-MCP; reuse Ui.Vision; optionally Playwright CLI/MCP.
- **Tier 3:** DevTools, Browser MCP, pywinauto, AutoHotkey, FlaUI, PAD, Dagu, Node-RED, WinSW, APScheduler, FastMCP, existing agent hosts.
- **Tier 4/defer:** full new multi-agent stack, multiple browser controllers on same profile, n8n/Windmill for a single script, unknown-cost GUI agents, publicly exposed shell proxies.

## Four architecture alternatives
A. Work/ChatGPT -> Commander -> PowerShell/CLI: smallest, current baseline; depends on conversation/connection.
B. A + one GUI tool + one browser tool: expands useful coverage, adds focus/profile/session risk.
C. Work -> deterministic local supervisor -> Codex/workers: only for recurring reliable tasks; requires ownership, state, idempotency, bounded retry and logs.
D. Multi-agent orchestration: most complex/resource-intensive; not justified without measured collaborative need.
**Recommendation:** A first, targeted B second, C on evidence, D defer.

## Mandatory operational scenarios
01 CPU/RAM/process read: supported via CIM.  
02 identify high-memory applications: read-only first, close only with user approval.  
03 PowerShell commands: supported; write approval separate.  
04 Python/Node: interpreter execution reported.  
05 Codex status: process/log available; semantic thread tracking needs supported API/events.  
06 Worker monitoring: combine PID, start time, heartbeat, log, endpoint and task state.  
07 log reading: bounded tail, redact secrets.  
08 Windows GUI: native capability or selected bridge, not yet locally proven.  
09 local browser session: explicit profile/tab/domain matching required.  
10 files: available, scoped write permission required.  
11 Git/tests: on-demand, no unapproved merge.  
12 install/config: not authorized by research.  
13 scheduling: Task Scheduler or approved scheduled capability.  
14 worker recovery: graceful stop, ownership and bounded retry; requires approval.  
15 local tool expansion: CLI first, then MCP when needed.  
16 tool composition: observe -> decide -> authorized execute -> verify.  
17 project management: evidence from source, tests and runtime; no new team required.  
18 security/stop/audit: separate revoke, process stop, cancellation and rollback semantics.

## Proposed workflows
1. **RAM triage:** capture baseline -> group processes -> exclude VPN/browser and unsaved work -> propose closures -> explicit approval -> close selected -> compare measured RAM.
2. **Codex scoped task:** verify repository/branch -> approve file scope -> execute one task with structured events -> run tests -> inspect diff -> handoff; merge separately approved.
3. **Local website extraction:** identify authorized domain/tab/profile -> use existing Ui.Vision or one Playwright controller -> extract page-grounded fields -> never send form/message without approval.
4. **Stalled worker:** verify PID + heartbeat + output + endpoint + approval-wait state -> propose recovery -> authorized bounded restart -> verify real output.

## Security
Least privilege, explicit scopes, no public localhost proxy, no secrets/cookies in chat or logs, allowlists at enforcement boundary (not just prompts), trusted upstream releases, approval gates for consequential actions, session/profile isolation, prompt-injection treatment of site/log content as untrusted data. Command-blocking and allowed directories are NOT a sandbox. Stopping the remote bridge does not necessarily terminate child processes. Codex sandbox does not constrain a separate unrestricted Commander shell.

## Resource policy
8 GB installed RAM with ~5.88 GiB usable means avoid always-on redundant runtimes. One GUI controller per interactive session and one active project job during early tests. Measure full process tree and paging; do not assume the agent host's RSS equals total cost. A provisional sub-200 MiB incremental bridge target is a TEST HYPOTHESIS, not measured fact.

## Test plan (NOT RUN)
T01 device identity; T02 RAM installed/usable/free; T03 filesystem scope; T04 asynchronous PID tracking; T05 Python/Node encoding and exit; T06 Codex events/tests; T07 approval boundary; T08 correct GUI window/element; T09 Persian/DPI; T10 correct browser session/domain; T11 emergency stop and child state; T12 quota/overage hard stop; T13 no duplicate scheduled jobs; T14 bounded recovery; T15 injection resistance; T16 RAM responsiveness; T17 revocation/rollback.

## Phased proposal (not authorization)
P0 verify current Commander account limits, permissions, Computer Use entitlement.  
P1 low-risk diagnostics/log reading.  
P2 one scoped Codex task with structured evidence.  
P3 one GUI option, real foreground interaction.  
P4 one browser option with correct existing session.  
P5 one deterministic recurring workflow.  
P6 fault/reboot/sleep/recovery tests.  
P7 decide whether supervisor or orchestration is warranted.

## Open questions / verification backlog
Native Computer Use account eligibility; Ui.Vision extension/MCP and edition limits; Commander subscription hard stop; Codex rate-limit API compatibility; OpenAgents claimed credits; RAM impact of GUI/browser bridges; Persian/DPI correctness; locked-session behavior; remote restart and child-process ownership; independent verification of Work's release/pricing/source claims.

## Provenance and authorization
Source: user-pasted Work report, mission DJMRN-DESKTOP-CAPABILITY-EXPANSION-2026-001, 2026-11-06. This file preserves a structured synthesis and explicit uncertainty; original report includes longer per-tool notes, pricing/license discussion, scenario and test tables. No official-source URLs/citations were included in the pasted text itself, so vendor-specific assertions remain **reported by Work, not independently source-verified**. This research is NOT approval to install, configure, stop processes, schedule jobs, pay, or expose local services.
