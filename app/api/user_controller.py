from flask import Blueprint
from app.services import user_services

user_controller_bp = Blueprint('user_controller', __name__)


@user_controller_bp.route('/delete', methods=['DELETE'])
def delete_user():
    return user_services.delete_user()
