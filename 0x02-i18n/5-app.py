#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Any, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> Any:
    """determines the locale/language of the application """
    if "locale" in request.args:
        if request.args["locale"] in app.config["LANGUAGES"]:
            return request.args["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[dict, None]:
    """
    get user rturns a user dict or none if the user id can't be
    found or login_as was not passed
    """
    if "login_as" in request.args:
        result = int(request.args["login_as"])
        user_dict = users.get(result)

        if user_dict:
            return user_dict

    return None


@app.before_request
def before_request() -> None:
    """
     executed before all other functions.
     uses get_user to find a user if any and set it as global on
     flask.g.user
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
