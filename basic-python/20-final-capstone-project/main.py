# main.py — TaskFlow: Project & Task Manager
#
# A complete vanilla Python application (no third-party packages).
# It combines everything from the Basic Python stage:
#   - Object-Oriented Programming (models.py)
#   - Module imports (this file imports the other modules)
#   - Functions and business logic (services.py)
#   - Input validation (validators.py)
#   - File handling / JSON persistence (storage.py)
#   - Helper utilities (utils.py)
#
# Run it with:  python main.py

from datetime import date

# Import our own modules
from models import Project
from services import (
    add_task_to_project,
    create_project,
    delete_task,
    filter_tasks,
    list_projects,
    show_statistics,
    update_task_status,
)
from storage import load_projects, save_projects
from utils import ask_input, parse_date, print_header, print_task_table
from validators import (
    is_valid_date,
    is_valid_menu_choice,
    is_valid_priority,
    is_valid_status,
    is_non_empty,
)


def show_main_menu():
    """Display the main menu options."""
    print_header("TASKFLOW — MAIN MENU")
    print("  1. Create a new project")
    print("  2. List projects")
    print("  3. Open a project (task workspace)")
    print("  4. Save all data")
    print("  5. Exit")


def show_project_menu(project):
    """Display the task workspace menu for one project."""
    print_header(f"PROJECT: {project.name.upper()}")
    print("  1. Add a task")
    print("  2. List all tasks")
    print("  3. List tasks by priority")
    print("  4. List tasks by status")
    print("  5. Show overdue tasks")
    print("  6. Update task status")
    print("  7. Delete a task")
    print("  8. Show statistics")
    print("  9. Back to main menu")


def handle_create_project(projects):
    """Create a new project from user input."""
    name = ask_input("  Project name: ")
    if is_non_empty(name):
        create_project(projects, name)


def handle_add_task(project):
    """Add a task to the current project with full validation."""
    title = ask_input("  Task title: ")
    if not is_non_empty(title):
        return

    description = ask_input("  Description: ")

    priority = ask_input("  Priority (low/medium/high): ").lower()
    if not is_valid_priority(priority):
        return

    date_text = ask_input("  Due date (YYYY-MM-DD): ")
    if not is_valid_date(date_text):
        return
    due_date = parse_date(date_text)
    if due_date < date.today():
        print("  Error: due date cannot be in the past.")
        return

    add_task_to_project(project, title, description, priority, due_date)


def handle_list_by_priority(project):
    """Show tasks filtered by a chosen priority."""
    priority = ask_input("  Priority to show (low/medium/high): ").lower()
    if is_valid_priority(priority):
        print_task_table(filter_tasks(project.tasks, priority=priority))


def handle_list_by_status(project):
    """Show tasks filtered by a chosen status."""
    status = ask_input("  Status to show (todo/in_progress/done): ").lower()
    if is_valid_status(status):
        print_task_table(filter_tasks(project.tasks, status=status))


def handle_update_status(project):
    """Change the status of a task."""
    task_id = ask_input("  Task ID (e.g., T001): ").upper()
    new_status = ask_input("  New status (todo/in_progress/done): ").lower()
    if is_valid_status(new_status):
        update_task_status(project, task_id, new_status)


def handle_delete_task(project):
    """Delete a task by ID."""
    task_id = ask_input("  Task ID to delete (e.g., T001): ").upper()
    delete_task(project, task_id)


def project_workspace(project):
    """The inner loop for managing one project's tasks."""
    while True:
        show_project_menu(project)
        choice = ask_input("  Choose an option (1-9): ")

        if choice == "1":
            handle_add_task(project)
        elif choice == "2":
            print_task_table(project.tasks)
        elif choice == "3":
            handle_list_by_priority(project)
        elif choice == "4":
            handle_list_by_status(project)
        elif choice == "5":
            print_task_table(filter_tasks(project.tasks, overdue_only=True))
        elif choice == "6":
            handle_update_status(project)
        elif choice == "7":
            handle_delete_task(project)
        elif choice == "8":
            show_statistics(project)
        elif choice == "9":
            break
        else:
            print("  Please enter a number between 1 and 9.")


def open_project(projects):
    """Select a project and enter its workspace."""
    list_projects(projects)
    if not projects:
        return

    choice = ask_input("  Enter project number: ")
    try:
        index = int(choice) - 1
        project = projects[index]
    except (ValueError, IndexError):
        print("  Error: invalid project number.")
        return

    project_workspace(project)


def main():
    """Application entry point."""
    projects = load_projects()
    print_header("WELCOME TO TASKFLOW")
    print("  Your data is stored in 'taskflow_data.json'.")

    while True:
        show_main_menu()
        choice = ask_input("  Choose an option (1-5): ")

        if choice == "1":
            handle_create_project(projects)
        elif choice == "2":
            list_projects(projects)
        elif choice == "3":
            open_project(projects)
        elif choice == "4":
            if save_projects(projects):
                print("  All data saved.")
        elif choice == "5":
            if save_projects(projects):
                print("  Data saved. Goodbye!")
            break
        else:
            print("  Please enter a number between 1 and 5.")


# The main guard: run only when executed directly
if __name__ == "__main__":
    main()
