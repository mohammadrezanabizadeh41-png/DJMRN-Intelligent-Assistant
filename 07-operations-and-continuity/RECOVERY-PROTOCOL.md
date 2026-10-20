# Recover project state after interruption or failed write
1. Check `https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` with GitHub connected app, branch `main`, HEAD SHA, repo visibility and read permission. Treat unexpected repo missing/access failure as **BLOCKED**, do not use another similarly named repo.
2. Read README, PROJECT-RULES, CURRENT, TASK and Work LEDGER. Check newest commit and CHANGELOG before making an overwrite; reconcile exact path and SHA.
3. For pending Work request: request exists? response exists? report readback verified? review exists? source and STATUS accurate? If partial, record BLOCKED/NEEDS-REVIEW, not pretend complete.
4. If a GitHub write returned network/error unknown, **fetch file/ref before retry**. Do not reuse or increment WQ ID blindly; do not clobber Work answers or user commits.
5. If tool response seems inconsistent with Notion, check current canonical documents and source dates, tag discrepancy, do not silently override one authority.
6. Historical test proves only exact fixture; local Windows running state is UNKNOWN without current user-approved inspection.
7. After a verified change, write short changelog + task status + CURRENT, including next bounded action. Avoid storing raw secrets or large dumps.
8. To recover a broken workflow, favor reversible action and original Git version; force pushes, deletion or destructive migration require explicit user approval.
