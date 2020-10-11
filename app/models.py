"""
classes inherit from db.model, a base class for all models from flask-sqlalch,
this class defines several fields as class variables, fields are created
as instances of the db.Column class, which takes the field type as an arg,
plus other optional args
"""
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
import random

"""
the extension (flask-login) expects a configuration as a user loader function
that can be called to load a user given the id
the user loader is registered with Flask-Login via the decorator, the id
that Flask-Login passes to the function as an argument will be a string so
we convert to int to allow the db to use this
"""
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    cards = db.relationship('Card', backref='author', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<user {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
                digest, size)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer) # 1 for text 2 for code
    front = db.Column(db.String(300))
    back = db.Column(db.String(1000))
    known = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def card_list(author_id):
        cards = Card.query.filter(Card.user_id == author_id).all()
        finish = []
        while(len(finish) < len(cards)):
            k = random.randint(0,(len(cards)-1))
            check = False
            for i in finish:
                if i == cards[k]:
                    check = True
                    break
            if check:
                continue
            finish.append(cards[k])
        return finish
