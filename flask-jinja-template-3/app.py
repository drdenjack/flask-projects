from datetime import datetime

from flask import Flask, abort, jsonify
from flask.templating import render_template

from model import db, load_db, save_db

app = Flask(__name__)

# see all defined routes with app.url_map

# basic route
@app.route("/")
def welcome():
    return render_template("welcome.html")



@app.route("/datetime")
def get_datetime():
    return f"The time is now: {datetime.now()}"

@app.route("/world")
def world():
    my_jinja_message = "Look Ma, I'm a template!"
    return render_template("world.html", my_jinja_message=my_jinja_message)

@app.route("/users")
def user_list_route():
    return render_template("user_list.html", user_list=db)


@app.route("/user/<int:idx>")
def user_route(idx):
    try:
        user = db[idx]
        return render_template(
            "user.html", user=user, idx=idx, max_idx=len(db)-1)
    except IndexError:
         abort(404)

@app.route("/api/user/<int:idx>")
def api_user_detail(idx):
    try:
        return db[idx]
    except IndexError:
        abort(404)

@app.route("/api/user/")
def api_user_list():
    # lists need to be jsonified
    # returning lists directly is bad.
    # Lists can get too big, and other security reasons.
    return jsonify(db)