# CAP-006 — DJMRN V0 read-only document search (no Agent / no LLM)

**Status:** SOURCE CREATED + 16 SYNTHETIC OFF-DEVICE TESTS PASS. **NOT RUN ON USER'S WINDOWS.**  
**Canonical owner/repo:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` — branch main. No dependency installation or model download.

This minimal CLI takes an explicitly provided directory (`--root`), 1–20 explicit **relative** `--file` paths, and a `--query`. It reads allowed **UTF-8 TXT/MD/CSV/JSON as plain lines** (not structured parsing), normalizes Persian Arabic `ك/ک`, `ي/ی/ى`, ZWNJ/tatweel and digit variants **only for matching**, and prints JSON results with original source lines, 1-based line numbers, relative file paths, raw-byte SHA256 and a repeatable request+content fingerprint.

## No-install local test command (NOT YET executed on user's Windows)
At the root of a local checkout on Windows, with a pre-existing supported Python interpreter:
```powershell
python "05-assistants-and-capabilities/src/document_search_v0/docsearch_v0.py" --root "05-assistants-and-capabilities/src/document_search_v0/fixtures" --file sample_alpha.txt --file sample_beta.md --query "كتاب"
```
Run only if the user separately approves on-device execution. For a safe independent test on non-user sandbox:
```sh
cd 05-assistants-and-capabilities/src/document_search_v0
python -m unittest discover -v
```
The command displays results on stdout only; it does **not** modify, rewrite, crawl or upload any selected file. Exit code 0 success, 2 rejected input. All samples are artificial and safe; no real customer information.

## Contract, limits and warnings
- Input = explicit root, exact allowlist, query; no glob, recursive scan, hidden network, database, background service or credential access.
- Rejects absolute/parent paths, symlink/junction components, unsupported suffix, non-UTF8, duplicates, size over 1MiB per file; limit 20 files / 100 matches.
- JSON status, error, `task_id` hash and per-file raw SHA are receipts, **not** a durable transaction ledger. `truncated` means more matches exist than the output limit.
- Matching runs per line; "relaxed-whitespace" removes spaces and can yield false positives. Always inspect cited raw original line. No Persian semantic accuracy claim, no OCR/PDF/Office or actual JSON field extraction.
- The allowlist checks are a defensive application restriction, **not an OS-level sandbox or atomic protection against hostile concurrent filesystem mutation**. Do not run against untrusted directories.
- Pure Python standard library; this component choice does not choose Python as the DJMRN control architecture. CPU/RAM/compatibility on Windows not yet measured.

## Source/tests
- `docsearch_v0.py` Git blob `0376c8d4a800d0a60b5137d08de6071e46178398`
- `test_docsearch_v0.py` Git blob `982a63f72e4fe0f0b080ba57effcf86fa65fc727`
- [Test register](../../../06-tests-and-evidence/TEST-REGISTER.md) and [evidence](../../../06-tests-and-evidence/logs/NEW-V0001-20261020.md).
- [Decision and scope](../../../02-project-management/V0-BUILD-DECISION.md), [technology comparison](../../../03-architecture-and-tools/V0-TECH-CHOICE.md).

## User-approved next test (2026-10-20)
User authorized **synthetic-only Windows smoke**; **not executed yet**. Follow [WINDOWS-SMOKE-PROTOCOL](WINDOWS-SMOKE-PROTOCOL.md). The packaged 4 code/fixture files are byte-identical with this repo's source blobs; the temporary chat ZIP is SHA256 `f6228e06b9efc565c971e08f6404e05f8fc9dbc4e625879d420130a9f0026af4`. Stop on any verification failure; no Python install and no private document read. [Self-contained continuity](../../../07-operations-and-continuity/PROJECT-STATE-HANDOFF-20261020.md).

## Windows first attempt was blocked (NEW-V0002, 2026-10-20)
User reported SHA mismatch for `fixtures/sample_alpha.txt` after extraction and **before any Python tests**. Original ZIP + embedded file hashes match published values in assistant container; user Windows extracted hash and cause unknown. [Failure record](../../../06-tests-and-evidence/logs/NEW-V0002-20261020.md). Do not skip integrity check or mark Windows PASS; inspect existing extracted file with read-only diagnostic.
