# Selective Soup | Justin Zou (Piggy), Wen Hao Dong (Jal Hordan), Roshani Shrestha (Pete)
# SoftDev 
# K14: Form and Function - Displays login and authenticate pages 
# 2021-10-15 

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage(): # function to display the initial login page
    print("\n\n\n")
    print("***DIAG: this Flask obj ***") 
    print(app)
    print("***DIAG: request obj ***") 
    print(request) # prints "<Request 'http://127.0.0.1:5000/' [GET]>" which is the information about the form request (request method used)
    print("***DIAG: request.args ***") 
    print(request.args) # prints a dictionary with the inputs of the user, which is empty right now
    # print("***DIAG: request.args['username']  ***") 
    # print(request.args['username']) # this creates a KeyError because request.args is empty
    print("***DIAG: request.headers ***")  
    print(request.headers) 
    return render_template( 'login.html' ) # serves template from localhost


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate(): # function that runs after the user submits their inputs 
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) 
    print("***DIAG: request obj ***") 
    print(request) # almost the same as previous function, but it also has "auth?" followed by the values of 'username' and 'sub1' (which is just 'Submit')
    print("***DIAG: request.args ***")
    print(request.args) # same as previous function except this time here are entries for the values of 'username' and 'sub1' (which is just 'Submit')
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username']) # this prints out the username provided by the user
    print("***DIAG: request.headers ***")
    print(request.headers) 
    return render_template('response.html', username=request.args['username'], method=request.method) #what is shown on our response page, using response.html as our template
   


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
