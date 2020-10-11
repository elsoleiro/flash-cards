"""
this module stores web form classes
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password= StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('sign in')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    password2 = StringField(
            'repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('please use a different email address.')

class EditCard(FlaskForm):
    front = StringField('front', widget=TextArea(), validators=[DataRequired()])
    back = StringField('back', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AddCard(FlaskForm):
    front = StringField('front', widget=TextArea(), validators=[DataRequired()])
    back = StringField('back', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class NextCard(FlaskForm):
    submit = SubmitField('Submit')



