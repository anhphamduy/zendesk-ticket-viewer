from flask import Flask
from flask_jsglue import JSGlue
from zenpy import Zenpy

from config import config

jsglue = JSGlue()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    jsglue.init_app(app)

    app.zenpy = Zenpy(**app.config['ZENDESK_CREDS'])

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.tickets import bp as tickets_bp
    app.register_blueprint(tickets_bp)

    return app
