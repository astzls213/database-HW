from app import create_app
from app.models import User
from app import db
from tests.test import create_admin
# 运行
if __name__ == "__main__":
    app = create_app('default')
    create_admin(app,db)
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )