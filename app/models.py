from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128)) # 存储哈希后的密码
    company = db.Column(db.String(100))
    position = db.Column(db.String(50))
    role = db.Column(db.String(20), default='user') # 'admin' 或 'user'
    can_view_others = db.Column(db.Boolean, default=False)
    is_checked_in = db.Column(db.Boolean, default=False)
    
    schedules = db.relationship('PersonalSchedule', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "company": self.company,
            "position": self.position,
            "can_view_others": self.can_view_others,
            "is_checked_in": self.is_checked_in,
            "role": self.role
        }
    
class PersonalSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "time": self.time,
            "location": self.location
        }