#!/usr/bin/python3
"""
script that starts a Flask web application with added route
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """states_page"""
    states = storage.all('State').values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", sorted_states=sorted_states)

@app.teardown_appcontext
def close_storage():
    """remove the current SQLAlchemy Session"""
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)