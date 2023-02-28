from flask import Blueprint, render_template
from models import User, Drink

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@site.route('/profile')
def profile():
    user = User.query.all()
    return render_template('profile.html', user=user)

@site.route('/drinks')
def drinks():
    drinks = Drink.query.all()
    return render_template('drinks.html', drinks=drinks)