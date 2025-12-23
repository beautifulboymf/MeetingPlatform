from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login' # 未登录时跳转的页面

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    try:
        from directory.routes import directory_bp
        from schedule.routes import schedule_bp
        from admin.routes import admin_bp
        from main.routes import main_bp
        from auth.routes import auth_bp # 新增认证模块

        app.register_blueprint(directory_bp)
        app.register_blueprint(schedule_bp)
        app.register_blueprint(admin_bp)
        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)
        
        print("✅ 成功注册所有蓝图，包含认证模块")
    except ImportError as e:
        print(f"❌ 蓝图注册失败: {e}")
        raise e 

    return app