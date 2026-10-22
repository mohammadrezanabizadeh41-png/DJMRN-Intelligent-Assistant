# KYNXA H3 — Confirm native local-GGUF import is in Settings, NOT connection form

Date: 2026-10-22. **Evidence:** user-supplied KYNXA 1.7.0 screenshot and independent official **v1.7.0 tagged** source read, plus prior real Notion Windows 11 model inventory.

## User screenshot and distinction
- Screenshot is a KYNXA **Models > My connections > Add model connection** form, with DeepSeek default, HTTPS API service, API key input and buttons Fetch models / Test / Save connection. **Do NOT save this cloud-provider form or type an API key to import already-downloaded GGUF.**
- Source-tagged `apps/desktop/Views/ShellPage.StorageSettings.cs`: `OpenLocalModels() => NavigateSettings("local-models")`, settings workspace registers `local-models` category and constructs an embedded `LocalModelsPage`. Thus exact navigation is main app **gear icon Settings > Local Models**; this is separate from the Models connection window.
- Source-tagged `apps/desktop/Views/LocalModelsPage.Layout.cs` creates `_import` with `ConfigureButton(_import, "导入 GGUF", "LocalModelsImport")` attached to the local model page toolbar.
- Source-tagged `apps/desktop/Views/LocalModelsPage.Actions.cs` opens file picker filtering `.gguf`, with import popup checkbox `复制到模型目录（不勾选则引用原文件）` (Copy to model folder; unchecked references original), plus optional vision projector. `ImportAsync` can reference original instead of duplicating. Import DOES NOT imply inference model automatically enabled or tool access granted.

## Existing-model candidate and resource caution
- User's historical Notion AI install/testing log https://app.notion.com/p/3fbc8c6846908184b4e32c586686e3 documented **`gemma-3-1b-it-qat-Q4_0.gguf` ~0.67 GiB** in `%USERPROFILE%\.cache\huggingface\hub` nested snapshots, plus Gemma3 4B ~2.35 GiB, Gemma3 12B ~4.44 GiB and Jan managed Jan-v3.5 4B ~2.79 GiB. Path and file continued existence on the current Windows desktop **not freshly confirmed**; no complete 1B snapshot folder should be invented. User can browse/search file name in already-recorded Hugging Face cache.
- KYNXA idle screenshot/readout: RAM available only 1.18 GiB, 11 related processes and 611 MiB summed working set. Therefore recommend locating and **importing/reference-only first** without enabling/starting inference; use one small 1B model at a time, reassess memory before actual load. Don't claim compatibility tested or missing model downloaded.

Sources:
- https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/ShellPage.StorageSettings.cs
- https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/LocalModelsPage.Layout.cs
- https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/LocalModelsPage.Actions.cs

Status: `LOCAL_IMPORT_UI_PATH_SOURCE_VERIFIED`; **user navigation screenshot, GGUF import, model enable, model run, benchmark NOT_RUN**. Host D-005 architecture remains OPEN, G3B file guard closed; no device action by coordinator.
