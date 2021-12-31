from app.main import blueprint
from flask import render_template

@blueprint.route('/')
def index():
    return render_template("main/index.html")


@blueprint.route('/test')
def test():
    return "You are at test"
