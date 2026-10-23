DJMRN P2F synthetic-only one-shot 2026-10-23; no provider API, accounts, customer data, Windows, paid operations. Two Docker internal bridges only.

P2F retry1: add startup trace safe diagnostics; previous Actions 39965861881 73/73 source tests, P2F front not ready after 35 seconds. No provider/window/paid access.

Retry 2: previous run 39966303514 exact PermissionError /ledger/initialized.marker due --cap-drop ALL root vs runner-owned mode0700 volume; run adapter as same host UID:GID, preserve private 0700, no privilege broaden.
