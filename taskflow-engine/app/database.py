import sqlite3

def get_connection():
    return sqlite3.connect("tasks.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority INTEGER,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
