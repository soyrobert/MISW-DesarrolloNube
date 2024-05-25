from flask import Blueprint, request, jsonify
from application.models.models import db, User

signup_blueprint = Blueprint('signup', __name__)


@signup_blueprint.route('/ping', methods=['GET'])
def ping():
    try:
        return jsonify({'message': 'pong'}), 200
    except Exception as e:
        return jsonify({
            'message': 'Ha ocurrido un error',
            'error': str(e)
        }), 500


@signup_blueprint.route('/', methods=['POST'])
def signup():
    """
    Permite crear una cuenta con los campos para nombre de usuario, correo electrónico y
    contraseña. El nombre y el correo electrónico deben ser únicos en la plataforma,
    mientras que la contraseña debe seguir unos lineamientos mínimos de seguridad.
    Adicionalmente, la clave debe ser solicitada dos veces para que el usuario confirme que
    la ingresa de forma correcta.

    Args:
    - username : str, el nombre del usuario.
    - password1: str, el password del usuario.
    - password2: str, el password del usuario. Debe ser igual a password1.
    - email: str, el correo electrónico del usuario.

    Returns:
    - 201: Usuario creado    
    """
    try:
        data = request.get_json()

        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')
        email = data.get('email')

        # valdiate basic validation str and return error if not empty
        error = basic_validation(data)
        if error:
            return error

        # validate user in the database and return error if not empty
        error = user_validation(username, email)
        if error:
            return error

        new_user = User(username=username, email=email, password1=password1)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Usuario creado'}), 201
    except Exception as e:
        return jsonify({
            'message': 'Ha ocurrido un error',
            'error': str(e)
        }), 500


def basic_validation(data) -> dict:
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')
    email = data.get('email')

    if not username or not password1 or not password2 or not email:
        return jsonify({'message': 'Faltan campos por llenar'}), 400

    if password1 != password2:
        return jsonify({'message': 'Las contraseñas no coinciden'}), 400

    if len(password1) < 8:
        return jsonify({'message': 'La contraseña debe tener al menos 8 caracteres'}), 400

    return None

# validation of user in the database
def user_validation(username: str, email: str) -> dict:
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'El usuario ya existe'}), 400
    
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'El correo electrónico ya existe'}), 400

    return None

