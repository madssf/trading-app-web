# trading-app-web

- Django, React-Redux, Python, PostgreSQL

## Docker

1. Go to /backend/, make a file called 'project.env', add the following (fill in the blanks):

```.env
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

DATABASE=postgres
DATABASE_HOST=postgresdb
DATABASE_PORT=5432

SUPERUSER_USERNAME=
SUPERUSER_PASSWORD=
SUPERUSER_EMAIL=
DJANGO_SECRET_KEY=
```

Terminal to /backend/:

```bash
docker-compose up --build
```

## Running scripts

See:
[Running scripts](scripts/README.md)

## Running backend without Docker

```bash
cd backend
# python 3
python3 -m virtualenv venv
source venv/bin/activate #deactivate to quit
pip install -r requirements.txt
cd server

# set up db
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser

./manage.py runserver
```
