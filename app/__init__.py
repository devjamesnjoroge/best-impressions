from flask import Flask
from flask import make_response
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)


    #import Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Creating the app configurations

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #initialising flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
