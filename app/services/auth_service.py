from flask import render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_user
from app.models.user import User
from app.services import user_services
from app.db import db


def login_user_to_session():
    if request.method != 'POST':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = user_services.get_user_by_email(email)

    if not user:
        flash('Usuário não encontrado', 'danger')
        return render_template('login.html')

    if not user.verify_password(password):
        flash('Email ou senha incorretos', 'danger')
        return render_template('login.html')

    login_user(user)
    flash('Usuário logado com sucesso', 'success')
    return redirect(url_for('home.index'))

def register_user():
    if request.method != 'POST':
        return render_template('register.html')

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if not username or not email or not password:
        flash('todos os campos são obrigatórios')
        return redirect(url_for('auth.register'))

    if user_services.check_if_user_exists(email):
        flash('usuário já existe')
        return redirect(url_for('auth.login'))

    db_user = User(username=username, email=email, password=password)

    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)

    login_user(db_user)

    flash('usuário registrado com sucesso')
    return redirect(url_for('home.index'))

def logout_user_from_session():
    logout_user()
    flash('usuário deslogado com sucesso')
    return redirect(url_for('home.index'))


