from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    is_stuff = db.Column(db.Boolean)
    username = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), default="", server_default="")

    author = relationship('Author', uselist=False, back_populates='user')
    def __init__(self, username, is_staff=False, password=None, email=None, first_name=None, last_name=None):
        self.username = username
        self.is_stuff = is_staff
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User #{self.id} {self.username}>"

    def __str__(self):
        return self.username
