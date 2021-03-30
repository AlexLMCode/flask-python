from wtforms import Form, StringField, PasswordField, BooleanField, HiddenField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from .models import User


def cody_validator(form, field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('Username codi is not available')


def length_honeypot(form, field):
    if len(field.data):
        raise validators.ValidationError('Only humans can register on this site!!')


class LoginForm(Form):
    username = StringField("Username", validators=[
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])

    password = PasswordField("Password", validators=[
        validators.DataRequired(message='El password es requerido')
    ])


class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50),
        cody_validator
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

    honeypot = HiddenField("", validators=[length_honeypot])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('There is already an username with that username')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('There is already an account with that email ')

    def validate(self, extra_validators=None):

        if not Form.validate(self):
            return False

        if len(self.password.data) <= 4:
            self.password.errors.append('Password is too short')
            return False

        return True
