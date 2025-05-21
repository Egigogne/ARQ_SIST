from models.task import Estudiante
from views.task_view import mostrar_estudiante
from storage.task_repo import guardar_datos

materias_disponibles = ["Matemáticas", "Ciencias", "Historia", "Literatura"]

def registrar_estudiante(data):
    nombre = input("Nombre completo: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío")
        nombre = input("Nombre completo: ").strip()

    edad = 0
    while edad <= 0:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("La edad debe ser positiva")
        except ValueError:
            print("Edad inválida")

    correos = input("Correo electrónico: ").strip()
    while "@" not in correos or "." not in correos:
        print("Correo inválido")
        correos = input("Correo electrónico: ").strip()

    estudiante = Estudiante(id=data["next_id"], nombre=nombre, edad=edad, correos=correos)
    data["estudiantes"].append(estudiante)
    data["next_id"] += 1
    guardar_datos(data)
    print(f"Estudiante {nombre} registrado con ID {estudiante.id}")
