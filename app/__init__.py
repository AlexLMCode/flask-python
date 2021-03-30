from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()

from .views import page
from .models import User


def create_app(config):
    app.config.from_object(config)
    csrf.init_app(app)

    if not app.config.get('TEST', False):
        bootstrap.init_app(app)

    app.register_blueprint(page)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
