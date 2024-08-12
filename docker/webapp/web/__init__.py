from flask import Blueprint

web_blueprint = Blueprint('web', __name__)


@web_blueprint.route('/')
def home():
    return "Welcome to the web blueprint!"
