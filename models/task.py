class Task:
    """
    Représente une tâche individuelle dans la ToDoList.
    """

    def __init__(self, id: int, title: str, completed: bool = False):
        """Initialise une nouvelle tâche."""
        self.id = id
        self.title = title
        self.completed = completed

    def mark_done(self):
        """Marque la tâche comme terminée."""
        self.completed = True

    def __str__(self) -> str:
        """Retourne une chaîne lisible pour affichage en CLI."""
        status = "✅" if self.completed else "❌"
        return f"{self.id}. {self.title} - {status}"

    def to_dict(self) -> dict:
        """Transforme la tâche en dictionnaire (utile pour JSON/API)."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
