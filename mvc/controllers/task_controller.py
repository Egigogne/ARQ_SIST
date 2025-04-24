from storage.task_repo import load_tasks, save_tasks
from models.tasks import Task

def get_tasks():
    return load_tasks()

def add_task(title):
    tasks = load_tasks()
    tasks.append(Task(title))
    save_tasks(tasks)

def mark_task_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index].done = True
        save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
