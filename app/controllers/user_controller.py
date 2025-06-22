from flask import Blueprint, render_template
from flask_login import current_user

user_bp = Blueprint('user_controller', __name__)


@user_bp.route('/')
def index():
    return render_template('profile.html', user=current_user)
