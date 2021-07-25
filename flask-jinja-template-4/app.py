from datetime import datetime

from flask import Flask, abort, jsonify, request, redirect, url_for
from flask.templating import render_template
from werkzeug.utils import redirect

from model import db, load_db, save_db

app = Flask(__name__)

# see all defined routes with app.url_map

# basic route
@app.route("/")
def welcome():
    return render_template("welcome.html")


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

@app.route("/api/add_user/", methods=["GET", "POST"])
def add_user_view():
    if request.method == "POST":
        new_user = {
            "name": request.form["name"],
            "email": request.form["email"],
        }
        db.append(new_user)
        save_db()
        return redirect(url_for("user_route", idx=len(db)-1))
    else:
        return render_template("add_user.html")

@app.route("/api/remove_user/<int:idx>", methods=["GET", "POST"])
def remove_user_view(idx):
    try:
        if request.method == "POST":
            if idx < len(db):
                db.pop(idx)
                save_db()
            return redirect(url_for("user_list_route", user_list=db))
        else:
            user = db[idx]
            return render_template("remove_user.html", user=user)
    except IndexError:
        abort(404)
