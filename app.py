from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/thao")
def thao():
    return "Hello, Thao!"

@app.route("/tyler")
def tyler():
    return "Hello, TJ!"

@app.route("/maddy")
def maddy():
    return "Hello, Maddy!"
