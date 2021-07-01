#  Copyright (c) 2021 SoulSen.
#  All rights reserved.

from flask import render_template

from . import Blueprints

thank_you = Blueprints.THANK_YOU


@thank_you.route('/thankyou', methods=['GET', 'POST'])
def thank_you():
    return render_template('thankyou.html')
