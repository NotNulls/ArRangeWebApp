from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

bootstrap = Bootstrap()



def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    bootstrap.init_app(app)

    return app
