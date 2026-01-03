class Task:
    def __init__(self, id, title, description, due_date, priority):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "pending"

    def __str__(self):
        return f"[{self.id}] {self.title} (Priority: {self.priority}, Due: {self.due_date}, Status: {self.status})"
