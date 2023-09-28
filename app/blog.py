from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort



bp = Blueprint('blog', __name__, url_prefix='/blog')
@bp.route('/')
def index():
    return render_template('blog/index.html')

@bp.route('/create')
def create():
    return render_template('blog/create.html')
@bp.route('/read')
def read():
    return render_template('blog/read.html')

@bp.route('/update')
def update():
    return render_template('blog/update.html')
