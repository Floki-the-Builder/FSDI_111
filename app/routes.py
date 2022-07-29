from flask import Flask  # imported Flask class from flask module

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
