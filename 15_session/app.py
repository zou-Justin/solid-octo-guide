# Selective Soup | Justin Zou (Piggy), Wen Hao Dong (Jal Hordan), Roshani Shrestha (Pete)
# SoftDev 
# K15: Sessions Greetings - Uses session capabilities to allow a user to login and logout 
# 2021-10-18

from sys import argv
from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET']) #, methods=['GET', 'POST'])
def disp_loginpage(): # displays the initial login page or welcome page if the user is logged in
    """
    Sessions are used to see if the user is logged in. 
    If so, it displays the welcome page at the root, which is created by rendering response.html. 
    If not, it displays the login page at the root, which is created by rendering login.html.
    The username and password are checked to see if they are correct, which are compared to a hardcoded single username/password combination.
    Messages are displayed if login fails.
    """
    if (request.method == 'POST'): # checks if the request method is POST
        try:
            if (request.form['username'] == 'Selective Soup' and request.form['password'] == 'hello'): # checks if the username and password are both correct
                session['user'] = request.form['username'] # adds session data
            else: # the case that the username and password are not both correct
                # print("***DIAG: request.form ***") 
                # print(request.form)
                # print("***DIAG: request.form['username'] ***") 
                # print(request.form['username'])
                # print("***DIAG: request.form['password'] ***") 
                # print(request.form['password'])
                if (request.form['username'] != 'Selective Soup' and request.form['password'] != 'hello'): # checks if both are incorrect 
                    return render_template( 'login.html', logged = "Wrong username and password")
                elif (request.form['username'] != 'Selective Soup'): # checks if only username is incorrect
                    return render_template( 'login.html', logged = "Wrong username")
                else: # the last case is that only the password is incorrect
                    return render_template( 'login.html', logged = "Wrong password")
        except AttributeError:
            print('request.form does not exist')

    if "user" in session: # checks if the user is logged in
        # print("***DIAG: session['user'] ***") 
        # print(session['user'])
        return render_template('response.html', username = session['user'])
    else:
        return render_template( 'login.html', logged = "")

@app.route("/logout", methods = ['POST', 'GET'])
def logoutPg(): # returns to the login page after the user presses the Logout button
    """
    Redirects to the login page after the user presses the Logout button, allowing the user to log back in.
    Removes the session.  
    """
    session.pop('user') # removes the session
    return redirect('http://localhost:5000/') # redirects the page back to the login page, which is at the root




if __name__ == "__main__":
    app.debug = True
    app.secret_key = os.urandom(32) # generates a secret key
    app.run()
