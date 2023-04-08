import click
from flask.cli import with_appcontext

from werkzeug.security import generate_password_hash
from blog.extensions import db


@click.command("init-db")
@with_appcontext
def init_db():
    """Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("db done!")


@click.command("create-users")
@with_appcontext
def create_users():
    """Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models.user import User
    admin = User(username="admin", is_staff=True, password=generate_password_hash('admin'))
    james = User(username="james", password=generate_password_hash('james'))
    jhon = User(username="jhon", is_staff=True, password=generate_password_hash('jhon'))
    db.session.add(admin)
    db.session.add(james)
    db.session.add(jhon)
    db.session.commit()
    print("done! created users:", admin, james, jhon)
