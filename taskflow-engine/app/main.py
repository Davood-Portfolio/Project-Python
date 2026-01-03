import argparse
from task_manager import TaskManager
from database import init_db

# Initialize database
init_db()

manager = TaskManager()

parser = argparse.ArgumentParser(description="TaskFlow Engine CLI")

parser.add_argument("--add", type=str, help="Add a new task title")
parser.add_argument("--desc", type=str, help="Task description")
parser.add_argument("--due", type=str, help="Due date (YYYY-MM-DD)")
parser.add_argument("--priority", type=int, help="Task priority")

parser.add_argument("--list", action="store_true", help="List all tasks")
parser.add_argument("--remove", type=int, help="Remove task by ID")
parser.add_argument("--done", type=int, help="Mark task as done")
parser.add_argument("--sort", type=str, help="Sort tasks by 'priority' or 'date'")

args = parser.parse_args()

# Add task
if args.add:
    manager.add_task(
        title=args.add,
        description=args.desc or "",
        due_date=args.due or "2099-12-31",
        priority=args.priority or 5
    )
    print(f"Task '{args.add}' added.")

if args.list:
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks found.")
    else:
        print("ID | Title               | Priority | Due Date     | Status")
        print("---------------------------------------------------------------")
        for t in tasks:
            print(f"{t[0]:<3}| {t[1]:<20}| {t[4]:<8}| {t[3]:<12}| {t[5]}")

# Remove task
if args.remove:
    manager.remove_task(args.remove)
    print(f"Task {args.remove} removed.")

# Mark done
if args.done:
    manager.mark_done(args.done)
    print(f"Task {args.done} marked as done.")

# Sorting
if args.sort:
    if args.sort == "priority":
        tasks = manager.sort_by_priority()
    elif args.sort == "date":
        tasks = manager.sort_by_due_date()
    else:
        print("Invalid sort option.")
        exit()

    for t in tasks:
        print(t)
