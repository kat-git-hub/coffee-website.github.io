import os
import json


def load_json(file_name):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', file_name)
    with open(json_path, 'r') as f:
        return json.load(f)
