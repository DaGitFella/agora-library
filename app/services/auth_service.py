from flask import redirect, render_template, request, url_for, jsonify
from flask_login import login_user, logout_user

from app.db import db
from app.models.user import User
from app.services import user_services


def login_user_to_session():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_services.get_user_by_email(email)

    if not user:
        return jsonify({
            'success': False,
            'error': 'Usuário não encontrado',
        }), 404

    if not user.verify_password(password):
        return jsonify({
            'success': False,
            'error': 'Email ou senha incorretos'
        }), 401

    login_user(user)

    return redirect(url_for('home.index')), jsonify({
        'success': True,
        'message': 'usuário logado com sucesso'
    }), 200


def register_user():
    if request.method != 'POST':
        return render_template('register.html')

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({
            'success': False,
            'error': 'Todos os campos são obrigatórios'
        }), 422

    if user_services.check_integrity(email):
        return jsonify({
            'success': False,
            'error': 'O email já está em uso'
        }), 409

    db_user = User(username=username, email=email, password=password)

    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)

    login_user(db_user)

    return redirect(url_for('home.index')), jsonify({
        'success': True,
        'message': 'Usuário registrado com sucesso'
    }), 400


def logout_user_from_session():
    logout_user()
    return redirect(url_for('home.index')), jsonify({
        'success': True,
        'message': 'Usuário deslogado com sucesso'
    }), 200
