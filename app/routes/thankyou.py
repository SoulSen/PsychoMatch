from flask import render_template

from . import thank_you_


@thank_you_.route('/thankyou', methods=['GET', 'POST'])
def thank_you():
    return render_template('thankyou.html')
