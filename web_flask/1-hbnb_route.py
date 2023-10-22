#!/usr/bin/python3
"""
script that starts a Flask web application with added route
"""
from flask import Flask

my_app = Flask(__name__)


@my_app.route("/", strict_slashes=False)
def homepage():
    """home_page"""
    return "Hello HBNB!"


@my_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb_page"""
    return "HBNB"


if __name__ == "__main__":
    my_app.run(host='0.0.0.0', port=5000, debug=True)
