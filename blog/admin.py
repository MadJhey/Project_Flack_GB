from flask import url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect

from blog import models
from blog.extensions import db


# Customized admin interface
class CustomAdminView(ModelView):
    def create_blueprint(self, admin):
        blueprint = super().create_blueprint(admin)
        blueprint.name = f'{blueprint.name}_admin'
        return blueprint

    def get_url(self, endpoint, **kwargs):
        if not (endpoint.startswith('.') or endpoint.startswith('admin.')):
            endpoint = endpoint.replace('.', '_admin.')
        return super().get_url(endpoint, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_stuff

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("auth.login"))


class CustomAdminIndexView(AdminIndexView):
    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_stuff):
            return redirect(url_for('auth.login'))
        return super().index()


class TagAdminView(CustomAdminView):
    column_searchable_list = ('name',)
    create_modal = True
    edit_modal = True


class ArticleAdminView(CustomAdminView):
    can_export = True
    export_types = ('csv', 'xlsx')
    column_filters = ('author_id',)


class UserAdminView(CustomAdminView):
    column_exclude_list = ('password',)
    column_details_exclude_list = ('password',)
    column_export_exclude_list = ('password',)
    form_columns = ('first_name', 'last_name', 'is_stuff')
    can_delete = False
    can_edit = True
    can_create = False
    can_view_details = False
    column_editable_list = ('first_name', 'last_name', 'is_stuff')


admin = Admin(name='Admin panel my', index_view=CustomAdminIndexView(), template_mode='bootstrap4', )
admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(ArticleAdminView(models.Article, db.session, category="Models"))
admin.add_view(UserAdminView(models.User, db.session, category='Models'))
