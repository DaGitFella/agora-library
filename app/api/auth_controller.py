from flask import Blueprint, render_template

from app.services import auth_service

auth_api_bp = Blueprint('api/auth', __name__)

@auth_api_bp.route('/login', methods=['POST'])
def login():
    return auth_service.login_user_to_session()

@auth_api_bp.route('/logout', methods=['POST'])
def logout():
    return auth_service.logout_user_from_session()


@auth_api_bp.route('/register', methods=['POST'])
def register():
    return auth_service.register_user()
