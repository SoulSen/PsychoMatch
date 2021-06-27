from flask import request, render_template, redirect, url_for

from . import patient_
from .. import App
from ..utils.actors import Patient


@patient_.route('/patient', methods=["GET"])
def patient_survey_get():
    return render_template('patient.html')


@patient_.route('/patient', methods=['POST'])
def patient_survey_post():
    form_ = request.form
    patient = Patient(form_)

    App.match_patient(patient)


    return redirect(url_for('thank_you.thank_you'))
