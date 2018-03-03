'''
debug flask config
'''
import os

DEBUG = True
SQLALCHEMY_ECHO = False

appFolder = os.path.dirname(__file__)

# os.urandom(24)
SECRET_KEY = b'l\xc3\xfc\x10\xb1\xcd\xa5\xe1\x85\xf9X\xb88\xba\xc5C\xb3\x07\xc7\x8cS\x81\x1a\xc0'
USERNAME = 'admin'
PASSWORD = 'default'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(appFolder, r"../", 'data.db')
