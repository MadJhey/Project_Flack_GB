from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models.user import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
@login_required
def user_list():
    # from blog.models.user import User
    users = User.query.all()
    return render_template('users/list.html',
                           users=users
                           )


@user.route('/<int:pk>')
@login_required
def get_user(pk: int):
    # from blog.models.user import User
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f'User id {pk} not found')

    return render_template(
        'users/details.html',
        user=selected_user,
    )
