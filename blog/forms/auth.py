from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class AuthForm(FlaskForm):
    username = StringField('User name', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
