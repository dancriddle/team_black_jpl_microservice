__author__ = 'paultrelease'

from flask import Flask, render_template, request, json
import requests
import os
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkfortitle')
def check_for_title():
    #here, we'll make the call to url = 'http://0.0.0.0:5010/titlefromreference' etc'
    return render_template("a_new_is_this_your)_title_template.html")
    #the above template will call the removerestriction route below.



@app.route('/removerestriction', methods=['POST'])
def remove_restriction():
    referencenumber = request.form.get('referencenumber')
    # Need to find a way to change this to the cloud 9 url when appropriate.
    # Probably set up an environment.sh, that just gets picked up locally.
    url = '%s/titlefromreference' % app.config['CASEWORK_STUB']
    #http://0.0.0.0:5010
    data = {"reference": referencenumber}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    titlenumber = r.text
    app.logger.debug(r.text)
    return render_template("restriction_removed.html", referencenumber=referencenumber, titlenumber=titlenumber)
    #and here call the casework servivce to remove te restriction flag.


if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5009)))
