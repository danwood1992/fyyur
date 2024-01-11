
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)
