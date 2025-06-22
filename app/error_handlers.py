from flask import jsonify, render_template, request
from app.db import db

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        if request.accept_mimetypes.accept_json \
                and not request.accept_mimetypes.accept_html:
            return jsonify({
                'success': False,
                'error': 'Recurso não encontrado',
            }), 404
        return render_template("errors/error_404.html"), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 'Email ou senha incorretos',
        }), 401

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

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template("500.html"), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({"error": "Internal Server Error"}), 500
