def mostrar_menu_principal():
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE ESTUDIANTES (JSON)".center(50))
    print("="*50)
    print("1. Registrar nuevo estudiante")
    print("2. Listar todos los estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Agregar materia a estudiante")
    print("5. Calcular promedio de estudiante")
    print("6. Generar reporte de todos los estudiantes")
    print("7. Exportar datos a JSON")
    print("8. Importar datos desde JSON")
    print("9. Salir")
    print("="*50)

def mostrar_estudiante(estudiante):
    print("\n" + "-"*50)
    print(f"ID: {estudiante.id}")
    print(f"Nombre: {estudiante.nombre}")
    print(f"Edad: {estudiante.edad}")
    print(f"Correo: {estudiante.correos}")
    print("Materias inscritas:")
    for materia, nota in estudiante.materias.items():
        print(f"  - {materia}: {nota if nota is not None else 'Sin calificación'}")
    print("-"*50)

def validar_opcion(min_val, max_val):
    while True:
        try:
            opcion = int(input(f"Seleccione una opción ({min_val}-{max_val}): "))
            if min_val <= opcion <= max_val:
                return opcion
            else:
                print(f"Por favor ingrese un número entre {min_val} y {max_val}")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
