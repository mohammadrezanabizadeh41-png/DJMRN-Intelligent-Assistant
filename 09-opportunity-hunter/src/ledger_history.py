"""OH-04 history extension. Synthetic database testing first."""
import sqlite3
from contextlib import closing
from datetime import datetime, timezone

def prepare(db_path):
    with closing(sqlite3.connect(db_path)) as db, db:
        db.execute("""CREATE TABLE IF NOT EXISTS opportunity_history (
            id INTEGER PRIMARY KEY, opportunity_id INTEGER NOT NULL,
            event TEXT NOT NULL, old_title TEXT, new_title TEXT,
            old_url TEXT, new_url TEXT, recorded_utc TEXT NOT NULL,
            FOREIGN KEY(opportunity_id) REFERENCES opportunities(id))""")

def record_with_history(db_path, item):
    from ledger import record
    site, external_id = item["source_site"], item["external_id"]
    with closing(sqlite3.connect(db_path)) as db:
        before = db.execute("SELECT id,title,canonical_url,status FROM opportunities WHERE source_site=? AND external_id=?", (site,external_id)).fetchone()
    result = record(db_path,item)
    if result["event"] in ("NEW","UPDATED"):
        with closing(sqlite3.connect(db_path)) as db, db:
            db.execute("INSERT INTO opportunity_history(opportunity_id,event,old_title,new_title,old_url,new_url,recorded_utc) VALUES(?,?,?,?,?,?,?)",
                (result["id"],result["event"],before[1] if before else None,item["title"],before[2] if before else None,item.get("canonical_url"),datetime.now(timezone.utc).isoformat()))
    return result
