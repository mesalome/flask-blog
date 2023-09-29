from flask import Blueprint, render_template,request

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/')
def index():
    return render_template('about.html', current_url=request.path)
