import sqlite3

class DataLoader:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Connection error: {e}")
            return None

    def fetch_all(self, query, params=None):
        conn = self.connect()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
            return rows
        except sqlite3.Error as e:
            print(f"Query error: {e}")
            return []
