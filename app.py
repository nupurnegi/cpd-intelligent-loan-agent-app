#!/usr/bin/python3

# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, session, render_template, flash, send_from_directory
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY=os.environ.get('SECRET_KEY', 'development key')
))

strings = {
    "CHECKING STATUS": ["no_checking", "less_0", "0_to_200", "greater_200"],
    "CREDIT HISTORY": ["outstanding_credit", "prior_payments_delayed", "credits_paid_to_date", "all_credits_paid_back", "no_credits"],
    "EMPLOYMENT DURATION": ["unemployed", "less_1", "1_to_4", "4_to_7", "greater_7"],
    "EXISTING SAVINGS": ["unknown", "less_100", "100_to_500", "500_to_1000", "greater_1000"],
    "FOREIGN WORKER": ["yes", "no"],
    "HOUSING": ["own", "free", "rent"],
    "INSTALLMENT PLANS": ["none", "stores", "bank"],
    "JOB": ["skilled", "management_self-employed", "unemployed", "unskilled"],
    "OWNS PROPERTY": ["car_other", "savings_insurance", "unknown", "real_estate"],
    "SEX": ["female", "male"],
    "TELEPHONE": ["yes", "none"],
    "LOAN PURPOSE": ["repairs", "appliances", "car_new", "furniture", "car_used", "business", "radio_tv", "education", "vacation", "other", "retraining"],
    "OTHERS ON LOAN": ["none", "co-applicant", "guarantor"]
}
stringstag = {
    "CHECKING STATUS": ["no checking", "< 0", "0 to 200", "> 200"],
    "CREDIT HISTORY": ["outstanding credit", "prior payments delayed", "credits paid to date", "all credits paid back", "no credits"],
    "EMPLOYMENT DURATION": ["unemployed", "< 1", "1 to 4", "4 to 7", "> 7"],
    "EXISTING SAVINGS": ["unknown", "< 100", "100 to 500", "500 to 1000", "> 1000"],
    "FOREIGN WORKER": ["yes", "no"],
    "HOUSING": ["own", "free", "rent"],
    "INSTALLMENT PLANS": ["none", "stores", "bank"],
    "JOB": ["skilled", "management self-employed", "unemployed", "unskilled"],
    "OWNS PROPERTY": ["car", "savings insurance", "unknown", "real estate"],
    "SEX": ["female", "male"],
    "TELEPHONE": ["yes", "none"],
    "LOAN PURPOSE": ["repairs", "appliances", "car new", "furniture", "car used", "business", "radio tv", "education", "vacation", "other", "retraining"],
    "OTHERS ON LOAN": ["none", "co-applicant", "guarantor"]
} 
# min, max, default value
floats = {
    "INSTALLMENT PERCENT": [1, 10, 3],
    "LOAN AMOUNT": [200, 750000, 3500]
}

# min, max, default value
ints = {
    "AGE": [18, 80, 35],
    "DEPENDENTS": [0, 10, 1],
    "CURRENT RESIDENCE DURATION": [1, 10, 3],
    "EXISTING CREDITS COUNT": [1, 7, 1],
    "LOAN DURATION": [1, 72, 24]
}

labels = ["No Risk", "Risk"]


def generate_input_lines():
        
    result = f'<table align="center">'

    counter = 0
    for k in floats.keys():
        minn, maxx, vall = floats[k]
        if (counter % 2 == 0):
            result += f'<tr>'
        result += f'<td>{k}'
        result += f'<input type="number" class="form-control" min="{minn}" max="{maxx}" step="1" name="{k}" id="{k}" value="{vall}" required (this.value)">'
        result += f'</td>'
        if (counter % 2 == 1):
            result += f'</tr>'
        counter = counter + 1

    counter = 0
    for k in ints.keys():
        minn, maxx, vall = ints[k]
        if (counter % 2 == 0):
            result += f'<tr>'
        result += f'<td>{k}'
        result += f'<input type="number" class="form-control" min="{minn}" max="{maxx}" step="1" name="{k}" id="{k}" value="{vall}" required (this.value)">'
        result += f'</td>'
        if (counter % 2 == 1):
            result += f'</tr>'
        counter = counter + 1

    counter = 0
    for k in stringstag.keys():
        if (counter % 2 == 0):
            result += f'<tr>'
        result += f'<td>{k}'
        result += f'<select class="form-control" name="{k}">'
        for value, j in zip(strings[k], stringstag[k]):
            result += f'<option value="{value}" selected>{j}</option>'
        result += f'</select>'
        result += f'</td>'
        if (counter % 2 == 1):
            result += f'</tr>'
        counter = counter + 1

    result += f'</table>'

    return result


app.jinja_env.globals.update(generate_input_lines=generate_input_lines)


# def get_token():
#     auth_token = os.environ.get('AUTH_TOKEN')
#     auth_username = os.environ.get('AUTH_USERNAME')
#     auth_password = os.environ.get('AUTH_PASSWORD')
#     auth_url = os.environ.get('AUTH_URL')

#     if (auth_token):
#         # All three are set. bad bad!
#         if (auth_username and auth_password):
#             raise EnvironmentError('[ENV VARIABLES] please set either "AUTH_TOKEN" or ("AUTH_USERNAME", "AUTH_PASSWORD", and "AUTH_URL"). Not both.')
#         # Only TOKEN is set. good.
#         else:
#             return auth_token
#     else:
#         # Nothing is set. bad!
#         if not (auth_username and auth_password):
#             raise EnvironmentError('[ENV VARIABLES] please set "AUTH_USERNAME", "AUTH_PASSWORD", and "AUTH_URL" as "TOKEN" is not set.')
#         # Only USERNAME, PASSWORD are set. good.
#         else:
#             response_preauth = requests.get(auth_url, auth=HTTPBasicAuth(auth_username, auth_password), verify=False)
#             if response_preauth.status_code == 200:
#                 return json.loads(response_preauth.text)['accessToken']
#             else:
#                 raise Exception(f"Authentication returned {response_preauth}: {response_preauth.text}")


class riskForm():
    @app.route('/js/<path:path>')
    def send_js(path):     
        return send_from_directory('templates/js', path)

    @app.route('/img/<path:path>')
    def send_img(path):     
        return send_from_directory('templates/img', path)
    

    @app.route('/css/<path:path>')
    def send_css(path):     
        return send_from_directory('templates/css', path)

    @app.route('/fonts/<path:path>')
    def send_fonts(path): 
        return send_from_directory('templates/fonts', path)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        print(request)

        if request.method == 'POST':
            ID = 999

            session['ID'] = ID
            data = {}

            for k, v in request.form.items():
                data[k] = v
                session[k] = v

            scoring_href = os.environ.get('MODEL_URL')

            if not (scoring_href):
                raise EnvironmentError('[ENV VARIABLES] Please set "URL".')

            for field in ints.keys():
                data[field] = int(data[field])
            for field in floats.keys():
                data[field] = float(data[field])

            input_data = list(data.keys())
            input_values = list(data.values())

            payload_scoring = {"input_data": [
                {"fields": input_data, "values": [input_values]}
            ]}
        
            print("Payload is: ")
            print(payload_scoring)

            API_KEY=os.environ.get('API_Key')
            token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
            mltoken = token_response.json()["access_token"]

            header_online = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

            response_scoring = requests.post(
                scoring_href,
                json=payload_scoring,
                headers=header_online)
            result = response_scoring.json()

            print("Result is ", result)

            # result_json = json.loads(result)
            result_keys = result["predictions"][0]["fields"]
            result_vals = result["predictions"][0]["values"]

            result_dict = dict(zip(result_keys, result_vals[0]))

            loan_risk = result_dict["predictedLabel"].lower()
            no_percent = result_dict["probability"][0] * 100
            yes_percent = result_dict["probability"][1] * 100
            flash('Percentage of this loan representing risk is: %.0f%%'
                  % yes_percent)
            return render_template(
                'score.html',
                result=result_dict,
                loan_risk=loan_risk,
                yes_percent=yes_percent,
                no_percent=no_percent,
                response_scoring=response_scoring,
                labels=labels)

        else:
            return render_template('input.html')


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
port = os.environ.get('PORT', '5000')
host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
    app.run(host=host, port=int(port))
