# Evidence provenance & result handling
- For each important claim: **type** (OFFICIAL FACT/USER OBSERVATION/WORK REPORT/INDEPENDENT TEST/ASSUMPTION/JUDGMENT), observed date, exact URL/file path, version/hash/commit as possible, context, limitations.
- Report `PASS` only for tested scope. If tool call returned success but no content readback → `WRITE RETURNED / NOT VERIFIED`; if only user pasted command output → `USER-REPORTED PASS`.
- Do not upload unredacted system dumps, private path with username, serials, customer data, API keys, OAuth artifacts, browser cookies or raw messages to repo. Sanitize before commit, not after.
- Keep failures and negative evidence with cause UNKNOWN when not established; do not erase old records to make new option look better.
- Raw machine evidence remains at device/source unless securely captured/authorized; this repo stores minimal sanitized extract + source and hash where appropriate. GitHub private != secret vault.
- Work returns research evidence candidates; Coordinator validates/decides; User authorizes actions.
