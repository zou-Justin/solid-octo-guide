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

app.run()

# Returns website saying "No hablo queso!". \
# Then prints "about to print __name__..." on the next line
# and prints __main__ on the line after that

# DISCOVERIES
# After testing our hypothesis, we discovered that it would only print
# after clicking the link provided by the terminal.
# Print output was the same as expected.
