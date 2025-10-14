# 📝 ToDoList CLI (Exercice 1)

Une mini API en ligne de commande pour gérer une liste de tâches, développée en **Python** en suivant le modèle **MVC** et les principes de la **POO**.

## 🚀 Utilisation

### Ajouter une tâche
```bash
python main.py add "Faire les devoirs"
```

### Lister les tâches
```bash
python main.py list
```

### Marquer une tâche comme faite
```bash
python main.py done 1
```

## 🧱 Structure du projet
```
ToDoList/
├── controllers/
│   └── task_controller.py
├── models/
│   └── task.py
├── views/
│   └── cli.py
├── main.py
├── requirements.txt
└── README.md
```

## 🧠 Concepts utilisés
- **MVC** : séparation claire entre modèle, vue et contrôleur
- **POO** : utilisation d’une classe `Task`
- **CLI** : interaction en ligne de commande
- **Bonnes pratiques Python** : code propre, documenté et structuré

## ✨ Auteur
**Exercice1-Nom-Prénom**
