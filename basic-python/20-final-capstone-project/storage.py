# storage.py
# Handles saving and loading data to a JSON file.
# Uses the json module (part of the Python standard library).

import json
import os

from models import Project

DATA_FILE = "taskflow_data.json"


def save_projects(projects):
    """Save all projects to the JSON file.

    Returns True on success, False on failure.
    """
    try:
        data = [project.to_dict() for project in projects]
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        return True
    except OSError as error:
        print(f"  Error saving data: {error}")
        return False


def load_projects():
    """Load all projects from the JSON file.

    Returns a list of Project objects (empty if the file
    does not exist or cannot be read).
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [Project.from_dict(project_data) for project_data in data]
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as error:
        print(f"  Warning: could not load data file ({error}). Starting fresh.")
        return []
