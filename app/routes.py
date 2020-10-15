from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditCard, AddCard
from sqlalchemy import func
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Card, JSONEncoder
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title="home")

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title="sign in", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('registration complete')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/cards/<username>') # '<>' denotes dynamic componenet
@login_required
def cards(username):
    user = User.query.filter_by(username=username).first_or_404()
    cards = Card.query.filter_by(author=current_user)
    return render_template('cards.html', user=user, cards=cards)

@app.route('/user/<username>') # '<>' denotes dynamic componenet
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.route('/edit/<card_id>', methods=['GET', 'POST'])
@login_required
def edit(card_id):
    form = EditCard()
    card = Card.query.filter_by(id=card_id).first()
    if form.validate_on_submit():
        card.front = form.front.data
        card.back = form.back.data
        db.session.commit()
        flash('this card has been updated')
 
    form.front.data = card.front
    form.back.data = card.back
    return render_template('edit.html', card=card, form=form)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_card():
    form = AddCard()
    if form.validate_on_submit():
        card = Card(type=1, front=form.front.data, back=form.back.data,
                author=current_user)
        db.session.commit()
        flash('added card')
        return redirect(url_for('cards', username=current_user.username))
    return render_template('add.html', form=form)

@app.route('/delete/<card_id>')
@login_required
def delete(card_id):
    card = Card.query.filter_by(id=card_id).first()
    db.session.delete(card)
    db.session.commit()
    flash('card deleted')
    return redirect(url_for('cards', username=current_user.username))

@app.route('/learn', methods=['GET'])
@login_required
def learn():
    card = Card.query.filter_by(author=current_user).order_by(func.random()).first()
    return render_template('learn.html', card=card, user=current_user)

@app.route('/learn2', methods=['GET'])
@login_required
def learn2():
    card = Card.query.filter_by(author=current_user).order_by(func.random()).first()
    cards = Card.card_list(current_user.id)
    cards = Card.jsonify_cards(cards)
    tempcard = card.__dict__
    tempcard.pop("_sa_instance_state")  # watch the leading underscore
    card = JSONEncoder().encode(tempcard)
    card = JSONEncoder().encode(card)
    return render_template('learn2.html', cards=cards, card=card, user=current_user)
 

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
