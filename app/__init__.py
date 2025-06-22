import flask_login
from flask import Flask
from flask_admin import Admin

from app.api import auth_controller
from app.routes import auth_routes, home_routes, user_routes
from app.db import db, migrate
from app.models import book as book
from app.models import user as user
from app.models.user import User
from config import Config

login_manager = flask_login.LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    admin = Admin(app, name='agora_library', template_mode='bootstrap3')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'

    app.register_blueprint(home_routes.home_bp)
    app.register_blueprint(user_routes.user_bp, url_prefix='/user')
    app.register_blueprint(auth_routes.auth_bp, url_prefix='/auth')
    app.register_blueprint(auth_controller.auth_api_bp, url_prefix='/api/auth')

    return app
