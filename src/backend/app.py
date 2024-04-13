from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
from config import Config
from extensions import db
from application.controllers.video_controller import video_blueprint
from application.controllers.registro_controller import signup_blueprint, login_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = "45fba08e-3e90-4fc0-8daa-09f9cc564281"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
    jwt = JWTManager(app)

    app.register_blueprint(video_blueprint, url_prefix='/api')
    app.register_blueprint(signup_blueprint, url_prefix='/api')
    app.register_blueprint(login_blueprint, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
