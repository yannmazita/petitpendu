# Petit pendu
Petit jeu du pendu, multijoueur

## Installation

### Poetry
```commandline
poetry install
```
### Sinon
Par exemple dans un venv :
```commandline
pip install -r requirements.txt
```

## Lancement

### Poetry
Dans la racine du projet :
```commandline
env PYTHONPATH=$PYTHONPATH:'.' poetry run python -u src/presentation/app.py
```
### Sinon
Par exemple dans un venv :
```commandline
env PYTHONPATH=$PYTHONPATH:'.' python -u src/presentation/app.py
```
Voir ./LICENSE pour plus d'informations sur la license de ce programme.