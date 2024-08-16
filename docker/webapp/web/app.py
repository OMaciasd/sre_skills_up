from flask import Flask


def create_app():
    app = Flask(__name__)
    # Configura la aplicación, incluyendo las rutas

    @app.route('/app')
    def app_route():
        return 'This is the app route!'
    return app
