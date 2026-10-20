# DJMRN — Mandatory Work Repository Identity Lock (D-010)

Effective: 2026-10-20 | USER-DIRECTED | Project research protocol

## Canonical target for THIS project's WQ/WA

- Exact `repository_full_name`: **`mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`**
- Exact URL: **https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant**
- Branch: **`main`** unless a user-approved request specifies another *existing branch in the same repo*.
- Work request: `04-work-research-bridge/requests/WQ####.md`
- Work report ONLY: `04-work-research-bridge/responses/WA####.md`
- Work may write the **single authorized report file**; it may not edit the request, other GitHub files, reviews, ledger, status, Notion, Windows or connected accounts.

## Similar name = NOT same repository

- `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` is the **separate Applied research library bridge**. May be **read-only** research input, NEVER the WQ/WA output target.
- Any older repo named DJMRN, `djmrn`, similarly named owner/repo, or a prior connected GitHub window is NOT an automatic fallback.
- The relative path `04-work-research-bridge/` is insufficient to determine destination. Never rely on memory or fuzzy GitHub search to choose a write repository.

## Mandatory Work preflight — stop on mismatch

1. Receive the fully qualified **owner/repo**, **URL**, **branch**, **WQ file** and **WA destination** in the dispatch/request. These values MUST agree with this lock file.
2. Fetch repository metadata using exact repository lookup / exact URL and check `full_name === "mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant"`; verify branch is `main`. If repo identity or write scope cannot be verified, return **BLOCKED; DO NOT WRITE**.
3. Fetch *this lock file*, `04-work-research-bridge/README.md`, and the exact `requests/WQ####.md` **from that verified repo**. Verify WQ/WA ID pair and exact response path; do not guess the ID.
4. If any context points to `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` or another repository for output, **STOP**, report the conflict; no copying/migrating reports between repos without explicit user instructions.
5. Commit only `04-work-research-bridge/responses/WA####.md` to `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`. Report research status separately from artifact persistence.
6. **Read back from the same owner/repo and target commit/branch**. Verify exact response file path, WQ/WA ID, and the saved response blob SHA / commit SHA. A good commit in a *different repo* is a FAILURE for this request.
7. Short Work final receipt must contain:
   ```text
   repository_full_name: mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant
   WQ####/WA#### | SUCCESS/PARTIAL/BLOCKED
   commit: <actual SHA or NONE>
   response_blob: <actual SHA or NONE>
   readback: VERIFIED / NOT VERIFIED
   ```
   If mismatch or uncertain GitHub write, say BLOCKED and **do not retry on an alternate repo**.

## Independent coordinator verification

Upon receiving a receipt, coordinator uses exact `repository_full_name` in its GitHub tool to fetch response and commit, ensures target file and WQ/WA IDs match, compares hashes, and reads back content before advancing LEDGER or accepting research. Wrong repo = `WRONG-REPO/BLOCKED`; do not automatically copy the artifact over.

This governance applies to **future requests**, without silently editing immutable WQ0001/WA0001 or older GitHub receipts. It grants no permission to run local tests, install tools, activate accounts, spend money or modify another repository.
