import os

"""
configuration settings are defined as class variables, if application needs
more configuration items, subclasses are made of Config.
"""

class Config(object):
    """
    SECRET_KEY useful to generate signatures or tokens, used by flask-wtf to
    protect webforms against CSRF
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
