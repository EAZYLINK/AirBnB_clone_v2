#!/usr/bin/python3
"""Flask framework
    """
from flask import Flask

app = Flask(__name__)


@app.route("airbnb-onepage", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
