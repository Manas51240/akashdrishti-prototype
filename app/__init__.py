# app/__init__.py

from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # ✅ Load from config.py

    from .routes.main import main
    app.register_blueprint(main)

    return app
