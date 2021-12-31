from flask import Flask
from app.db import db
from app.auth.loginmanager import login_manager
from app.main import bluepriint as main_blueprint
from app.auth import blueprint as auth_blueprint

def create_app():
    app = Flask(__name__)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app:Flask):
    db.init_app(app)
    # login_manager.init_app(app)
    pass

def register_blueprints(app: Flask):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
