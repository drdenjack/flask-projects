"""init_db.py

This is a good place to setup inital data and run DDL, etc.

Note on creating tables and adding fixture data:
Model classes need to be declared and inherit from db.Model 
BEFORE calling db.create_all.  These calls must also be performed 
on the same instance of "db = SQLAlchemy()"

"""
from flask import Flask

from src.app_log import log
from src.config import DATABASE_CONNECTION_URI
from src.database import db
from src.fixtures import add_fixture_data
    
if __name__ == "__main__":
    # This does not run if calling from 'flask run' 
    log.info('Getting started')

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)

    log.info('Dropping all tables ...')
    # # for some reason this reflect() call may to be here for drop_all() to work
    # db.reflect()  
    db.drop_all()

    log.info('Creating all tables ...')
    db.create_all()
    
    log.info('Adding initial data ...')
    add_fixture_data()

    log.info('Done.')
    log.info('')
