# DJMRN — Previously recorded Windows model-file paths for KYNXA GGUF reuse

**As of 2026-10-22.** **Evidence:** actually fetched canonical Notion [Windows 11 Desktop AI Installation & Testing Log](https://app.notion.com/p/3fbc8c6846908184b4e32c586686e3), with user reports from 2026-10-17 and 2026-10-18. NOT a new filesystem scan. KYNXA installation UI and no-model RAM measurements are in prior H2/H3 receipts.

## Exact full file paths documented by user on 2026-10-17

- **Gemma 3 4B Q4_0**, approx 2.35 GiB: `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-4b-it-qat-GGUF\snapshots\bbcac0d065076c47042838c0675c602411b0dd4c\gemma-3-4b-it-qat-Q4_0.gguf`
- **Gemma 3 12B Q2_K**, approx 4.44 GiB: `%USERPROFILE%\.cache\huggingface\hub\models--tensorblock--gemma-3-12b-it-GGUF\snapshots\ab7d363cf93e3786c6853083170681d86b946492\gemma-3-12b-it-Q2_K.gguf`

## Other known GGUF model inventory (EXACT absolute file path is NOT documented)

- Gemma 3 1B Q4_0, `gemma-3-1b-it-qat-Q4_0.gguf`, ~0.67 GiB, somewhere under `%USERPROFILE%\.cache\huggingface\hub`.
- Gemma 3 4B image projector, `mmproj-model-f16-4B.gguf`, ~0.79 GiB under same HF cache; **not a standalone conversation LLM**.
- Jan-v3.5-4B Q4_K_XL, `model.gguf` under a `Jan-v3.5-4B-Q4_K_XL`-named folder below `%APPDATA%\Jan\data\llamacpp\models`, ~2.79 GiB.
- Sentence transformer embeddings, `model.gguf` under sentence-transformer named folder in Jan same location, ~0.04 GiB; **not a chat LLM**.
- LM Studio: `google/gemma-4-e4b`, previously `lms ls` download present ~6.33 GB; location not independently recorded and previous loading stalled at 79%; no inference success.
- Ollama: previously `ollama list` EMPTY; Ollama executable installed, no models confirmed in Ollama's own repository at that reading.
- KYNXA: screenshot shows `Qwen3 4B Q4_K_M` ~2.33 GiB in KYNXA managed `%LOCALAPPDATA%\Programs\KYNXA\Data\Models\Local`; installed and enabled, not inference-tested; exact filename visible in screenshot and H3 record.

## Proposed one-shot, read-only current-path verification

Only recursively enumerate GGUF files within these four **known model storage locations**:
`%USERPROFILE%\.cache\huggingface\hub`;
`%APPDATA%\Jan\data\llamacpp\models`;
`%USERPROFILE%\.lmstudio\models` (common default, not verified);
`%LOCALAPPDATA%\Programs\KYNXA\Data\Models\Local`.
Print *all* observed `.gguf` full names, sizes and source; report missing source directories. Do not browse personal documents, execute downloaded binaries, register/import files, copy, delete, re-download, invoke model inference, enable KYNXA tools, or assume historic files remain at same path.

Source-verified KYNXA v1.7.0 `Settings > Local models > Import GGUF` provides an unchecked `Copy to model folder` option that references existing GGUF file in-place, avoiding duplicate file storage. Importing a file is different from model enabling and inference. Initial model suitable for low-RAM test (prior OS available 1.18 GiB while KYNXA UI open) is Gemma3 1B, and 4B/12B should not be automatically loaded together.

**State:** `HISTORICAL_PATHS_RECOVERED` with two exact GGUF paths; **live filesystem recheck NOT_RUN**; no new import, model download or load; D-005 selection OPEN.
