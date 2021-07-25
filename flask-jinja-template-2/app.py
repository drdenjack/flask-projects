from datetime import datetime

from flask import Flask
from flask.templating import render_template

from model import db, load_db, save_db

app = Flask(__name__)

# see all defined routes with app.url_map

# basic route
@app.route("/")
def welcome():
    return "welcome to this page!"


@app.route("/datetime")
def get_datetime():
    return f"The time is now: {datetime.now()}"

@app.route("/world")
def world():
    my_jinja_message = "Look Ma, I'm a template!"
    return render_template("welcome.html", my_jinja_message=my_jinja_message)

@app.route("/users")
def user_list_route():
    return render_template("user_list.html", user_list=db)


@app.route("/user")
def user_route():
    return render_template("user.html", user=db[0])