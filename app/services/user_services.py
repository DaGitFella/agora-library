from flask import jsonify, flash

from app.models.user import User
from app.db import db
from flask_login import current_user

def check_integrity(email):
    db_user = User.query.filter_by(email=email).first()
    if db_user:
        return True
    return False

def get_user_or_404(email):
    db_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if db_user:
        return db_user
    return None

def get_all_users():
    users = User.query.all()
    return users

def delete_user():
    user = db.session.execute(db.select(User).where(User.id == current_user.id)).scalar()
    if user:
        db.session.delete(user)
        db.session.commit()
        flash(f'user {current_user.name} deleted', 'success')
        return jsonify({
            'success': True,
        })

    return jsonify({
        'success': False,
        'message': 'user not found',
    }), 404