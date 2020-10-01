from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Elias'}
    posts = [
        {
            'author': {'username': 'Jimmy'},
            'body': 'Hello there'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'Hello there'
        }
        ]
        
    return render_template('index.html', title="home", user=user, posts=posts)
