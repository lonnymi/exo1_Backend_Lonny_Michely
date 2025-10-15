from flask import Flask, request, jsonify
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController()

@app.get("/")
def health():
    return {"status": "ok", "message": "ToDoList API running"}, 200

# 1) AFFICHER
@app.get("/tasks")
def list_tasks():
    tasks = [t.to_dict() for t in controller.list_tasks()]
    return jsonify(tasks), 200

# 2) AJOUTER
@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "Field 'title' is required"}), 400
    task = controller.add_task(title)
    return jsonify(task.to_dict()), 201

# 3) SUPPRIMER
@app.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    ok = controller.delete_task(task_id)
    if not ok:
        return jsonify({"error": "Task not found"}), 404
    return "", 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
