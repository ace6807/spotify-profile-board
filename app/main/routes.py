from app.main import blueprint
from flask import render_template
from flask_login import current_user, login_required
from app.clients import spotify_client

@blueprint.route('/')
def index():
    return render_template("main/index.html")


@blueprint.route('/test')
def test():
    return "You are at test"

@blueprint.route('/top-tracks')
@login_required
def top_tracks():
    resp = spotify_client.get_top_tracks(current_user.access_token).json()
    tracks = [
        {
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "album": item["album"]["name"]
        }
        for item
        in resp["items"]
    ]

    return render_template("main/top_tracks.html", tracks=tracks)