class CLIView:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("Aucune tâche pour le moment 💤")
        else:
            for task in tasks:
                print(task)

    @staticmethod
    def show_added(task):
        print(f"Tâche ajoutée : {task}")

    @staticmethod
    def show_deleted(ok, task_id):
        if ok:
            print(f"Tâche supprimée : {task_id} 🗑️")
        else:
            print("Tâche introuvable ❌")

    @staticmethod
    def show_help():
        print("""
Commandes disponibles :
  python main.py add "Nom de la tâche"   → ajoute une tâche
  python main.py list                    → affiche toutes les tâches
  python main.py delete <id>             → supprime une tâche
""")
