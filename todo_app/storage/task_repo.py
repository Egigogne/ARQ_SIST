import os
import json
from models.task import Estudiante

DATA_FILE = "storage/task.json"

def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return {"next_id": 1, "estudiantes": []}

    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            data["estudiantes"] = [Estudiante.from_dict(e) for e in data["estudiantes"]]
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"next_id": 1, "estudiantes": []}

def guardar_datos(data):
    data_copy = {
        "next_id": data["next_id"],
        "estudiantes": [e.to_dict() for e in data["estudiantes"]]
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data_copy, file, indent=2)
