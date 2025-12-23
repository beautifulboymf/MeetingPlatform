from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user
from app.models import PersonalSchedule

schedule_bp = Blueprint('schedule', __name__, template_folder='../templates')

@schedule_bp.route('/view/my-schedule')
@login_required
def view_my_schedule():
    return render_template('my_schedule.html')

@schedule_bp.route('/api/my-schedule')
@login_required
def get_my_schedule():
    # 自动获取当前登录用户的行程
    schedules = PersonalSchedule.query.filter_by(user_id=current_user.id).all()
    return jsonify([s.to_dict() for s in schedules])