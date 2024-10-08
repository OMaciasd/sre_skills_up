from flask import Blueprint, request, jsonify
from users.models.user_model import Users
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db')  # Use your database URL
Session = sessionmaker(bind=engine)
session = Session()


user_controller = Blueprint('user_controller', __name__)


@user_controller.route('/api/users', methods=['GET'])
def get_users():
    print("listado de usuarios")
    users = Users.query.all()
    result = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'username': user.username
        }
        for user in users
    ]
    return jsonify(result)


@user_controller.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    print("obteniendo usuario")
    user = Users.query.get_or_404(user_id)
    return jsonify(
        {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'username': user.username
        }
    )


@user_controller.route('/api/users', methods=['POST'])
def create_user():
    print("creando usuario")
    data = request.json

    new_user = Users(
        name=data['name'],
        email=data['email'],
        username=data['username'],
        password=data['password']
    )

    session.add(new_user)
    session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@user_controller.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    print("actualizando usuario")
    user = Users.query.get_or_404(user_id)
    data = request.json
    user.name = data['name']
    user.email = data['email']
    user.username = data['username']
    user.password = data['password']
    return jsonify({'message': 'User updated successfully'})


@user_controller.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    })
    return jsonify({'message': 'User deleted successfully'})
