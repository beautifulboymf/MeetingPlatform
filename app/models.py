from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    company = db.Column(db.String(100))
    position = db.Column(db.String(50))
    can_view_others = db.Column(db.Boolean, default=False)
    is_checked_in = db.Column(db.Boolean, default=False)
    # 建立与行程的一对多关联
    schedules = db.relationship('PersonalSchedule', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "company": self.company,
            "position": self.position,
            "can_view_others": self.can_view_others,
            "is_checked_in": self.is_checked_in
        }
    
class PersonalSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False) # 行程名称
    time = db.Column(db.String(50), nullable=False)  # 时间点
    location = db.Column(db.String(100))             # 地点

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "time": self.time,
            "location": self.location
        }