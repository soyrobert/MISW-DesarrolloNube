from flask import Blueprint, request, jsonify
from application.models.models import  User
from flask_jwt_extended import create_access_token
from datetime import timedelta

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/auth/login/ping', methods=['GET'])
def ping():
    try:
        User.query.first()
        return jsonify({'message': 'pong'}), 200
    except Exception as e:
        return {'message': 'Ha ocurrido un error'}, 500

@login_blueprint.route('/auth/login', methods=['POST'])
def login():
    """
    Permite recuperar el token de autorización para consumir los recursos del API
    suministrando el nombre de usuario y la contraseña de una cuenta previamente
    registrada.

    Args:
    - username : str, el nombre del usuario.
    - password: str, el password del usuario.

    Returns:
    - 200: Usuario autenticado
    - 401: Usuario no autenticado
    """
    try:
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        # valdiate basic validation str and return error if not empty
        error = basic_validation(data)
        if error:
            return error

        # validate user in the database and return error if not empty
        error = user_validation(username, password)
        if error:
            return error
        
        # create jwt
        token = create_access_token(identity=username, expires_delta = timedelta(days = 1))
        return jsonify({'token': token}), 200
    except:
        return {'message':'Ha ocurrido un error'}, 500


def basic_validation(data) -> str:
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Faltan campos por llenar'}), 400

    if len(password) < 8:
        return jsonify({'message': 'La contraseña debe tener al menos 8 caracteres'}), 400

    return None



def user_validation(username: str, password: str) -> str:
    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({'message': 'Usuario no encontrado'}), 401

    if not user.check_password(password):
        return jsonify({'message': 'Contraseña incorrecta'}), 401

    return None