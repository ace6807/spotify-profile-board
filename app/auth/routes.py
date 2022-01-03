from urllib.parse import urlsplit, urlunsplit
from flask_login.utils import login_required, logout_user
from app.db import db
from app.auth import blueprint
from flask import render_template, request, current_app, url_for, redirect
from flask_login import login_user, current_user
from app.models import User

def build_route(root_url:str, controller:str):
    scheme, netloc, _, _, _ = urlsplit(root_url)
    redirect_path = url_for(controller)
    return urlunsplit((scheme,netloc,redirect_path,"",""))

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    # TODO: Pass request state
    context = {
        "client_id": current_app.config.get("SPOTIFY_CLIENT_ID"),
        "response_type": "code",
        "redirect_uri": build_route(request.root_url, 'auth.redirect_from_authorization'),
        "scope": "user-read-email playlist-read-private user-top-read",
    }
    return render_template("auth/login.html", **context)

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@blueprint.route('/authorization-redirect', methods=["GET", "POST"])
def redirect_from_authorization():
    """Endpoint that user gets redirected back to from Spotify authorization. Incoming
    authorization code can be excahnged for an access token.

    The request query string should contain:
        Success: code and state
        Failure: error and state

    """
    # TODO: Check request state
    if request.args.get("error"):
        return request.args.get("error")

    from app.clients import spotify_client
    ret = spotify_client.get_access_token(
        current_app.config.get("SPOTIFY_CLIENT_ID"),
        current_app.config.get("SPOTIFY_CLIENT_SECRET"),
        request.args.get("code"),
        build_route(request.root_url, 'auth.redirect_from_authorization')
    )

    access_token = ret.json().get("access_token")

    prof_resp = spotify_client.get_user_profile(access_token).json()

    existing_user = User.query.filter_by(spotify_id=prof_resp.get("id")).first()

    if existing_user:
        login_user(existing_user)
        return "Welcome Back"

    try:
        new_user = User(
            spotify_id=prof_resp.get("id"),
            email=prof_resp.get("email"),
            display_name=prof_resp.get("display_name")
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return "Success"
    except:
        return "Failed to login"
