#!/bin/bash
HOST=localhost
PORT=3000

# setup database
pipenv run python -m src.init_db

# run flask app
PYTHONPATH=. FLASK_ENV=developement FLASK_DEBUG=1 FLASK_APP=src/app.py pipenv run flask run -h $HOST -p $PORT
