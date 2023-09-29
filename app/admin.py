import functools
import re
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2

from flask_admin import Admin

from app.db import get_db

bp = Blueprint('admin', __name__)

