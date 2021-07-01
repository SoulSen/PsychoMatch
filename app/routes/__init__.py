#  Copyright (c) 2021 SoulSen.
#  All rights reserved.

from flask import Blueprint

name = __name__


class Blueprints:
    HOME = Blueprint('home', name)
    PATIENT = Blueprint('patient', name)
    PSYCHOLOGIST = Blueprint('psychologist', name)
    THANK_YOU = Blueprint('thank_you', name)


from . import home, patient, psychologist, thankyou
