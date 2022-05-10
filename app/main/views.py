from flask_login import login_required
from . import main
from flask import render_template
from ..models import User

@main.route('/')
def home():

    return render_template('index.html')

@main.route('/categories')
@login_required
def categories():

    return render_template('categories.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
