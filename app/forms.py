"""
this module stores web form classes
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password= StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('sign in')

