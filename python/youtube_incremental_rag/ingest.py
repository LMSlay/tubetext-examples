"""Offline example: validate exported TubeText rows and persist replay-safe documents.
No network, model, embedding, or Apify calls. One timestamped segment per document.
"""
import argparse, hashlib, json, math, re, sqlite3

def valid_number(x):
    if not isinstance(x, (int, float)) or isinstance(x, bool):
        return False
    try:
        return math.isfinite(x)
    except (OverflowError, TypeError, ValueError):
        return False

def ingest(rows, db):
    if not isinstance(rows, list):
        raise ValueError('Export must be a JSON array')
    db.execute('CREATE TABLE IF NOT EXISTS videos (video_id TEXT PRIMARY KEY, fingerprint TEXT NOT NULL, row_json TEXT NOT NULL)')
    db.execute('CREATE TABLE IF NOT EXISTS documents (id TEXT PRIMARY KEY, video_id TEXT NOT NULL, text TEXT NOT NULL, start REAL NOT NULL, end REAL NOT NULL, source_url TEXT NOT NULL)')
    result = {'inserted': [], 'duplicates': [], 'review': []}
    for index, row in enumerate(rows):
        reason = None
        if not isinstance(row, dict):
            result['review'].append({'index': index, 'reason': 'not_an_object'})
            continue
        vid = row.get('videoId')
        if row.get('status') != 'ok': reason = 'non_ok_status'
        elif not isinstance(vid, str) or not re.fullmatch(r'[A-Za-z0-9_-]{11}', vid): reason = 'invalid_video_id'
        elif row.get('source') == 'ai': reason = 'ai_row_in_captions_only_pipeline'
        elif not isinstance(row.get('transcript'), str) or not row['transcript'].strip(): reason = 'empty_transcript'
        elif not isinstance(row.get('segments'), list) or not row['segments']: reason = 'missing_segments'
        docs = []
        if reason is None:
            previous_start = -1
            for n, seg in enumerate(row['segments']):
                if not isinstance(seg, dict): reason = 'invalid_segment'; break
                start, duration, text = seg.get('start'), seg.get('duration'), seg.get('text')
                if not valid_number(start) or not valid_number(duration) or start < 0 or duration < 0 or start < previous_start or not valid_number(start + duration):
                    reason = 'invalid_segment_time'; break
                if not isinstance(text, str) or not text.strip(): reason = 'empty_segment_text'; break
                previous_start = start
                docs.append((f'{vid}:{n}', vid, text, start, start + duration,
                             f'https://www.youtube.com/watch?v={vid}&t={math.floor(start)}s'))
        if reason:
            result['review'].append({'index': index, 'videoId': vid, 'reason': reason, 'status': row.get('status')})
            continue
        # Only source content is fingerprinted; fluctuating views/metadata cannot create a new video.
        try:
            canonical = json.dumps({'transcript': row['transcript'], 'segments': row['segments'], 'language': row.get('language')}, ensure_ascii=False, sort_keys=True, allow_nan=False)
            row_json = json.dumps(row, ensure_ascii=False, allow_nan=False)
        except (ValueError, TypeError, OverflowError):
            result['review'].append({'index': index, 'videoId': vid, 'reason': 'invalid_json_value'})
            continue
        fingerprint = hashlib.sha256(canonical.encode()).hexdigest()
        # SQLite serializes this transaction. A process failure cannot commit a video without documents.
        with db:
            db.execute('BEGIN IMMEDIATE')
            old = db.execute('SELECT fingerprint FROM videos WHERE video_id=?', (vid,)).fetchone()
            if old:
                if old[0] == fingerprint: result['duplicates'].append(vid)
                else: result['review'].append({'index': index, 'videoId': vid, 'reason': 'changed_content_requires_explicit_refresh'})
                continue
            db.execute('INSERT INTO videos VALUES (?,?,?)', (vid, fingerprint, row_json))
            db.executemany('INSERT INTO documents VALUES (?,?,?,?,?,?)', docs)
        result['inserted'].append(vid)
    return result

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('export_json'); p.add_argument('sqlite_db')
    args = p.parse_args()
    with open(args.export_json, encoding='utf-8') as f: rows = json.load(f)
    with sqlite3.connect(args.sqlite_db) as db:
        print(json.dumps(ingest(rows, db), ensure_ascii=False, indent=2))
