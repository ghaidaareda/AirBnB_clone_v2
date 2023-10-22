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


@my_app.route("/c/<text>", strict_slashes=False)
def variable(text):
    """text_page"""
    return "C {}".format(text.replace('_', ' '))



@my_app.route("/python/<text>", strict_slashes=False , defaults={'text': 'is cool'})
def py_variable(text):
    """text_page"""
    return "Python {}".format(text.replace('_', ' '))


@my_app.route("/number/<int:n>", strict_slashes=False)
def n_variable(n):
    """number_page"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    my_app.run(host='0.0.0.0', port=5000, debug=True)
