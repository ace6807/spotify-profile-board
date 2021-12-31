from app.main import bluepriint
from flask import render_template

@bluepriint.route('/')
def index():
    return render_template("main/index.html")


@bluepriint.route('/test')
def test():
    return "You are at test"

