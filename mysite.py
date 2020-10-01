from app import app, db
from app.models import User, Card

"""
flask shell command preimports the application instance, this is the
configuration.
the decorator registers the function as a shell context function, when
the flask shell command runs it will invoke this function and register the
items returned by it in the shell session.
in venv:
    flask shell
    >> db
    >> User
    >> Card
"""
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Card': Card}


