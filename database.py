import sqlite3

db = sqlite3.connect("database.db")

db.execute("""
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    issue TEXT,
    priority TEXT,
    status TEXT
)
""")

db.close()

print("Database created successfully")
