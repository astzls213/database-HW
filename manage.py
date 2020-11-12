from app import create_app
from app.models import *
# 运行
if __name__ == "__main__":
    app = create_app('default')
    # 初始化数据库表项（如果没有的话
    with app.app_context():
        db.create_all()
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )