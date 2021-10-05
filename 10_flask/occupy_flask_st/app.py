from flask import Flask

import random
import csv

app = Flask(__name__)

@app.route("/") 

def main(): 
    return heading() + "\n" + listoccupations()

def heading():
    return "<h3> Mark Zhu, Justin Zou, Han Zhang </h3>"

def listoccupations(): 
    dict = {}
    with open("occupations.csv", mode = 'r') as csvfile:
        file = csv.DictReader(csvfile)

        for lines in file:
            dict[lines['Job Class']] = float(lines['Percentage'])
    
    dict.pop('Total')

    return "<br/><br/><b>List of occupations: </b> <br/>" + "<br />".join(dict.keys())

app.run() 
                