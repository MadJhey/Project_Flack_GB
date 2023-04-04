from flask_login import UserMixin
from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    is_stuff = db.Column(db.Boolean)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, default="", server_default="")

    def __init__(self, username, is_staff=False):
        self.username = username
        self.is_stuff = is_staff

    def __repr__(self):
        return f"<User #{self.id} {self.username}>"
