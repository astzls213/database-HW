from werkzeug.security import(
    generate_password_hash,
    check_password_hash
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    LoginManager
)

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
login_manager.login_message = "请登录，坏蛋。"
login_manager.login_message_category = "warning"

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    type = db.Column(db.Boolean(), nullable=False)  # 管理员 True 普通账户 False

    @property
    def password(self):
        raise AttributeError('Cannot look password ^ ^')

    # 存储密码的哈希值
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 验证密码
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __init__(self, name, em, pw, t):
        self.username = name
        self.email = em
        self.password = pw
        self.type = t
        
    def __repr__(self):
        return '<User %r email %r>' % (self.username, self.email)




