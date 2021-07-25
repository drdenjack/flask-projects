# wsgi = web server gateway interface
# for some reason I always forget these initials

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
