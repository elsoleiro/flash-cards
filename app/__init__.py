from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config) # config items accessed via dictionary syntax
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors

'''
create the application object as an instance of class Flask imported from the
flask package. 

__name__ is passed to the Flask class, __name__ is a predefined variable
which is set to the name of the module in which it is used.

flask uses the location of the module passed here as a starting point
'''

