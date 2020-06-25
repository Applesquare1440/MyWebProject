from habrClone import db
from datetime import datetime
#need to improve this one

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f'Пользователь: {self.username}, email {self.email}'