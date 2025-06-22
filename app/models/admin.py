from flask_admin import AdminIndexView
from flask_login import current_user
from flask import flash, redirect, url_for

class AdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        flash('Você não tem permissão para acessar este recurso.', 'danger')
        return redirect(url_for('auth_bp.login'))
