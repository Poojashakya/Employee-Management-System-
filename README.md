employee-management/
├─ requirements.txt
├─ .env.example
├─ README.md
├─ manage.py
├─ Dockerfile
├─ docker-compose.yml
├─ employee_project/
│ ├─ __init__.py
│ ├─ asgi.py
│ ├─ settings.py
│ ├─ urls.py
│ ├─ wsgi.py
├─ employees/
│ ├─ __init__.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ models.py
│ ├─ serializers.py
│ ├─ views.py
│ ├─ urls.py
│ ├─ filters.py
│ ├─ tests.py
│ ├─ management/
│ │ └─ commands/
│ │ └─ seed_data.py
│ └─ migrations/
│ └─ __init__.py
├─ templates/
│ └─ charts.html
└─ .gitignore

Django==5.0.6
djangorestframework==3.15.2
drf-yasg==1.21.7
djangorestframework-simplejwt==5.3.1
python-dotenv==1.0.1
django-filter==24.2
psycopg2-binary==2.9.9
gunicorn==22.0.0

# Django
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=*


# DB (Postgres in docker-compose) — fallback to SQLite if not set
DB_ENGINE=django.db.backends.postgresql
DB_NAME=employees
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432


# DRF Pagination
PAGE_SIZE=10


# Django Employee Management System


A minimal Django REST API for managing Employees, Departments, Attendance, and Performance.


## Features
- 4 models with relationships (Employee, Department, Attendance, Performance)
- CRUD via Django REST Framework
- JWT Auth (SimpleJWT)
- Filtering, searching, ordering, pagination
- Swagger UI at `/swagger/`
- Seed command: `python manage.py seed_data`
- Optional Docker setup (Postgres)
- Simple chart template (`templates/charts.html`)


## Quickstart (Local, SQLite)
1. Create and activate a virtualenv.
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set values. For quick local dev, you can just set `SECRET_KEY` and `DEBUG=True`.
4. `python manage.py migrate`
5. (Optional) `python manage.py createsuperuser`
6. Seed sample data: `python manage.py seed_data`
7. Run: `python manage.py runserver`


Open:
- API root: `http://127.0.0.1:8000/api/`
- Swagger: `http://127.0.0.1:8000/swagger/`
- Get JWT: `POST http://127.0.0.1:8000/api/token/` with `{"username":"<youruser>", "password":"<yourpass>"}`


## Docker (Postgres)
1. Ensure Docker is running.
2. `cp .env.example .env` (keep DB_* vars as-is for docker)
3. `docker-compose up --build`
4. Run migrations inside the container: `docker compose exec web python manage.py migrate`
5. Seed data: `docker compose exec web python manage.py seed_data`


## API Examples
- Employees list (with pagination/filtering): `GET /api/employees/?department=<id>&search=jane&ordering=-date_joined`
- CRUD on `/api/employees/` (JWT auth required)


## Tests
Add tests in `employees/tests.py` and run: `python manage.py test`


## Deployment
- Set `DEBUG=False`, configure `ALLOWED_HOSTS`, and a real `SECRET_KEY`
- Use gunicorn: `gunicorn employee_project.wsgi:application --bind 0.0.0.0:8000`


## License
MIT
