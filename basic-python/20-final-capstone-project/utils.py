# utils.py
# Small helper functions shared across the application.

from datetime import datetime


def print_header(title):
    """Print a formatted section header."""
    print()
    print("=" * 45)
    print(title)
    print("=" * 45)


def parse_date(date_text):
    """Convert a YYYY-MM-DD string to a date object (assumes valid format)."""
    return datetime.strptime(date_text, "%Y-%m-%d").date()


def format_date(date_value):
    """Format a date object as a readable string."""
    return date_value.strftime("%d %b %Y")


def ask_input(prompt):
    """Ask for input and strip whitespace."""
    return input(prompt).strip()


def print_task_table(tasks):
    """Print tasks in a simple aligned table."""
    if not tasks:
        print("  (no tasks to show)")
        return

    print(f"  {'ID':<6}{'TITLE':<22}{'PRIORITY':<10}{'STATUS':<13}DUE DATE")
    print("  " + "-" * 60)
    for task in tasks:
        flag = " !" if task.is_overdue() else ""
        print(
            f"  {task.id:<6}{task.title:<22}{task.priority:<10}"
            f"{task.status:<13}{format_date(task.due_date)}{flag}"
        )
    print("  (! = overdue)")
