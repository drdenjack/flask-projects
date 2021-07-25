# ideas from here: 
https://towardsdatascience.com/how-to-deploy-ml-models-using-flask-gunicorn-nginx-docker-9b32055b3d0
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

# run the app

        pipenv run gunicorn -w 1 -b 0.0.0.0:8000 my_app.wsgi:app -D

- This runs on port 8000
- use "-D" for daemon mode

# use gunicorn + nginx for production server
- flask server is not good enough for production environments.  gunicorn is better for production security and traffic
- use nginx as reverse proxy to handle all the crap before it gets to gunicorn

# nginx
## service control
- use systemctl (all with sudo of course)
systemctl status nginx
systemctl stop nginx
systemctl start nginx
systemctl restart nginx
systemctl disable nginx
systemctl enable nginx

## nginx setup
(You need sudo access for all of these operations)
- Create a file in /etc/nginx/sites-available/

An example file will look something like this
/etc/nginx/sites-available/myexample.com
```
        server {
                listen 9000;
                server_name myexample.com;
                access_log  /var/log/nginx/myexample.log;

                location / {
                        proxy_pass http://0.0.0.0:8000;
                        proxy_set_header Host $host;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }
        }
```

Notice the "proxy_pass" host and port match those used in the gunicorn setup

- Create a symlink to this file from /etc/nginx/sites-enabled/

        $ cd /etc/nginx/sites-enabled/
        $ sudo ln -s /etc/nginx/sites-available/myexample.com myexample.com

- Restart the service

        $ sudo systemctl restart nginx

# That's it!
- Use a browser and go to 127.0.0.1:9000  (specified by nginx)
- This redirects to  http://0.0.0.0:8000  where gunicorn is running!


# NOTES:
I initially tried all this in a Linux Mint VM.  
Python3.8.10 was already installed in Mint.
I used apt to install gunicorn and pip, then pip3 to install flask globally.  I did not use a python virtual env.
