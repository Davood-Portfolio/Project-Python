class Task:
    def __init__(self, task_id, title, description, due_date, priority, status="pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def mark_as_done(self):
        self.status = "done"

    def __str__(self):
        return f"[{self.id}] {self.title} (Priority: {self.priority}, Due: {self.due_date}, Status: {self.status})"
