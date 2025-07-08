# config.py

import os

class Config:
    # App security
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-default-secret")

    # Email configuration (for email_alert.py)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "your-email@gmail.com")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "your-app-password")
