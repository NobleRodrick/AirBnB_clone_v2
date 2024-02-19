#!/usr/bin/python3
"""
simple flask app
- will be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB"
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
    the second route, HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
