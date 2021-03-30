from wtforms import Form, StringField, PasswordField, BooleanField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username = StringField("Username", validators=[
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])

    password = PasswordField("Password", validators=[
        validators.DataRequired(message='El password es requerido')
    ])


class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])

    email = EmailField('Email', validators=[
        validators.length(min=6, max=100),
        validators.DataRequired(message='Email is required'),
        validators.Email(message='It must be a valid email')
    ])

    password = PasswordField('Password', validators=[
        validators.DataRequired(message='Password is required'),
        validators.EqualTo('confirm_password', message='Passwords are different')
    ])

    confirm_password = PasswordField('Repeat password')
    accept = BooleanField(validators=[
        validators.DataRequired()
    ])
