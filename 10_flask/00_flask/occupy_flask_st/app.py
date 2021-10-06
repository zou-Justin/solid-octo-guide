# Team MJH: Mark Zhu(Bob the 3rd Jr), Justin Zou(Piggy), Han Zhang(Sirap)
# SoftDev
# K10: Putting Little Pieces Together
# 2021-10-4

from flask import Flask
import random
import csv


app = Flask(__name__)  # create instance of class Flask

@app.route("/")  # assign fxn to route

def main(): 
    return heading() + "\n" + occupations()

def heading():
    return "<h3> Mark Zhu, Justin Zou, Han Zhang </h3>"

def occupations():
    return randomoccupation() + listoccupations()

def listoccupations(): 
    dict = {}
    with open("occupations.csv", mode = 'r') as csvfile:
        file = csv.DictReader(csvfile)

        for lines in file:
            dict[lines['Job Class']] = float(lines['Percentage'])
    
    dict.pop('Total')

    return "<br/><br/><b>List of occupations: </b> <br/>" + "<br />".join(dict.keys())

def randomoccupation():
    randomNum = random.random()* 99.8
    dict = {}
        
    with open("occupations.csv", mode = 'r') as csvfile:
        file = csv.DictReader(csvfile)

        for lines in file:
            dict[lines['Job Class']] = float(lines['Percentage'])

    x = 0.0
    for i, j in dict.items():
        if x <= randomNum < x + j:
            return ("<b>Your occupation is: " + i + "</b>")
            break
        x += j
    
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()     
