# Project-Portfilio
A collection of my Python and data projects
# Project-Python

A curated portfolio of Python projects.

**Featured Project:**  
**TaskFlow Engine** — a clean, modular, and extensible command-line task manager built with Python, Object-Oriented Programming principles, and SQLite persistence.

---

## TaskFlow Engine — Overview

TaskFlow Engine is a professional and scalable CLI task manager developed in Python.  
It demonstrates clean OOP design, persistent storage using SQLite, and a modular architecture that is easy to extend.

---

## Features

- SQLite database for reliable task persistence
- Full CRUD operations (Create, Read, Update, Delete)
- Task filtering and sorting (priority, status, due date)
- Clean and readable CLI output
- Object-Oriented architecture (Task, TaskManager, Database)
- Modular and extensible project structure
- Cross-platform support (Windows, macOS, Linux)

---

## Tech Stack

- Python 3.x
- SQLite (via `sqlite3` standard library)
- argparse
- Object-Oriented Programming (OOP)

---

## Project Structure

```text
Project-Python/
├── taskflow-engine/
│   ├── app/
│   │   ├── app.py              # Interactive CLI version
│   │   ├── main.py             # Argument-based CLI version
│   │   ├── task.py             # Task model
│   │   ├── task_manager.py     # CRUD operations and sorting
│   │   ├── database.py         # Database initialization and connection
│   │   ├── tasks.db            # SQLite database
│   │   └── __init__.py
└── README.md
```

## Development Notes

All tasks are stored in tasks.db using SQLite.

The project is fully modular and easy to extend.

A GUI or REST API can be added on top of the existing architecture.

## Running the Interactive CLI (Recommended)

To launch the menu-driven interactive interface:
```bash
python app.py
```

```text
Example menu:
==============================
       TASKFLOW ENGINE
==============================
[1] Add Task
[2] View Tasks
[3] Mark Task as Done
[4] Delete Task
[5] Exit
```
## Running the Argument-Based CLI

The main.py file uses argparse and is suitable for automation or scripting.

## Add a task
```bash
python main.py --add "Learn Python" --desc "OOP section" --due 2025-12-30 --priority 2
```

## List all tasks
```bash
python main.py --list
```

## Remove a task
```bash
python main.py --remove <task_id>
```

## Mark a task as done
```bash
python main.py --done <task_id>
```

## Sort tasks
```bash
python main.py --sort priority
```

## Sort by due date
```bash
python main.py --sort date
```


## License
This project is open-source and free to use for learning or development purposes.