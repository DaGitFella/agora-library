from flask import render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_user
from app.models.user import User
from app.services import user_services
from app.db import db


def login_user_to_session():
    user = user_services.get_user_by_email(request.form.get('email'))
    if not user:
        flash('usuário não encontrado')
    if request.method == 'POST' and user.verify_password(request.form.get('password')):
        login_user(user)
        flash('usuário logado com sucesso')
        return redirect(url_for('home.index'))
    flash('Email ou senha incorretos')
    return render_template('login.html')

def register_user():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    db_user = User(username=username, email=email, password=password)
    if not user_services.check_if_user_exists(db_user, email):
        flash('usuário já existe')
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        db.session.add(db_user)
        db.session.commit()
        login_user()
        flash('usuário registrado com sucesso')
        return redirect(url_for('home.html'))

    return render_template('register.html')

def logout_user():
    logout_user()
    flash('usuário deslogado com sucesso')
    return redirect(url_for('home.html'))


