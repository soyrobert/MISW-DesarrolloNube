from flask import Blueprint, jsonify


default_blueprint = Blueprint('default', __name__)

@default_blueprint.route("/", methods=['GET'], strict_slashes=False)
def default():
    try:
        return jsonify({'message': 'Ok'}), 200
    except Exception as e:
        return jsonify({
            'message': 'Ha ocurrido un error',
            'error': str(e)
        }), 500
