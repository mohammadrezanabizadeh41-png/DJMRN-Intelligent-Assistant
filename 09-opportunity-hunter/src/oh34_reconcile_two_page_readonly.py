"""OH-34 offline-only reconciliation of two Ui.Vision OH-05 exports.

Never launches a browser, sends network requests, modifies production SQLite or
contacts employers. Fails closed on unexpected export structure and DB baseline.
"""
import argparse
import hashlib
import json
import re
import sqlite3
import sys
import urllib.parse
from contextlib import closing
from pathlib import Path

SCHEMA = 'djmrn.oh.export.v1'
SITE = 'freelancermap'
EXPECTED_COUNTS = {'opportunities': 44, 'opportunity_history': 44,
                   'opportunity_details': 4, 'outbound_attempts': 0}
EXPECTED = (
    ('DJMRN-OH05-freelancermap-2026-10-28T22-31-03-823Z.json', 6224, 6, 16),
    ('DJMRN-OH05-freelancermap-2026-10-28T22-31-08-420Z.json', 5975, 8, 14),
)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def normalize_url(url):
    if not isinstance(url, str):
        raise RuntimeError('INVALID_PROJECT_URL')
    p = urllib.parse.urlsplit(url)
    if (p.scheme != 'https' or p.hostname not in ('freelancermap.com', 'www.freelancermap.com')
            or p.username or p.password or p.port or p.query or p.fragment
            or not p.path.startswith('/project/') or p.path == '/project/'):
        raise RuntimeError('INVALID_PROJECT_URL:' + url[:120])
    # The site can present either its apex or www host; same canonical path -> same listing.
    return p.path.rstrip('/')


def load_export(path, expected):
    path = Path(path).resolve(strict=True)
    name, bytelen, numeric_expected, fallback_expected = expected
    if path.name != name or path.stat().st_size != bytelen:
        raise RuntimeError('EXPORT_RECEIPT_FILE_OR_SIZE_MISMATCH:' + path.name)
    payload = json.loads(path.read_text(encoding='utf-8-sig'))
    if not isinstance(payload, dict) or payload.get('schema_version') != SCHEMA:
        raise RuntimeError('EXPORT_SCHEMA_INVALID')
    rows = payload.get('opportunities')
    if not isinstance(rows, list) or len(rows) != 22:
        raise RuntimeError('EXPORT_ROWS_NOT_22')
    ids, urls = set(), set()
    numerics = 0
    fallbacks = 0
    validated = []
    for index, r in enumerate(rows):
        if not isinstance(r, dict) or r.get('site') != SITE:
            raise RuntimeError('ROW_SITE_INVALID:' + str(index))
        ident, title, url = r.get('external_id'), r.get('title'), r.get('url')
        if not all(isinstance(v, str) and v.strip() for v in (ident, title, url)):
            raise RuntimeError('ROW_FIELDS_INVALID:' + str(index))
        canonical = normalize_url(url)
        if ident.isdecimal():
            numerics += 1
            # Check numeric ID still matches the last numeric slug token, as in OH-05.
            if not canonical.endswith('-' + ident):
                raise RuntimeError('ROW_NUMERIC_ID_URL_MISMATCH:' + str(index))
        elif ident == 'url:' + canonical:
            fallbacks += 1
        else:
            raise RuntimeError('ROW_FALLBACK_ID_URL_MISMATCH:' + str(index))
        if ident in ids or canonical in urls:
            raise RuntimeError('PAGE_DUPLICATE_ID_OR_URL:' + str(index))
        ids.add(ident)
        urls.add(canonical)
        validated.append({'id': ident, 'title': title.strip(), 'url': url, 'path': canonical})
    if (numerics, fallbacks) != (numeric_expected, fallback_expected):
        raise RuntimeError('EXPORT_NUMERIC_FALLBACK_COUNTS_MISMATCH')
    return validated


def database_rows(path):
    path = Path(path).resolve(strict=True)
    with closing(sqlite3.connect(path.as_uri() + '?mode=ro', uri=True, timeout=10)) as conn:
        conn.execute('PRAGMA query_only=ON')
        if conn.execute('PRAGMA quick_check').fetchone() != ('ok',):
            raise RuntimeError('PRODUCTION_DB_INTEGRITY_FAILED')
        if conn.execute('SELECT value FROM metadata WHERE key=?', ('schema_version',)).fetchone() != ('djmrn.oh.local.v1',):
            raise RuntimeError('PRODUCTION_DB_SCHEMA_MISMATCH')
        counts = {key: conn.execute('SELECT count(*) FROM ' + key).fetchone()[0]
                  for key in EXPECTED_COUNTS}
        if counts != EXPECTED_COUNTS:
            raise RuntimeError('PRODUCTION_DB_COUNTS_CHANGED:' + json.dumps(counts))
        rows = conn.execute('SELECT external_id,title,canonical_url FROM opportunities WHERE source_site=?', (SITE,)).fetchall()
    return rows


def reconcile(page1, page2, existing):
    all_rows = page1 + page2
    by_path = {}
    by_id = {}
    overlap_paths = set(row['path'] for row in page1) & set(row['path'] for row in page2)
    for row in all_rows:
        ident, path = row['id'], row['path']
        if ident in by_id and by_id[ident]['path'] != path:
            raise RuntimeError('CROSS_PAGE_ID_CONFLICT')
        if path in by_path and by_path[path]['id'] != ident:
            raise RuntimeError('CROSS_PAGE_URL_ID_CONFLICT')
        by_id[ident] = row
        by_path[path] = row
    if len(by_path) == len(page1):
        raise RuntimeError('PAGE_2_HAS_NO_UNIQUE_LISTINGS')
    existing_by_id = {}
    existing_by_path = {}
    for ident, title, url in existing:
        path = normalize_url(url)
        existing_by_id[ident] = (title, path)
        existing_by_path[path] = (ident, title)
    counts = {'NEW_TO_LOCAL_DB': 0, 'SEEN': 0, 'UPDATED_TITLE': 0}
    samples = []
    for row in by_path.values():
        old = existing_by_id.get(row['id'])
        if old is not None:
            if old[1] != row['path']:
                raise RuntimeError('DB_ID_URL_MISMATCH')
            prior_title = old[0]
        else:
            prior = existing_by_path.get(row['path'])
            if prior is not None and prior[0] != row['id']:
                raise RuntimeError('DB_URL_ID_MISMATCH')
            prior_title = prior[1] if prior is not None else None
        status = ('NEW_TO_LOCAL_DB' if prior_title is None else
                  'SEEN' if prior_title == row['title'] else 'UPDATED_TITLE')
        counts[status] += 1
        if status != 'SEEN' and len(samples) < 5:
            samples.append({'status': status, 'title': row['title'], 'url': row['url']})
    return {'page1_rows': len(page1), 'page2_rows': len(page2),
            'total_rows': len(all_rows), 'cross_page_overlaps': len(overlap_paths),
            'unique_across_two_pages': len(by_path),
            'local_db': counts, 'samples': samples}


def run(page1, page2, database):
    page1, page2, database = map(Path, (page1, page2, database))
    if page1.parent.resolve() != page2.parent.resolve():
        raise RuntimeError('EXPORT_FILES_NOT_IN_SAME_FOLDER')
    if page1.resolve() == page2.resolve():
        raise RuntimeError('DUPLICATED_FILE_ARGUMENT')
    db_sha_before = sha256(database)
    current = database_rows(database)
    a = load_export(page1, EXPECTED[0])
    b = load_export(page2, EXPECTED[1])
    result = reconcile(a, b, current)
    if sha256(database) != db_sha_before:
        raise RuntimeError('PRODUCTION_DB_CHANGED_DURING_READ')
    print('OH34_INPUT1_SHA256=' + sha256(page1))
    print('OH34_INPUT2_SHA256=' + sha256(page2))
    print('OH34_RECONCILIATION=' + json.dumps(result, ensure_ascii=False, sort_keys=True))
    print('OH34_READONLY_RECONCILIATION=PASS')
    print('BROWSER_LAUNCH=NO; PRODUCTION_SQLITE_WRITES=0; OUTBOUND_ACTIONS=0')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--page1', required=True)
    parser.add_argument('--page2', required=True)
    parser.add_argument('--database', required=True)
    args = parser.parse_args()
    try:
        run(args.page1, args.page2, args.database)
    except Exception as exc:
        print('OH34_RECONCILIATION=FAIL; REASON=' + str(exc), file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
