import os


class Database:
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')


class Secrets:
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


class Superuser:
    USERNAME = os.getenv('SUPERUSER_USERNAME')
    PASSWORD = os.getenv('SUPERUSER_PASSWORD')
    EMAIL = os.getenv('SUPERUSER_EMAIL')
