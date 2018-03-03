import os
import sqlite3
from flask_script import Manager, prompt_bool
from flask import g
from flaskr import app, db


manager = Manager(app)


@manager.command
def initDB():
    """Initializes the database."""
    if prompt_bool("Are you sure you want to lose all your data"):
        db.create_all(bind=None)


@app.before_request
def before_request():
    g.USERNAME = app.config['USERNAME']
    g.PASSWORD = app.config['PASSWORD']


@app.teardown_appcontext
def close_db_teardown(error):
    """Closes the database again at the end of the request."""
    pass


if __name__ == '__main__':
    manager.run()
