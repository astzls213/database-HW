from flask import (
    Blueprint,
    flash,
    redirect,
    url_for,
    render_template
)
from .forms import (
    LoginForm,
    RegisterForm
)
from .models import (
    db,
    User
)
# 创建名为 main 的蓝本
main = Blueprint('main', __name__)

### 开始定义路由

#################### 认证部分 ####################
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # POST
    if form.validate_on_submit():
        # 检查邮箱
        user = User.query.filter_by(email=form.email.data).first()
        # 检查密码
        if user is not None and user.verify_password(form.passwd.data):
            # 登录成功
            return redirect(url_for('main.index'))
        else:
            # 登录失败
            flash('无效的用户名或密码！', 'danger')
            return redirect(url_for('main.login'))
    # GET
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # POST
    if form.validate_on_submit():
        # 构造新 User 对象
        new_user = User(
            name=form.username.data,
            em=form.email.data,
            pw=form.passwd.data,
            t=False
        )
        # 插入 users 表中
        db.session.add(new_user)
        db.session.commit()
        flash('注册成功！您可以登录啦！', 'success')
        return redirect(url_for('main.login'))
    # GET
    return render_template('register.html',form=form)
####################  分割线  ####################

#################### 主体部分 ####################
@main.route('/index')
def index():
    return render_template('index.html')

####################  分割线  ####################