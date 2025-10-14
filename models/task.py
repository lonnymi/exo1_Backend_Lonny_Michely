class Task:
    """
    Représente une tâche individuelle dans la ToDoList.
    """

    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def mark_done(self):
        """
        Marque la tâche comme terminée.
        """
        self.completed = True

    def __str__(self):
        """
        Retourne une représentation textuelle lisible de la tâche.
        """
        status = "✅" if self.completed else "❌"
        return f"{self.id}. {self.title} - {status}"
