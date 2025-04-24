import json
import os
from models.tasks import Task

TASK_FILE = "storage/task.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        data = json.loads(content)
        return [Task.from_dict(d) for d in data]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)
