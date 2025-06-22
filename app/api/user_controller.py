from flask import Blueprint

user_controller_bp = Blueprint('user_controller', __name__)


@user_controller_bp.route('/', methods=['DELETE'])
def delete_user():
    ...
