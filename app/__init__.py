import flask_login
from flask import Flask
from flask_admin import Admin

from app.api.auth_controller import auth_controller_bp
from app.api.book_controller import book_controller_bp
from app.api.user_controller import user_controller_bp
from app.db import db, migrate
from app.error_handlers import register_error_handlers
from app.models import book as book
from app.models import user as user
from app.models.admin import AdminUserView, AdminView
from app.models.user import User
from app.routes.auth_routes import auth_bp
from app.routes.book_routes import book_bp
from app.routes.home_routes import home_bp
from app.routes.user_routes import user_bp
from config import Config

login_manager = flask_login.LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    admin = Admin(app, name='agora_library',
                  template_mode='bootstrap3',
                  index_view=AdminView()
                  )
    admin.add_view(AdminUserView(User, db.session))
    register_error_handlers(app, login_manager)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'

    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(book_bp, url_prefix='/books')
    app.register_blueprint(auth_controller_bp,
                           url_prefix='/api/auth')
    app.register_blueprint(user_controller_bp,
                           url_prefix='/api/users')
    app.register_blueprint(book_controller_bp,
                           url_prefix='/api/books')

    return app
