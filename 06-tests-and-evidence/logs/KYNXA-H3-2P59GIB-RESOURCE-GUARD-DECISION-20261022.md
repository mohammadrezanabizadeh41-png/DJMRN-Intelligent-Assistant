# KYNXA H3 — 2.59 GiB free RAM, request to temporarily disable native resource guard

**Date:** 2026-10-22. **Evidence:** user's pasted local read-only PowerShell memory sample and explicit user proposal: "من پیشنهاد میکنم فعلا محافظ منابع رو غیر فعال کنیم بعدا تنظیمش می کنیم". Not a system setting change and not a KYNXA inference test. Coordinator does not have access to this Windows device.

## Observed
- Windows reported **AvailableRAM_GiB = 2.59** with KYNXA previously opened.
- Prior PowerShell estimated-budget helper printed **EstimatedKYNXABudget_GiB = 1**. It used `[math]::Max(0,$free*0.7-0.5)`; passing integer literal `0` can select an integer numeric overload/coerce real number, making the printed whole integer potentially misleading. **Mathematical double-precision estimate from rounded 2.59 GiB free = 0.7*2.59 - 0.5 = 1.313 GiB (~1.31 GiB)**. Windows actual resource service budget has **NOT** been queried.
- Previously user-confirmed: `Gemma3 1B Q4_0` installed/enabled, `RuntimeState=waiting-resource`, `modelIdentityVerified=False`; other five disabled, local model policy `on-demand`. Last sample before this user report was 1.85 GiB available, `llama-server` processes zero.

## Version-tagged v1.7.0 source review
- `apps/resource-service/src/budget.rs` `memory_capacity()` takes 70% of currently available real RAM minus 512 MiB and caps at half total, accounting for outstanding leases and other constraints. At 2.59 GiB free, **nominal** capacity ~1.31 GiB, before lease differences, GPU state and sample-time changes.
- `apps/agent-core/src/models/gateway_local_engine.rs` `residency_plan()` estimates host buffer at **512 MiB** plus model weight size and minimum context 512*65536 bytes (~32 MiB); 0.67 GiB 1B model rough minimum ~1.20 GiB on CPU, leaving only ~0.11 GiB nominal headroom at the current observed sample. Actual model bytes/context/hardware readings may differ and GPU offload can change request.
- KYNXA source `ResourceService.acquire_waiting()` is a dependency in the load path and `RESOURCE_RUNTIME_UNAVAILABLE` results when the resource service is absent; simply killing/disabling the **kynxa-resource-service.exe** would **not** bypass admission in a supported way, it would break the engine.
- Checked the official local-model Settings implementation: `Enabled` controls local-model availability, and `On demand` is a load scheduling policy; **not an independent verified off switch for resource admission**. No documented safe per-session admission bypass identified in examined UI/source. Rewriting guard code or bypassing service on a production 5.88 GiB OS-visible laptop is not an authorized default.
- No need to re-download models, change pagefile, turn off Windows protections, alter resource service binaries or run background agents.

## Bounded practical next step
- Recommend retaining guard; Windows available 2.59 GiB already has a **borderline but mathematically plausible** admission budget for 1B if no other reservations. User can try ONE new plain Chat request using selected **Gemma3 1B only** and prompt `فقط OK بنویس.`. Stop any previous unfinished generations through the UI beforehand; do not enable Tools/Skills/Windows file access.
- If waiting persists, optionally close unused *foreground* user-selected browser/apps through GUI (save work first), target ~3.0 GiB available (an experimental target, not published requirement). Read-only retrieve `RuntimeState`, `RuntimeCode`, `RuntimePID` via established `GET http://127.0.0.1:5218/api/local-models`, no mutation. Consider inspecting resource reservations via supported read-only diagnostics, not fabricated API paths. If still rejected with >3 GiB free, compare alternate host/model service rather than disabling guard.
- For a corrected user-only local **estimator**, use explicit floating-point typed calculation, not mixed `[math]::Max(0,<double>)`: `$b=0.7*[double]$free-0.5; if($b -lt 0){$b=0.0}; [math]::Round($b,2)`.
- Distinguish user proposal from **approval to patch software**; user has NOT actually disabled anything. **No model response or runtime resource-admission receipt observed yet**.

**Status:** H3 waiting-resource observed earlier, now user measured 2.59 GiB Windows available; guard remains ON/NOT_MODIFIED; no new inference attempt reported; D-005 still OPEN, G3B file guard CLOSED. Sources: https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/resource-service/src/budget.rs ; https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/agent-core/src/models/gateway_local_engine.rs .
