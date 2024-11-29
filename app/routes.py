from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm, RegistrationForm
from app.models import load_json
from app import app
from app.models import User
from app import db


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))
        else:
            flash('User already exists!')
    return render_template('create_user.html', title='Register', form=form)
