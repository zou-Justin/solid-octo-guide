# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# Runs the same as v2, but Debug mode: on instead of Debug mode: off
# Not sure what Debug mode does?

# DISCOVERIES
# Debug mode: on as expected
# Terminal also prints out
# Debugger is active!
# Debugger PIN: 144-797-667

# Everything else works as intended.
