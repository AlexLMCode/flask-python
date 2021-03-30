class Config:
    SECRET_KEY = 'alexcodigo'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web_facilito'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
