#!/bin/bash
HOST=localhost
PORT=3000

echo "killing old docker processes"
docker-compose -f database/docker-compose-pg.yml rm -fs

echo "building docker container"
docker-compose -f database/docker-compose-pg.yml up -d 

echo "initializing database with src/init_db"
pipenv run python -m src.init_db

echo "starting the flask server"
PYTHONPATH=. FLASK_ENV=developement FLASK_DEBUG=1 FLASK_APP=src/app.py pipenv run flask run -h $HOST -p $PORT
