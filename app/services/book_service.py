from flask import request, jsonify, redirect, url_for, flash

from app.db import db
from app.models.book import Book


def get_all_books():
    books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return books


def create_book(book):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')
    publisher = data.get('publisher')
    publication_date = data.get('publication_date')
    status = data.get('status')
    donated = data.get('donated')
    unit_price = data.get('unit_price')
    stock = data.get('stock')

    new_book = Book(
        title=title,
        author=author,
        genre=genre,
        publisher=publisher,
        publication_date=publication_date,
        status=status,
        donated=donated,
        unit_price=unit_price,
        stock=stock,
    )

    db.session.add(new_book)
    db.session.commit()
    db.session.refresh(new_book)
    flash('Livro criado com sucesso!','success')
    return redirect(url_for('book_bp.catolog'))
