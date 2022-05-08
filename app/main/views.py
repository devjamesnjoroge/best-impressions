from . import main
from flask import render_template, make_response

@main.route('/')
def home():

    resp = make_response(render_template('index.html'))

    resp.set_cookie('',expires=0)

    

    return resp

@main.route('/categories')
def categories():

    return render_template('categories.html')




