#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask web app with a single route to display
    the States in the database, along with their cities

    Functions
    =========
    cities_by_states - Route function for '/states_list' url
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask("__name__", template_folder="./web_flask/templates")
app.url_map.strict_slashes = False


@app.teardown_appcontext
def renew_session(exc):
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    all_states = storage.all(State).values()
    return (render_template("8-cities_by_states.html", all_states=all_states))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
