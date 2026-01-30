import sqlite3
from datetime import datetime, timedelta

DB_PATH = "db/cloud_costs.db"

def is_cache_expired(key, hours=24):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT value FROM metadata WHERE key=?", (key,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return True

    last_updated = datetime.fromisoformat(row[0])
    return datetime.now() - last_updated > timedelta(hours=hours)
