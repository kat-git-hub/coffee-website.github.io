from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def load_json(file_name):
    json_path = os.path.join(app.root_path, 'data', 'products.json')
    with open(json_path, 'r') as f:
        return json.load(f)


@app.route('/')
def index():
    return render_template('index.html', title="Coffee Cafe")


@app.route('/coffee')
def coffee():
    products = load_json('products.json')
    return render_template('coffee.html', products=products, title="Coffee")


@app.route('/subscribe')
def subscribe():
    return render_template('subscription.html', title="Subscribe")


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title="About Us")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
