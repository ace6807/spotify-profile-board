from app.auth import blueprint
from flask import render_template

@blueprint.route('/login')
def login():
    return render_template("auth/login.html")
