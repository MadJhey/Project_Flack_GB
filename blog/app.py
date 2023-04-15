from flask import Flask
from blog import commands
from blog.extensions import db, login_manager, migrate, csrf
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

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.auth.views import auth
    from blog.user.views import user
    from blog.article.views import article
    from blog.author.views import author


    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(article)
    app.register_blueprint(author)



def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_tags)
