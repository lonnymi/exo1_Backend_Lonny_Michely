class CLIView:
    """
    Vue en ligne de commande pour afficher les tâches et les messages.
    """

    @staticmethod
    def show_tasks(tasks):
        """
        Affiche toutes les tâches.
        """
        if not tasks:
            print("Aucune tâche pour le moment 💤")
        else:
            for task in tasks:
                print(task)

    @staticmethod
    def show_added(task):
        """
        Affiche un message après ajout d'une tâche.
        """
        print(f"Tâche ajoutée : {task}")

    @staticmethod
    def show_done(task):
        """
        Affiche un message après avoir marqué une tâche comme terminée.
        """
        if task:
            print(f"Tâche terminée : {task}")
        else:
            print("Tâche introuvable ❌")

    @staticmethod
    def show_help():
        """
        Affiche les commandes disponibles.
        """
        print("""\
Commandes disponibles :
  python main.py add "Nom de la tâche"   → ajoute une tâche
  python main.py list                    → affiche toutes les tâches
  python main.py done <id>               → marque une tâche comme terminée
""")
