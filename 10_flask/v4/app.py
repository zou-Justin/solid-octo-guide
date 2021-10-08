# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# If __name__ is not __main__ then there is no output.
# However, expected to have the same output as v3, because v3 would print
# __name__ as "__main__"


# DISCOVERIES
# Ran as expected
# Unsure about what will happen if __name__ is not "__main__"
# Why is __name__ = "__main__"?
