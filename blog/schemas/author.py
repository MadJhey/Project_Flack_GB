from combojsonapi.utils import Relationship
from marshmallow import pre_load
from marshmallow_jsonapi import Schema, fields


class AuthorSchema(Schema):
    class Meta:
        type_ = 'author'
        self_url = 'author_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'author_list'

    id = fields.Integer(as_string=True)

    user = Relationship(
        nested='UserSchema',
        attribute='user',
        related_url='user_detail',
        related_url_kwargs={'id': '<id>'},
        schema='UserSchema',
        type_='user',
        many=False,
    )

    articles = Relationship(
        nested='ArticleSchema',
        attribute='article',
        related_url='article_detail',
        related_url_kwargs={'id': '<id>'},
        schema='ArticleSchema',
        type_='article',
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