# services.py
# Business logic: the functions that power the application.
# They receive validated input and work with the models.

from models import Project, Task

from utils import format_date


def create_project(projects, name):
    """Create a new project and add it to the list."""
    project = Project(name)
    projects.append(project)
    print(f"  Project '{name}' created.")
    return project


def list_projects(projects):
    """Print all projects with their task counts."""
    if not projects:
        print("  No projects yet. Create one first.")
        return

    for index, project in enumerate(projects, start=1):
        counts = project.task_counts()
        print(
            f"  {index}. {project.name} "
            f"[{counts['todo']} todo, {counts['in_progress']} in progress, "
            f"{counts['done']} done]"
        )


def add_task_to_project(project, title, description, priority, due_date):
    """Create a task and add it to the given project."""
    try:
        task = Task(title, description, priority, due_date)
    except ValueError as error:
        print(f"  Error: {error}")
        return None

    project.add_task(task)
    print(f"  Task '{task.id}' added to project '{project.name}'.")
    return task


def update_task_status(project, task_id, new_status):
    """Change a task's status. Returns True on success."""
    task = project.get_task(task_id)
    if task is None:
        print(f"  Error: no task with ID '{task_id}'.")
        return False

    if new_status == "done":
        task.mark_done()
    elif new_status == "in_progress":
        task.mark_in_progress()
    else:
        task.status = "todo"
    print(f"  Task {task_id} is now '{new_status}'.")
    return True


def delete_task(project, task_id):
    """Remove a task from the project. Returns True on success."""
    if project.remove_task(task_id):
        print(f"  Task {task_id} deleted.")
        return True
    print(f"  Error: no task with ID '{task_id}'.")
    return False


def filter_tasks(tasks, priority=None, status=None, overdue_only=False):
    """Return tasks matching the given filters (all filters optional)."""
    result = tasks
    if priority:
        result = [t for t in result if t.priority == priority]
    if status:
        result = [t for t in result if t.status == status]
    if overdue_only:
        result = [t for t in result if t.is_overdue()]
    return result


def show_statistics(project):
    """Print statistics for a project."""
    counts = project.task_counts()
    total = len(project.tasks)

    print(f"  Total tasks:    {total}")
    print(f"  To do:          {counts['todo']}")
    print(f"  In progress:    {counts['in_progress']}")
    print(f"  Done:           {counts['done']}")
    print(f"  Completion:     {project.completion_percentage():.1f}%")

    overdue = [t for t in project.tasks if t.is_overdue()]
    print(f"  Overdue:        {len(overdue)}")
    for task in overdue:
        print(f"    - {task.id} ({format_date(task.due_date)})")
