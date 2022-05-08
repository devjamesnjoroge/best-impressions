from flask_login import login_required
from . import main
from flask import render_template

@main.route('/')
def home():

    return render_template('index.html')

@main.route('/categories')
@login_required
def categories():

    return render_template('categories.html')
