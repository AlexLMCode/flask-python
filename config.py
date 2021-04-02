from decouple import config


class Config:
    SECRET_KEY = 'alexcodigo'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web_facilito'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'alexlm0212@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')  # MAIL_PASSWORD


class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web_facilito_test'
    TEST = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}
