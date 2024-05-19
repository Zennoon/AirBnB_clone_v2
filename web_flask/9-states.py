#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask web app with 1 route to display
    a state with an optional given ID

    Functions
    =========
    state_by_id - Route function for urls matching '/states/'
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def renew_session(exc):
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def state_by_id(id="all"):
    all_states = storage.all(State).values()
    return (render_template("9-states.html", all_states=all_states,
                            id=id))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
