from controllers import task_controller as ctrl
from views import task_view as view

def main():
    while True:
        choice = view.show_menu()
        if choice == "1":
            view.show_tasks(ctrl.get_tasks())
        elif choice == "2":
            title = view.ask_for_task_title()
            ctrl.add_task(title)
        elif choice == "3":
            view.show_tasks(ctrl.get_tasks())
            index = view.ask_for_task_index()
            ctrl.mark_task_done(index)
        elif choice == "4":
            view.show_tasks(ctrl.get_tasks())
            index = view.ask_for_task_index()
            ctrl.delete_task(index)
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
