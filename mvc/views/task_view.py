def show_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Listar tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    return input("Seleccione una opción: ")

def show_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
        return
    for i, task in enumerate(tasks):
        status = "✔" if task.done else "✘"
        print(f"{i + 1}. [{status}] {task.title}")

def ask_for_task_title():
    return input("Ingrese el título de la tarea: ")

def ask_for_task_index():
    return int(input("Ingrese el número de la tarea: ")) - 1
