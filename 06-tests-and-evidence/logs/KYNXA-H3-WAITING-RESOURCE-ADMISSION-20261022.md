# KYNXA H3 — Gemma3 1B blocked in waiting-resource before llama-server (user snapshot)

**2026-10-22. Source:** User ran a **read-only local GET** to `http://127.0.0.1:5218/api/local-models` on their own Windows machine and pasted the sanitized PowerShell result. No direct device actions, modified local settings, model download, process changes or tool permissions by the assistant.

## Exact user-observed internal state
```text
GlobalEnabled : True
LoadPolicy    : on-demand
InstalledCount: 6

Name                     Id                          Enabled Status RuntimeState       Verified
gemma-3-1b-it-qat-Q4_0   import-027ad2ad30124ed0     True     ready  waiting-resource     False
gemma-3-4b-it-qat-Q4_0   import-133fed7fb1c444c0     False    ready  stopped              False
model                    import-c2fad6be125f4145     False    ready  stopped              False
gemma-3-12b-it-Q2_K      import-f1ddfc262b474c51     False    ready  stopped              False
gemma-4-E4B-it-Q4_K_M    import-f2579c1ec3ed4185     False    ready  stopped              False
Qwen3 4B Q4_K_M          q3-4b-q4km                  False    ready  stopped              False
```
Last separate Windows read-only process sample (not guaranteed simultaneous with exact local GET): available RAM **1.85 GiB**, committed 5.48 GiB, `llama-server` 0, while KYNXA.Desktop, gateway and resource-service were running. A selected Work-mode imported id `import-027ad2ad30124ed0` is **now verified to be Gemma3 1B**. Five other models all disabled.

**Do not confuse `Status=ready` with ready-to-infer:** it refers to the GGUF library/import; `RuntimeState=waiting-resource`, `Verified=False`, blank PID and no valid generation are the controlling runtime result. Likewise `on-demand` is the desired low-memory load policy and `GlobalEnabled=True` means global local models enabled.

## Version-tagged original source assessment (not a device runtime audit)
- [KYNXA engine](https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/agent-core/src/models/gateway_local_engine.rs): sets `state=waiting-resource` immediately before `ResourceService.acquire_waiting` (or on regaining memory for a sleeping server), **before spawning private `llama-server.exe`**; thus zero llama-server processes is consistent with resource admission pending.
- [Resource-service budget](https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/resource-service/src/budget.rs): computes `memory_capacity = min(max(0,0.7 * memory.available_bytes - 512 MiB), total_bytes/2)` for compute, minus unreconciled leases; denies with `RESOURCE_PRESSURE` when requested RAM exceeds remaining capacity, preserves waiting queue if caller asked to wait. It does **not** simply use total physical DIMM capacity or pagefile allocation.
- [Engine residency plan](https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/agent-core/src/models/gateway_local_engine.rs): minimum host reservation is roughly weight bytes + 512 MiB host buffer + minimum 512-token KV estimate (512*65,536 bytes = 32 MiB), subject to legitimate measured GPU offload; external imported 1B GGUF file was 0.67 GiB by user's earlier GGUF inventory.
- **Illustrative conditional calculation:** if resource-service saw the same 1.85 GiB RAM available as prior OS sample, no other leased resources and no verified dedicated GPU offload, compute RAM capacity `~0.795 GiB`; min estimated request `~1.20 GiB`; hence likely denied and queued. This is a **strong source-backed hypothesis, not a directly observed resource-service `RESOURCE_PRESSURE` receipt or guarantee**, because sample timing, GPU and active reservations have not been inspected.

## Next controlled user-only step
1. Stop still-pending KYNXA generation using its normal UI button (not forced taskkill). Close only **user-selected, nonessential foreground applications** through their UI after saving work. Do not stop `svchost`, Defender, KYNXA gateway, KYNXA resource service, Jan/Ollama or other tools automatically; user can choose to shut unused app GUIs voluntarily.
2. Read only Windows FreePhysicalMemory; **aim for approximately 3 GiB available** (provisional experimental headroom, not vendor minimum; 2.5 GiB may be borderline). This might require closing Chrome/other unnecessary apps or restarting after saving work; only user opts in.
3. Retest **ONLY Gemma3 1B** in fresh plain Chat, short text `فقط OK بنویس.`; monitor runtime `RuntimeState`, verified PID or local error code, no tool/agent/work file rights.
4. If `waiting-resource` remains even after sufficient Windows free memory, investigate the resource-service's actual observed memory budget/queued leases, GPU monitor state and permissions. **Never bypass the limiter, fake admission receipts, grow pagefile to misrepresent physical RAM, disable protection, or hard-kill services**.
5. If memory headroom cannot rise, park KYNXA local engine and compare a lighter host using existing Jan/Ollama models, not blind reinstall/redownload.

**Test status:** `H3_LOCAL_MODEL_IMPORTED_SELECTED_ACTIVATED_BUT_RESOURCE_WAITING`, `H3_CHAT_NO_SUCCESS`, `ROOT_CAUSE_LIKELY_MEMORY_BUDGET_UNCONFIRMED`. User did not report rerun after additional RAM headroom. Architecture D-005 OPEN, G3B Windows personal-file guard remains CLOSED, goose remains second candidate.
