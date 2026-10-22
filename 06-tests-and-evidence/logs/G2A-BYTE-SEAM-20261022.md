# G2A BYTE-SEAM-001 — CAP-006 additive no-path-reopen API and bounded off-device smoke

**Date:** 2026-10-22 | **Execution claim:** **ISOLATED PURE-FUNCTION OFF-DEVICE SMOKE 4/4 PASS**, NOT full canonical CAP-006 suite, NOT user's Windows/G3 and NOT an OS security proof.  
**User authorization:** `اوکی انجام بدیم` following explicit recommendation to investigate the CAP-006 path reopen race and, if needed, make a narrow source modification.  
**Canonical repo:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` / `main`.  
**Implementation commit:** [0fb92f7d188f8ade8bf4641146e0b0c0bcd1b5f2](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/0fb92f7d188f8ade8bf4641146e0b0c0bcd1b5f2), parent `3f18d5f2bf8ff15acf952db61148aff48c6f01fa`.

## 1. Why a change was necessary

Before this patch existing `docsearch_v0.search(root, selected, query)` resolves paths and does `file.stat(); file.read_bytes(); file.stat()`. G2A's separate guard could inspect a handle but passing the filename back into legacy CAP reopens the path, leaving a TOCTOU/file-switch gap. Even equal pre/post hashes are insufficient to prove no unauthorized bytes were temporarily accessed. Windows CreateFile/FILE_FLAG_OPEN_REPARSE_POINT documentation further cautions that reparse behavior is context-specific; source/API research cannot replace an OS-specific threat-model review and tests.

The patch **adds** `search_preloaded_bytes(documents: list[tuple[str,bytes]], query, limit=8)`, strictly a pure byte-snapshot analyzer. It accepts only one/two distinct relative `.md` labels, <=1MiB bytes/file and max8 match results, checks UTF-8, keeps original lines, matches with existing `normalize()` and `_compact()`, hashes raw bytes and returns a legacy-shaped result with `permission_scope="caller-supplied-bytes/NOT-OS-authorized"`. **It never opens a path**. Caller remains responsible for Windows file identity and human permission. Not a standalone new security gate.

**Legacy preservation proof:** programmatic comparison of the GitHub original blob `0376c8d4a800d0a60b5137d08de6071e46178398` against patched blob `708abfb4ee092f26a58d51194567e5ed52cc2e98` after removing only the added `search_preloaded_bytes` block produced **exact original complete source text**. The unchanged `search()` and CLI continue as before. Tests were added to existing `test_docsearch_v0.py` without deleting previous cases.

## 2. Actual off-device narrow smoke

Assistant's isolated Python 3.13 container copied the pure new function and its `normalize/_compact` helpers (not a checkout/materialization of the private repo), using synthetic inline byte strings. The following **4** isolated unit tests completed PASS in ~0.002s:

1. Persian `كتاب/کتاب`, digit variants, first line and original raw-byte SHA256, while `Path.read_bytes` was mocked to reject all calls.
2. Invalid path labels/extension, duplicate and third file, invalid UTF-8 and non-bytes inputs all rejected.
3. Result limit/truncation and boolean limit rejection.
4. Document sorting deterministic by relative display label.

**Limits:** these are not the repository's 16 pre-existing CAP tests, nor the four newly committed repository test methods run as part of the full suite. No complete Python 3.14 user-Windows execution, real Win32 handles, G3 race/symlink/junction/hardlink, Jan/LLM tool calling, source/card rendering, model download or any real user file read performed. Existing CAP behavior was compared *structurally* via exact original code restoration, not regression-tested by running the full suite in this turn. The test source is reproduced in GitHub repository tests for a later separately authorized run.

## 3. GitHub write and readback

Git compare `3f18d5f..`→`0fb92f7..`: **one commit, five modified paths, zero modifications outside CAP-006 and `m1_pilot`**, precisely:
- `05-assistants-and-capabilities/src/document_search_v0/docsearch_v0.py`: additive 96 lines.
- `05-assistants-and-capabilities/src/document_search_v0/test_docsearch_v0.py`: additive 53 test lines.
- `05-assistants-and-capabilities/src/document_search_v0/README.md`: source-only API note.
- `05-assistants-and-capabilities/src/m1_pilot/core/windows_guard.py`: HOLD points to preloaded API and need for verified reader; **still ALWAYS raises `WindowsGuardHold`**.
- `05-assistants-and-capabilities/src/m1_pilot/README.md`: update that CAP source has an additive API while M1 does not call it.

GitHub main equals commit `0fb92f7d188f8ade8bf4641146e0b0c0bcd1b5f2` on implementation readback. No Jan/config/model/GUI/installation/provider changes.

## 4. Remaining hard HOLD / next scope

**Not solved:** A future Windows component must obtain a specific file handle, authenticate it against a human-approved manifest/volume/file identity, check reparse/hardlink/rename and trustworthy same-handle bytes under Windows constraints, then supply those exact bytes to the pure API. `m1_pilot/core/session.py` **must remain fail-closed and must not call any real CAP path read until this path is independently designed, audited, approved and tested**. If a security requirement cannot be met, do not silently fall back to legacy `search(root,...)`. A Windows G3 execution/installation needs its own user authorization. The next work should target **source-only verified-handle design and implementation plus off-device mock/contract tests**; no automatic Jan adapter or full independent UI.

**Disposition:** `G2A BYTE INTERFACE CREATED / LEGACY PRESERVED / OS VERIFIED-READER AND COMPLETE M1 STILL HOLD`.
