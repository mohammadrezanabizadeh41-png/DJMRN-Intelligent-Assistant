"""OH-19 approved atomic production import of the second 22 Freelancermap listings."""
import argparse,sqlite3,hashlib
from pathlib import Path
from contextlib import closing
from datetime import datetime,timezone
from urllib.parse import urlsplit
from ingest import load

def snap(db,t):
    rows=db.execute("SELECT * FROM "+t+" ORDER BY rowid").fetchall()
    return len(rows),hashlib.sha256(repr(rows).encode()).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--export",required=True)
    p.add_argument("--database",required=True)
    p.add_argument("--backups",required=True)
    p.add_argument("--approve",required=True)
    a=p.parse_args()
    if a.approve!="APPROVE_OH19_22":raise RuntimeError("APPROVAL_REQUIRED")
    items=load(a.export)
    if len(items)!=22:raise RuntimeError("EXPECTED_22_ROWS")
    for row in items:
        u=urlsplit(row["canonical_url"] or "")
        if u.scheme!="https" or u.hostname not in ("freelancermap.com","www.freelancermap.com") or not u.path.startswith("/project/"):
            raise RuntimeError("INVALID_FREELANCERMAP_URL")
    if len({r["canonical_url"] for r in items})!=22:raise RuntimeError("DUPLICATE_URL")
    path=Path(a.database).resolve(strict=True)
    backupdir=Path(a.backups).resolve(strict=True)
    if not backupdir.is_dir():raise RuntimeError("BACKUP_DIR_INVALID")
    with closing(sqlite3.connect(path,timeout=15)) as db:
        db.execute("PRAGMA foreign_keys=ON")
        if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise RuntimeError("DB_INTEGRITY")
        if db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()!=("djmrn.oh.local.v1",):raise RuntimeError("SCHEMA_VERSION")
        tables=("opportunities","opportunity_history","opportunity_details","outbound_attempts")
        before={t:snap(db,t) for t in tables}
        if [before[t][0] for t in tables]!=[22,22,2,0]:raise RuntimeError("BASELINE_CHANGED_REVIEW_REQUIRED")
        for row in items:
            if db.execute("SELECT 1 FROM opportunities WHERE source_site=? AND (external_id=? OR canonical_url=?)",(row["source_site"],row["external_id"],row["canonical_url"])).fetchone():
                raise RuntimeError("EXPORT_ALREADY_PRESENT_OR_CONFLICT")
        stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup=backupdir/("opportunities-pre-oh19-"+stamp+".sqlite3")
        with closing(sqlite3.connect(backup)) as b:db.backup(b)
        with closing(sqlite3.connect(backup)) as b:
            if b.execute("PRAGMA integrity_check").fetchone()[0]!="ok" or {t:snap(b,t) for t in tables}!=before:
                raise RuntimeError("BACKUP_VERIFY_FAILED")
        print("OH_19_BACKUP=PASS; FILE="+str(backup),flush=True)
        try:
            db.execute("BEGIN IMMEDIATE")
            for row in items:
                stamp=datetime.now(timezone.utc).isoformat()
                cur=db.execute("INSERT INTO opportunities(source_site,external_id,title,canonical_url,created_utc) VALUES(?,?,?,?,?)",
                    (row["source_site"],row["external_id"],row["title"],row["canonical_url"],stamp))
                db.execute("INSERT INTO opportunity_history(opportunity_id,event,old_title,new_title,old_url,new_url,recorded_utc) VALUES(?,?,?,?,?,?,?)",
                    (cur.lastrowid,"NEW",None,row["title"],None,row["canonical_url"],stamp))
            after={t:snap(db,t) for t in tables}
            if [after[t][0] for t in tables]!=[44,44,2,0]:raise RuntimeError("COUNT_MISMATCH")
            if any(after[t]!=before[t] for t in ("opportunity_details","outbound_attempts")):raise RuntimeError("OTHER_TABLE_CHANGED")
            if db.execute("PRAGMA foreign_key_check").fetchall():raise RuntimeError("FOREIGN_KEYS")
            if db.execute("PRAGMA quick_check").fetchone()[0]!="ok":raise RuntimeError("QUICK_CHECK")
            db.commit()
        except BaseException:
            db.rollback()
            raise
        if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise RuntimeError("POST_COMMIT_INTEGRITY")
        print("OH_19_PRODUCTION_IMPORT=PASS")
        print("EVENTS_NEW=22; BEFORE=22; AFTER=44; HISTORY_AFTER=44; DETAILS=2; OUTBOUND_ATTEMPTS=0")
        print("BACKUP_RETAINED=YES; OUTBOUND_ACTIONS=0; APPLICATIONS_USED=0")
if __name__=="__main__":main()
