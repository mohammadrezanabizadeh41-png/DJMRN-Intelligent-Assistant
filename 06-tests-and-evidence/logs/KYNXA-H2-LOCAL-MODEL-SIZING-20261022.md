# KYNXA 1.7.0 installer — optional Qwen3 models on 8GiB laptop

**Date:** 2026-10-22. **Source:** user screenshot of the installer dropdown, real on-device Windows DIMM/free-RAM measurements, official KYNXA v1.7.0 catalog, official Qwen GGUF file listings. **Result is a provisional recommendation, not a runtime benchmark, download, approval or architecture adoption.**

## User's actual Windows resources
- Installed RAM: 8.00 GiB; visible to Windows: 5.88 GiB (hardware reservation approx. 2.12 GiB).
- Latest pre-install available RAM after restarting and keeping ChatGPT Desktop closed: **2.55 GiB**.
- KYNXA base host memory footprint has **NOT** been measured.

## Exact catalog model files and choice
Original KYNXA version-tagged `apps/agent-core/src/models/local_model_catalog.json`, `v1.7.0`, includes:
- Qwen3 1.7B Q8_0: **1,834,426,016 bytes (~1.83 decimal GB)**; catalog RAM recommendation **8 GB**. First trial model.
- Qwen3 4B Q4_K_M: **2,497,280,256 bytes (~2.50 decimal GB)**; catalog RAM recommendation **8 GB**. **Largest reasonable experimental candidate**, contingent on KYNXA no-model idle benchmark, headroom and responsiveness; not promised to run smoothly with only 5.88 GiB usable RAM.
- Qwen3 8B Q4_K_M: **5,027,783,488 bytes (~5.03 decimal GB)**; despite catalog recommendation 8 GB RAM, the user's OS usable 5.88 GiB and host/OS/KV cache overhead make this unsuitable for responsive local use.
- 14B Q4_K_M: **9,001,752,960 bytes (~9.00 decimal GB)**; exceeds OS-visible RAM before overhead.
- Larger 30B/32B variants are not appropriate for this device's local execution.

Sources: https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/agent-core/src/models/local_model_catalog.json ; https://huggingface.co/Qwen/Qwen3-4B-GGUF ; https://huggingface.co/Qwen/Qwen3-1.7B-GGUF . File download size is NOT equal to memory consumption: model runtime, Windows, KYNXA host, KV cache and context length add overhead, and pagefile swaps reduce responsiveness.

**Installer screenshot:** Dropdown includes 1.7B Q8_0, 4B Q4_K_M, 8B Q4_K_M, 14B Q4_K_M, 30B-A3B Q4_K_M, 32B Q4_K_M, 32B Q8_0. In earlier installation screenshot the `Download and enable` checkbox was unchecked. **User should keep it unchecked for initial installation**; model selection within the disabled dropdown alone should not download any weights.

**Next gated experiment:** After user reports completed install and no-model host idle memory, separately authorize downloading/enabling 1.7B and measure CPU/RAM/response; optionally test 4B Q4_K_M *one model at a time* if headroom allows. No model download, load or installation outcome has been reported in this conversation. D-005 overall stack remains NOT DECIDED.
