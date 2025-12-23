import os
from flask import Blueprint, jsonify, request, render_template
from app.models import User
from app import db

directory_bp = Blueprint(
    'directory', 
    __name__, 
    template_folder='../app/templates'
)

@directory_bp.route('/view/directory')
def view_directory():
    return render_template('directory.html')

@directory_bp.route('/api/directory')
def get_directory():
    # 模拟获取当前登录用户 (实际开发中这里通过 session 获取)
    # 为了测试方便，我们假设 URL 传参 ?user_id=1
    viewer_id = request.args.get('user_id', type=int)
    viewer = User.query.get(viewer_id)

    if not viewer:
        return jsonify({"error": "请先登录"}), 401
    
    # 权限检查：如果后台没有开启该用户的查看权限
    if not viewer.can_view_others:
        return jsonify({"error": "管理员未授权您查看参会者名录"}), 403

    # 获取所有已签到的参会者
    attendees = User.query.filter_by(is_checked_in=True).all()
    return jsonify([u.to_dict() for u in attendees])