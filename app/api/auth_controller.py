from flask import Blueprint

from app.services import auth_service

auth_controller_bp = Blueprint('auth_controller', __name__)


@auth_controller_bp.route('/login', methods=['POST'])
def login():
    return auth_service.login_user_to_session()


@auth_controller_bp.route('/logout', methods=['GET'])
def logout():
    return auth_service.logout_user_from_session()


@auth_controller_bp.route('/register', methods=['POST'])
def register():
    return auth_service.register_user()
