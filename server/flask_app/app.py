import os
from flask import Flask

"""
These are for holding the application data
I am using them as a quick replacement for a database
"""
wish_list = []
users = [{"id": 1}, {"id": 2}]
books = [{"id": 1}, {"id": 2}]


def load():
    app = Flask(__name__, static_folder=None)

    # set the env variable APPLICATION_ROOT to the URL path where the app is served
    app.config["APPLICATION_ROOT"] = os.environ.get("APPLICATION_ROOT", "/")
    prefix = app.config["APPLICATION_ROOT"]
    if app.config["APPLICATION_ROOT"] == "/":
        prefix = ""

    # register the blueprint using the prefix defined in the configuration as
    # the application root.
    from .api import api
    api_prefix = "{}/api".format(prefix)
    app.logger.info("using api url prefix {}".format(api_prefix))
    app.register_blueprint(api, url_prefix=api_prefix)

    # log the URL paths that are registered
    for url in app.url_map.iter_rules():
        app.logger.debug(repr(url))

    return app
