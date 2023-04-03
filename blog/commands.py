import click
from werkzeug.security import generate_password_hash
from blog.extensions import db
@click.command("init-db")
def init_db():
    """Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@click.command("create-users")
def create_users():
    """Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models.user import User
    admin = User(username="admin", is_staff=True)
    james = User(username="james")
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
