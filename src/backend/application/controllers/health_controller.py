from flask import Blueprint, jsonify, make_response
from application.models.models import db
from sqlalchemy import text

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health', methods=['GET'])
def health_check():
    response = {
        "status": "healthy",
        "database": "connected"
    }

    try:

        db.session.execute(text('SELECT 1'))
        db.session.commit()

        return make_response(jsonify(response), 200)
    except Exception as e:
        db.session.rollback()
        response["database"] = "disconnected"
        response["status"] = "unhealthy"
        response["error"] = str(e)

        return make_response(jsonify(response), 503)
