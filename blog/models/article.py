from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from blog.app import db
from blog.models.article_tag import article_tag_association_table


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='article')
    tag = relationship(
        "Tag",
        secondary=article_tag_association_table,
        back_populates="article",
    )

    def __init__(self, author_id, title, text):
        self.author_id = author_id
        self.title = title
        self.text = text

    def __str__(self):
        return self.title
