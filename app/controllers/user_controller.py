import flask_login
from flask import Blueprint, render_template
from flask_login import current_user

user_bp = Blueprint('user', __name__)


@user_bp.route('/me')
@flask_login.login_required
def me():
    return render_template('profile.html', user=current_user)
