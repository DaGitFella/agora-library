from flask import flash, redirect, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms import BooleanField, Form, StringField
from wtforms.validators import DataRequired, Email


class AdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        flash('Você não tem permissão para acessar este recurso.', 'danger')
        return redirect(url_for('home_bp.index'))


class UserForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    is_admin = BooleanField('Is Admin')


class AdminUserView(ModelView):
    form = UserForm
    can_create = True
    column_list = ('id', 'name', 'email', 'is_admin')
