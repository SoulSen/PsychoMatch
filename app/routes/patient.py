#  Copyright (c) 2021 SoulSen.
#  All rights reserved.

from flask import request, render_template, redirect, url_for

from . import Blueprints
from .. import App
from ..utils.actors import Patient

patient = Blueprints.PATIENT


@patient.route('/patient', methods=["GET"])
def patient_survey_get():
    return render_template('patient.html')


@patient.route('/patient', methods=['POST'])
def patient_survey_post():
    form_ = request.form
    patient = Patient(form_)

    App.match_patient(patient)

    return redirect(url_for('thank_you.thank_you'))
