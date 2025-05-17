from flask import Blueprint
from app.services import auth_service

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return auth_service.login_user_to_session()

@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return auth_service.logout_user()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return auth_service.register_user()




