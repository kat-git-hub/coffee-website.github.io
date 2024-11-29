from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from config import Config
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(Config)
db = SQLAlchemy(model_class=Base)
db.init_app(app)
engine = create_engine("sqlite://", echo=True)
from app import routes  # noqa: F401, E402
