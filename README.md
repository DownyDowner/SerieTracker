# Projet web - Seconde session

Ce projet est une application web composée de trois dossiers principaux :

- **api** : Backend en Django
- **front** : Frontend en Vue.js avec Vuetify.
- **backup** : Scripts de sauvegarde.

Le projet utilise Docker et Docker Compose pour gérer et orchestrer les différents services.

## Structure du Projet

- `api/` : Contient l'application Django.
- `front/` : Contient l'application Vue.js.
- `backup/` : Contient les scripts pour les opérations de sauvegarde.

## Services Docker

Le projet démarre avec les services suivants via Docker Compose :

1. **PostgreSQL** : Base de données pour l'application.
2. **Backend** : Service pour l'API Django.
3. **Frontend** : Service pour l'application Vue.js.
4. **Backup** : Service pour la gestion des sauvegardes.

## Démarrer les Services

```
docker compose up

docker exec -it BACK_DJANGO bash -c "python /app/projet01/manage.py makemigrations serieTracker && python /app/projet01/manage.py migrate && python /app/projet01/populate.py"
```

## Accès à l'Application

Une fois les services démarrés, vous pouvez accéder à l'application via les URLs suivantes :

- Backend (API Django) : http://localhost:8000/
- Frontend (Vue.js) : http://localhost:5173/

## Informations de Connexion

L'application est préconfigurée avec les utilisateurs suivants :

    Administrateur
        Utilisateur : admin
        Mot de passe : admin

    Utilisateur lambda 1
        Utilisateur : vspies
        Mot de passe : test

    Utilisateur lambda 2
        Utilisateur : boris
        Mot de passe : test

## Arrêt des Services

Pour arrêter tous les services Docker, exécutez :
`docker compose down`
