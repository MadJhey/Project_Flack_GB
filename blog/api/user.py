from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models import User
from blog.schemas import UserSchema
from blog.api.permissions.user import UserListPermission, UserPatchPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserListPermission]

    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_patch': [UserPatchPermission],
    }

# {
#   # "data": {
#     "type": "user",
#     "id": 2,
#     "attributes": {
#       "last_name": "string1",
#       "first_name": "string2"
#     }
#   }
# }