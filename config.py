import os

base_dir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    TEMPLATE_DIR = os.path.abspath('../templates')
    STATIC_DIR = os.path.abspath('../static')
