#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template
from typing import Any

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """simple '/' route that outputs 
       'welcome to holberton' as a page title and
       'hello world' as a header(<h1>)
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
