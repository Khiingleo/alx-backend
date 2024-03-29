#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template, request
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


app.config.from_object("3-app.Config")


@app.route('/', strict_slashes=False)
def hello_world() -> Any:
    """ hello world output"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> Any:
    """determines the locale/language of the application """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
