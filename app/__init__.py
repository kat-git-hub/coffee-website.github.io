import os
from flask import Flask
from dotenv import load_dotenv
from app import routes


def create_app():
    load_dotenv()
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

    with app.app_context():
        #from app import routes
        app.register_blueprint(routes.bp)

    return app