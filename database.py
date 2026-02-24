import sqlite3

conn = sqlite3.connect("velqorix.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER PRIMARY KEY,
    protection INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS warnings (
    user_id INTEGER,
    group_id INTEGER,
    warn_count INTEGER DEFAULT 0,
    PRIMARY KEY(user_id, group_id)
)
""")

conn.commit()
