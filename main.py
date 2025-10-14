import sys
from controllers.task_controller import TaskController
from views.cli import CLIView

controller = TaskController()
view = CLIView()

def main():
    if len(sys.argv) < 2:
        view.show_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("⚠️  Veuillez entrer le titre de la tâche.")
            return
        title = " ".join(sys.argv[2:])
        task = controller.add_task(title)
        view.show_added(task)

    elif command == "list":
        tasks = controller.list_tasks()
        view.show_tasks(tasks)

    elif command == "done":
        if len(sys.argv) < 3:
            print("⚠️  Utilisation : python main.py done <id>")
            return
        try:
            task_id = int(sys.argv[2])
            task = controller.mark_done(task_id)
            view.show_done(task)
        except ValueError:
            print("⚠️  L’ID doit être un nombre.")

    else:
        print("Commande inconnue 😅")
        view.show_help()

if __name__ == "__main__":
    main()
