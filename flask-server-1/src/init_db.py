"""init_db.py

This is a good place to setup inital data and run DDL, etc.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.app_log import log
from src.config import DATABASE_CONNECTION_URI
from src.models.user import User

db = SQLAlchemy()

def add_some_users():
    u1 = User()
    u1.first_name = "Denny"
    u1.last_name = "Jackson"
    u1.email = "denny.jackson@gmail.com"

    db.session.add(u1)
    db.session.commit()
    all_users = db.session.query(User).all()
    print(f'all_users: {all_users}')

    u2 = User(first_name='Homer', last_name='Simpson', email='hjs@denjack.com')
    db.session.add(u2)
    db.session.commit()
    all_users = db.session.query(User).all()
    print(f'all_users: {all_users}')

    
if __name__ == "__main__":
    # This does not run if calling from 'flask run' 
    log.info('Getting started')


    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)

    log.info('Dropping all tables ...')
    db.reflect()  # for some reason this reflect() call has to be here for drop_all() to work
    db.drop_all()

    log.info('Creating all tables ...')
    db.create_all()

    log.info('Adding some users ...')
    add_some_users()

    log.info('Done.')
    log.info('')
