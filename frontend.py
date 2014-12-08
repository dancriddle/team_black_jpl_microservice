__author__ = 'paultrelease'

from flask import Flask, render_template, request, json
import requests
import os
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkfortitle', methods=['POST'])
def check_for_title():
    url = '%s/titlefromreference' % app.config['CASEWORK_STUB']
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
    
    



@app.route('/removerestriction', methods=['POST'])
def remove_restriction():
    print "Remove restriction"
    
    referencenumber = request.form.get('referencenumber')
    titlenumber = request.form.get('titlenumber')
    url = '%s/complete' % app.config['CASEWORK_STUB']
    referencenumber = request.form.get('referencenumber')
    data = {"reference": referencenumber}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    
    if r.text != "True":
        return render_template("restriction_not_removed.html", referencenumber=referencenumber, titlenumber=titlenumber)
    else:
        return render_template("restriction_removed.html", referencenumber=referencenumber, titlenumber=titlenumber)
    
    

if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5009)))
