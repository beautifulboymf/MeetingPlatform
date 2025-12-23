from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

# app/__init__.py
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # 确保是从顶级目录导入 directory
    try:
        from directory.routes import directory_bp
        app.register_blueprint(directory_bp)
    except ImportError as e:
        print(f"蓝图注册失败: {e}")

    return app