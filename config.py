import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(base_dir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    TEMPLATE_DIR = os.path.abspath('../templates')
    STATIC_DIR = os.path.abspath('../static')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
