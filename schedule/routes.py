from flask import Blueprint, jsonify, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import PersonalSchedule

schedule_bp = Blueprint('schedule', __name__, template_folder='../templates')

@schedule_bp.route('/view/my-schedule')
@login_required
def view_my_schedule():
    # 管理员不需要行程安排，若访问则重定向
    if current_user.role == 'admin':
        flash('管理员账号无需查看个人行程')
        return redirect(url_for('main.index'))
    return render_template('my_schedule.html')

@schedule_bp.route('/api/my-schedule')
@login_required
def get_my_schedule():
    # 自动获取当前登录用户的行程
    schedules = PersonalSchedule.query.filter_by(user_id=current_user.id).all()
    return jsonify([s.to_dict() for s in schedules])