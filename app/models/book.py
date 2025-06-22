from enum import Enum

from sqlalchemy import Enum as SQLEnum

from app.db import db


class BookStatus(Enum):
    new = 'new'
    used = 'used'
    semi_new = 'semi-new'


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120))
    publication_date = db.Column(db.DateTime)
    status = db.Column(SQLEnum(BookStatus, name='book_status'), nullable=False)
    donated = db.Column(db.Boolean, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
