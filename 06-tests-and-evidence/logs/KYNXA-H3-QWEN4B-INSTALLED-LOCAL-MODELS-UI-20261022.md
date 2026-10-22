# KYNXA H3 — User screenshot confirms installed and enabled local Qwen3 4B

**Observed on 2026-10-22. Provenance:** actual screenshot of user's KYNXA v1.7.0 Settings > Local models. **Do not confuse downloaded/enabled with inference loaded or successful chat.** Assistant has no direct execution on laptop.

## Actual visible local-model state
- Settings > Local models panel, top toggle **Enabled** ON.
- Installed tab selected and count **62 models · 1 installed**.
- One displayed model: **Qwen3 4B Q4_K_M**, family Qwen3, 4B, quantization Q4_K_M, file approx **2.33 GiB** in KYNXA's managed Local model directory. UI shows **Enabled** status and separate available action **Disabled** (disable), plus **Delete**. Disk installation folder reports ~115.06 GiB free and Installed models about 2.33 GiB.
- UI explicitly says **Recommended RAM 8 GB · VRAM 5 GB**, **Text · Tool calling · Model not yet verified · Tool capability not yet checked**.
- Loading policy currently **Automatic scheduling**, alternatives **On demand** and **Startup warmup**. No runtime state of ready/loading, no current chat answer or actual GPU/VRAM allocation is visible.
- **Import GGUF** button is visible next to search box. This is the native GGUF file importer, not Settings > Models > API connections.
- Screenshot resolves prior ambiguity: model selection menu said *No models are configured*, referring to external connection picker at that moment; current internal Settings clearly proves **one local model installed AND enabled**. How/when model downloaded/was enabled is not independently known. Do not treat prior assumption of unchecked install wizard model as proof no later download took place.
- Latest user Windows snapshot before this screenshot: 8 GiB installed DIMMs, 5.88 GiB usable, 1.18 GiB RAM available with KYNXA host running, 11 related processes / 611 MiB grouped Working Set. This screenshot is NOT a new RAM measurement.

## Recommended next action, not executed
1. Switch local model loading policy to **On demand** (source-tagged KYNXA v1.7.0 implementation says load on use, not background warmup; may delay first reply). Leave built-in Qwen3 4B **installed and enabled**, do not hit Disable or Delete without separate reason; this is not evidence of actual inference compatibility on device.
2. To reuse already-downloaded, smaller Jan/isolated Hugging Face Gemma 3 1B ~0.67GiB: select **Import GGUF**, find `gemma-3-1b-it-qat-Q4_0.gguf` in historically observed Hugging Face cache. In import options keep **Copy to model folder UNCHECKED** (external reference, no duplicate weights), no projector for initial plain text test. The exact current on-device file path / import success remain unknown.
3. Do **not** enable/load both 4B and 1B models simultaneously; test smaller model with cautious RAM check first if user elects, or evaluate Qwen3 4B later under memory pressure observation. Keep Ask for approval and tool/file connections off.
4. **Do not claim Qwen3 4B inference passed or its tools have been validated**. Further user evidence needed.

**Primary verified code refs:**
- https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/LocalModelsPage.Layout.cs (settings loading policy and Import button)
- https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/LocalModelsPage.Actions.cs (import file picker, no-copy external reference)
- https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/LocalModelsPage.cs (load policy and picker visibility logic)
- Historical Jan/HF inventory: https://app.notion.com/p/3fbc8c6846908184b4e32c586686e3

**Status:** `H3_LOCAL_MODEL_QWEN3_4B_INSTALLED_ENABLED_UI_CONFIRMED`; policy change, Gemma GGUF import, actual local model loading, Persian response, tool use and speed/RAM **NOT_RUN**. Global architecture D-005 OPEN, file guard G3B unchanged.
