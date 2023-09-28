from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import index
app.register_blueprint(index.bp)

from app import auth
app.register_blueprint(auth.bp)

from app import blog
app.register_blueprint(blog.bp)
# app.add_url_rule('/', endpoint='blog.index')

from app import about
app.register_blueprint(about.bp)
