from flask import Flask
from flask_jsglue import JSGlue
from zenpy import Zenpy

from config import Config

jsglue = JSGlue()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    jsglue.init_app(app)

    app.zenpy = Zenpy(**app.config["ZENDESK_CREDS"])

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.tickets import bp as main_bp
    app.register_blueprint(main_bp)

    return app
