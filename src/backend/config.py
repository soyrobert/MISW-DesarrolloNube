import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_secreta')
    
    DB_NAME = os.environ.get('DB_NAME', 'idlr_db')
    DB_USER = os.environ.get('DB_USER', 'admin')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'admin')
    DB_CONNECTION_NAME = os.environ["DATABASE_CONNECTION_NAME"]
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@/"
        f"{DB_NAME}?unix_sock=/cloudsql/{DB_CONNECTION_NAME}/.s.PGSQL.5432"
    )
    
    # DATABASE_IP= os.environ['DATABASE_IP']
    # SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@" + DATABASE_IP + "/idlr_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # if 'DB_IP' in os.environ:
    #     SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@{os.environ['DB_IP']}/idlr_db"
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'tu_jwt_clave_secreta')
    UPLOAD_FOLDER = 'uploads/videos_sin_editar'
    UPLOAD_FOLDER_EDIT = 'uploads/videos_editados'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
