from app.db import db

class User(db.Model):
    """User model

    Fields:
        username (str): Username [max 50]
        email (str): Email [max 150]
        first_name (str): First Name [max 50] (optional)
        last_name (str): Last Name [max 50] (optional)
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username