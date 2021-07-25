# Create a Flask app for crud on the Users object
  Include some db stuff too

## run postgres db in docker

    $ docker-compose -f database/docker-compose-pg.yml up -d 

- Connect to db vm manually:
    $ docker exec -it <hash id> /bin/bash

  - Another easy way is to use docker dashboard and just click the button!

## Initialize the db with fresh fixture data

    $ pipenv run python -m src.init_db

## Run the flask app

  Assuming host:port = localhost:3000 ...

    $ PYTHONPATH=. FLASK_DEBUG=1 FLASK_APP=src/app.py pipenv run flask run -h localhost -p 3000

## Run all the parts together
Create the docker container, initialize db with tables and data, start the flask server

    ./start_server.sh

## Connect to the server

Try the various request methods for the url:
http://localhost:3000/users/

# Ideas for later
- use Marshmallow package for easier python schemas from models
- add swagger 
- Run the whole app in docker
- Use alembic for data load?
