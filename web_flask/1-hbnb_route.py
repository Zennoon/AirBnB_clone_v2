#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask application with two routes defined, listening
    on 0.0.0.0:5000

    Functions
    =========
    home - Route function for the '/' url

    hbnb - Route function for the '/hbnb' url
"""
from flask import Flask


app = Flask("__name__")
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """Route function for the '/' url"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """Route function for the '/hbnb' url"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
