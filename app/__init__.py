from flask import Flask
from app.db import db
from app.auth.loginmanager import login_manager
from app.main import blueprint as main_blueprint
from app.auth import blueprint as auth_blueprint
from config import Config

def create_app(config: Config):
    app = Flask(__name__)
    app.config.from_object(config)    
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app:Flask):
    db.init_app(app)
    login_manager.init_app(app)
    pass

def register_blueprints(app: Flask):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

from app.models import User