
# Project Overview

This project is a web application composed of three main directories:

- **api**: Backend using Django.
- **front**: Frontend using Vue.js with Vuetify.
- **backup**: Backup scripts.

The project uses Docker and Docker Compose to manage and orchestrate the different services.

## Project Structure

- `api/`: Contains the Django application.
- `front/`: Contains the Vue.js application.
- `backup/`: Contains the backup operation scripts.

## Docker Services

The project starts with the following services via Docker Compose:

1. **PostgreSQL**: Database for the application.
2. **Backend**: Service for the Django API.
3. **Frontend**: Service for the Vue.js application.
4. **Backup**: Service for managing backups.

## Starting the Services

```
docker compose up

docker exec -it BACK_DJANGO bash -c "python /app/projet01/manage.py makemigrations serieTracker && python /app/projet01/manage.py migrate && python /app/projet01/populate.py"
```

## Accessing the Application

Once the services are up and running, you can access the application via the following URLs:

- Backend (Django API): http://localhost:8000/
- Frontend (Vue.js): http://localhost:5173/

## Login Information

The application is preconfigured with the following users:

    Administrator
        Username: admin
        Password: admin

    Regular User 1
        Username: downy
        Password: test

    Regular User 2
        Username: boris
        Password: test

## Stopping the Services

To stop all Docker services, run:
`docker compose down`

