import sqlite3


def get_connection():
    conn = sqlite3.connect("task.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


create_table()