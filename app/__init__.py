import flask_login
from flask import Flask

from app.controllers.auth_controller import auth_bp
from app.controllers.home_controller import home_bp
from app.controllers.user_controller import user_bp
from app.db import db, migrate
from app.models.user import User
from config import Config

login_manager = flask_login.LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
