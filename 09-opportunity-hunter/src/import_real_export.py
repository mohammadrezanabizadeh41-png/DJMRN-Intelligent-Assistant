"""OH-05 explicitly approved production import, guarded by backup and preflight."""
import argparse
import sqlite3
import shutil
from collections import Counter
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest import load
from ledger_history import record_with_history

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--export",required=True)
    p.add_argument("--database",required=True)
    p.add_argument("--backups",required=True)
    p.add_argument("--approve",required=True)
    a=p.parse_args()
    if a.approve!="APPROVE_OH05_22": raise RuntimeError("APPROVAL_TOKEN_MISSING")
    dbpath=Path(a.database).resolve(strict=True)
    rows=load(a.export)
    if len(rows)!=22 or any(r["source_site"]!="freelancermap" for r in rows):
        raise RuntimeError("EXPORT_NOT_APPROVED_22")
    with closing(sqlite3.connect(f"file:{dbpath.as_posix()}?mode=ro",uri=True)) as db:
        version=db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
        if not version or version[0]!="djmrn.oh.local.v1":raise RuntimeError("SCHEMA_VERSION_MISMATCH")
        if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise RuntimeError("DB_INTEGRITY_FAILED")
        tables={r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not {"opportunities","opportunity_history"}.issubset(tables):raise RuntimeError("TABLES_MISSING")
        old_count=db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
        old_history=db.execute("SELECT COUNT(*) FROM opportunity_history").fetchone()[0]
        old_ids={(r[0],r[1]) for r in db.execute("SELECT source_site,external_id FROM opportunities")}
    backups=Path(a.backups)
    if not backups.is_dir():raise RuntimeError("BACKUP_DIR_MISSING")
    stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup=backups/("opportunities-pre-oh05-"+stamp+".sqlite3")
    if backup.exists():raise RuntimeError("BACKUP_COLLISION")
    with closing(sqlite3.connect(f"file:{dbpath.as_posix()}?mode=ro",uri=True)) as src, closing(sqlite3.connect(backup)) as dst:
        src.backup(dst)
    with closing(sqlite3.connect(backup)) as check:
        if check.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise RuntimeError("BACKUP_INTEGRITY_FAILED")
        if check.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]!=old_count:raise RuntimeError("BACKUP_COUNT_MISMATCH")
    print("OH_05_BACKUP=PASS",flush=True)
    print("BACKUP_FILE="+str(backup),flush=True)
    print("IMPORT_ROWS="+str(len(rows)),flush=True)
    results=Counter()
    for row in rows:
        event=record_with_history(str(dbpath),row)["event"]
        results[event]+=1
    with closing(sqlite3.connect(f"file:{dbpath.as_posix()}?mode=ro",uri=True)) as db:
        final_count=db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
        final_history=db.execute("SELECT COUNT(*) FROM opportunity_history").fetchone()[0]
        integrity=db.execute("PRAGMA integrity_check").fetchone()[0]
        stored=sum(db.execute("SELECT COUNT(*) FROM opportunities WHERE source_site=? AND external_id=?",(row["source_site"],row["external_id"])).fetchone()[0] for row in rows)
    if integrity!="ok" or stored!=22 or final_count!=old_count+results["NEW"]:
        raise RuntimeError("POST_IMPORT_VERIFICATION_FAILED; RESTORE_FROM_BACKUP_MANUALLY")
    print("OH_05_PRODUCTION_IMPORT=PASS")
    print("EVENTS_NEW={}; EVENTS_SEEN={}; EVENTS_UPDATED={}".format(results["NEW"],results["SEEN"],results["UPDATED"]))
    print("BEFORE={}; AFTER={}; HISTORY_BEFORE={}; HISTORY_AFTER={}".format(old_count,final_count,old_history,final_history))
    print("VERIFIED_STORED={}; INTEGRITY={}; OUTBOUND_ACTIONS=0".format(stored,integrity))
    print("BACKUP_RETAINED=YES")

if __name__=="__main__":main()
