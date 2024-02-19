#!/usr/bin/python3
"""a simple flask app
must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of
        the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet_hbnb():
    """
    the root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show_hbnb():
    """
    hbnb route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    """
    c what route
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hows_python(text='is cool'):
    """
    Tell us that Python is cool
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
