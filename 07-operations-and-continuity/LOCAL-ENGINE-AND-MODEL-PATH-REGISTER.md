# DJMRN — Windows Installed Software, Engines, GGUF and Endpoint Path Register

## 2026-10-23 correction — check this before older snapshots
- New [21-item statistical inventory](../01-system-inventory/INSTALLATION-AND-DEPLOYMENT-STATISTICS-20261023.md) and [14-event install log](../01-system-inventory/installation-events.csv) separate historical user-installed items, current CLI-verified versions and failed downloads.
- **Goose was later installed/launched, user screenshots G1–G4 on 2026-10-22 confirm basic Gemma3 1B text generation but poor Persian self-introduction quality.** Older "goose NOT_INSTALLED" below refers only to earlier snapshot and is superseded.
- **Node.js v24.22.1 currently CLI-verified. Native Bifrost v2.3.2 still NOT_OPERATIONAL**: cache 57,943 bytes vs vendor official HEAD 134,305,792. Valid PE header alone does not permit execution; do not use old rename-only EFTYPE ZIP. [Incident](../06-tests-and-evidence/logs/WINDOWS-BIFROST-TRUNCATED-PE-20261023.md). User Windows `main` process/Jan/Groq unverified; Github CI is offdevice.

**Canonical permanent reference; updated 2026-10-22.** Prepared by reconciling: (1) [user's nine-file PowerShell readout](../06-tests-and-evidence/logs/KYNXA-H3-GGUF-NINE-FILES-USER-INVENTORY-20261022.md), (2) [Notion desktop installation/testing log](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3), (3) [KYNXA H2/H3 actual user processes and loopback state](../06-tests-and-evidence/logs/KYNXA-H3-WAITING-RESOURCE-ADMISSION-20261022.md), and (4) canonical [KYNXA→goose comparison queue](../03-architecture-and-tools/READY-MADE-HOST-EVALUATION-QUEUE-20261022.md). *This is a historical evidence ledger, NOT a new live Windows application/registry scan.* Private local username is deliberately normalized to environment variables; Windows expands `%USERPROFILE%`, `%APPDATA%`, `%LOCALAPPDATA%`. PowerShell can use `$HOME` / `$env:APPDATA` / `$env:LOCALAPPDATA`. Model paths are taken from user read-only PowerShell and are **user-verified at that sampling time**; whether cache files move in the future must be checked only if a failure arises. No secret/config/API keys/credential content recorded.

## Snapshot and counts
- **Windows:** Windows 11 Pro x64, Ryzen 5 3500U, **8 GiB physical RAM, ~5.88 GiB OS-usable**; available RAM fluctuated ~1.18–2.59 GiB in actual KYNXA tests. Never confuse RAM physically installed with available memory. Save work, avoid two simultaneously loaded LLMs.
- **GGUF inventory:** **9 files** found in four specific roots: **6 chat-weight files**, **2 mmproj vision projector files**, **1 embedding file**. Nominal sum of displayed file sizes ~**19.30 GiB**, **NOT** a reliable unique disk-usage figure because caches may use links/shared content.
- **AI applications/engines included:** KYNXA Desktop, KYNXA private llama.cpp, Jan Desktop/internal llama.cpp, Jan Agent CLI, Ollama, LM Studio, Bionic, independent Llama desktop app, ChatGPT Desktop. **Not all independently tested for current version/EXE location.**
- **Development/support:** Python/pip/venv, Git, VS Code, WinGet, sqlite3 module, WSL capability. Explicitly **Hermes NOT PRESENT** on current Win11, **goose NOT INSTALLED** as of this register.
- **H3 state:** KYNXA local chat never confirmed replying; native Gemma 3 1B `waiting-resource`. Jan connection saved in KYNXA without proven generated text. Ollama importer / direct llama-server tests were **suggested but NOT run**. **KYNXA PARKED/HOLD, do not uninstall by default**. Candidate #2 goose now the evaluation target, but not yet installed/adopted.

## A. Software and inference engines (installed/reported vs execution proof)

| Name | Version / evidence | Executable location | State and critical note |
|---|---|---|---|
| KYNXA Desktop | 1.7.0 | `NOT_VERIFIED` | **user-installed/GUI-launched**; HOLD, native managed 1B waiting-resource; six imported chat model records; no successful response observed |
| KYNXA managed llama.cpp | b11669 per source tag, runtime binary build not user checked | `UNVERIFIED; if bundled see `<KYNXA_APPLICATION_ROOT>\runtime\local-llm\llama.cpp\b11669\<cpu/vulkan>\...\llama-server.exe` or KYNXA data root `LocalRuntime\llama.cpp\b11669\<cpu/vulkan>\...`` | **runtime source path identified; binary path UNVERIFIED**; No safe on/off guard setting verified; do not label EXE present without live check |
| Jan Desktop + internal llama.cpp | app version NOT_VERIFIED; llama.cpp engine 0.5.0 build b11146 per historical Notion | `NOT_VERIFIED` | **installed, GUI launched, prior local Persian inference user-reported**; Jan-v3.5-4B, Gemma3 1B/4B/12B imported historically; model concurrency 1 |
| Jan Agent CLI | 0.8.6-64 agent-nightly | `%USERPROFILE%\.local\bin\jan.exe` | **CLI installed/version user-tested 2026-10-17**; distinct from Jan Desktop; tool calling/sandbox integration not validated |
| Ollama | 0.40.6-rc1 per Oct 17 record | `NOT_VERIFIED` | **CLI and local service previously tested**; One-shot Ollama registration was PROPOSED in chat only; no run result, no guaranteed model now installed |
| LM Studio | NOT_VERIFIED | `NOT_VERIFIED` | **installed UI launched**; Gemma4 E4B not verified as able to load/respond |
| LM Studio Bionic/llmster | NOT_VERIFIED | `NOT_VERIFIED` | **installed, GUI launched per user**; do not merge with LM Studio classic; AI/tool success not tested |
| Llama desktop app / LlamaApp | 0.12.0 previously user-reported, exact application identity not reverified | `NOT_VERIFIED` | **user-reported installed and launched**; possible independent app; distinguish from llama.cpp library |
| ChatGPT Desktop | NOT_VERIFIED | `NOT_VERIFIED` | **user-installed/UI previously used**; not a local GGUF engine |
| Python | 3.14.7 | `%LOCALAPPDATA%\Programs\Python\Python314\python.exe` | **CLI tested in user environment**; Bare python in PATH depends on shell environment |
| Git for Windows | 2.55.0.windows.5 | `C:\Program Files\Git\cmd\git.exe` | **CLI tested**; installed via WinGet |
| VS Code | 1.142.0 user historical, not independently version tested in Oct 17 Notion | `NOT_VERIFIED` | **installed user-reported**; do not treat as inference engine |
| WinGet/App Installer | 1.11.510 | `system App Installer resolved by winget; exact filesystem executable path NOT_VERIFIED` | **CLI tested**; install-on-demand policy |
| SQLite Python module | 3.50.4 historically | `bundled Python sqlite3 module, not a separate database engine exe` | **built-in Python sqlite3 tested**; do not claim independent SQLite server installed |
| WSL | distribution unverified | `NOT_VERIFIED` | **WSL feature present (historical), no confirmed Ubuntu runtime**; do not require WSL/Docker for goose GUI |
| Hermes Agent | old Windows installation only | `NOT_PRESENT` | **NOT INSTALLED on current clean Win11 per user report**; exclude from installed count |
| goose Desktop | v1.55.0 latest official checked 2026-10-22 | `NOT_PRESENT` | **NOT_INSTALLED / NEXT CANDIDATE**; candidate #2, candidate evaluation not same as adoption |

**Executable path rule:** `NOT_VERIFIED` means no user CLI `(Get-Process ...).Path` or signed package path was captured, **not** that the application is missing. Never invent `Jan.exe`/Ollama/LM Studio absolute paths. Jan Agent CLI exact installed path, Python and Git paths are **real historical user confirmations**. KYNXA private runtime example is a **source-derived directory pattern** (not a confirmed file), and its CPU vs Vulkan binary cannot be guessed. No routine future PowerShell needed to look up models; only a newly required real executable location would need a bounded one-time check.

## B. Full GGUF path inventory — exact user-file locations, environment-normalized

| # | Purpose | Model / file | GiB (user readout) | File path |
|---|---|---|---:|---|
| 1 | chat | Gemma 3 1B Q4_0 | 0.67 | `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-1b-it-qat-GGUF\snapshots\c2531de7eec944fecd05bb2c23804c50d5a915c4\gemma-3-1b-it-qat-Q4_0.gguf` |
| 2 | chat | Gemma 3 4B Q4_0 | 2.35 | `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-4b-it-qat-GGUF\snapshots\bbcac0d065076c47042838c0675c602411b0dd4c\gemma-3-4b-it-qat-Q4_0.gguf` |
| 3 | vision_projector | Gemma 3 4B mmproj F16 | 0.79 | `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-4b-it-qat-GGUF\snapshots\bbcac0d065076c47042838c0675c602411b0dd4c\mmproj-model-f16-4B.gguf` |
| 4 | chat | Gemma 3 12B Q2_K | 4.44 | `%USERPROFILE%\.cache\huggingface\hub\models--tensorblock--gemma-3-12b-it-GGUF\snapshots\ab7d363cf93e3786c6853083170681d86b946492\gemma-3-12b-it-Q2_K.gguf` |
| 5 | chat | Jan-v3.5 4B Q4_K_XL | 2.79 | `%APPDATA%\Jan\data\llamacpp\models\Jan-v3.5-4B-Q4_K_XL\model.gguf` |
| 6 | embedding | sentence-transformer-mini | 0.04 | `%APPDATA%\Jan\data\llamacpp\models\sentence-transformer-mini\model.gguf` |
| 7 | chat | Qwen3 4B Q4_K_M | 2.33 | `%LOCALAPPDATA%\Programs\KYNXA\Data\Models\Local\q3-4b-q4km\Qwen3-4B-Q4_K_M.gguf` |
| 8 | chat | Gemma 4 E4B Q4_K_M | 4.97 | `%USERPROFILE%\.lmstudio\models\lmstudio-community\gemma-4-E4B-it-GGUF\gemma-4-E4B-it-Q4_K_M.gguf` |
| 9 | vision_projector | Gemma 4 E4B mmproj BF16 | 0.92 | `%USERPROFILE%\.lmstudio\models\lmstudio-community\gemma-4-E4B-it-GGUF\mmproj-gemma-4-E4B-it-BF16.gguf` |

**Do not import auxiliary `mmproj` or embedding GGUF as standalone chat models.** Qwen3 4B was already inside KYNXA; five other chat models were imported by user via KYNXA Import GGUF and had names in `GET /api/local-models`. `Installed` and `Enabled` are NOT inference success. For Jan/HuggingFace GGUF external references, moving/purging original HF snapshot breaks any no-copy KYNXA reference. Jan-v3.5 4B uses a generic basename `model.gguf` in a distinctive folder.

## C. Model service endpoints — listenability vs documentation

| Service | Endpoint | Evidence / status |
|---|---|---|
| KYNXA model gateway | `http://127.0.0.1:5218/api/local-models` | user verified GET (2026-10-22); **6 installed, 1 enabled, waiting-resource 1B when last checked** |
| Jan Local API Server | `http://127.0.0.1:1337/v1` | Notion historical Running/GET; latest KYNXA Saved connection; **Jan API actual model response in latest KYNXA attempt NOT VERIFIED** |
| Ollama local API | `http://127.0.0.1:11434/v1` | source-documented KYNXA preset; Ollama historically installed; **not freshly checked for responsiveness, models then EMPTY** |
| LM Studio local API | `http://127.0.0.1:1234/v1` | source-documented KYNXA preset; not proven started; **NOT VERIFIED on this PC** |
| KYNXA direct llama.cpp trial | `http://127.0.0.1:11888/v1` | previously PROPOSED only, not existing listening endpoint; **NOT STARTED/NOT VERIFIED** |

**No provider/server is permanently running just because an endpoint URL is recorded.** The loopback `127.0.0.1` addresses bind only to the same computer. Never copy local API keys into GitHub. Direct `11888` route was ONLY a hypothetical scripted test, not a service that the user launched.

## D. Retrieval for subsequent DJMRN and goose conversations
1. **READ THIS FILE FIRST** for installed apps, definitive GGUF snapshot locations and endpoint map; don't ask user to enumerate model files again.
2. Need models? Use the nine paths above. Need a runtime? The only directly confirmed full executable locations are Python, Git and Jan Agent. For other executables, keep **NOT_VERIFIED**, not fabricated.
3. Before **goose**: use preinstalled Python/Git if needed but **Desktop x64 CPU/non-CUDA release** preferred for AMD iGPU, only on user opt-in. No automatic model downloads, cloud accounts, full shell/file tool privileges, or multi-daemon stacks.
4. **Acceptance gate:** go from launch to a one-model plain Persian reply with no routine PowerShell and without unhealthy RAM pressure; permissions remain ask-first/disabled until separate test. If goose also requires unsupported resource-heavy/multi-engine plumbing, park it under same stop rule. First candidate KYNXA remains kept but PARKED.
5. Historical models/app inventory scope is AI + DJMRN dev components, **not a claim to list every Windows application or currently installed driver**.

## E. Sources / provenance
- [Canonical Notion Windows 11 desktop installation log](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3) — software/engine history and Jan Agent/Python/Git paths.
- [Nine actual user GGUF paths](../06-tests-and-evidence/logs/KYNXA-H3-GGUF-NINE-FILES-USER-INVENTORY-20261022.md) — exact paths and sizes.
- [KYNXA H2/H3 user observed state](../06-tests-and-evidence/logs/KYNXA-H3-PARKED-AUTOMATION-CRITERION-20261022.md) — permission/status/goose next candidate.
- [Official KYNXA v1.7.0 engine path/guard source](https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/agent-core/src/models/gateway_local_engine.rs) — versioned pattern only.
- [Official goose GitHub release and Windows Desktop assets](https://github.com/aaif-goose/goose/releases/tag/v1.55.0) — as researched 2026-10-22.

**No Windows side effects:** This inventory is a repo documentation write only. No hardware/environment changes or paid software activation.
