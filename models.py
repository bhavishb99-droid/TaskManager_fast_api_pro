from database.database import get_connection

def create_task(task):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
                    INSERT INTO tasks(title,description,priority,status)
                    VALUES(?,?,?,?)""",(
                        task.title,
                        task.description,
                        task.priority,
                        task.status
                    ))
    conn.commit()
    task_id=cursor.lastrowid
    conn.close()
    return task_id

def get_all_task():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute(" SELECT * FROM tasks ")
    tasks=cursor.fetchall()
    conn.close()
    return tasks 

def get_task_by_id(task_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM tasks
    WHERE id=?
    """,
    (task_id,))
    task=cursor.fetchone()
    conn.close()
    return task
def update_task(task_id,task_data):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE tasks
            SET title=?,
                description=?,
                priority=?,
                status=?
            WHERE id=?""",(
                 task_data.title,
                 task_data.description,
                 task_data.priority,
                 task_data.status,
                 task_id
            ))
    conn.commit()
    updated=cursor.rowcount>0
    conn.close()
    return updated

def delete_id(task_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?",(task_id,))
    deleted=cursor.rowcount>0
    conn.commit()

    conn.close()
    return deleted

