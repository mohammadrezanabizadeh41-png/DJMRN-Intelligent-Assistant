# KYNXA H3 — User-observed zero llama-server processes; next read-only local gateway status

**Date:** 2026-10-22. **Evidence:** user pasted their own read-only Windows PowerShell process/memory snapshot following a KYNXA imported model chat test that yielded no visible answer. Coordinator did not access computer, alter any process or run model inference.

## Exact user-supplied results
```text
AvailableRAM_GiB     : 1.85
CommitUsed_GiB       : 5.48
LlamaServerProcesses : 0

ProcessName               PID  WorkingSet_MiB
KYNXA.Desktop          11772             282
kynxa-gateway           5708              43
kynxa-resource-service  6688               9
```

**Interpretation:** KYNXA Desktop, gateway and resource-service exist, but **no process named `llama-server` was running at time of sample**. This alone does NOT prove an installation failure, fatal RAM shortage, absence of model files or a gateway bug. User's prior UI in **Work** showed one `Generation stopped` with no text, and another `Replying... Generating` without visible tokens; whether the sampled process list was taken while still generating cannot be proven. On-demand policy may leave runtime off before a request; a previously stopped/failed child also disappears; application also can idle-sleep. Available 1.85 GiB is not a definitive failure threshold. No specific error code observed yet.

## Independently read exact KYNXA v1.7.0 code
- `apps/desktop/Services/Integration/ModelGatewayService.cs`: default model gateway **`http://127.0.0.1:5218`** unless KYNXA_MODEL_API_URL overrides; gateway initialized when app opens.
- `apps/desktop/Services/Models/LocalModelsApiClient.cs`: GUI retrieves local model state with HTTP **GET `/api/local-models`** (no POST mutation); responses include `Enabled`, `Installed`, `Status`, `Runtime`.
- `apps/agent-core/src/models/gateway_local_models.rs`: GET local model snapshot with **runtime** observation for each id, including state and code via `gateway_local_engine::status`. Imports do not automatically register an enabled provider until manually enabled; user says external models imported, enable result not yet independently verified.
- `apps/desktop/Views/LocalModelsPage.Rows.cs`: UI possible runtime states `preparing`, `preparing-runtime`, `loading`, `ready`, `sleeping`, `failed`; `Enabled` is not running state.
- `apps/agent-core/src/models/gateway_local_engine.rs`: managed engine requires its own **llama-server.exe** private subprocess on loopback; may install fixed CPU or Vulkan runtime when not bundled, use resource admission, abort startup on load failure and capture failure code/diagnostics. `On demand` avoids idle preload. **No device runtime file/path test performed**.
- UI **Work vs Chat** difference is a useful controlled test, not a verified root cause.

## Next safe diagnostic, NOT_YET_RUN
User runs **read-only** PowerShell `Invoke-RestMethod -Method Get http://127.0.0.1:5218/api/local-models` with brief timeout, printing ONLY `enabled, loadPolicy, installed names/ids/enabled/status/runtime.state/runtime.code/runtime.backend/runtime.processId/modelIdentityVerified`, not original private file paths, errors, tokens, credentials or raw response. This call should only read the status and **not** POST enable, run, install, import or download. If GET cannot connect, user returns `LOCAL_API_READ_FAILED` without exposing private error text, then verify gateway address/readiness. Re-enable/import actions should **not** be automated. Await actual runtime state/error to differentiate model-disabled, runtime missing/downloading, resource admission, failed process/CPU/Vulkan, or stopped/sleeping.

**Status:** `H3_NO_LLAMASERVER_AT_SNAPSHOT / KYNXA_INFERENCE_NO_SUCCESS_EVIDENCE / NEXT_LOCAL_STATUS_QUERY_NOT_RUN`. D-005 global stack OPEN; Windows file guard G3B CLOSED; goose evaluation still candidate #2. No model download/delete/reinstall or system settings/permissions changes authorized.
