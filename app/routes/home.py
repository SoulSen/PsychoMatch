from flask import render_template

from . import home_


@home_.route('/')
def index():
    return render_template('home.html')
