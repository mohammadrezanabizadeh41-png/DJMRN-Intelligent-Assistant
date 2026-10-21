# G1 — Dual-chat readiness inspection / READ-ONLY on user's Windows

**Date:** 2026-10-21  
**Authority:** User explicitly replied `بله` to the coordinator's request for **G1 ONLY**: inspect existing Jan installation/version, RAM/current OS resources, and availability of MCP settings in ChatGPT Desktop on **Plus**.  
**State:** **G1 INSPECTION AUTHORIZED / DEVICE INSPECTION NOT YET PERFORMED / OUTCOME UNKNOWN**.  
**Context:** [approved G0 direction and feature gates](../../03-architecture-and-tools/DUAL-SURFACE-CHAT-TOOL-CORE-PROPOSAL-20261021.md), [D-015](../../02-project-management/DECISION-REGISTER.md), [TASK-0017](../../02-project-management/TASK-REGISTER.md), [REQ-012](../../02-project-management/CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md), [WA0003 reviewed](../../04-work-research-bridge/reviews/WQ0003.md).

## What the user did and did not authorize

- **YES:** one-off **read-only** Windows machine metadata and current memory snapshot, local already-installed app presence/version and process WorkingSet, plus visual reading of Jan's existing tool/MCP permission controls and ChatGPT Desktop's actual settings (if accessible).
- **NO:** install/update/download of any app or model, changes to a setting, new MCP server/plugin/host registration, running an Agent or inference/model workload, running CAP-006 again, reading/exfiltrating credentials/config content/chat histories, shell commands with external actions, permanent scheduler/service, account upgrade, API key, network tunnel, cloud upload, changing GPU/BIOS/pagefile, system configuration or writing local diagnostic reports.
- **Execution environment:** No direct physical Windows execution tool is connected to this coordinator. The user executes the one-off diagnostic PowerShell block **only if comfortable**; the coordinator must treat new outputs as **USER-REPORTED**, not `ran it remotely`.
- **Privacy:** Never print/store exact Windows username, machine serial, Windows product/device ID, filesystem personal home path, full process command line, config content, tokens, auth details, full app inventories or personal files. If sending UI screenshots, crop identifying account/email/keys and chat history. GitHub only receives sanitized relevant readings if user supplies them.
- **If the GUI is closed:** user is *not* asked to start models/Agents or enable Shell just to examine a screen. App launching may itself initialize services; check installed metadata first and decide on minimal safe manual GUI inspection. No CLI as routine end-user interface; PowerShell is this one-time engineering diagnostic only.

## A. Narrow, transient read-only metadata inspection (Windows PowerShell)

Paste as **one whole block** in an existing user PowerShell window. No elevation, no download, no file creation, no setting/environment changes or external network access. It uses OS CIM and installed-app metadata; does **not** read MCP config files.

```powershell
& {
    $ErrorActionPreference = 'Stop'
    Write-Host '=== DJMRN G1 READ-ONLY DEVICE SNAPSHOT ===' -ForegroundColor Cyan
    $os = Get-CimInstance -ClassName Win32_OperatingSystem
    $pc = Get-CimInstance -ClassName Win32_ComputerSystem
    Write-Host ('WINDOWS: {0}; BUILD: {1}' -f $os.Caption, $os.BuildNumber)
    Write-Host ('PHYSICAL_RAM_GIB: {0:N2}' -f ([double]$pc.TotalPhysicalMemory / 1GB))
    Write-Host ('OS_USABLE_GIB: {0:N2}' -f ([double]$os.TotalVisibleMemorySize / 1MB))
    Write-Host ('AVAILABLE_GIB: {0:N2}' -f ([double]$os.FreePhysicalMemory / 1MB))
    $targets = @(
        @{Label='Jan user-local'; Path=(Join-Path $env:LOCALAPPDATA 'Programs\jan\Jan.exe')},
        @{Label='Jan program-files'; Path=(Join-Path $env:ProgramFiles 'Jan\Jan.exe')},
        @{Label='Cherry user-local'; Path=(Join-Path $env:LOCALAPPDATA 'Programs\Cherry Studio\Cherry Studio.exe')},
        @{Label='Cherry program-files'; Path=(Join-Path $env:ProgramFiles 'Cherry Studio\Cherry Studio.exe')}
    )
    foreach ($app in $targets) {
        if (Test-Path -LiteralPath $app.Path -PathType Leaf) {
            $info = (Get-Item -LiteralPath $app.Path).VersionInfo
            Write-Host ('APP_FILE: {0}; PRESENT; PRODUCT_VERSION: {1}; FILE_VERSION: {2}' -f $app.Label,$info.ProductVersion,$info.FileVersion)
        } else {
            Write-Host ('APP_FILE: {0}; NOT FOUND AT STANDARD PATH' -f $app.Label)
        }
    }
    try {
        $packs = @(Get-AppxPackage -ErrorAction Stop | Where-Object { $_.Name -match '(?i)chatgpt|openai' })
        if ($packs.Count -eq 0) { Write-Host 'CHATGPT_STORE_PACKAGE: NOT FOUND' }
        foreach ($p in $packs) {
            Write-Host ('CHATGPT_STORE_PACKAGE: {0}; VERSION: {1}' -f $p.Name,$p.Version)
        }
    } catch { Write-Host 'CHATGPT_STORE_PACKAGE: UNKNOWN (package inventory unavailable)' }
    try {
        $apps = @(Get-StartApps -ErrorAction Stop | Where-Object { $_.Name -match '(?i)^(jan|chatgpt|cherry studio)(\b|\s|$)' })
        if ($apps.Count -eq 0) { Write-Host 'START_MENU_APPS: NO TARGET NAME MATCH' }
        foreach ($a in $apps) { Write-Host ('START_MENU_APP: {0}' -f $a.Name) }
    } catch { Write-Host 'START_MENU_APPS: UNKNOWN (not available)' }
    $running = @(Get-Process -ErrorAction SilentlyContinue | Where-Object {
        $_.ProcessName -match '(?i)^(jan|chatgpt|cherrystudio|cherry studio|codex)$'
    })
    if ($running.Count -eq 0) { Write-Host 'TARGET_APP_PROCESSES: NONE MATCHED' }
    foreach ($p in $running) {
        Write-Host ('PROCESS: {0}; WORKING_SET_MIB: {1:N0}' -f $p.ProcessName,([double]$p.WorkingSet64 / 1MB))
    }
    Write-Host '=== G1 METADATA SNAPSHOT COMPLETE (NO CHANGES) ===' -ForegroundColor Green
}
```

**Interpretation:** `NOT FOUND AT STANDARD PATH` ≠ confirmed not installed anywhere; `Get-AppxPackage` ≠ proof the actual web/desktop **Plus** account can add custom MCP; `PROCESS ... WORKING_SET` is only a snapshot, not peak/RAM overhead attributable to all spawned child processes. No model inference is launched. If `Get-CimInstance` is disabled/blocked, report `BLOCKED` and do **not** change system policy.

## B. Visual permission/UI capability survey (without changes)

After examining Part A output, choose the smallest relevant **already-open** interface:
1. **Jan Desktop, if available:** look at current About/version and MCP Servers list/tool controls, and note whether Shell is present and currently shown ON/OFF, whether approval setting displays `Allow All`, and any non-sensitive list of enabled tool *categories*. **Do not click Save, install, enable/disable, delete servers, run agent/model, enter prompts, or expose API tokens.** Jan 0.8.7 official release warns its Shell toggle defaults **ON**, but the current installed version and actual settings remain UNKNOWN until viewed. If app closed and opening might launch models/daemon, **do not open solely for this inspection** pending a new safe launch plan.
2. **ChatGPT Desktop, if already running:** inspect Settings (documented desktop shortcut `Ctrl+,`), note presence/absence of `MCP servers`, `Plugins`, `Codex`, and app version/about if visible. No `Add server`, install, save, restart or connect. UI availability for current Plus account and Chat/Work/Codex surfaces must be stated separately. **No entitlement inferred from generic official docs or from existing GitHub/Notion plugin use.**
3. If either GUI cannot be safely inspected in this phase, mark `NOT OBSERVED`, not `NO SUPPORT`. No requirement to take screenshots of account-specific secret settings or chat history.

## C. G1 outcomes and later gates

Record, after actual user-shared evidence:
- `os_build`, `physical_GiB`, `usable_GiB`, `available_GiB`, old/new snapshot distinction;
- Jan version **INSTALLED/DOWNLOADED/RUNNING/UNKNOWN**, Shell toggle observed state, MCP configured/available, tool approval setting;
- ChatGPT Windows app installed/version and whether local `MCP servers` menu genuinely appears on **Plus** (not proof of custom self-hosted connection in regular chat);
- current allowed cloud inference and tool-calling model: **UNKNOWN** unless separately verified (no download/test in G1);
- security flags, consent next and `G1=PARTIAL/COMPLETE/BLOCKED`.

**G1 does not approve** Jan update, downloading any LLM, attaching a new MCP tool, changing Shell, starting an Agent, testing actual tool call or modifying project Python source. After evidence, compare Jan/Cherry/custom alternative suitability, privacy/real RAM safety and advise G2 only after explicit user go-ahead. G1 is a **readiness check**, not a PASS on security/isolation.

## 2026-10-21 FIRST ACTUAL USER RESULT & LABEL ERRATUM
- The user executed **Part A** and supplied actual sanitized stdout. [G1-R0001](../logs/G1-R0001-20261021.md) is the authoritative follow-up receipt. **G1=PARTIAL**, not `NOT EXECUTED` anymore; earlier pre-execution state at document top is historical for this original protocol.
- **Bug/semantic erratum of printed field**: `PHYSICAL_RAM_GIB` is derived from `Win32_ComputerSystem.TotalPhysicalMemory`, and showed 5.88GiB, identical to OS visible. This value must **not** be treated as installed DIMM module capacity. Historical installed=8GiB from Win32_PhysicalMemory records/Task Manager remains unchanged until independently remeasured; usable OS=5.88 and current available=1.73.
- Two guessed Jan.exe standard path checks failed, but `START_MENU_APP: Jan` succeeded. This does **not** prove Jan absent; identify shortcut target via **visual read-only Start menu Properties** before any installation decision. ChatGPT Store package not found ≠ no Desktop app/Plus MCP. Targeted processes none matched, ≠ no background processes at all.
- **Remaining G1:** Jan executable target/version and existing MCP/Shell/approval controls, plus actual ChatGPT Desktop (if currently open) Settings/Plus feature visual observation. **No G2/G3/G4 activation** or broad model startup. Do not demand the same Part A script again or require PowerShell for ordinary user requests. Any additional diagnostic would need a specific justified scope, and user can use GUI rather than shell.

## G1 screenshot follow-up — Jan-Desktop.exe basename (2026-10-21)

User sent a screenshot of the **Jan Start shortcut Properties**. It shows a target ending in `%LOCALAPPDATA%\Programs\Jan\Jan-Desktop.exe`, **not** the `Jan.exe` filename probed in Part A. The former `NOT FOUND AT STANDARD PATH` result for `Jan.exe` was a wrong-name check; it does **not** show that actual Jan-Desktop.exe is missing. The Windows user-account path fragment present in the screenshot is **not stored**. Full sanitized finding is appended to [G1-R0001](../logs/G1-R0001-20261021.md). Existing shortcut Properties window may use **Open File Location** to verify target existence and executable Properties → Details for version **without launching Jan**. No model/UI/MCP/settings test has been performed. G1 PARTIAL, later gates not approved.
