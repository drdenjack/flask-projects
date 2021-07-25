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

def add_routes(app):
    add_users_routes(app)

def setup_db(app):
    # db.session.close_all()
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    
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
