import os
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
import controllers

# TODO: connect to a local postgresql database

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

app = Flask(__name__)

moment = Moment(app)

db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/fyyur'

SECRET_KEY = os.urandom(32)

DEBUG = True

