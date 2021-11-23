# Justin Zou, Hebe Huang
# SoftDev
# K19: A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html",pic = "https://apod.nasa.gov/ap…ctiveSun_NuSTAR_1600.jpg")


if __name__ == "__main__":
    app.debug = True
    app.run()
