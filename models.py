import os
import json


def load_json(file_name):
    json_path = os.path.join('data', 'products.json')
    with open(json_path, 'r') as f:
        return json.load(f)
