from flask import Blueprint


iauthfunctions = Blueprint(
    "iauthfunctions", __name__)


def page():
    return "Hello, iauthfunctions!"


iauthfunctions.add_url_rule(
    "/iauthfunctions/page", view_func=page)


def get_blueprints():
    return [iauthfunctions]
