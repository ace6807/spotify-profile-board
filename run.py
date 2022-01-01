from app.db import db
from app import create_app
from config import Config
from app import models

app_config = Config()
app = create_app(app_config)

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": models.User
    }