"""DJMRN Opportunity Hunter OH-W2: local-only SQLite bootstrap, no browser/network/send.

Run: py bootstrap.py --root <Windows OpportunityHunter path>
"""
import argparse
import json
from pathlib import Path
import sqlite3
from datetime import datetime, timezone

VERSION = "djmrn.oh.local.v0"
DIRS = ("app", "config", "data", "logs", "exports", "backups")

def bootstrap(root: Path):
    root = root.expanduser().resolve()
    if not root.is_dir() or any(not (root / name).is_dir() for name in DIRS):
        raise ValueError("EXPECTED_WINDOWS_FOLDERS_MISSING")
    db_path = root / "data" / "opportunities.sqlite3"
    with sqlite3.connect(db_path, timeout=5) as db:
        db.execute("PRAGMA foreign_keys=ON")
        db.execute("PRAGMA busy_timeout=5000")
        db.execute("""CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY, value TEXT NOT NULL
        )""")
        db.execute("""CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_site TEXT NOT NULL,
            external_id TEXT NOT NULL,
            canonical_url TEXT,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'DISCOVERED'
                CHECK(status IN ('DISCOVERED','REVIEW','REJECTED','DRAFTED','SENT','UNKNOWN_SEND','REPLIED')),
            created_utc TEXT NOT NULL,
            UNIQUE(source_site,external_id)
        )""")
        db.execute("INSERT OR IGNORE INTO metadata(key,value) VALUES('schema_version',?)", (VERSION,))
        version = db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()[0]
        if version != VERSION:
            raise ValueError("SCHEMA_VERSION_MISMATCH")
        count = db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
        check = db.execute("PRAGMA quick_check").fetchone()[0]
        if check != "ok":
            raise RuntimeError("SQLITE_QUICK_CHECK_FAILED")
    return {"result":"PASS","schema_version":VERSION,"root":str(root),
            "database":str(db_path),"opportunities":count,
            "sqlite_quick_check":check,"outbound_actions":0}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root",required=True)
    args = parser.parse_args()
    print(json.dumps(bootstrap(Path(args.root)),ensure_ascii=False,indent=2))
