# models.py
# Data models for the TaskFlow project.
# Uses OOP: encapsulation, class variables, and magic methods.

from datetime import date


class Task:
    """A single task in a project."""

    # Class variable: counts every task created (used for auto IDs)
    _counter = 0

    # Allowed values for priority and status
    PRIORITIES = ("low", "medium", "high")
    STATUSES = ("todo", "in_progress", "done")

    def __init__(self, title, description, priority, due_date):
        # Validate inputs before storing them (encapsulation)
        if priority.lower() not in self.PRIORITIES:
            raise ValueError(f"Priority must be one of {self.PRIORITIES}")
        if due_date < date.today():
            raise ValueError("Due date cannot be in the past.")

        Task._counter += 1
        self.id = f"T{Task._counter:03d}"
        self.title = title
        self.description = description
        self.priority = priority.lower()
        self.due_date = due_date          # a datetime.date object
        self.status = "todo"
        self.created_at = date.today()

    def mark_done(self):
        """Set the task status to done."""
        self.status = "done"

    def mark_in_progress(self):
        """Set the task status to in_progress."""
        self.status = "in_progress"

    def is_overdue(self):
        """Return True if the due date has passed and task is not done."""
        return self.status != "done" and self.due_date < date.today()

    def to_dict(self):
        """Convert the task to a dictionary (for JSON storage)."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date.isoformat(),
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Task object from a dictionary (from JSON storage)."""
        task = cls(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            due_date=date.fromisoformat(data["due_date"]),
        )
        task.id = data["id"]
        task.status = data["status"]
        task.created_at = date.fromisoformat(data["created_at"])
        # Keep the class counter ahead of restored IDs
        number = int(data["id"][1:])
        if number > cls._counter:
            cls._counter = number
        return task

    def __str__(self):
        flag = " [OVERDUE]" if self.is_overdue() else ""
        return f"[{self.id}] {self.title} ({self.status}){flag}"


class Project:
    """A project that groups related tasks."""

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a Task object to the project."""
        self.tasks.append(task)
        return task.id

    def get_task(self, task_id):
        """Find a task by its ID. Returns None if not found."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def remove_task(self, task_id):
        """Remove a task by ID. Returns True if removed."""
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
                return True
        return False

    def task_counts(self):
        """Return a dict with counts per status."""
        counts = {status: 0 for status in Task.STATUSES}
        for task in self.tasks:
            counts[task.status] += 1
        return counts

    def completion_percentage(self):
        """Return the percentage of done tasks (0 if no tasks)."""
        if not self.tasks:
            return 0.0
        done = sum(1 for task in self.tasks if task.status == "done")
        return (done / len(self.tasks)) * 100

    def to_dict(self):
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks],
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data["name"])
        for task_data in data["tasks"]:
            project.tasks.append(Task.from_dict(task_data))
        return project

    def __str__(self):
        return f"Project '{self.name}' ({len(self.tasks)} tasks)"
