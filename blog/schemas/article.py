from combojsonapi.utils import Relationship
from marshmallow import pre_load
from marshmallow_jsonapi import Schema, fields


class ArticleSchema(Schema):
    class Meta:
        type_ = 'article'
        self_url = 'article_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'article_list'

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False, required=True)
    text = fields.String(allow_none=False, required=True)
    created_at = fields.DateTime(allow_none=False)
    updated_at = fields.DateTime(allow_none=False)

    author = Relationship(
        self_url="/api/articles/{id}/relationships/author",
        nested='AuthorSchema',
        attribute='author',
        related_url='author_detail',
        related_url_kwargs={'id': '<id>'},
        schema='AuthorSchema',
        type_='author',
        many=False,
    )

    tags = Relationship(
        nested='TagSchema',
        attribute='tags',
        related_url='tag_detail',
        related_url_kwargs={'id': '<id>'},
        schema='TagSchema',
        type_='tag',
        many=True,
    )

    @pre_load
    def remove_id_before_deserializing(self, data, **kwargs):
        """
        We don't want to allow editing ID on POST / PATCH
        Related issues:
        https://github.com/AdCombo/flask-combo-jsonapi/issues/34
        https://github.com/miLibris/flask-rest-jsonapi/issues/193
        """
        if 'id' in data:
            del data['id']
        return data
