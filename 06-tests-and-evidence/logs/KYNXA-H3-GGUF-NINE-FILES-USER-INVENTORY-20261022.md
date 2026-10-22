# KYNXA H3 — User-verified existing GGUF files inventory (no duplicate download)

**Date:** 2026-10-22. **Source:** user-pasted one-shot read-only PowerShell enumerating `*.gguf` only within four explicit, previously known model storage roots: HF cache, Jan, LM Studio, KYNXA. **Observation level:** USER-REPORTED, not assistant filesystem access. No file operations, downloads, server/model starts, tools or account connections performed.

## Nine files from exact user device output (normalized paths with Windows environment variables)

| Source | Type | File path rooted in environment | Size GiB |
|---|---|---|---:|
| HuggingFace | CHAT, Gemma3 1B Q4_0 | `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-1b-it-qat-GGUF\snapshots\c2531de7eec944fecd05bb2c23804c50d5a915c4\gemma-3-1b-it-qat-Q4_0.gguf` | 0.67 |
| HuggingFace | CHAT, Gemma3 4B Q4_0 | `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-4b-it-qat-GGUF\snapshots\bbcac0d065076c47042838c0675c602411b0dd4c\gemma-3-4b-it-qat-Q4_0.gguf` | 2.35 |
| HuggingFace | VISION PROJECTOR, NOT CHAT | `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-4b-it-qat-GGUF\snapshots\bbcac0d065076c47042838c0675c602411b0dd4c\mmproj-model-f16-4B.gguf` | 0.79 |
| HuggingFace | CHAT, Gemma3 12B Q2_K | `%USERPROFILE%\.cache\huggingface\hub\models--tensorblock--gemma-3-12b-it-GGUF\snapshots\ab7d363cf93e3786c6853083170681d86b946492\gemma-3-12b-it-Q2_K.gguf` | 4.44 |
| Jan | CHAT, Jan-v3.5 4B Q4_K_XL | `%APPDATA%\Jan\data\llamacpp\models\Jan-v3.5-4B-Q4_K_XL\model.gguf` | 2.79 |
| Jan | EMBEDDING ONLY, NOT CHAT | `%APPDATA%\Jan\data\llamacpp\models\sentence-transformer-mini\model.gguf` | 0.04 |
| KYNXA | CHAT, Qwen3 4B Q4_K_M | `%LOCALAPPDATA%\Programs\KYNXA\Data\Models\Local\q3-4b-q4km\Qwen3-4B-Q4_K_M.gguf` | 2.33 |
| LM Studio | CHAT, Gemma4 E4B Q4_K_M | `%USERPROFILE%\.lmstudio\models\lmstudio-community\gemma-4-E4B-it-GGUF\gemma-4-E4B-it-Q4_K_M.gguf` | 4.97 |
| LM Studio | VISION PROJECTOR, NOT CHAT | `%USERPROFILE%\.lmstudio\models\lmstudio-community\gemma-4-E4B-it-GGUF\mmproj-gemma-4-E4B-it-BF16.gguf` | 0.92 |

**Count** exactly nine files: SIX chat model weight files, TWO optional image/vision projector files, ONE embedding-only file. Five CHAT GGUFs external to KYNXA are candidates for import-by-reference; sixth KYNXA Qwen3 4B is already installed/enabled. No duplicate importing Qwen3. `Copy to model folder` checkbox **unchecked** on `Settings > Local models > Import GGUF` makes KYNXA reference the original instead of copying it (official tagged v1.7.0 source https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Views/LocalModelsPage.Actions.cs). Imported model must then be manually enabled to appear among local chat choices; KYNXA `LocalModelsPage.cs` includes picker refresh on enabled changes. Future use of an original file depends on it staying at that absolute path; HF snapshots and caches may later be purged.

## Safe staged recommendation, not runtime proof

1. Set native load policy `On demand`, do not preload.
2. Import existing Gemma 3 1B Q4_0 **by reference**, give recognizable display name and choose NO projector for plain-text test, then separately enable only if the user's RAM test allows. H2 first idle snapshot available RAM only 1.18 GiB.
3. Optionally import other chat files **as catalog references only** for later exploration (Gemma 3 4B, Jan-v3.5 4B, Gemma 3 12B, Gemma4 E4B) but DO NOT automatically load them or treat them as compatible: previous Jan Gemma3 4B Vulkan out-of-device-memory and 12B severe slowness, and LM Studio Gemma4 load stalled. KYNXA 1.7 runtime compatibility with Gemma4 unverified.
4. Two vision projectors are auxiliaries paired only with architecture-compatible models, not separate chat imports. Jan sentence transformer is embedding-only.

**Observed actual state at receipt:** user GGUF paths found, Qwen3 4B previously screenshot installed and enabled, but **no 5 external model imports done, no H3 generation benchmark and no KYNXA chatting/tool use verified**. Current default host decision D-005 OPEN; Windows file guard remains CLOSED.
