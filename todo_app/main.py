from storage.task_repo import cargar_datos
from views.task_view import mostrar_menu_principal, validar_opcion
from controllers import task_controller as ctrl

def main():
    data = cargar_datos()

    while True:
        mostrar_menu_principal()
        opcion = validar_opcion(1, 9)

        if opcion == 1:
            ctrl.registrar_estudiante(data)
        # Implementar llamadas a otras funciones aquí...
        elif opcion == 9:
            print("¡Hasta pronto!")
            break

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
