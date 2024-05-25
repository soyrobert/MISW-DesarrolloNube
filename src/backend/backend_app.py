from flask import Flask, g, request
import uuid
import time
from flask_jwt_extended import JWTManager
from datetime import timedelta
from config import Config
from extensions import db
from application.controllers.video_controller import video_blueprint
from application.controllers.registro_controller import signup_blueprint
from application.controllers.login_controller import login_blueprint
from application.controllers.video_download_controller import video_download_blueprint
from application.controllers.health_controller import health_blueprint
from application.controllers.default_controller import default_blueprint




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 20 MB max size upload
    app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
    print("init app")
    db.init_app(app)
    print("app iniciada")
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = "45fba08e-3e90-4fc0-8daa-09f9cc564281"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
    jwt = JWTManager(app)

    print("Registering blueprints...")
    app.register_blueprint(video_blueprint, url_prefix='/api/tasks')
    app.register_blueprint(signup_blueprint, url_prefix='/api/auth/signup')
    app.register_blueprint(login_blueprint, url_prefix='/api/auth/login')
    app.register_blueprint(default_blueprint, url_prefix='/ping')
    app.register_blueprint(video_download_blueprint, url_prefix='/api/video')
    app.register_blueprint(health_blueprint, url_prefix='/api/health')
    print("Registered blueprints...")

    return app


app = create_app()

@app.before_request
def before_request_func():
    execution_id = uuid.uuid4()
    g.start_time = time.time()
    g.execution_id = execution_id
    print(g.execution_id, "ROUTE CALLED ", request.url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
