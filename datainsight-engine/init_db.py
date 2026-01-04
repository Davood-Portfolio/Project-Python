import sqlite3

# Create database file
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Run schema.sql
with open("database/schema.sql", "r") as f:
    cursor.executescript(f.read())

# Run sample_data.sql
with open("database/sample_data.sql", "r") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully!")
