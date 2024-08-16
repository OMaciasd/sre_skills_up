from flask import Blueprint, render_template

web_blueprint = Blueprint('web', __name__)



@web_blueprint.route('/')
def home():
    return render_template('index.html')



@web_blueprint.route('/about')
def about():
    return render_template('about.html')
