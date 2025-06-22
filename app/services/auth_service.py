from flask import flash, jsonify, redirect, request, abort, url_for
from flask_login import login_user, logout_user

from app.db import db
from app.models.user import User
from app.services import user_services


def login_user_to_session():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_services.get_user_or_404(email)

    if not user:
        return jsonify({
            'sucess': False,
            'message': 'Email ou senha incorretos',
        }), 401

    if not user.verify_password(password):
        return jsonify({
            'sucess': False,
            'message': 'Email ou senha incorretos',
        }), 401

    login_user(user)

    flash('usuário logado com sucesso', 'success')
    return jsonify({
        'success': True,
    })


def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        abort(422)

    if user_services.check_integrity(email):
        abort(409)

    db_user = User(username=username, email=email, password=password)

    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)

    login_user(db_user)

    flash('Usuário registrado com sucesso', 'success')
    return jsonify({
        'success': True,
    })


def logout_user_from_session():
    logout_user()
    flash('Usuário deslogado com sucesso', 'success')
    return redirect(url_for('auth_bp.login'))
