#!/usr/bin/python3
""" writing a simple flask app
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value
        of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY

"""
from flask import Flask, render_template
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
    hbnb route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    """
    c what the route
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hows_python(text='is cool'):
    """Tell us about Python
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """accept the integer and show it
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def page_dependent(n):
    """show page if only n is integer
    """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """only display when n is integer
    and some other restrictions
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
