from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # config items accessed via dictionary syntax

from app import routes

'''
create the application object as an instance of class Flask imported from the
flask package. 

__name__ is passed to the Flask class, __name__ is a predefined variable
which is set to the name of the module in which it is used.

flask use the location of the module passed here as a starting point
'''

