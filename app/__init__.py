from flask import Flask
from .config import Config
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
migrate = Migrate(app, db)


mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
from . import views

