#  Copyright (c) 2021 SoulSen.
#  All rights reserved.

import collections
import smtplib
import sqlite3
from configparser import ConfigParser
from email.mime.text import MIMEText

from flask import Flask

from .utils.predicates import age_predicate, compare_predicate, checkbox_predicate

_config = ConfigParser()
_config.read("config.ini")

EMAIL = _config['EMAIL_CREDS']['EMAIL']
PASSWORD = _config['EMAIL_CREDS']['PASSWORD']

MATCH_COLUMNS = {"age": age_predicate, "gender": checkbox_predicate, "race": checkbox_predicate,
                 "communication": compare_predicate, "doctor_personality": checkbox_predicate,
                 "meeting": compare_predicate,
                 "place_to_meet": compare_predicate, "meds": compare_predicate}


class App:
    def __init__(self):
        self.app = Flask(__name__)

        self._setup_database()

        from .routes import Blueprints

        attrs = [attr for attr in dir(Blueprints) if
                 not attr.startswith('__') and not callable(getattr(Blueprints, attr))]

        for blueprint in attrs:
            self.app.register_blueprint(getattr(Blueprints, blueprint))

        self.app.run(host='0.0.0.0', port=8080)

    @staticmethod
    def store_psychologist(psychologist_):
        with sqlite3.connect('./app/database/database.sqlite') as conn:
            cur = conn.cursor()
            cursor = cur.execute('SELECT * FROM PsychoInfo')

            column_names = list(map(lambda x: x[0], cursor.description))

            values = [getattr(psychologist_, column) for column in column_names]

            cur.execute('''INSERT INTO PsychoInfo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', values)

    @staticmethod
    def match_patient(patient_):
        scores = collections.defaultdict(int)
        print("hello")

        with sqlite3.connect('./app/database/database.sqlite') as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute('SELECT * FROM PsychoInfo')

            for row in rows.fetchall():
                row = dict(row)

                psycho_name = row["name"]

                for column, pred in MATCH_COLUMNS.items():
                    if pred(patient_, row, column):
                        scores[psycho_name] += 1

                scores[psycho_name] += 0

        sorted_scores = sorted(scores, key=scores.get, reverse=True)

        with sqlite3.connect('./app/database/database.sqlite') as conn:
            conn.row_factory = sqlite3.Row

            rows = conn.execute('SELECT * FROM PsychoInfo WHERE name=?', (sorted_scores[0],))

            row = rows.fetchall()[0]

        App._send_email(patient_.email, dict(row))

    @staticmethod
    def _setup_database():
        with sqlite3.connect('./app/database/database.sqlite') as conn:
            cur = conn.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS PsychoInfo (name text, email text, phone_number text, hospital 
            text, age number, gender text, race text, communication text, doctor_personality text, meeting text, 
            place_to_meet text, meds text, user_message text)''')

    @staticmethod
    def _send_email(receiver, matched_psychologist):
        name = matched_psychologist["name"]
        email = matched_psychologist["email"]
        phone_number = matched_psychologist["phone_number"]
        hospital = matched_psychologist["hospital"]

        body = f"Your perfect psychologist is: {name}\n\nTo contact them:\nEmail: {email}\nPhone Number: {phone_number}" \
               f"\nHospital: {hospital}"

        message = MIMEText(body)
        message['Subject'] = f"Matched Psychologists - {name}"
        message['From'] = EMAIL
        message['To'] = receiver

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, [receiver], message.as_string())
            server.quit()

        except Exception as e:
            print(e)
