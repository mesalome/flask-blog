import functools
import re
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username'].lower()
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None

        spaces_in_username = re.search(' ', username)
        spaces_in_password = re.search(' ', password)
        
        def strong_password(text):
            return re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()_\-+={[}\]|:;\"'<,>.?/]).{8,}$", text)
        
        if not username:
            error = 'Username is required.'
        elif spaces_in_username:
            error = "Username can't contain spaces."
        elif not password:
            error = 'Password is required.'
        elif spaces_in_password:
            error = "Password can't contain spaces."
        elif len(password) < 8:
            error = "Password must contain at least 8 characters."
        elif not strong_password(password):
            error = "Password must contain upper and lower case letters, numbers, and special characters."

        if error is None:
            try:
                cursor = db.cursor()
                cursor.execute(
                    "INSERT INTO users (username, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)",
                    (username, first_name, last_name, email, generate_password_hash(password)),
                )
                db.commit()
                cursor.close()
            except psycopg2.IntegrityError:
                error = f"User {username} is already registered."
            else:
                cursor = db.cursor()
                cursor.execute("SELECT * FROM groups")
                available_groups = cursor.fetchall()
                cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
                user_id = cursor.fetchone()
                for group in available_groups:
                    group_id = group[0]
                    field_name = f"group_{group_id}"
                    if field_name in request.form and request.form[field_name] == "on":
                        cursor.execute(
                            "INSERT INTO user_group_association (user_id, group_id) VALUES (%s, %s)",
                            (user_id, group_id)
                        )
                
                db.commit()
                cursor.close()
                return redirect(url_for("auth.login"))
        
        flash(error, "danger")

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM groups")
    groups = cursor.fetchall()
    return render_template('auth/register.html', groups=groups)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            cursor = db.cursor()
            cursor.execute(
                'SELECT * FROM users WHERE username = %s',
                (username,)
            )
            user = cursor.fetchone()
            cursor.close()

            if user is None:
                error = 'Incorrect username.'
            elif not check_password_hash(user[5], password):
                error = 'Incorrect password.'

            if error is None:
                session.clear()
                session['user_id'] = user[0]
                return redirect(url_for('blog.index'))

        flash(error, "danger")

    return render_template('auth/login.html')



@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        cursor = get_db().cursor()
        cursor.execute(
            'SELECT * FROM users WHERE id = %s', (user_id,)
        )
        user = cursor.fetchone()
        cursor.close()

        if user is None:
            g.user = None
        else:
            g.user = user


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

