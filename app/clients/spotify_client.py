import requests
import base64

api_url = "https://accounts.spotify.com"

def get_access_token(client_id: str, client_secret:str, code: str, redirect_uri:str):
    post_url = f"{api_url}/api/token"
    encoded_token = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    post_headers = {
        "Authorization": f"Basic {encoded_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    post_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }
    return requests.post(post_url, post_data, headers=post_headers)