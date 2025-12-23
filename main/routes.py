from flask import Blueprint, render_template

# 定义首页蓝图，指定模板路径为平级 app 文件夹下的 templates
main_bp = Blueprint('main', __name__, template_folder='../templates')

@main_bp.route('/')
def index():
    # 渲染首页模板
    return render_template('index.html')