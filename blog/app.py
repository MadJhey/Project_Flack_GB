import os

from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask, send_from_directory
from blog import commands
from blog.extensions import db, login_manager, migrate, csrf, api
from blog.admin import admin
from blog.models.user import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.settings')
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
                'User': 'User API',
                'Author': 'Author API',
                'Article': 'Article API',
            }
        ),
    ]
    api.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')


def register_blueprints(app: Flask):
    from blog.auth.views import auth
    from blog.user.views import user
    from blog.article.views import article
    from blog.author.views import author
    from blog.api.views import api_blueprint

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(article)
    app.register_blueprint(author)
    app.register_blueprint(api_blueprint)

# def register_api_routes(app):
#     from blog.api.tag import TagList
#     from blog.api.tag import TagDetail
#     from blog.api.user import UserList
#     from blog.api.user import UserDetail
#     from blog.api.author import AuthorList
#     from blog.api.author import AuthorDetail
#     from blog.api.article import ArticleList
#     from blog.api.article import ArticleDetail
#
#     api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
#     api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')
#
#     api.route(UserList, 'user_list', '/api/users/', tag='User')
#     api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')
#
#     api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
#     api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')
#
#     api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
#     api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_tags)
