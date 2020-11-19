class Config():
    SECRET_KEY = 'zls is just a genius'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dev:usefordev@localhost/dev_db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dbhw:iamp@$$wd@localhost/hw_db'


config = {
    'dev': DevConfig,
    'production': ProductionConfig,
    'default': DevConfig
}