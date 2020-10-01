"""
classes inherit from db>model, a base class for all models from flask-sqlalch,
this class defines several fields as class variables, fields are created
as instances of the db.Column class, which takes the field type as an arg,
plus other optional args
"""
from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    cards = db.relationship('Card', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<user {}>'.format(self.username)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer) # 1 for text 2 for code
    front = db.Column(db.String(300))
    back = db.Column(db.String(1000))
    known = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<card front: {} back: {}>'.format(self.front, self.back)

