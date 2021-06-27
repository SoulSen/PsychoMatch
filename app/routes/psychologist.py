from flask import request, render_template, redirect, url_for

from . import psychologist_
from .. import App
from ..utils.actors import Psychologist


@psychologist_.route('/psychologist', methods=["GET"])
def psychologist_survey_get():
    return render_template('psychologist.html')


@psychologist_.route('/psychologist', methods=['POST'])
def psychologist_survey_post():
    form_ = request.form
    psychologist = Psychologist(form_)

    App.store_psychologist(psychologist)

    return redirect(url_for('thank_you'))
