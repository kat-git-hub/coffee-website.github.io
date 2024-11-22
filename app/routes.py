from flask import Blueprint, render_template, redirect, flash, url_for
#from dotenv import load_dotenv
from app.forms import LoginForm
from app.models import load_json
#import os


# load_dotenv()
# app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html', title="Coffee Cafe")


@bp.route('/coffee')
def coffee():
    products = load_json('products.json')
    return render_template('coffee.html', products=products, title="Coffee")


@bp.route('/subscribe')
def subscribe():
    return render_template('subscription.html', title="Subscribe")


@bp.route('/about_us')
def about_us():
    return render_template('about_us.html', title="About Us")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)
