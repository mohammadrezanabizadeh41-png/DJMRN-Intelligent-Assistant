"""OH-31: one-shot CLI wrapper navigation -> existing OH-05 export -> readonly reconciliation.

The existing OH-31 wrapper navigates to a single fixed /projects page and calls
OH-05 Export; no scheduling, pagination, database writes, or outbound messages.
"""
import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import time
import urllib.parse
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

MACRO = 'DJMRN-OH31-Freelancermap-Auto-Start-One-Page'
PARENT_REF = '/macros/' + MACRO + '.json'
HTML_SHA256 = 'D142697C5E1A27338C65DB5D53F3E9C746C396A2B8EA283FD71C45BC2CB579E6'
MACRO_GIT_BLOB = '9347a0ffd85f0e9f402ebc7c2009beacad8b6372'
SOURCE_SITE = 'freelancermap'
CSV_LIMIT = 1000
EXPECTED_COUNTS = {'opportunities': 44, 'opportunity_history': 44, 'opportunity_details': 4, 'outbound_attempts': 0}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def gitblob(path):
    raw = Path(path).read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\x00' + raw).hexdigest()


def validate_export(path):
    payload = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if payload.get('schema_version') != 'djmrn.oh.export.v1':
        raise RuntimeError('INVALID_EXPORT_SCHEMA')
    rows = payload.get('opportunities')
    if not isinstance(rows, list) or not (1 <= len(rows) <= CSV_LIMIT):
        raise RuntimeError('INVALID_EXPORT_COUNT')
    external_ids = set()
    urls = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or row.get('site') != SOURCE_SITE:
            raise RuntimeError('INVALID_SITE:' + str(index))
        eid, title, url = row.get('external_id'), row.get('title'), row.get('url')
        if not all(isinstance(v, str) and v.strip() for v in (eid, title, url)):
            raise RuntimeError('INVALID_ROW:' + str(index))
        u = urllib.parse.urlsplit(url)
        if (u.scheme != 'https' or u.hostname not in ('freelancermap.com', 'www.freelancermap.com')
                or not u.path.startswith('/project/') or u.username or u.password or u.query or u.fragment):
            raise RuntimeError('INVALID_PROJECT_URL:' + str(index))
        if eid in external_ids or url in urls:
            raise RuntimeError('DUPLICATE_ID_OR_URL')
        external_ids.add(eid)
        urls.add(url)
    return rows


def check_database(database):
    path = Path(database).resolve(strict=True)
    uri = path.as_uri() + '?mode=ro'
    with closing(sqlite3.connect(uri, uri=True, timeout=10)) as db:
        db.execute('PRAGMA query_only=ON')
        if db.execute('PRAGMA quick_check').fetchone() != ('ok',):
            raise RuntimeError('DB_INTEGRITY_FAILED')
        if db.execute('SELECT value FROM metadata WHERE key=?', ('schema_version',)).fetchone() != ('djmrn.oh.local.v1',):
            raise RuntimeError('DB_SCHEMA_VERSION_UNEXPECTED')
        counts = {key: db.execute('SELECT count(*) FROM ' + key).fetchone()[0] for key in EXPECTED_COUNTS}
        if counts != EXPECTED_COUNTS:
            raise RuntimeError('DB_BASELINE_CHANGED:' + str(counts))
        old = db.execute('SELECT external_id,title,canonical_url FROM opportunities WHERE source_site=?', (SOURCE_SITE,)).fetchall()
    return old


def reconcile(rows, old):
    by_id = {eid: (title, url) for eid, title, url in old}
    by_url = {url: (eid, title) for eid, title, url in old}
    out = {'NEW_TO_LOCAL_DB': 0, 'SEEN': 0, 'UPDATED_TITLE': 0}
    samples = []
    for row in rows:
        eid, title, url = row['external_id'], row['title'], row['url']
        if eid in by_id:
            prior_title, prior_url = by_id[eid]
            if prior_url != url and url in by_url and by_url[url][0] != eid:
                raise RuntimeError('DB_ID_URL_CONFLICT')
        elif url in by_url:
            prior_title = by_url[url][1]
        else:
            prior_title = None
        kind = 'NEW_TO_LOCAL_DB' if prior_title is None else ('SEEN' if prior_title == title else 'UPDATED_TITLE')
        out[kind] += 1
        if kind != 'SEEN' and len(samples) < 5:
            samples.append({'status': kind, 'title': title, 'url': url})
    return out, samples


def validate_log(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != 'Status=OK':
        raise RuntimeError('UIVISION_LOG_NOT_OK:' + (lines[0][:150] if lines else 'EMPTY'))
    # Ui.Vision CLI v10.0.303 identifies browser-stored macros by /macros/<name>.json.
    # In-IDE logs may instead use the bare macro name. Accept only these exact identities.
    if not any(x.strip() in ('[status] Playing macro ' + MACRO,
                             '[status] Playing macro ' + PARENT_REF) for x in lines):
        raise RuntimeError('WRONG_MACRO_IN_LOG')
    if not any('Finished running' in line and 'DJMRN-OH05-Freelancermap-Export-Pilot' in line and MACRO in line for line in lines):
        raise RuntimeError('CHILD_MACRO_RETURN_MISSING')
    if not any('[echo] DJMRN_OH05_EXPORT=' in line for line in lines):
        raise RuntimeError('EXPORT_ECHO_MISSING')
    if not any('Macro completed' in line for line in lines):
        raise RuntimeError('MACRO_COMPLETION_MISSING')
    if any(re.search(r'^\[error\]', line, re.I) for line in lines):
        raise RuntimeError('MACRO_ERROR_IN_LOG')
    return True


def verify_existing(log_path, downloads, database):
    """Check a prior real CLI receipt and corresponding export; no Chrome launch or DB writes."""
    folder = Path(downloads).resolve(strict=True)
    log = Path(log_path).resolve(strict=True)
    db = Path(database).resolve(strict=True)
    if not folder.is_dir() or log.parent != folder:
        raise RuntimeError('LOG_NOT_IN_DOWNLOADS')
    before = sha256(db)
    old = check_database(db)
    log_text = log.read_text(encoding='utf-8-sig')
    validate_log(log_text)
    prefix = '[echo] DJMRN_OH05_EXPORT='
    echoes = [line[len(prefix):] for line in log_text.splitlines() if line.startswith(prefix)]
    if len(echoes) != 1:
        raise RuntimeError('EXPORT_ECHO_AMBIGUOUS')
    info = json.loads(echoes[0])
    if not isinstance(info, dict):
        raise RuntimeError('EXPORT_ECHO_INVALID')
    name = info.get('download')
    if not isinstance(name, str) or not re.fullmatch(
            r'DJMRN-OH05-freelancermap-\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}-\d{3}Z\.json', name):
        raise RuntimeError('EXPORT_FILENAME_UNEXPECTED')
    export = folder / name
    if not export.is_file() or export.stat().st_size != info.get('bytes'):
        raise RuntimeError('EXPORT_FILE_MISSING_OR_SIZE_CHANGED')
    rows = validate_export(export)
    numeric = sum(str(row['external_id']).isdigit() for row in rows)
    fallback = len(rows) - numeric
    if (info.get('rows') != len(rows) or info.get('numeric') != numeric
            or info.get('fallback') != fallback
            or info.get('network_actions') != 0 or info.get('database_writes') != 0):
        raise RuntimeError('EXPORT_ECHO_MISMATCH')
    counts, samples = reconcile(rows, old)
    if sha256(db) != before:
        raise RuntimeError('PRODUCTION_DB_FILE_CHANGED')
    print('OH31_PRIOR_CLI_LOG=PASS')
    print('OH31_EXISTING_JSON=PASS')
    print('OH31_JSON_SHA256=' + sha256(export))
    print('OH31_EXPORT_FILE=' + str(export))
    print('OH31_TOTAL_ON_PAGE=' + str(len(rows)))
    print('OH31_LOCAL_DB_RECONCILIATION=' + json.dumps(counts, sort_keys=True))
    print('OH31_REVIEW_SAMPLES=' + json.dumps(samples, ensure_ascii=False))
    print('OH31_OFFLINE_VERIFICATION=PASS')
    print('BROWSER_LAUNCH=NO; PRODUCTION_SQLITE_WRITES=0; OUTBOUND_ACTIONS=0')


def run(opts):
    launcher = Path(opts.launcher).resolve(strict=True)
    chrome = Path(opts.chrome).resolve(strict=True)
    macro_file = Path(opts.macro_file).resolve(strict=True)
    downloads = Path(opts.downloads).resolve(strict=True)
    db = Path(opts.database).resolve(strict=True)
    if not downloads.is_dir():
        raise RuntimeError('DOWNLOAD_FOLDER_MISSING')
    if sha256(launcher) != HTML_SHA256:
        raise RuntimeError('LAUNCH_HTML_SHA256_MISMATCH')
    if gitblob(macro_file) != MACRO_GIT_BLOB:
        raise RuntimeError('EXPORTED_MACRO_VERSION_MISMATCH')
    metadata = json.loads(macro_file.read_text(encoding='utf-8-sig'))
    if metadata.get('Name') != MACRO or len(metadata.get('Commands', [])) != 3:
        raise RuntimeError('MACRO_DEFINITION_UNEXPECTED')
    old = check_database(db)
    before_db_sha = sha256(db)
    prefix = 'DJMRN-OH05-freelancermap-'
    prior = {p.name for p in downloads.glob(prefix + '*.json') if p.is_file()}
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    logname = 'DJMRN-OH31-CLI-' + stamp + '.txt'
    log = downloads / logname
    query = urllib.parse.urlencode({
        'direct': '1', 'macro': MACRO, 'storage': 'browser',
        'closeRPA': '0', 'closeBrowser': '0',
        'continueInLastUsedTab': '1', 'savelog': logname,
    })
    url = launcher.as_uri() + '?' + query
    if not url.startswith('file:///') or '?direct=1&macro=' not in url:
        raise RuntimeError('CLI_URL_INVALID')
    print('OH31_PREFLIGHT=PASS', flush=True)
    print('OH31_MACRO=' + MACRO, flush=True)
    print('OH31_CLI_URL=' + url, flush=True)
    subprocess.Popen([str(chrome), url], close_fds=True)
    print('OH31_CHROME_LAUNCH_REQUEST=SUBMITTED', flush=True)
    newest = None
    for _ in range(60):
        time.sleep(1)
        files = [p for p in downloads.glob(prefix + '*.json') if p.is_file() and p.name not in prior]
        if len(files) > 1:
            raise RuntimeError('MULTIPLE_NEW_EXPORT_FILES_REVIEW_REQUIRED')
        if files:
            newest = files[0]
        if log.is_file() and newest and newest.is_file():
            try:
                first = newest.stat().st_size
                time.sleep(.25)
                if first > 10 and first == newest.stat().st_size:
                    break
            except OSError:
                pass
    if not log.is_file():
        raise RuntimeError('CLI_LOG_NOT_FOUND:' + str(log))
    validate_log(log.read_text(encoding='utf-8-sig'))
    if newest is None:
        raise RuntimeError('EXPORT_FILE_NOT_FOUND_AFTER_OK_LOG')
    rows = validate_export(newest)
    counts, samples = reconcile(rows, old)
    if sha256(db) != before_db_sha:
        raise RuntimeError('PRODUCTION_DB_FILE_CHANGED_DURING_RUN')
    print('OH31_CLI_LOG_STATUS=OK')
    print('OH31_JSON_EXPORT=PASS')
    print('OH31_JSON_SHA256=' + sha256(newest))
    print('OH31_JSON_FILE=' + str(newest))
    print('OH31_LOG_FILE=' + str(log))
    print('OH31_TOTAL_ON_PAGE=' + str(len(rows)))
    print('OH31_LOCAL_DB_RECONCILIATION=' + json.dumps(counts, sort_keys=True))
    print('OH31_REVIEW_SAMPLES=' + json.dumps(samples, ensure_ascii=False))
    print('OH31_WINDOWS=PASS')
    print('PRODUCTION_SQLITE_WRITES=0; OUTBOUND_ACTIONS=0; APPLICATIONS_USED=0')


def main():
    ap = argparse.ArgumentParser()
    for key in ('launcher', 'chrome', 'macro-file'):
        ap.add_argument('--'+key)
    for key in ('downloads', 'database'):
        ap.add_argument('--'+key, required=True)
    ap.add_argument('--verify-existing-log', help='Read-only verification; does not launch browser')
    args = ap.parse_args()
    try:
        if args.verify_existing_log:
            verify_existing(args.verify_existing_log, args.downloads, args.database)
        else:
            if not all((args.launcher, args.chrome, args.macro_file)):
                raise RuntimeError('CLI_LAUNCH_ARGUMENTS_REQUIRED')
            run(args)
    except Exception as exc:
        print('OH31_WINDOWS=FAIL; REASON=' + str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
