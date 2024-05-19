#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask application with a single route, listening
    on 0.0.0.0:5000

    Functions
    =========
    home - Route function for the '/' url
"""
from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def home():
    """Route function for the '/' url"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
