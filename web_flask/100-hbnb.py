#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask web app with 1 route to display
    the places of the application

    Functions
    =========
    hbnb - Route function for the '/hbnb' url
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def renew_session(exc):
    storage.close()


@app.route('/hbnb')
def hbnb(id="all"):
    all_amenities = storage.all(Amenity).values()
    all_states = storage.all(State).values()
    all_places = storage.all(Place).values()    
    return (render_template("100-hbnb.html", amenities=all_amenities,
                            all_states=all_states, 
                            all_places=all_places))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
