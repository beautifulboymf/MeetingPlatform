from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
from app.models import User
from app import db

directory_bp = Blueprint('directory', __name__, template_folder='../templates')

@directory_bp.route('/view/directory')
@login_required
def view_directory():
    return render_template('directory.html')

@directory_bp.route('/api/directory')
@login_required
def get_directory():
    if not current_user.can_view_others:
        return jsonify({"error": "管理员未授权您查看参会者名录"}), 403
    attendees = User.query.filter_by(is_checked_in=True).all()
    return jsonify([u.to_dict() for u in attendees])