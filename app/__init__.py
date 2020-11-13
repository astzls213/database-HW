from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config
from .models import db

bootstrap = Bootstrap()


def create_app(env_name):
    # 生成 Flask APP
    app = Flask(__name__)
    # 注册app变量
    app.config.from_object(config[env_name])
    # 初始化插件
    bootstrap.init_app(app)
    db.init_app(app)
    # 注册蓝本
    from .blueprint import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
