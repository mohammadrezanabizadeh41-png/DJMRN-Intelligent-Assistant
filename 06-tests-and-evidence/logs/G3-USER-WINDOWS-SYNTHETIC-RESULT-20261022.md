# DJMRN G3-USER-WIN-001 — first real Windows 11 synthetic probe receipt (user-reported)

**Date:** 2026-10-22. **Status:** `USER-REPORTED WIN11 SYNTHETIC PASS FOR EXECUTED CASES / G3 OVERALL PARTIAL_G3_HOLD`. **Source authority:** actual user-pasted terminal JSON in ChatGPT conversation, reviewed against the unchanged canonical GitHub runner and G2A Windows reader. **Not:** independently observed Windows process trace, production safety proof, operator-grant test, Jan/model/assistant integration or permission to remove any guard.

## Scope and verified project source

- **Repository:** private `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, branch `main`; read before this report at `64e21158d3b239b04d671afad3c2ccdc528a1221`. Existing original [runner](../../05-assistants-and-capabilities/src/m1_pilot/g3_synthetic_probe.py) Git blob `1988282914635940e485dc246a0b6ff0fc87db6b`, [Win32 reader](../../05-assistants-and-capabilities/src/m1_pilot/core/windows_reader.py) Git blob `730f35208dd7f3f08cec3260b4fe7ef775d2faa2`, [fail-closed guard](../../05-assistants-and-capabilities/src/m1_pilot/core/windows_guard.py) Git blob `2ad992932489b1f12417c9e5e5eb4a1d2c40d12a`.
- **User authorization:** explicit prior `بله` specifically for two synthetic files, no install, no real document, no account/provider, no Jan. [Authorization journal](../../07-operations-and-continuity/WORK-JOURNAL.md).
- **Prior attempt:** original CMD invoked Microsoft Store WindowsApps alias instead of real Python; interpreter discovery was patched in [commit `d4e2ab5`](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/d4e2ab522801836c34557dda6e94cd6f7f773db0). A later user screenshot showed interpreter found and the no-run preflight passed, with `Decision:` prompt.
- **This receipt:** user pasted subsequent full terminal output after entering `RUN`, including JSON and `Press any key to continue...`. No raw personal paths, file contents, usernames, credentials or device IDs included. Direct remote command execution, independent OS/file audit, or separate source-bundle attestation were NOT performed by coordinator. A pinned source is a runtime claim from the probe; only its code's known behavior can be cross-checked here.

## Reported per-case results, matched to the exact GitHub runner

| Case | User-reported status | Detail | What that particular test actually exercises |
|---|---|---|---|
| G3-00A | PASS | OK | Check hashes of three existing project core source blobs, not independent hash of runner .py or .cmd |
| G3-00B | PASS | NTFS_HANDLE_ENROLLMENT | Real Win32 handle metadata for two synthetic .md fixtures; volume serial/index, size, type and final path |
| G3-01 | PASS | TWO_SAME_HANDLE_SNAPSHOTS | Read both approved synthetic payloads; compare bytes and SHA; no path-reopening fallback from CAP |
| G3-02 | PASS | OUTSIDE_MANIFEST | Third/unapproved **ID** rejected and tracked CreateFile count unchanged; no third file created or accessed |
| G3-02B | PASS | INVALID_SELECTION | Duplicate ID denied |
| G3-03 | PASS | HASH_MISMATCH | Same-byte-length fixture change after enrollment rejected by SHA mismatch |
| G3-04 | PASS | IDENTITY_OR_SIZE | Fixture replacement by the other approved file rejected based on identity/size; **not a concurrent race** |
| G3-04B | NOT_RUN | REPARSE_AND_CONCURRENT_RACE | Junction/reparse and active rename/race still need a bounded new test |
| G3-05 | NOT_RUN | CANCELLATION_UNIMPLEMENTED | No cooperative cancellation hook or cancel-in-flight test |
| G3-06 | PASS | OK | Test wrapper's intercepted `CreateFileW/CloseHandle` counts balanced for its covered read paths; **not an OS-wide handle leak audit** |
| G3-07 | PASS | M1_STILL_BLOCKED | Direct call to `require_verified_read` remains unconditionally denied; **not** an end-to-end Jan/dispatcher run |
| G3-08 | PARTIAL | NO_NETWORK_CODE; NOT_MONITORED | Runner has no explicit network operations; **no independent egress monitor** |

**Totals:** 9 PASS; 2 NOT_RUN; 1 PARTIAL; 0 FAIL in the JSON provided. Summary reported `"device_tested": true`, `"overall": "PARTIAL_G3_HOLD"`, `"cleanup": "OWN_FIXTURES_REMOVED"`. Cleanup is a user-program-reported result, **not an independently checked filesystem inventory**.

## Bounded engineering interpretation

1. **Now supported (within the synthetic scenario, as user-reported):** Windows API code executed, real NTFS handle enrollment + same-handle read succeeded, expected identity/hash/selection denials occurred, covered handle closes balanced and existing guard stayed blocked.
2. **Not proven:** symlink/junction ancestor attacks, actively concurrent race, trusted owner SID and user consent binding, revoke/cancellation mid-read, full error/fault injection and resource tracking, network egress, all device storage types, malware resistance/OS sandbox guarantees, or real conversational file-access safety.
3. **No change authorized or performed:** `core/windows_reader.py`, `core/windows_guard.py`, `core/session.py`, CAP original file search, Jan, inference/model runtimes, user accounts, system settings. `D-005` remains undecided; the file boundary must **continue to fail closed**. Do not equate 9 PASS with a finished G3/security sign-off.
4. **Smallest next investigation:** a code-reviewed synthetic-only G3-B harness for junction/reparse/rename negative behavior and a cooperative cancellation + handle cleanup contract (with negative tests). Evaluate whether the cancellation requirement belongs to the reader or the calling session; maintain separate operator-approval path. Avoid new framework, admin rights, browser/network, third user-document access and source/authority duplication. A later laptop run changing test scope requires explicit consent.

**Provenance warning:** this document records what the user actually reported and what the pinned source implements; it does not independently verify the laptop's exact binary and environment. There are no independent executable logs outside this conversation.
