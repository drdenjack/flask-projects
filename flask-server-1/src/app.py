import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

from src.app_log import log
from src.database import db, clear_data
from src.config import DATABASE_CONNECTION_URI
from src.users_api import add_users_routes
from src.models.user import User

hostname = os.environ.get('FLASK_HOSTNAME')
if hostname is None:
    hostname = 'localhost'

# @event.listens_for(User.__table__, 'after_create')
def add_some_users():
    u1 = User()
    u1.first_name = "Denny"
    u1.last_name = "Jackson"
    u1.email = "denny.jackson@gmail.com"

    u2 = User(first_name='Homer', last_name='Simpson', email='hjs@denjack.com')

    db2 = SQLAlchemy()
    db2.session.add(u1)
    db2.session.commit()
    all_users = db2.session.query(User).all()
    print(f'all_users: {all_users}')

    # db.session.add(u2)
    # db.session.commit()
    # all_users = db.session.query(User).all()
    # print(f'all_users: {all_users}')

def add_routes(app):
    add_users_routes(app)

def refresh_db(app):
    log.info('reflect()')
    db.reflect()
    log.info('drop_all()')
    db.drop_all()
    log.info('create_all()')
    db.create_all()
    log.info('adding_some_users()')
    add_some_users()

def setup_db(app):
    # db.session.close_all()
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    log.info('done with stup_db')
    # refresh_db()
    
def create_app():
    print('creating app ...')
    app = Flask(__name__)
    setup_db(app)
    log.info('adding routes ...')
    add_routes(app)
    return app



if __name__ == "__main__":
    # This does not run if calling from 'flask run' 
    log.msg('Getting started')

    app = create_app()
    
    print('Starting app.run() ...')
    # Default Flask run command
    app.run(host=hostname, port=3000, debug=True)

    print('READY!')
