import os

base_dir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "'9a40917e4c539ade06ee9b2e63754df14620b8be199bfa5f5c00da80219adfee'"
    DEBUG = True
    TEMPLATE_DIR = os.path.abspath('../templates')
    STATIC_DIR = os.path.abspath('../static')