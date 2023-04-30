from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from blog.forms.auth import AuthForm
from blog.models.user import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def login():
    form = AuthForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('user.get_user', pk=current_user.id))

    return render_template(
        'auth/login.html', form=form
    )


@auth.route('/login', methods=('POST',))
def login_post():
    name = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=name).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.get_user', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
