'''
setuptools config
'''
from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_script',
        'flask_sqlalchemy',
	'flask_admin',
        'flask_login',
    ],
)
