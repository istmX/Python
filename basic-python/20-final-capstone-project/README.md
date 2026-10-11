# Final Capstone Project: TaskFlow — Project & Task Manager 🏆

**Congratulations on reaching the final project of the Basic Python stage!**

TaskFlow is a complete, industry-style command-line application built
with **pure vanilla Python** — no third-party packages. It combines
everything you learned in this stage:

- Object-Oriented Programming (classes, encapsulation, magic methods)
- Module imports and multi-file project structure
- Functions and separation of concerns
- Input validation and exception handling
- File handling with JSON persistence
- Standard library modules (`json`, `os`, `datetime`)

---

## 🧠 What Does TaskFlow Do?

TaskFlow helps you organize work into **projects** and **tasks**:

- Create multiple projects
- Add tasks with a title, description, priority, and due date
- Track task status: `todo`, `in_progress`, `done`
- Filter tasks by priority, status, or overdue
- View project statistics and completion percentage
- Everything is saved to a JSON file and reloaded on the next run

---

## 📂 Files in This Folder

| File | Responsibility |
|------|----------------|
| `main.py` | Entry point: menus, user interaction, main loop |
| `models.py` | OOP data models: `Task` and `Project` classes |
| `services.py` | Business logic: create, update, filter, statistics |
| `validators.py` | Input validation functions |
| `storage.py` | Save/load data to `taskflow_data.json` |
| `utils.py` | Shared helpers: formatting, printing, input |

Notice how each file has **one clear responsibility** — this is how
real-world projects are organized.

---

## ▶️ How to Run

```bash
python main.py
```

The program is interactive. A typical session:

```
=============================
TASKFLOW — MAIN MENU
=============================
  1. Create a new project
  2. List projects
  3. Open a project (task workspace)
  4. Save all data
  5. Exit
  Choose an option (1-5): 1
  Project name: Learn Python
  Project 'Learn Python' created.
```

Data is stored in `taskflow_data.json` (created automatically).
Delete that file to start over.

---

## 🧠 Concepts Demonstrated

### OOP (models.py)
- `Task` and `Project` classes with attributes and methods
- Encapsulation: invalid data is rejected in `__init__`
- Class variables (`Task._counter`) for auto-generated IDs
- Magic methods: `__str__`, `to_dict()`, `from_dict()`

### Modules and imports (main.py)
- Importing your own modules: `from services import ...`
- Importing standard library: `import json`, `from datetime import date`
- The `if __name__ == "__main__":` guard

### Functions (services.py, validators.py, utils.py)
- Small, single-purpose functions
- Validation functions return `True`/`False` with helpful messages
- Business logic separated from user interface

### File handling (storage.py)
- JSON persistence with `json.dump()` / `json.load()`
- Graceful handling of missing or corrupted files

### Exception handling (throughout)
- `ValueError` raised for invalid task data
- `try/except` blocks in storage and models
- Input validation prevents crashes

---

## 🏋️ Practice Exercises

1. Add a "search tasks by title" feature to the project workspace.
2. Allow editing a task's title and description.
3. Add project-level statistics (e.g., highest-priority task first).
4. Export a project's tasks to a CSV file.
5. Add color-coded priority display (e.g., red for high priority).

---

## 🎓 What You Have Learned

By building and understanding this project, you have practiced:

| Topic | Where it appears |
|-------|------------------|
| OOP | `models.py` |
| Modules & imports | `main.py` |
| Functions | all files |
| Exception handling | `models.py`, `storage.py`, `main.py` |
| File handling | `storage.py` |
| Standard library | `json`, `os`, `datetime` |
| Input validation | `validators.py` |

**You are now ready for the Intermediate Python stage!**

---

## 📚 Official Python Documentation

- `json` — JSON encoder and decoder  
  https://docs.python.org/3/library/json.html

- `datetime` — Basic date and time types  
  https://docs.python.org/3/library/datetime.html

- `os` — Miscellaneous operating system interfaces  
  https://docs.python.org/3/library/os.html

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
