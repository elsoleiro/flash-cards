"""
classes inherit from db>model, a base class for all models from flask-sqlalch,
this class defines several fields as class variables, fields are created
as instances of the db.Column class, which takes the field type as an arg,
plus other optional args
"""
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<user {}>'.format(self.username)

