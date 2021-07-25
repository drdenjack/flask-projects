from src.database import db

# NOTE: about sqlalchemy models
# SQLAlechemy's ORM will take care of generating id's and populating objects with them
# if you use the Declarative Base based class that you've defined to create instances of your object.

# For composit primary_keys, the 'autoincrement=True' option might need to be added to the id column


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # this should autoincrement by default since it is the first integer column
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} - {self.email}"

    @property
    def serialize(self):
        # This is fine here, but for complicated things it might be better to use Marshmallow
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }