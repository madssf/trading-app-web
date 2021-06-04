# trading-app-web

## Docker

Might need:

```bash
sudo chmod +x entrypoint.sh
```

Gunicorn

```bash
gunicorn server.wsgi:application --bind 0.0.0.0:8000 --workers=4
```

## Backend:

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

# create super user
./manage.py createsuperuser
# load seed data
#./manage.py loaddata seed.json
./manage.py runserver
```

## Scripts:

```bash
cd scripts
# python 3
python3 -m virtualenv venv
source venv/bin/activate #deactivate to quit
pip install -r requirerments.txt

```

## Tech stack:

- Django, React, Python, PostgreSQL

## Business goals:

- Make coin research easier and social
- Automated trading strategies based on research
- Ability to have your portfolio use other peoples strategies
- Staking optimizing
- Minimizing market risk
- Encouraging fundamental view and hodling???
