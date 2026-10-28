"""OH-13: approved backup-first outbound ledger schema migration; NO SEND."""
import argparse,sqlite3,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
from contextlib import closing

TABLES=("opportunities","opportunity_history","opportunity_details")
SCHEMA="""CREATE TABLE IF NOT EXISTS outbound_attempts (
 id INTEGER PRIMARY KEY,
 site TEXT NOT NULL,
 account TEXT NOT NULL,
 project_key TEXT NOT NULL,
 state TEXT NOT NULL CHECK(state IN ('RESERVED','SENT','UNKNOWN_SEND','FAILED_CONFIRMED')),
 created_utc TEXT NOT NULL,
 updated_utc TEXT NOT NULL,
 UNIQUE(site,account,project_key))"""
EXPECTED=["id","site","account","project_key","state","created_utc","updated_utc"]

def snapshot(db,table):
    rows=db.execute("SELECT * FROM "+table+" ORDER BY rowid").fetchall()
    return len(rows),hashlib.sha256(repr(rows).encode("utf-8")).hexdigest()

def run(args):
    dbpath=Path(args.database).resolve(strict=True)
    backupdir=Path(args.backups).resolve(strict=True)
    if not dbpath.is_file() or not backupdir.is_dir():raise ValueError("PATH_INVALID")
    with closing(sqlite3.connect(dbpath,timeout=15)) as db:
        db.execute("PRAGMA foreign_keys=ON")
        db.execute("PRAGMA busy_timeout=15000")
        if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise RuntimeError("SOURCE_INTEGRITY_FAILED")
        if db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()!=("djmrn.oh.local.v1",):raise RuntimeError("SCHEMA_VERSION_UNEXPECTED")
        before={t:snapshot(db,t) for t in TABLES}
        if [before[t][0] for t in TABLES]!=[22,22,2]:raise RuntimeError("UNEXPECTED_BASELINE")
        existed=db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='outbound_attempts'").fetchone() is not None
        if existed:
            cols=[r[1] for r in db.execute("PRAGMA table_info(outbound_attempts)")]
            if cols!=EXPECTED:raise RuntimeError("EXISTING_OUTBOUND_SCHEMA_UNEXPECTED")
            if db.execute("SELECT COUNT(*) FROM outbound_attempts").fetchone()[0]:raise RuntimeError("EXISTING_OUTBOUND_ROWS_REQUIRE_REVIEW")
        stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup=backupdir/("opportunities-pre-oh13-"+stamp+".sqlite3")
        with closing(sqlite3.connect(backup)) as b:db.backup(b)
        with closing(sqlite3.connect(backup)) as b:
            if b.execute("PRAGMA integrity_check").fetchone()[0]!="ok" or {t:snapshot(b,t) for t in TABLES}!=before:raise RuntimeError("BACKUP_VERIFY_FAILED")
        print("OH_13_BACKUP=PASS")
        print("BACKUP_FILE="+str(backup),flush=True)
        try:
            db.execute("BEGIN IMMEDIATE")
            db.execute(SCHEMA)
            cols=[r[1] for r in db.execute("PRAGMA table_info(outbound_attempts)")]
            if cols!=EXPECTED:raise RuntimeError("LEDGER_SCHEMA_MISMATCH")
            if db.execute("SELECT COUNT(*) FROM outbound_attempts").fetchone()[0]!=0:raise RuntimeError("LEDGER_NOT_EMPTY")
            if {t:snapshot(db,t) for t in TABLES}!=before:raise RuntimeError("ORIGINAL_DATA_CHANGED")
            if db.execute("PRAGMA foreign_key_check").fetchall():raise RuntimeError("FOREIGN_KEY_CHECK_FAILED")
            if db.execute("PRAGMA quick_check").fetchone()[0]!="ok":raise RuntimeError("QUICK_CHECK_FAILED")
            db.commit()
        except:
            db.rollback()
            raise
        if {t:snapshot(db,t) for t in TABLES}!=before:raise RuntimeError("POSTCOMMIT_ORIGINAL_DATA_CHANGED")
        print("OH_13_PRODUCTION_MIGRATION=PASS")
        print("OPPORTUNITIES=22; HISTORY=22; DETAILS=2; OUTBOUND_ATTEMPTS=0")
        print("ORIGINAL_DATA_UNCHANGED=YES; INTEGRITY=ok; FOREIGN_KEYS=ok")
        print("BACKUP_RETAINED=YES; SENDS=0")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    p.add_argument("--backups",required=True)
    p.add_argument("--approve-production-write",action="store_true")
    a=p.parse_args()
    if not a.approve_production_write:raise SystemExit("EXPLICIT_APPROVAL_FLAG_REQUIRED")
    run(a)
