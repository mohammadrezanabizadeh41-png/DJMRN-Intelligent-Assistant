import sqlite3
from contextlib import closing
from datetime import datetime, timezone

def record(db_path, item):
    site = item["source_site"]
    external_id = item["external_id"]
    title = item["title"]
    url = item.get("canonical_url")
    with closing(sqlite3.connect(db_path)) as db, db:
        existing = db.execute("SELECT id,title,canonical_url,status FROM opportunities WHERE source_site=? AND external_id=?", (site, external_id)).fetchone()
        if existing is None:
            cursor = db.execute("INSERT INTO opportunities(source_site,external_id,title,canonical_url,created_utc) VALUES(?,?,?,?,?)", (site,external_id,title,url,datetime.now(timezone.utc).isoformat()))
            return {"event":"NEW","id":cursor.lastrowid,"status":"DISCOVERED"}
        if (existing[1],existing[2]) == (title,url):
            return {"event":"SEEN","id":existing[0],"status":existing[3]}
        db.execute("UPDATE opportunities SET title=?,canonical_url=? WHERE id=?", (title,url,existing[0]))
        return {"event":"UPDATED","id":existing[0],"status":existing[3]}
