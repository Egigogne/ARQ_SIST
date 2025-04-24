import json
import os

TASKS_FILE = "monolitic/tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Ingrese el título de la tarea: ")
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Tarea agregada.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas.")
        return
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i + 1}. [{status}] {task['title']}")

def mark_done():
    list_tasks()
    index = int(input("Ingrese el número de la tarea completada: ")) - 1
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Tarea marcada como completada.")
    else:
        print("Índice inválido.")

def delete_task():
    list_tasks()
    index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tarea eliminada: {deleted['title']}")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Listar tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Seleccione una opción: ")
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
