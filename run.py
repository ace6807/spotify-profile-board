from app import create_app
from config import Config

app_config = Config()
app = create_app(app_config)