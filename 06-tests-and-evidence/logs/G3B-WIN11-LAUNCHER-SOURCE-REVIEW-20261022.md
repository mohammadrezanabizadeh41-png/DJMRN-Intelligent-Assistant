# DJMRN G3-B — final source review, opt-in Windows launcher and isolated tests

**Date:** 2026-10-22. **Classification:** `TESTED-OFFDEVICE / G3-B WINDOWS DEVICE NOT_RUN / NOT USER-APPROVED / FILE GUARD HOLD`.
**Canonical project:** private `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` branch `main`. User asked to conduct code review and prepare launcher, not to execute a new Windows file test.

## Authority and exact-source review

Before any change, live Notion **DJMRN — Persistent Operating Memory** and **DJMRN — Tool Governance & Architecture Intelligence** fetched and actual private repository `main@cec13d50a57cfb022aeb078cfbac5cf3158092bb` verified. Inspected PROJECT-RULES, leading CURRENT, the candidate G3B runner, its 15 pre-existing tests, Win32 reader, original G3 runner and launcher, G3B test protocol/evidence. Primary official [Python 3.14 pathlib](https://docs.python.org/3.14/library/pathlib.html) documents `Path.is_junction()` (added in Python 3.12); [Microsoft CreateFile sharing](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew) documents `FILE_SHARE_DELETE` interactions. These primary docs do NOT prove this custom test's safety.

## Security findings and precise changes

1. **Old candidate cleanup gap:** only `is_symlink` tested, with no explicit rejection of junction path or unexpected created filename. Revised test-only `fixture_cleanup` rejects a junction/symlink folder or file, >2/duplicate/unexpected fixture paths, and stops for manual investigation rather than attempting a broad recursive removal. Junction checks require **Python 3.12+**, so the candidate device path now stops for older interpreters (known prior user laptop Python 3.14.7, current installation still subject to local preflight). Still not an atomic OS sandbox against an adversarial path swap.
2. **Old candidate source verification gap:** the candidate supported only a default plan or live run, without explicit source-only verification command. Added `--verify-source`, which validates pinned exact Git blobs of existing G3/core files and returns without creating synthetic fixtures. It remains separate from `--run-synthetic`. 
3. **New launcher:** [`G3B-REVIEW-AND-RUN.cmd`](../../05-assistants-and-capabilities/src/m1_pilot/G3B-REVIEW-AND-RUN.cmd) avoids WindowsApps `python` aliases by preferring a working `py -3`, then tested `python`, then existing per-user Python 3.14. It verifies **the new G3B runner's exact Git blob first**, then asks that runner to verify pinned dependencies, and only then launches its interactive `--run-synthetic` flow. The **literal `RUN` prompt is in Python**, default Enter aborts with zero file tests. User must separately authorize laptop testing before typing RUN.
4. **No test scope enlargement:** exactly two fake Markdown names `alpha.md`/`beta.md` under unique local temporary NTFS folder; one attempt to rename/replace between those same files while approved handles are held; local test-only result-revocation fence; guard must remain closed. Real junction construction, adversarial concurrent races, OS `CancelSynchronousIo`, independent native egress inspection and production permission binding all remain NOT_RUN/UNPROVEN. No Jan/CAP/session/guard integration or real documents.
5. **Integrity caveat:** the launcher checks the *runner* Git blob, and runner verifies four pinned dependencies. The launcher itself is not OS-signed; no immutable trust anchor or independent local executable attestation. Source-check success alone is not execution authorization.

## Exact GitHub source receipts

| Artifact | Current Git blob (readback and local match) | Role |
|---|---|---|
| [G3B test runner](../../05-assistants-and-capabilities/src/m1_pilot/g3b_synthetic_probe.py) | `dc7ad400f6a25749f4ad7c47d6f121f26aa67465` | Test-only candidate, Python 3.12+ |
| [G3B harness tests](../../05-assistants-and-capabilities/src/m1_pilot/tests/test_g3b_probe_offdevice.py) | `9ed250be6f6b3072595a156a5b206a7409ce65e0` | Original 15 + 4 new checks |
| [G3B Windows launcher](../../05-assistants-and-capabilities/src/m1_pilot/G3B-REVIEW-AND-RUN.cmd) | `478f5ee88dde0f14825e440ca32257dd9e691aa0` | Python discovery + pin-first review + interactive test gate |
| [Launcher static tests](../../05-assistants-and-capabilities/src/m1_pilot/tests/test_g3b_launcher_static.py) | `df7833918220b0808817c48ab679bb9cd7b366c1` | Six static source/ordering tests |
| Existing [Win32 reader](../../05-assistants-and-capabilities/src/m1_pilot/core/windows_reader.py) | `730f35208dd7f3f08cec3260b4fe7ef775d2faa2` | UNCHANGED; only original source/mock and prior bounded user G3 |
| Existing [M1 guard](../../05-assistants-and-capabilities/src/m1_pilot/core/windows_guard.py) | `2ad992932489b1f12417c9e5e5eb4a1d2c40d12a` | UNCHANGED, unconditionally denies |

## Actual isolated verification

Assistant-owned Linux Python 3.13.5, using exact original reader/manifest and test sources plus new test-only candidate. No user's Windows execution or new filesystem permission. Command:

```sh
PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s tests -p 'test_*.py' -v
```

**Result: `Ran 37 tests in 0.011s — OK` (37 PASS / 0 FAIL / 0 SKIP).** Breakdown: 12 old exact-reader Win32 API mocks; 19 candidate/offdevice checks including four new safety conditions; six new **static** launcher checks. Ran default runner locally: `G3-B PLAN ONLY`. Attempted `--run-synthetic` in Linux: expected `FAIL_HOLD/WINDOWS_ONLY` exit 2, no fixture created. Static launcher tests do NOT execute cmd.exe or prove Windows quoting/runtime behavior.

**No new Win11 proof:** original G3 user-reported Windows test 9 PASS/2 NOT_RUN/1 PARTIAL is still the last observed native execution; new G3B has **NOT_RUN** on Windows. No actual junction, active adversarial race, OS cancellation, native egress monitor, owner consent, production security or Jan model/file access was enabled.

## Gating status

`CODE REVIEW AND LAUNCHER SOURCE READY / 37 ISOLATED TESTS PASS / G3-B WINDOWS NOT_RUN / G3 PARTIAL_G3_HOLD`.

The next consequential action is a **separate user approval** for one controlled G3B user-local test of two fictitious files, including an attempted replacement of one synthetic file with the other. No installer, admin permissions, registry/network/system changes or personal file reads are authorized. On failure, stop and report a sanitized result; do not auto-retry, bypass OS warnings, run as Administrator, install libraries or force-delete any leftover fixtures.
