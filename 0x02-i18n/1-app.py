#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
        configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def hello_world() -> Any:
    """ hello world output"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
