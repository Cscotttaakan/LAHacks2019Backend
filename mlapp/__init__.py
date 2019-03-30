import logging
import json

from flask import current_app, Flask, redirect, url_for
from . import model_mongodb

def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    if not app.testing:
        logging.basicConfig(level=logging.INFO)

#    with app.app_context():
#        model = model_mongodb
#        model.init_app(app)

    @app.route("/")
    def index():
        return 'it works!'

    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occured: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500


