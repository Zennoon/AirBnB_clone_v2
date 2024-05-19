#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask web app with a single route to display
    the States in the database

    Functions
    =========
    states_list - Route function for '/states_list' url
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def renew_session(exc):
    storage.close()


@app.route('/states_list')
def states_list():
    all_states = storage.all(State).values()
    return (render_template("7-states_list.html", all_states=all_states))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
