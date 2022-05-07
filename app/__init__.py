from flask import Flask
from config import config_options


def create_app(config_name):

    app = Flask(__name__)

    #import Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Creating the app configurations

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    return app
