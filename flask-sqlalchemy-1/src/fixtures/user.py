from src.database import db
from src.models.user import User

def add_users():
    u1 = User()
    u1.first_name = "Bob"
    u1.last_name = "Belcher"
    u1.email = "burberboss@my-name-is.bob"

    db.session.add(u1)
    db.session.commit()
    all_users = db.session.query(User).all()
    print(f'all_users: {all_users}')

    u2 = User(first_name='Homer', last_name='Simpson', email='hjs@my-name-is-homer.com')
    db.session.add(u2)
    db.session.commit()
    all_users = db.session.query(User).all()
    print(f'all_users: {all_users}')
