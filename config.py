import os

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/fyyur'

SECRET_KEY = os.urandom(32)

DEBUG = True

