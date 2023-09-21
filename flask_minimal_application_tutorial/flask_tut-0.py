#!/usr/bin/python3
# how a minimal flask application looks like

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    """Simple Flask function."""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
