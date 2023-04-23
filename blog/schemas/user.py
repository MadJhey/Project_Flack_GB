from combojsonapi.utils import Relationship
from marshmallow import pre_load
from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_url = 'user_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'user_list'

    id = fields.Integer(as_string=True)
    first_name = fields.String(allow_none=False, required=True)
    last_name = fields.String(allow_none=False, required=True)
    email = fields.Email(allow_none=False, required=True)
    is_stuff = fields.Boolean(allow_none=False)

    author = Relationship(
        nested='AuthorSchema',
        attribute='author',
        related_url='author_detail',
        related_url_kwargs={'id': '<id>'},
        schema='AuthorSchema',
        type_='author',
        many=False,
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