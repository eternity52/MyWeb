from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from shop import db

class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class User(db.Model, BaseModel):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    pwd = db.Column(db.String(128))
    nick_name = db.Column(db.String(32))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(32))


    

    @property
    def password(self):
        return self.pwd
    
    @password.setter
    def password(self, pwd):
        # 给密码数据加密
        self.pwd = generate_password_hash(pwd) # 数据加密

    def check_password(self, pwd):
        # 检查密码是否正确
        return check_password_hash(self.pwd, pwd)
