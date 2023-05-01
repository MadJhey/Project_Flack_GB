from sqlalchemy.orm import relationship
from blog.app import db
from blog.models.article_tag import article_tag_association_table


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    article = relationship('Article', secondary=article_tag_association_table, back_populates='tag')

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
