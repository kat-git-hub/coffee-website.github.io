import os
import json
from app import db
from sqlalchemy.orm import Mapped, mapped_column


def load_json(file_name):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', file_name)
    with open(json_path, 'r') as f:
        return json.load(f)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    image_file: Mapped[str] = mapped_column(default='default.jpg')
    password: Mapped[str]

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
