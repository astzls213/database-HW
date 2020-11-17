from flask import (
    Blueprint,
    flash,
    redirect,
    url_for,
    render_template,
    request
)
from flask_login import (
    login_required,
    login_user,
    logout_user
)
from datetime import datetime
from .forms import (
    LoginForm,
    RegisterForm
)
from .models import (
    db,
    User,
    Journal,
    writing,
    management
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
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            # 登录失败
            flash('无效的用户名或密码！', 'danger')
            return redirect(url_for('main.login'))
    # GET
    logout_user()   # 先登出用户，无论如何
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

# 主界面
@main.route('/index')
@login_required
def index():
    # 获取数据库所有 journal 数据
    journals = Journal.query.all()
    return render_template('index.html', journals=journals)

# 搜索功能路由
@main.route('/search', methods=['POST'])
@login_required
def search():
    # 获取 POST 数据
    option = request.form.get('option', None)
    found = request.form.get('search', '')
    # 检查输入栏是否为空
    if found is '':
        flash('输入栏为空!','info')
        return redirect(url_for('main.index'))
    else:
        start = datetime.now()  # 记录开始时间点
        # 根据 Option 查找与 found 模糊匹配的数据库
        if option == 'cn_name':
            found = Journal.cn_name.like('%{}%'.format(found))
            results = Journal.query.filter(found).all()
        elif option == 'issn':
            found = Journal.issn.like('{}%'.format(found))
            results = Journal.query.filter(found).all()
        elif option == 'cn':
            found = Journal.cn.like('{}%'.format(found))
            results = Journal.query.filter(found).all()
    end = datetime.now()  # 记录结束时间点
    msg = '查询用时: %.3fms' % ((end-start).total_seconds()*1000,)
    flash(msg,'success')
    # 渲染结果
    return render_template('sear_result.html', results=results)

# 增添期刊路由
@main.route('/insert', methods=['GET','POST'])
@login_required
def insert():
    pass

# 删除期刊路由
@main.route('/delete', methods=['GET','POST'])
@login_required
def delete():
    pass
# 修改期刊路由
@main.route('/update', methods=['GET','POST'])
@login_required
def update():
    pass

# 期刊详细信息路由
@main.route('/detail', methods=['POST'])
@login_required
def detail():
    pass

# 生成报表路由
@main.route('/report', methods=['GET','POST'])
@login_required
def report():
    pass
####################  分割线  ####################