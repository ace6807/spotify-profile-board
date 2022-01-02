from urllib.parse import urlsplit, urlunsplit, urlparse
from app.auth import blueprint
from flask import render_template, request, current_app, url_for

def build_route(root_url:str, controller:str):
    scheme, netloc, _, _, _ = urlsplit(root_url)
    redirect_path = url_for(controller)
    return urlunsplit((scheme,netloc,redirect_path,"",""))

@blueprint.route('/login')
def login():
    # TODO: Pass request state
    context = {
        "client_id": current_app.config.get("SPOTIFY_CLIENT_ID"),
        "response_type": "code",
        "redirect_uri": build_route(request.root_url, 'auth.redirect_from_authorization'),
        "scope": "user-read-email playlist-read-private user-top-read",
    }
    return render_template("auth/login.html", **context)

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

    print(request)

    from app.clients import spotify_client
    ret = spotify_client.get_access_token(
        current_app.config.get("SPOTIFY_CLIENT_ID"),
        current_app.config.get("SPOTIFY_CLIENT_SECRET"),
        request.args.get("code"),
        build_route(request.root_url, 'auth.redirect_from_authorization')
    )
    return "Success"

