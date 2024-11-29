import os
from dotenv import load_dotenv


class Config:
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
