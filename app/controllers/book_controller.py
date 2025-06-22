import flask_login
from flask import Blueprint

book_bp = Blueprint('book', __name__)

@book_bp.route('/')
@flask_login.login_required
def index():
    ...