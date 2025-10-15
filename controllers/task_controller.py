import os, json
from models.task import Task

# chemins absolus : .../back/controllers → .../back/data/tasks.json
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR  = os.path.dirname(BASE_DIR)
DATA_DIR  = os.path.join(ROOT_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")

class TaskController:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self._load()

    # ---------- PERSISTENCE ----------
    def _load(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.next_id = data.get("next_id", 1)
        self.tasks = [Task(**t) for t in data.get("tasks", [])]

    def _save(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {"next_id": self.next_id, "tasks": [t.to_dict() for t in self.tasks]},
                f, ensure_ascii=False, indent=2
            )

    # ---------- MÉTIER (3 actions) ----------
    def add_task(self, title: str) -> Task:
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        self._save()
        return task

    def list_tasks(self) -> list[Task]:
        return self.tasks

    def get_task(self, task_id: int) -> Task | None:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def delete_task(self, task_id: int) -> bool:
        t = self.get_task(task_id)
        if not t:
            return False
        self.tasks.remove(t)
        self._save()
        return True
