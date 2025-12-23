from flask import Blueprint, jsonify, request, render_template, redirect
from app.models import User, PersonalSchedule
from app import db

admin_bp = Blueprint('admin', __name__, template_folder='../templates')

@admin_bp.route('/admin')
def admin_dashboard():
    users = User.query.all()
    return render_template('admin.html', users=users)

@admin_bp.route('/admin/toggle_view/<int:user_id>')
def toggle_view(user_id):
    user = User.query.get(user_id)
    if user:
        user.can_view_others = not user.can_view_others
        db.session.commit()
    return redirect('/admin')

@admin_bp.route('/admin/add_schedule', methods=['POST'])
def add_schedule():
    user_id = request.form.get('user_id')
    title = request.form.get('title')
    time = request.form.get('time')
    
    if user_id and title and time:
        new_event = PersonalSchedule(user_id=user_id, title=title, time=time)
        db.session.add(new_event)
        db.session.commit()
    return redirect('/admin')