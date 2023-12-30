#!/usr/bin/python3
"""
A script that starts a flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def txt(text):
    """return the content of a text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytxt(text='is cool'):
    """return the content of a text or 'is cool' if text is none"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def isnumber(n):
    """displays n is a number only if n is an integer"""
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
