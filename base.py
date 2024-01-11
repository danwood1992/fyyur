
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

moment = Moment(app)

db = SQLAlchemy(app)