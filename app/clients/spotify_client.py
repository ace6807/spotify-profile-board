import requests
import base64

accounts_api_url = "https://accounts.spotify.com"
api_url = "https://api.spotify.com/v1"

def _get_access_token(client_id:str, client_secret:str, post_data:dict):
    post_url = f"{accounts_api_url}/api/token"
    encoded_token = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    post_headers = {
        "Authorization": f"Basic {encoded_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return requests.post(post_url, post_data, headers=post_headers)

def get_access_token(client_id: str, client_secret:str, auth_code: str, redirect_uri:str):
    post_data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri
    }
    # TODO: Raise exception on bad return
    return _get_access_token(client_id, client_secret, post_data)

def refresh_access_token(client_id: str, client_secret:str, refresh_token: str):
    post_data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    # TODO: Raise exception on bad return
    return _get_access_token(client_id, client_secret, post_data)

def _get_spotify_endpoint(endpoint_url: str, access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    return requests.get(endpoint_url, headers=headers)

def get_user_profile(access_token:str):
    endpoint_url = f"{api_url}/me"
    return _get_spotify_endpoint(endpoint_url, access_token)

def get_top_tracks(access_token:str):
    endpoint_url = f"{api_url}/me/top/tracks"
    return _get_spotify_endpoint(endpoint_url, access_token)