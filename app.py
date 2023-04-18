from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "hello friends"


@app.route("/welcome")
def home():
    return "welcome home"

from controller import *