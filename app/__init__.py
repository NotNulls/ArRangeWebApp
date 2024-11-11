from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
import os

bootstrap = Bootstrap()
mail = Mail()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.debug = True

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    bootstrap.init_app(app)
    mail.init_app(app)

    return app
