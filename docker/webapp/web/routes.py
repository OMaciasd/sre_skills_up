from flask import Blueprint, render_template

# Crea un Blueprint llamado 'web_blueprint'
web_blueprint = Blueprint('web', __name__)

# Define una ruta para la página principal


@web_blueprint.route('/')
def home():
    return render_template('index.html')

# Define una ruta para otra página, por ejemplo, "about"


@web_blueprint.route('/about')
def about():
    return render_template('about.html')
