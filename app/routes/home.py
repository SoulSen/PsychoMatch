#  Copyright (c) 2021 SoulSen.
#  All rights reserved.

from flask import render_template

from . import Blueprints

home = Blueprints.HOME


@home.route('/')
def index():
    return render_template('home.html')
