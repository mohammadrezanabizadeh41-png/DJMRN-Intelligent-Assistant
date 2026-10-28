"""OH-04 atomic history extension for the existing SQLite schema."""
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
    site, eid, title = (item.get(k) for k in ("source_site", "external_id", "title"))
    url = item.get("canonical_url")
    if any(not isinstance(v, str) or not v.strip() for v in (site, eid, title)):
        raise ValueError("REQUIRED_FIELDS")
    if url is not None and not isinstance(url, str):
        raise ValueError("INVALID_URL")
    with closing(sqlite3.connect(db_path, timeout=5)) as db:
        db.execute("PRAGMA foreign_keys=ON")
        db.execute("BEGIN IMMEDIATE")
        try:
            before = db.execute("SELECT id,title,canonical_url,status FROM opportunities WHERE source_site=? AND external_id=?", (site, eid)).fetchone()
            if before is None:
                stamp = datetime.now(timezone.utc).isoformat()
                cur = db.execute("INSERT INTO opportunities(source_site,external_id,title,canonical_url,created_utc) VALUES(?,?,?,?,?)", (site,eid,title,url,stamp))
                oid, event, status = cur.lastrowid, "NEW", "DISCOVERED"
            else:
                oid, status = before[0], before[3]
                event = "SEEN" if (before[1],before[2]) == (title,url) else "UPDATED"
                if event == "UPDATED":
                    db.execute("UPDATE opportunities SET title=?,canonical_url=? WHERE id=?", (title,url,oid))
            if event != "SEEN":
                db.execute("INSERT INTO opportunity_history(opportunity_id,event,old_title,new_title,old_url,new_url,recorded_utc) VALUES(?,?,?,?,?,?,?)",
                    (oid,event,before[1] if before else None,title,before[2] if before else None,url,datetime.now(timezone.utc).isoformat()))
            db.commit()
        except BaseException:
            db.rollback()
            raise
    return {"event":event,"id":oid,"status":status,"outbound_actions":0}
