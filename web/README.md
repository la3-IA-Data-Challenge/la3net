# ia3net - web

## Backend

### Prérequis

- Python - 3.8.6
- python3-virtualenv - 20.0.32

### Installation

Se rendre dans le dossier `backend/`

```bash
cd backend/
```

Créer un environnement virtuel et l'activer

```bash
virtualenv venv -p python3
source venv/bin/activate
```

Installer les dépendances (librairies)

```bash
pip install -r requirements.txt
```

Migrer les migrations pour créer la base de données et les tables

```bash
./manage.py migrate
```

Créer un superutilisateur. Cette utilisateur pourra accéder à une interface d'administration des données de l'application à cette [adresse](http://localhost:8000/admin/).

```bash
./manage.py createsuperuser
```

### Lancement

(Optionnel) Avant de lancer le serveur de développement, il faut générer une version build de l'application frontend si la dernière version dernière n'a pas été fait. Voir section **Générer** dans **Frontend**.

Se rendre dans le dossier `backend/`

```bash
cd backend/
```

Activer l'environnement virtuel si ce n'est pas déjà fait

```bash
source venv/bin/activate
```

Lancer le serveur de développement

```bash
./manage.py runserver
```

## Frontend

Les informations et les instructions ci-dessous sont nécessaires uniquement pour le développement de la partie frontend de l'application. Pour tester cette dernière vous avez juste besoin de lancer le serveur de développement backend.

### Prérequis

- Node.js - v10.21.0
- npm - 6.14.8

### Installation

```bash
cd frontend/
npm install
```

### Lancement

Dans le dossier `frontend/`

```bash
npm start
```

### Générer

Créer une version build de l'application frontend dans le backend.

Dans le dossier `frontend/`

```bash
sh build.sh
```
