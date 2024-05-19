#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask web app with 1 route to display
    the filters of the application

    Functions
    =========
    hbnb_filters - Route function for the '/hbnb_filter' url
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask("__name__", template_folder="./web_flask/templates")
app.url_map.strict_slashes = False


@app.teardown_appcontext
def renew_session(exc):
    storage.close()


@app.route('/hbnb_filters')
def state_by_id(id="all"):
    all_amenities = storage.all(Amenity).values()
    all_states = storage.all(State).values()    
    return (render_template("10-hbnb_filters.html", amenities=all_amenities,
                            all_states=all_states))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
