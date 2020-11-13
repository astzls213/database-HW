from app.models import User

def create_admin(app,db):
    # 初始化数据库
    admin = User(
        'admin',
        'admin@6324.com',
        'iamadmin',
        True
    )
    
    with app.app_context():
        db.create_all()
        if admin.query.filter_by(email=admin.email).first() is None:
            db.session.add(admin)
            db.session.commit()
