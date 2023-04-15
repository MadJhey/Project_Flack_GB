from sqlalchemy import ForeignKey, Table
from blog.app import db

article_tag_association_table = Table(
    "article_tag_association",
    db.metadata,
    db.Column("article_id", db.Integer, ForeignKey("articles.id"), nullable=False),
    db.Column("tag_id", db.Integer, ForeignKey("tags.id"), nullable=False),
)
