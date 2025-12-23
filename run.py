from app import create_app, db
from app.models import User

app = create_app()

@app.cli.command("init-db")
def init_db():
    """初始化数据库并添加测试数据"""
    db.create_all()
    # 创建三个测试用户
    # 1. 有权限的VIP
    u1 = User(username="张三", company="科技公司", position="CEO", can_view_others=True, is_checked_in=True)
    # 2. 无权限的普通参会者
    u2 = User(username="李四", company="商贸公司", position="经理", can_view_others=False, is_checked_in=True)
    # 3. 未签到的用户（名录不显示）
    u3 = User(username="王五", company="制造工厂", position="技术员", can_view_others=True, is_checked_in=False)
    
    db.session.add_all([u1, u2, u3])
    db.session.commit()
    print("数据库初始化完成，测试数据已插入。")

if __name__ == '__main__':
    app.run(debug=True)