# webapp/__init__.py

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('webapp.config')

    # Importar y registrar blueprints
    from webapp.web import web_blueprint
    app.register_blueprint(web_blueprint)

    return app
