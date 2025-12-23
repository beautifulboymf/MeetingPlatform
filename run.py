from app import create_app, db
from app.models import User
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app = create_app()

@app.cli.command("init-db")
def init_db():
    db.drop_all()
    db.create_all()
    
    # 预设管理员账户
    admin = User(username="张三", company="科技公司", position="CEO", role="admin", can_view_others=True)
    admin.set_password("admin123")
    
    # 预设普通参会者
    user = User(username="李四", company="商贸公司", position="经理", role="user", is_checked_in=True)
    user.set_password("user123")
    
    db.session.add_all([admin, user])
    db.session.commit()
    print("数据库重置完成。")
    print("管理员账号：张三 密码：admin123")
    print("普通账号：李四 密码：user123")

if __name__ == '__main__':
    app.run(debug=True)