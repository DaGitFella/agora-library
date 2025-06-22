from flask import jsonify, render_template, request, flash, redirect, url_for

from app.db import db

def register_error_handlers(app, login_manager):
    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/error_404.html"), 404

    @app.errorhandler(401)
    def not_permited(error):
        return jsonify({
            'success': False,
            'error': 'Você precisa estar logado para acessar este recurso.'
        }), 401

    @app.errorhandler(403)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 'Sem permissões o suficiente.',
        }), 403

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 'Todos os campos são obrigatórios',
        }), 422

    @app.errorhandler(409)
    def integrity(error):
        return jsonify({
            'success': False,
            'error': 'Email já em uso',
        }), 409

    @login_manager.unauthorized_handler
    def login_manager_unauthorized():
        flash('Você precisa estar logado para acessar este recurso.', 'warning')
        return redirect(url_for('auth_bp.login'))


    @app.errorhandler(500)
    def internal_error(error):
        import traceback
        traceback.print_exc()
        db.session.rollback()
        return render_template("500.html"), 500
