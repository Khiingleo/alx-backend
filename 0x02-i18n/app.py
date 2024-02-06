#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Any, Union
import pytz
from pytz import timezone
from datetime import datetime


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
    return render_template("index.html")


@babel.localeselector
def get_locale() -> Any:
    """determines the locale/language of the application """
    if "locale" in request.args:
        if request.args["locale"] in app.config["LANGUAGES"]:
            return request.args["locale"]

    elif g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    else:
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
    g.current_time = format_datetime(datetime.now())


@babel.timezoneselector
def get_timezone() -> Any:
    """
    determines the time zone
    """
    # timezone from url parameters
    if "timezone" in request.args:
        timezone = request.args.get("timezone")
        try:
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return "UTC"
    # Time zone from user profile
    elif g.user and g.user.get("timezone"):
        try:
            return pytz.timezone(g.user.get("timezone")).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return "UTC"

    default_timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
    return request.accept_languages.best_match([default_timezone])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
