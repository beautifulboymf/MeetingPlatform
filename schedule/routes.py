from flask import Blueprint, jsonify, request, render_template
from app.models import User, PersonalSchedule
from app import db

schedule_bp = Blueprint('schedule', __name__, template_folder='../templates')

@schedule_bp.route('/view/my-schedule')
def view_my_schedule():
    return render_template('my_schedule.html')

@schedule_bp.route('/api/my-schedule/<int:user_id>')
def get_my_schedule(user_id):
    schedules = PersonalSchedule.query.filter_by(user_id=user_id).all()
    return jsonify([s.to_dict() for s in schedules])