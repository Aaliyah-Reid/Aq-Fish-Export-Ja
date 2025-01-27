from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
import os
from .config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
from app import views


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port)