from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm
from blog.models.user import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.get_user', pk=current_user.id))
    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():

        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append('user name is not uniq')
            return render_template('users/register.html', form=form)

        _user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        try:
            db.session.commit()
        except IntegrityError:
            errors.append('SQL Server Error ')
        else:
            login_user(_user)

    return render_template(
        'users/register.html',
        form=form,
        errors=errors,
    )


@user.route('/')
@login_required
def user_list():
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
