from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()
login_manager = LoginManager()

from .views import page
from .models import User, Task
from .consts import LOGIN_REQUIRED


def create_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = '.login'
    login_manager.login_message = LOGIN_REQUIRED

    if not app.config.get('TEST', False):
        bootstrap.init_app(app)

    app.app_context().push()

    mail.init_app(app)

    app.register_blueprint(page)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
