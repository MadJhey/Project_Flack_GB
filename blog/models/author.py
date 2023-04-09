from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from blog.app import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', back_populates='author')

    # def __init__(self, user_id):
    #     self.user_id = user_id
