'''
setuptools config
'''
from setuptools import setup

setup(
    name='pcf',
    packages=['pcf'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_script',
        'flask_sqlalchemy',
		'flask_admin',
        'flask_login',
        'pandas',
        'pyquery',
        'requests',
        'xlrd',
    ],
)
