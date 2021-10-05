from flask import Flask
app = Flask(__name__)

@app.route("/") 

def heading():
    return "<h3> Mark Zhu, Justin Zou, Han Zhang </h3>"

app.run() 
                