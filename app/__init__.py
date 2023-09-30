from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_admin import Admin
from app.models import User, Group, Post
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import index
app.register_blueprint(index.bp)

from app import auth
app.register_blueprint(auth.bp)

from app import blog
app.register_blueprint(blog.bp)
# app.add_url_rule('/', endpoint='blog.index')

from app import about
app.register_blueprint(about.bp)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Post, db.session))

