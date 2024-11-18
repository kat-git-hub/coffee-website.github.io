from flask import Flask, render_template
from dotenv import load_dotenv
from forms import LoginForm
from models import load_json
import os


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')


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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
