'''
main
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_admin import Admin

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config") # load config from this file , finance.py

# Load default config and override config from an environment variable
app.config.update(dict(
    SQLALCHEMY_TRACK_MODIFICATIONS=True
))
app.config.from_pyfile('config.py')
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
db = SQLAlchemy(app)

from .views import flakr


app.register_blueprint(flakr)

print(app.config['SQLALCHEMY_DATABASE_URI'])
