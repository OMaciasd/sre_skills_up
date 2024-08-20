from flask import Flask, render_template
from users.controllers.user_controller import user_controller


app = Flask(__name__)
app.config.from_object('config.Config')


app.register_blueprint(user_controller)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/edit/<string:id>')
def edit_user(id):
    print("id recibido", id)
    return render_template('edit.html', id=id)


if __name__ == '__main__':
    app.run()
