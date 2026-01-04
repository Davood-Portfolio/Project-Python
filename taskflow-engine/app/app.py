from task_manager import TaskManager

manager = TaskManager()

def show_menu():
    print("\n==============================")
    print("       TASKFLOW ENGINE")
    print("==============================")
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Mark Task as Done")
    print("[4] Delete Task")
    print("[5] Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Title: ")
        desc = input("Description: ")
        due = input("Due Date (YYYY-MM-DD): ")
        prio = int(input("Priority (1-5): "))

        manager.add_task(title, desc, due, prio)
        print("Task added successfully.")

    elif choice == "2":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nID | Title               | Priority | Due Date     | Status")
            print("---------------------------------------------------------------")
            for t in tasks:
                print(f"{t[0]:<3}| {t[1]:<20}| {t[4]:<8}| {t[3]:<12}| {t[5]}")

    elif choice == "3":
        task_id = int(input("Task ID to mark as done: "))
        manager.mark_done(task_id)
        print("Task marked as done.")

    elif choice == "4":
        task_id = int(input("Task ID to delete: "))
        manager.remove_task(task_id)
        print("Task deleted.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
