from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from . import views

