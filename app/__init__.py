import flask_login
from flask import Flask
from flask_admin import Admin

from app.api import auth_controller, user_controller
from app.db import db, migrate
from app.models import book as book
from app.models import user as user
from app.models.user import User
from app.models.admin import AdminView
from app.routes import auth_routes, home_routes, user_routes
from config import Config
from app.error_handlers import register_error_handlers

login_manager = flask_login.LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    admin = Admin(app, name='agora_library',
                  template_mode='bootstrap3',
                  index_view=AdminView()
                  )
    register_error_handlers(app, login_manager)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'

    app.register_blueprint(home_routes.home_bp)
    app.register_blueprint(user_routes.user_bp, url_prefix='/users')
    app.register_blueprint(auth_routes.auth_bp, url_prefix='/auth')
    app.register_blueprint(auth_controller.auth_controller_bp,
                           url_prefix='/api/auth')
    app.register_blueprint(user_controller.user_controller_bp,
                           url_prefix='/api/users')

    return app
