from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
import os

bootstrap = Bootstrap()

def create_app(config_class=Config):


    app = Flask(__name__)
    app.config.from_object(Config)
    

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    bootstrap.init_app(app)

    return app
