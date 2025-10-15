<<<<<<< HEAD
# ToDoList CLI (Exercice 1)
=======
ToDoList — CLI et API Flask (3 actions)
>>>>>>> 7a44d7c (CLI add/list/delete + Flask API (GET/POST/DELETE) + JSON persistence + README + .gitignore)

Mini application ToDoList en Python organisée en MVC, offrant deux interfaces :

<<<<<<< HEAD
## Utilisation
=======
une CLI (ligne de commande),

une API web Flask.

Fonctionnalités livrées : ajouter, afficher, supprimer des tâches.
Les tâches sont persistées dans un fichier JSON (data/tasks.json).

1. But du projet

Illustrer une architecture MVC claire en Python.

Proposer deux modes d’accès à la même logique métier :

CLI pour manipuler la ToDoList depuis le terminal.

API Flask pour une intégration web ou front-end.

Appliquer de bonnes pratiques de structuration (séparation des responsabilités, sérialisation JSON, persistance simple).

2. Comment ça marche (vue d’ensemble)

Model (models/task.py) : définit la classe Task (id, title, completed) et la sérialisation to_dict().

Controller (controllers/task_controller.py) : contient la logique métier pour gérer les tâches (ajout, liste, suppression) et la persistance JSON.

View CLI (views/cli.py) : s’occupe uniquement de l’affichage côté terminal.

CLI (main.py) : point d’entrée en ligne de commande. Parse la commande, appelle le contrôleur, délègue l’affichage à la vue CLI.

API Flask (app.py) : expose la même logique métier via des routes HTTP.

Flux type (CLI) :
commande utilisateur → main.py → TaskController → sauvegarde/lecture JSON → CLIView affiche

Flux type (API) :
requête HTTP → app.py → TaskController → sauvegarde/lecture JSON → réponse JSON

3. Structure du projet
back/
├─ controllers/
│  └─ task_controller.py
├─ models/
│  └─ task.py
├─ views/
│  └─ cli.py
├─ app.py
├─ main.py
├─ requirements.txt
└─ data/                 # créé automatiquement lors de la première sauvegarde
   └─ tasks.json         # persistance des tâches


Fichiers d’initialisation (facultatifs mais utiles pour les imports) :

controllers/__init__.py
models/__init__.py
views/__init__.py

4. Prérequis

Python 3.10 ou supérieur

Pip à jour

Environnement virtuel recommandé

5. Installation

Créer et activer un environnement virtuel, puis installer les dépendances.

Windows PowerShell
cd back
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

macOS / Linux
cd back
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

6. Utilisation — CLI

Commandes disponibles :

python main.py add "Nom de la tâche"   # ajoute une tâche
python main.py list                    # affiche toutes les tâches
python main.py delete <id>             # supprime la tâche d'identifiant <id>


Exemple :
>>>>>>> 7a44d7c (CLI add/list/delete + Flask API (GET/POST/DELETE) + JSON persistence + README + .gitignore)

python main.py add "Faire les devoirs"
python main.py list
python main.py delete 1
python main.py list


<<<<<<< HEAD
## Structure du projet
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

## Concepts utilisés
- **MVC** : séparation claire entre modèle, vue et contrôleur
- **POO** : utilisation d’une classe `Task`
- **CLI** : interaction en ligne de commande
- **Bonnes pratiques Python** : code propre, documenté et structuré

## ✨ Auteur
**Exercice1-Michely-Lonny**
=======
Sortie attendue (exemple) :

Tâche ajoutée : 1. Faire les devoirs - ❌
1. Faire les devoirs - ❌
Tâche supprimée : 1 🗑️
Aucune tâche pour le moment 💤


Remarque : la CLI et l’API partagent la même persistance JSON. Les modifications faites par l’un sont visibles par l’autre.

7. Utilisation — API Flask

Lancer le serveur :

python app.py
# Running on http://127.0.0.1:5000

Routes exposées

Lister toutes les tâches
GET /tasks → 200 OK
Réponse :

[
  {"id": 1, "title": "Faire les devoirs", "completed": false},
  {"id": 2, "title": "Lire un chapitre", "completed": false}
]


Ajouter une tâche
POST /tasks → 201 Created
Body JSON requis :

{"title": "Faire les devoirs"}


Réponse :

{"id": 1, "title": "Faire les devoirs", "completed": false}


Supprimer une tâche
DELETE /tasks/<id> → 204 No Content si supprimée, 404 sinon.

Exemples d’appels
Windows PowerShell (curl alias ≠ curl classique)

Utiliser curl.exe pour le curl “classique”.

# Lister
curl.exe http://127.0.0.1:5000/tasks

# Ajouter
curl.exe -X POST http://127.0.0.1:5000/tasks ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"Faire les devoirs\"}"

# Supprimer
curl.exe -X DELETE http://127.0.0.1:5000/tasks/1

macOS / Linux
curl http://127.0.0.1:5000/tasks

curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Faire les devoirs"}'

curl -X DELETE http://127.0.0.1:5000/tasks/1

8. Persistance des données

Les tâches sont enregistrées dans data/tasks.json.

Le dossier data/ est créé automatiquement lors de la première écriture.

Le contrôleur utilise des chemins absolus pour garantir que data/tasks.json se trouve toujours à la racine du projet, quelle que soit la commande de lancement.

Exemple de contenu du fichier :

{
  "next_id": 3,
  "tasks": [
    {"id": 1, "title": "T1", "completed": true},
    {"id": 2, "title": "T2", "completed": false}
  ]
}

9. Décisions de conception

MVC séparé : Task (Model) ne connaît pas Flask ni la CLI. Le contrôleur encapsule la logique métier. La vue CLI n’affiche que du texte.

Sérialisation explicite : Task.to_dict() pour garantir une sortie JSON propre côté API.

Persistance simple : JSON lisible, pratique pour un exercice et pour déboguer. Peut être remplacée par une base de données (SQLite, PostgreSQL) si besoin.

Chemins absolus : évitent les surprises liées au dossier courant.

10. Limitations et pistes d’amélioration

Pas d’édition du titre via CLI (volontaire pour se limiter à Ajouter/Afficher/Supprimer).
Facile à ajouter si nécessaire.

Pas de mise à jour partielle via l’API autre que la suppression.
On peut réintroduire PATCH /tasks/<id> si besoin (champs title ou completed).

Pas de validation avancée ni d’authentification.

Pas de tests automatisés inclus par défaut.
On peut ajouter pytest pour valider les routes et la logique du contrôleur.

Persistance JSON non concurrente. Pour plusieurs clients simultanés, privilégier une base de données.

11. Dépendances

requirements.txt minimal :

Flask>=3.0


Activer le venv et installer :

pip install -r requirements.txt

12. Conseils Git

Éviter de versionner les données locales :

# .gitignore
venv/
__pycache__/
*/__pycache__/
*.py[cod]
.env
.vscode/
.idea/
data/*.json

13. Auteurs / Licence

Auteur: renseigner vos nom et prénom

Licence: au choix (ex. MIT) si nécessaire
>>>>>>> 7a44d7c (CLI add/list/delete + Flask API (GET/POST/DELETE) + JSON persistence + README + .gitignore)
