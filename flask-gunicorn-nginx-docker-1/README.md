# ideas from here: 
        
        https://towardsdatascience.com/how-to-deploy-ml-models-using-flask-gunicorn-nginx-docker-9b32055b3d0

# run the app

        $ ./run_docker.sh

# use gunicorn + nginx for production server
- flask server is not good enough for production environments.  gunicorn is better for production security and traffic
- use nginx as reverse proxy to handle all the crap before it gets to gunicorn


# Access the page
Go to http://localhost in a browser!

