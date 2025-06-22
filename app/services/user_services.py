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

def delete_me():
    db.session.delete(current_user)
    db.session.commit()
    flash(f'Usuário {current_user.username} deletado com sucesso', 'success')
    return jsonify({
        'success': True,
    })

def update_me():
    ...
