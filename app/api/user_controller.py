import flask_login
from flask import Blueprint
from app.services import user_services

user_controller_bp = Blueprint('user_controller', __name__)


@user_controller_bp.route('/me', methods=['DELETE'])
@flask_login.login_required
def delete_user():
    return user_services.delete_me()

@user_controller_bp.route('/me', methods=['PUT'])
@flask_login.login_required
def update_me():
    return user_services.update_me()



