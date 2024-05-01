from flask import Blueprint, jsonify
from application.models.models import db

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health', methods=['GET'])
def health_check():
    response = {
        "status": "healthy",
        "database": "connected"
    }

    # Verificando conexión con la base de datos
    try:
        # Realiza una consulta simple
        result = db.session.execute('SELECT 1')
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        response["database"] = "disconnected"
        response["status"] = "unhealthy"
        response["error"] = str(e)

    return jsonify(response)
