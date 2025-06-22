from flask import jsonify, flash, request, abort

from app.models.user import User
from app.db import db
from flask_login import current_user

def check_integrity(resource_name: str, resource):
    if resource_name not in {"username", "email"}:
        raise ValueError("Invalid resource_name")
    db_user = User.query.filter_by(**{resource_name: resource}).first()
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
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if check_integrity('email', email):
        return jsonify({
            'success': False,
            'error': 'O email já existe',
        }), 409

    if check_integrity('username', username):
        return jsonify({
            'success': False,
            'error': 'O username já existe',
        }), 409

    if email and email != current_user.email:
        current_user.email = email

    if password:
        current_user.password = password

    if username and username != current_user.username:
        current_user.username = username

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Usuário atualizado com sucesso',
    })


