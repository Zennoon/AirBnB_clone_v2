#!/usr/bin/python3
"""

Contains:
    Misc
    ====
    Script to initialize a flask application with 6 routes defined, listening
    on 0.0.0.0:5000

    Functions
    =========
    home - Route function for the '/' url

    hbnb - Route function for the '/hbnb' url

    c_path - Route function for '/c/<text>' url

    python_path - Route function for '/python/<text>' url

    number_path - Route function for '/number/<num>' url

    number_template - Route function for the '/number_template/<num>' url
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """Route function for the '/' url"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """Route function for the '/hbnb' url"""
    return ("HBNB")


@app.route('/c/<text>')
def c_path(text):
    """
    Route function for urls matching '/c/<text>'

    Args:
        text (str): path following '/c/' in the URL fed to the function

    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def python_path(text="is cool"):
    """
    Route function for urls matching '/python/<text>'

    Args:
        text (str): path following '/python/' in the url,
                    default value='is cool'
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:num>')
def number_path(num):
    """
    Route function for urls matching '/number/<num>' where num is a positive
    integer

    Args:
        num (int): path following '/number/', converted to an int if possible
    """
    return ("{} is a number".format(num))


@app.route('/number_template/<int:num>')
def number_template(num):
    """
    Route function for urls matching '/number_template/<num>' where num is a
    positive integer

    Args:
        num (int): path following '/number_template/', converted to an int
    """
    return (render_template("5-number.html", num=num))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
