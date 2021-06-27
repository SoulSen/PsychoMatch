from flask import Blueprint

home_ = Blueprint('home', __name__)
patient_ = Blueprint('patient', __name__)
psychologist_ = Blueprint('psychologist', __name__)
thank_you_ = Blueprint('thank_you', __name__)

from . import home, patient, psychologist
