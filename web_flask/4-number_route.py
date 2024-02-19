#!/usr/bin/python3
"""simple flask app
must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of
        the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet_hbnb():
    """
    the first route, the root
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show_hbnb():
    """
    our second defined route,
    hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    """
    the route about c what
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hows_python(text='is cool'):
    """
    Tell us that python is something🥰
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    taking in a number
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
