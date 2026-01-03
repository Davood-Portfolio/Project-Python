from app.task import Task
from app.task_manager import TaskManager

manager = TaskManager()

task1 = Task(1, "Learn Python", "Finish OOP section", "2025-12-30", 2)
task2 = Task(2, "Build Project", "Start TaskFlow Engine", "2026-01-05", 1)

manager.add_task(task1)
manager.add_task(task2)

manager.list_tasks()
