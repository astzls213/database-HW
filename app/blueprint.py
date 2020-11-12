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
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.query.verify_password(form.passwd.data):
            # 登录成功
            return redirect(url_for('main.index'))
        else:
            # 登录失败
            flash('无效的用户名或密码！')
            return redirect(url_for('main.login'))
    # GET
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    pass
####################  分割线  ####################

#################### 主体部分 ####################
@main.route('/index')
def index():
    return render_template('index.html')

####################  分割线  ####################