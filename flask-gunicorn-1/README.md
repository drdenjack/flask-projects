# ideas from here: 
https://towardsdatascience.com/how-to-deploy-ml-models-using-flask-gunicorn-nginx-docker-9b32055b3d0

# run the app

        pipenv run gunicorn -w 1 -b 0.0.0.0:8000 my_app.wsgi:app

- This runs on port 8000
- use "-D" for daemon mode

# use gunicorn for production server
- flask server is not good enough for production environments
- also use nginx as reverse proxy to handle all the crap before it gets to gunicorn


# setup nginx to 
- edit the nginx config file to point to gunicorn
- look up default gunicorn + nginx configs

sudo service nginx restart






