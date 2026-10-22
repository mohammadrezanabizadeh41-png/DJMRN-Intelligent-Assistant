# KYNXA H3 — Latest Gemma3 1B resource admission block and Jan Local API alternative

Date: 2026-10-22. Evidence: directly pasted user PowerShell stdout, not assistant access to Windows.

## Direct reported measurement
- FreeRAM_GiB: **1.64**
- EstimatedBudget_GiB: **0.64** (user helper estimate, NOT native resource service budget)
- ModelState: **waiting-resource**
- ErrorCode: blank
- ModelVerified: **False**
- RuntimePID: blank

These values are from the same user snapshot. No ready local-model inference was observed. Earlier screenshot confirms user imported five external GGUFs; only Gemma3 1B enabled while others stopped. Previous free RAM was 2.59GiB, but it has since fallen.

## Source review
1. Official tagged KYNXA v1.7.0 resource-service/src/budget.rs calculates compute memory admission as ~70% of free physical memory minus 512MiB (capped total/2), further reduced by reservations. At 1.64 GiB free, ~0.65 GiB nominal matches user's 0.64 GiB within rounding. Actual native admission receipt and leases NOT observed.
2. Official tagged KYNXA v1.7.0 models/gateway_local_engine.rs sets waiting-resource before acquiring capacity/launching its own llama-server, and computes model reservation as weight size plus at least 512MiB host buffers and ~32MiB minimum KV; 0.67GiB Gemma3 1B file suggests ~1.20GiB CPU-only rough need (not runtime measured). Source: https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/agent-core/src/models/gateway_local_engine.rs and https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/resource-service/src/budget.rs .
3. Official KYNXA Provider presets includes **Local API (direct)**, **Ollama**, **LM Studio**, at https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Services/Models/ModelPresets.cs . Do not use default 127.0.0.1:8080/v1 for Jan; specify Jan's actual server URL.
4. Jan official https://docs.jan.ai/desktop/api-server describes GUI Settings > Local API Server, selecting an existing Jan local model and manually starting server, default loopback endpoint **http://127.0.0.1:1337/v1**. If Jan API Key configured, client must supply that key but should NOT share it with ChatGPT. Keep **Execute Tools on Server** OFF and bind only 127.0.0.1.

## Proposed operational next test (not performed)
- Native KYNXA resource guard remains enabled and model H3 NOT PASSED; repeated waits under 1.64 GiB Windows free cannot establish inference success.
- User may stop pending KYNXA generation using the UI, then try **Jan Desktop > Settings > Local API Server**, choose **Gemma 3 1B** already imported, Start Server and observe status, with no tools and no other models running. No external download.
- If Jan API server starts and system remains responsive, KYNXA > Models > Add model connection > Provider **Local API (direct)** > URL **http://127.0.0.1:1337/v1**, Fetch models/Test and save connection only when validated. API keys if necessary remain private. Simple Persian plain Chat test with zero Windows permissions or skills. If Jan alone can't fit with KYNXA, STOP and reconsider instead of memory guard bypass.
- External serving might bypass **KYNXA's internal local-model admission** but does NOT bypass physical RAM limits; running two application UIs may worsen overhead. There is no verified Jan API start, KYNXA connection, inference response or memory trial yet.
- No KYNXA app update, guard alteration, process termination, model download, account connections, Windows tool permissions or adopted architecture. D-005 OPEN; G3B guard CLOSED.

Status: H3_NATIVE_WAITING_RESOURCE; H3_EXTERNAL_JAN_API_FALLBACK_PROPOSED_NOT_RUN.
