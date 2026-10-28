import sqlite3
from contextlib import closing
import tempfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ledger import record

with tempfile.TemporaryDirectory(prefix="djmrn-oh04-") as tmp:
    dbpath = str(Path(tmp) / "test.sqlite3")
    with closing(sqlite3.connect(dbpath)) as db, db:
        db.execute("CREATE TABLE opportunities (id INTEGER PRIMARY KEY AUTOINCREMENT, source_site TEXT NOT NULL, external_id TEXT NOT NULL, canonical_url TEXT, title TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'DISCOVERED', created_utc TEXT NOT NULL, UNIQUE(source_site,external_id))")
    item = {"source_site":"freelancermap","external_id":"synthetic-001","title":"Video editing","canonical_url":"https://example.invalid/001"}
    first = record(dbpath,item)
    second = record(dbpath,item)
    changed = dict(item, title="Video editing revised")
    third = record(dbpath,changed)
    with closing(sqlite3.connect(dbpath)) as db, db:
        count = db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
        title = db.execute("SELECT title FROM opportunities").fetchone()[0]
    assert [first["event"],second["event"],third["event"]] == ["NEW","SEEN","UPDATED"]
    assert first["id"] == second["id"] == third["id"]
    assert count == 1 and title == "Video editing revised"
    print("OH_04_SYNTHETIC_LEDGER_TEST=PASS")
    print("EVENTS=NEW,SEEN,UPDATED")
    print("FINAL_COUNT=1")
    print("REAL_DATABASE_MODIFIED=NO")
