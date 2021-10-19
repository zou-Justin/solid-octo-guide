# Selective Soup | Justin Zou (Piggy), Wen Hao Dong (Jal Hordan), Roshani Shrestha (Pete)
# SoftDev
# K14: Form and Function - Displays login and authenticate pages
# 2021-10-15

from sys import argv
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET']) #, methods=['GET', 'POST'])
def disp_loginpage():
    if (request.method == 'POST'):
        if (request.form['username'] == 'Selective Soup' and request.form.get('Password')== 'hello'):
            session['user'] = request.form['username']
        else:
            if (request.form['username'] != 'Selective Soup'):
                return render_template( 'login.html', logged = "Wrong username")
            elif (request.form.get('Password') != 'hello'):
                return render_template( 'login.html', logged = "Wrong password")
            else:
                return render_template( 'login.html', logged = "Wrong username and password")
    if "user" in session:
        return render_template('response.html', username = session['user'])
    else:
        return render_template( 'login.html', logged = "")

@app.route("/logout", methods = ['POST', 'GET'])
def logoutPg():
    session.pop('user')
    return redirect('http://localhost:5000/')


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "foo"
    app.run()
