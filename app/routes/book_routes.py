from flask import Blueprint, render_template

from app.services import book_service

book_bp = Blueprint('book_bp', __name__)


@book_bp.route('/catalog', methods=['GET'])
def catalog():
    books = book_service.get_all_books()
    return render_template('catalog.html', books=books, include_header=True)

@book_bp.route('', methods=['GET'])
def create_book():
    return render_template('book_creation_page.html', include_header=True)
