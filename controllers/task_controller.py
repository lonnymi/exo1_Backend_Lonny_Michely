from models.task import Task

class TaskController:
    """
    Contrôleur principal pour gérer la liste des tâches.
    """

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """
        Ajoute une nouvelle tâche à la liste.
        """
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        """
        Retourne la liste de toutes les tâches.
        """
        return self.tasks

    def mark_done(self, task_id):
        """
        Marque une tâche comme terminée.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.mark_done()
                return task
        return None
