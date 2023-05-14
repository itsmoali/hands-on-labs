from Website import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# This is the model for the user
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150)) 
    is_authenticated = True

    def get_id(self):
        return str(self.id)
    
    # Checks if the user is authenticated
    def is_authenticated(self):
        return self.is_authenticated
    
    # Checks if the user is active
    def is_active(self):
        return True