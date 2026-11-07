import sqlite3

def get_connection():
    conn=sqlite3.connect("task.db")
    return conn

def create_table():
    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
            )"""

    )
    conn.commit()
    conn.close()

