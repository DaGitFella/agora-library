from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html', include_header=True)


@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html', include_header=True)
