"""OH-05 Windows real export integration, only on a disposable SQLite backup copy."""
import argparse
import sqlite3
import tempfile
from collections import Counter
from contextlib import closing
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ingest import load
from ledger_history import record_with_history

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--export",required=True)
    ap.add_argument("--database",required=True)
    args=ap.parse_args()
    source=Path(args.database)
    if not source.is_file(): raise RuntimeError("OPERATIONAL_DB_MISSING")
    records=load(args.export)
    if len(records)!=22: raise RuntimeError("UNEXPECTED_EXPORT_COUNT")
    with tempfile.TemporaryDirectory(prefix="djmrn-oh05-") as tmp:
        copy=Path(tmp)/"test.sqlite3"
        with closing(sqlite3.connect(f"file:{source.as_posix()}?mode=ro",uri=True)) as live,closing(sqlite3.connect(copy)) as test:
            live.backup(test)
        with closing(sqlite3.connect(copy)) as db:
            version=db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
            tables={r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if "opportunity_history" not in tables: raise RuntimeError("HISTORY_TABLE_MISSING")
            if not version or version[0]!="djmrn.oh.local.v1": raise RuntimeError("DB_SCHEMA_NOT_V1")
            before=db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
        first=Counter(record_with_history(str(copy),row)["event"] for row in records)
        second=Counter(record_with_history(str(copy),row)["event"] for row in records)
        with closing(sqlite3.connect(copy)) as db:
            after=db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
            integrity=db.execute("PRAGMA integrity_check").fetchone()[0]
        if first["NEW"]!=22 or second["SEEN"]!=22 or after-before!=22 or integrity!="ok":
            raise RuntimeError(f"TEST_ASSERTION_FAILED first={first} second={second} delta={after-before} integrity={integrity}")
        print("OH_05_REAL_EXPORT_LEDGER=PASS")
        print(f"VALIDATED_ROWS={len(records)}; FIRST_NEW={first['NEW']}; SECOND_SEEN={second['SEEN']}")
        print(f"TEMP_DB_COUNT={after}; TEMP_DB_INITIAL={before}; INTEGRITY={integrity}")
        print("OPERATIONAL_DATABASE_MODIFIED=NO")
    print("TEMP_COPY_CLEANUP=PASS")

if __name__=="__main__": main()
