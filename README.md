# trading-app-web

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

Go to main folder:

```bash
docker-compose up --build
```

## Running backend without Docker:

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

## Scripts:

1. Go to /scripts/, make a file called 'config.py', add the following:

```python
# Make a new instance, edit config.py to match project.env for Docker
import os

class Endpoints:
    # 8000 when running locally, 1337 with Docker/Nginx
    PORT = ["8000", "1337"]
    BASE = f"http://localhost:{PORT[1]}/api/v1/"
    LOGIN = BASE+"token/login"


class Parameters:
    # For coingecko
    BASE_FIAT = "USD"
    # Coins we don't need in our database, leave empty list if none.
    STABLECOINS = ['USDT', 'USDC', 'BUSD',
                   'TUSD', 'DAI', 'CUSDC', 'CDAI', 'CUSDC']


class Superuser:
    # Users for Django requests
    USERS = ['insert', 'usernames']
    PASSWORDS = ['insert', "passwords"]

```

2. Install requirements

```bash
cd scripts
# python 3
python3 -m virtualenv venv
source venv/bin/activate #deactivate to quit
pip install -r requirerments.txt

```

## Stack:

- Django, React, Python, PostgreSQL

## Business goals:

- Make coin research easier and social
- Automated trading strategies based on research
- Ability to have your portfolio use other peoples strategies
- Staking optimizing
- Minimizing market risk
- Encouraging fundamental view and hodling???
