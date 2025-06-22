from flask import Blueprint

from app.services import book_service

book_controller_bp = Blueprint('book_controller', __name__)


@book_controller_bp.route('', methods=['POST'])
def create_book():
    return book_service.create_book()
