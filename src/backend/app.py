from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt = JWTManager(app)

    from application.controllers.video_controller import video_blueprint
    app.register_blueprint(video_blueprint, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=False)
