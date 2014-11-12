__author__ = 'paultrelease'

from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/removerestriction', methods=['POST'])
def remove_restriction():
    referencenumber = request.form.get('referencenumber')
    #When this is done properly, a call to another microservice will take place
    #and if the case is successful then the page below will be rendered.
    return render_template("restriction_removed.html", referencenumber=referencenumber)



if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5010)))
