import sqlite3
from database import get_connection

class TaskManager:

    def add_task(self, title, description, due_date, priority):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks (title, description, due_date, priority, status)
            VALUES (?, ?, ?, ?, ?)
        """, (title, description, due_date, priority, "pending"))

        conn.commit()
        conn.close()

    def list_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        conn.close()
        return tasks

    def remove_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    def mark_done(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    def sort_by_priority(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks ORDER BY priority ASC")
        tasks = cursor.fetchall()

        conn.close()
        return tasks

    def sort_by_due_date(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks ORDER BY due_date ASC")
        tasks = cursor.fetchall()

        conn.close()
        return tasks
