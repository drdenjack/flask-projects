FROM python:3.8-slim-buster

WORKDIR /app

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
COPY Pipfile* /app/
RUN pipenv install

# copy project
COPY . /app/

# example commands not needed with docker-compose
# EXPOSE 5000
# CMD [ "pipenv", "run", "python", "-m", "src.app"]
