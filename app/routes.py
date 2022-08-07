from flask import (Flask, request)  # imported Flask class from flask module
from datetime import datetime
from app.database import user

version = "1.0.0"

app = Flask(__name__)  # app is an instance


@app.route("/")  # this is a route
def index():  # our view  function
    return "<h1>Hello world</h1>"  # return str


@app.route("/about")
def about():
    me = {
        "first_name": "Ardany",
        "last_name": "Mora",
        "age": 33,
        "home": "San Diego"
    }

    return me


@app.get("/users")
def get_all_users():
    user_list = user.scan()
    out = {
        "status": "ok",
        "users": user_list
    }
    return output


@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    user_obj = user.select_by_id(pk)
    out = {
        "status": "ok",
        "user": user_obj
    }
    return out


@app.post("/users")
def create_users():
    raw_data = request.json
    user.insert(raw_data)
    out = {
        "status": "ok",
        "message": "created"
    }
    return out, 201


@app.put("/users/<int:pk>")
def update_user(pk):
    raw_data = request.json(pk)
    user.update(pk, raw_data)
    return "", 204


@app.delete("/users/<int:pk>")
def deactivate_user(pk):
    user.deactivate(pk)
    return "", 204
