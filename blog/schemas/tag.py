from marshmallow import pre_load
from marshmallow_jsonapi import Schema, fields


class TagSchema(Schema):
    class Meta:
        type_ = 'tag'
        self_url = 'tag_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'tag_list'

    id = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)

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