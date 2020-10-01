"""
configuration settings are defined as class variables, if application needs
more configuration items, subclasses are made of Config.
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    SECRET_KEY useful to generate signatures or tokens, used by flask-wtf to
    protect webforms against CSRF
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    """
    take DATABASE_URL, else (if undefined), configure app.db located
    in main directory of the application which is stored in the basedir var
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False # do not flag changes to db
