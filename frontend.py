__author__ = 'paultrelease'

from flask import Flask, render_template, request, json
import requests
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkfortitle', methods=['POST'])
def check_for_title():
    #here, we'll make the call to url = 'http://0.0.0.0:5010/titlefromreference' etc'
    url = 'https://team-black-casework-2-srallis1-2.c9.io/titlefromreference'
    referencenumber = request.form.get('referencenumber')
    data = {"reference": referencenumber}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    titlenumber = r.text
    
    app.logger.debug(r.text)
    
    if titlenumber == "Referance not valid":
        return render_template("reference_invalid.html", referencenumber=referencenumber)
    else:
        return render_template("reference_valid.html", referencenumber=referencenumber, titlenumber=titlenumber)
    
    #the above template will call the removerestriction route below.



@app.route('/removerestriction', methods=['POST'])
def remove_restriction():
    referencenumber = request.form.get('referencenumber')
    titlenumber = request.form.get('titlenumber')
    # Need to find a way to change this to the cloud 9 url when appropriate.
    # Probably set up an environment.sh, that just gets picked up locally.
    #url = 'https://team-black-casework-2-srallis1-2.c9.io/titlefromreference'
    #data = {"reference": referencenumber}
    #headers = {'Content-Type': 'application/json'}
    #r = requests.post(url, data=json.dumps(data), headers=headers)
    #titlenumber = r.text
    
    #app.logger.debug(r.text)
    
    #if titlenumber == "Referance not valid":
        #return render_template("reference_invalid.html", referencenumber=referencenumber)
    #else:
    return render_template("restriction_removed.html", referencenumber=referencenumber, titlenumber=titlenumber)
    
    #return render_template("restriction_removed.html", referencenumber=referencenumber, titlenumber=titlenumber)
    #and here call the casework servivce to remove te restriction flag.
    

if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5009)))
