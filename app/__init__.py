from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from .views import page

app = Flask(__name__)
bootstrap = Bootstrap()

csrf = CSRFProtect()


def create_app(config):
    app.config.from_object(config)
    bootstrap.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(page)

    return app
