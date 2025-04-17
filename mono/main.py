"""
Aplicación monolítica básica para gestión de estudiantes usando JSON
"""

import json
import os

# =============================================
# Configuración inicial y variables globales
# =============================================
DATA_FILE = "estudiantes.json"
materias_disponibles = ["Matemáticas", "Ciencias", "Historia", "Literatura"]

# =============================================
# Funciones para manejo de JSON
# =============================================
def cargar_datos():
    """Carga los datos de estudiantes desde el archivo JSON"""
    if not os.path.exists(DATA_FILE):
        return {"next_id": 1, "estudiantes": []}
    
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"next_id": 1, "estudiantes": []}

def guardar_datos(data):
    """Guarda los datos de estudiantes en el archivo JSON"""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

# =============================================
# Funciones de utilidad
# =============================================
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

def mostrar_estudiante(estudiante):
    print("\n" + "-"*50)
    print(f"ID: {estudiante['id']}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Correo: {estudiante['correo']}")
    print("Materias inscritas:")
    for materia, nota in estudiante['materias'].items():
        print(f"  - {materia}: {nota if nota is not None else 'Sin calificación'}")
    print("-"*50)

# =============================================
# Funciones principales de la aplicación
# =============================================
def registrar_estudiante(data):
    """Registra un nuevo estudiante en el sistema"""
    print("\nREGISTRO DE NUEVO ESTUDIANTE")
    print("---------------------------")
    
    nombre = input("Nombre completo: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío")
        nombre = input("Nombre completo: ").strip()
    
    edad = 0
    while edad <= 0:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo")
        except ValueError:
            print("Por favor ingrese un número válido para la edad")
    
    correo = input("Correo electrónico: ").strip()
    while "@" not in correo or "." not in correo:
        print("Por favor ingrese un correo válido")
        correo = input("Correo electrónico: ").strip()
    
    nuevo_estudiante = {
        'id': data['next_id'],
        'nombre': nombre,
        'edad': edad,
        'correo': correo,
        'materias': {}
    }
    
    data['estudiantes'].append(nuevo_estudiante)
    data['next_id'] += 1
    guardar_datos(data)
    print(f"\nEstudiante {nombre} registrado con éxito! ID asignado: {nuevo_estudiante['id']}")

def listar_estudiantes(data):
    """Lista todos los estudiantes registrados"""
    print("\nLISTA DE ESTUDIANTES REGISTRADOS")
    print("-------------------------------")
    
    if not data['estudiantes']:
        print("No hay estudiantes registrados.")
        return
    
    for estudiante in data['estudiantes']:
        print(f"ID: {estudiante['id']} - Nombre: {estudiante['nombre']}")

def buscar_estudiante_por_id(data):
    """Busca un estudiante por su ID"""
    print("\nBUSCAR ESTUDIANTE POR ID")
    print("-----------------------")
    
    if not data['estudiantes']:
        print("No hay estudiantes registrados.")
        return
    
    try:
        id_busqueda = int(input("Ingrese el ID del estudiante: "))
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return
    
    encontrado = False
    for estudiante in data['estudiantes']:
        if estudiante['id'] == id_busqueda:
            mostrar_estudiante(estudiante)
            encontrado = True
            break
    
    if not encontrado:
        print(f"No se encontró ningún estudiante con ID {id_busqueda}")

def agregar_materia_a_estudiante(data):
    """Agrega una materia a un estudiante"""
    print("\nAGREGAR MATERIA A ESTUDIANTE")
    print("--------------------------")
    
    if not data['estudiantes']:
        print("No hay estudiantes registrados.")
        return
    
    try:
        id_estudiante = int(input("Ingrese el ID del estudiante: "))
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return
    
    estudiante_encontrado = None
    for estudiante in data['estudiantes']:
        if estudiante['id'] == id_estudiante:
            estudiante_encontrado = estudiante
            break
    
    if not estudiante_encontrado:
        print(f"No se encontró ningún estudiante con ID {id_estudiante}")
        return
    
    print("\nMaterias disponibles:")
    for i, materia in enumerate(materias_disponibles, 1):
        print(f"{i}. {materia}")
    
    try:
        opcion_materia = int(input("Seleccione el número de la materia a agregar: "))
        if 1 <= opcion_materia <= len(materias_disponibles):
            materia_seleccionada = materias_disponibles[opcion_materia-1]
            
            if materia_seleccionada in estudiante_encontrado['materias']:
                print(f"El estudiante ya está inscrito en {materia_seleccionada}")
                return
            
            # Preguntar si desea agregar calificación
            agregar_nota = input("¿Desea agregar una calificación? (s/n): ").lower()
            nota = None
            if agregar_nota == 's':
                while True:
                    try:
                        nota = float(input(f"Ingrese la calificación para {materia_seleccionada} (0-10): "))
                        if 0 <= nota <= 10:
                            break
                        else:
                            print("La calificación debe estar entre 0 y 10")
                    except ValueError:
                        print("Por favor ingrese un número válido")
            
            estudiante_encontrado['materias'][materia_seleccionada] = nota
            guardar_datos(data)
            print(f"Materia {materia_seleccionada} agregada con éxito al estudiante {estudiante_encontrado['nombre']}")
        else:
            print("Opción de materia inválida")
    except ValueError:
        print("Por favor ingrese un número válido")

def calcular_promedio_estudiante(data):
    """Calcula el promedio de un estudiante"""
    print("\nCALCULAR PROMEDIO DE ESTUDIANTE")
    print("----------------------------")
    
    if not data['estudiantes']:
        print("No hay estudiantes registrados.")
        return
    
    try:
        id_estudiante = int(input("Ingrese el ID del estudiante: "))
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return
    
    estudiante_encontrado = None
    for estudiante in data['estudiantes']:
        if estudiante['id'] == id_estudiante:
            estudiante_encontrado = estudiante
            break
    
    if not estudiante_encontrado:
        print(f"No se encontró ningún estudiante con ID {id_estudiante}")
        return
    
    if not estudiante_encontrado['materias']:
        print("El estudiante no tiene materias registradas.")
        return
    
    materias_con_nota = {m: n for m, n in estudiante_encontrado['materias'].items() if n is not None}
    
    if not materias_con_nota:
        print("El estudiante no tiene calificaciones registradas en ninguna materia.")
        return
    
    promedio = sum(materias_con_nota.values()) / len(materias_con_nota)
    print(f"\nPromedio de {estudiante_encontrado['nombre']}: {promedio:.2f}")
    print("Materias consideradas:")
    for materia, nota in materias_con_nota.items():
        print(f"  - {materia}: {nota}")

def generar_reporte_estudiantes(data):
    """Genera un reporte de todos los estudiantes"""
    print("\nREPORTE DE TODOS LOS ESTUDIANTES")
    print("------------------------------")
    
    if not data['estudiantes']:
        print("No hay estudiantes registrados.")
        return
    
    for estudiante in data['estudiantes']:
        mostrar_estudiante(estudiante)
        
        # Calcular promedio si tiene materias con notas
        materias_con_nota = {m: n for m, n in estudiante['materias'].items() if n is not None}
        if materias_con_nota:
            promedio = sum(materias_con_nota.values()) / len(materias_con_nota)
            print(f"Promedio: {promedio:.2f}")
        else:
            print("Promedio: No disponible (sin calificaciones)")
        
        print()

def exportar_a_json(data):
    """Exporta los datos a un archivo JSON seleccionado por el usuario"""
    print("\nEXPORTAR DATOS A JSON")
    print("--------------------")
    
    nombre_archivo = input("Ingrese el nombre del archivo para exportar (ej: backup_estudiantes.json): ").strip()
    if not nombre_archivo.endswith('.json'):
        nombre_archivo += '.json'
    
    try:
        with open(nombre_archivo, 'w') as file:
            json.dump(data, file, indent=2)
        print(f"Datos exportados correctamente a {nombre_archivo}")
    except Exception as e:
        print(f"Error al exportar datos: {str(e)}")

def importar_desde_json():
    """Importa datos desde un archivo JSON seleccionado por el usuario"""
    print("\nIMPORTAR DATOS DESDE JSON")
    print("-----------------------")
    
    nombre_archivo = input("Ingrese el nombre del archivo JSON a importar: ").strip()
    
    try:
        with open(nombre_archivo, 'r') as file:
            nuevo_data = json.load(file)
        
        # Validar estructura básica del JSON importado
        if 'estudiantes' not in nuevo_data or 'next_id' not in nuevo_data:
            print("El archivo no tiene el formato correcto")
            return None
        
        print(f"Datos importados correctamente desde {nombre_archivo}")
        return nuevo_data
    except FileNotFoundError:
        print("Archivo no encontrado")
    except json.JSONDecodeError:
        print("El archivo no es un JSON válido")
    except Exception as e:
        print(f"Error al importar datos: {str(e)}")
    
    return None

# =============================================
# Punto de entrada principal de la aplicación
# =============================================
def main():
    print("Bienvenido al Sistema de Gestión de Estudiantes")
    print("Versión con almacenamiento en JSON")
    
    # Cargar datos al iniciar
    data = cargar_datos()
    
    while True:
        mostrar_menu_principal()
        opcion = validar_opcion(1, 9)
        
        if opcion == 1:
            registrar_estudiante(data)
        elif opcion == 2:
            listar_estudiantes(data)
        elif opcion == 3:
            buscar_estudiante_por_id(data)
        elif opcion == 4:
            agregar_materia_a_estudiante(data)
        elif opcion == 5:
            calcular_promedio_estudiante(data)
        elif opcion == 6:
            generar_reporte_estudiantes(data)
        elif opcion == 7:
            exportar_a_json(data)
        elif opcion == 8:
            nuevo_data = importar_desde_json()
            if nuevo_data:
                data = nuevo_data
                guardar_datos(data)
        elif opcion == 9:
            print("\nGracias por usar el Sistema de Gestión de Estudiantes. ¡Hasta pronto!")
            break
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()