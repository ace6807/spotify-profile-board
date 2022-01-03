from app.db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """User model

    Fields:
        spotify_id (str): Spotify ID [max 100]
        email (str): Email [max 150]
        display_name (str): Display Name [max 50] (optional)
        first_name (str): First Name [max 50] (optional)
        last_name (str): Last Name [max 50] (optional)
    """
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    display_name = db.Column(db.String(100), unique=True, nullable=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    access_token = db.Column(db.String(100), nullable=True)
    refresh_token = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<User {self.spotify_id} - {self.email}>"