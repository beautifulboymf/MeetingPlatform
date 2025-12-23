from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    company = db.Column(db.String(100))
    position = db.Column(db.String(50))
    # 核心权限：是否允许该用户查看名录
    can_view_others = db.Column(db.Boolean, default=False)
    # 状态：是否已签到
    is_checked_in = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "company": self.company,
            "position": self.position,
            "is_checked_in": self.is_checked_in
        }