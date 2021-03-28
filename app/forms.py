from wtforms import Form, StringField, PasswordField
from wtforms import validators


class LoginForm(Form):
    username = StringField("Username", validators=[
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])
    
    password = PasswordField("Password", validators=[
        validators.DataRequired()
    ])
