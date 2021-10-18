# Selective Soup | Justin Zou (Piggy), Wen Hao Dong (Jal Hordan), Roshani Shrestha (Pete)
# SoftDev 
# K14: Form and Function - Displays login and authenticate pages 
# 2021-10-15 

from sys import argv
from flask import Flask, render_template, request

app = Flask(__name__)    


@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage(): 
    if (request.args['username'] == "Selective Soup" and request.args['Password'] == "hello"):
        return render_template( 'login.html' ) 


@app.route("/auth") 
def authenticate():  
    pass
    # return render_template() 
   


    
if __name__ == "__main__": 
    app.debug = True 
    app.run()