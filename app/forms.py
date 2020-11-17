from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    ValidationError
)
from wtforms.validators import (
    Required,
    Email,
    Length,
    EqualTo,
    Regexp
)
from .models import (
    User
)


# 登录表单
class LoginForm(FlaskForm):
    email = StringField(
        label='电邮',
        render_kw={
            "placeholder": "you@example.com"
        },
        validators=[
            Required(),
            Length(1,64),
            Email()
        ]
    )
    passwd = PasswordField(
        label='密码',
        validators=[
            Required()
        ]
    )
    login = SubmitField('登录')

# 注册表单
class RegisterForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            Required(),
            Length(1,32),
            Regexp(
                '^[A-Za-z][A-Za-z0-9_]*$',
                0,
                '用户名只能字母开头且只包含字母数字及下划线'
            )
        ]
    )
    email = StringField(
        label='电邮',
        render_kw={
            "placeholder": "you@example.com"
        },
        validators=[
            Email(),
            Required(),
            Length(1,64)
        ]
    )
    passwd = PasswordField(
        label='密码',
        validators=[
            Required(),
            EqualTo('passwd2', message='两次密码不相同')
        ]
    )
    passwd2 = PasswordField(
        label='确认密码',
        validators=[Required()]
    )
    submit = SubmitField('确认')
    # 定义内联检测函数
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电邮已被注册。')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被注册。')


