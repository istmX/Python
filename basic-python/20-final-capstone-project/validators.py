# validators.py
# Input validation functions.
# Every function returns True when the input is valid,
# and prints a helpful message when it is not.

from datetime import datetime


def is_non_empty(text):
    """True when the text is not empty or just spaces."""
    if not text.strip():
        print("  Error: this field cannot be empty.")
        return False
    return True


def is_valid_priority(priority):
    """True when priority is low, medium, or high."""
    valid = ("low", "medium", "high")
    if priority.lower() not in valid:
        print(f"  Error: priority must be one of {valid}.")
        return False
    return True


def is_valid_status(status):
    """True when status is todo, in_progress, or done."""
    valid = ("todo", "in_progress", "done")
    if status.lower() not in valid:
        print(f"  Error: status must be one of {valid}.")
        return False
    return True


def is_valid_date(date_text):
    """True when the date looks like YYYY-MM-DD."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        print("  Error: date must be in YYYY-MM-DD format (e.g., 2026-12-31).")
        return False


def is_valid_menu_choice(choice, allowed):
    """True when the choice is one of the allowed options."""
    if choice not in allowed:
        print(f"  Error: enter one of {allowed}.")
        return False
    return True
