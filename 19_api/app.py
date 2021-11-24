# Justin Zou, Hebe Huang
# SoftDev
# K19: A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)


@app.route("/")
def home():
    url = "https://api.nasa.gov/planetary/apod?api_key=7FDdoAzbN5DoWCsTmAqZz3NIeHSGgaDd6nxUTvWJ"
    http = urllib3.PoolManager()
    r = http.request('GET', 'url')
    w = json.loads(r.data)
    pic = w.get("url")
    return render_template("main.html",pic = pic)


if __name__ == "__main__":
    app.debug = True
    app.run()
