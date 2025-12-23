from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # 注册蓝图
    from directory.routes import directory_bp
    app.register_blueprint(directory_bp)

    return app