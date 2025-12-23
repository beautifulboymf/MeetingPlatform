from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models import User, PersonalSchedule
from app import db

admin_bp = Blueprint('admin', __name__, template_folder='../templates')

@admin_bp.route('/admin')
@login_required
def admin_dashboard():
    # 核心安全逻辑：检查是否为管理员
    if current_user.role != 'admin':
        flash('您没有权限进入管理后台')
        return redirect(url_for('main.index'))
    # 获取所有用户，以便管理他们的权限和行程
    users = User.query.all()
    return render_template('admin.html', users=users)

@admin_bp.route('/admin/toggle_view/<int:user_id>')
@login_required
def toggle_view(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))
    user = User.query.get(user_id)
    if user:
        user.can_view_others = not user.can_view_others
        db.session.commit()
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/admin/add_schedule', methods=['POST'])
@login_required
def add_schedule():
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))
    user_id = request.form.get('user_id')
    title = request.form.get('title')
    time = request.form.get('time')
    
    if user_id and title and time:
        new_event = PersonalSchedule(user_id=user_id, title=title, time=time)
        db.session.add(new_event)
        db.session.commit()
    return redirect(url_for('admin.admin_dashboard'))

# 新增：删除特定行程的路由
@admin_bp.route('/admin/delete_schedule/<int:schedule_id>')
@login_required
def delete_schedule(schedule_id):
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))
    schedule = PersonalSchedule.query.get(schedule_id)
    if schedule:
        db.session.delete(schedule)
        db.session.commit()
    return redirect(url_for('admin.admin_dashboard'))