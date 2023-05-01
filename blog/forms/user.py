from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    username = StringField("User")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("E-mail", [validators.Email(), validators.DataRequired()])
    password = PasswordField("Password", [
        validators.InputRequired(),
        validators.EqualTo('confirm_password', message='Fild must be equal to password')
    ])
    confirm_password = PasswordField("Confirm Password", [validators.DataRequired()])
    submit = SubmitField("Submit")
