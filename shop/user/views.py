from flask import request
from flask_restful import Resource
from shop.user import user_bp, user_api
from shop import models, db
# 在这里导入写的token文件
from shop.utils.token import generate_token, verify_token, login_required
import re

# 创建视图
@user_bp.route('/')
def index():
    return 'hello user' 

# 登陆功能
@user_bp.route('/login/', methods=['POST'])
def login():
    # 获取用户名
    # name = request.form.get('name')# content-type: application/x-www-form-urlencoded
    name = request.get_json().get('name') # content-type: application/json
    # 获取密码
    pwd = request.get_json().get('pwd')
    # 判断是否传递的数据是完整的
    if not all([name, pwd]):
        return {'status':400, 'msg':'参数不完整'}
    else:
        # 通过用户名获取用户对象
        user = models.User.query.filter(name == name).first()
        # 判断用户是否存在
        if user:
            # 判断密码是否正确
            if user.check_password(pwd):
                # 生成一个token
                token = generate_token({'id': user.id})
                return {'status': 200, 'msg': '登陆成功', 'data': {'token': token}}
            
        return {'status': 400, 'msg': '用户名或密码错误'}
    

class Users(Resource):
    def get(self):
        pass


    def post(self):
        # 注册用户
        # 接收用户信息
        name = request.get_json().get('name')
        pwd = request.get_json().get('pwd')
        real_pwd = request.get_json().get('real_pwd')
        # 验证数据的合法性
        if not all([name, pwd, real_pwd]):
            return {'status':400, 'msg': '参数不完整'}
        # 判断两次密码是否一致
        if pwd != real_pwd:
            return {'status':400, 'msg': '两次密码不一致'}
        # 判断用户名是否合法
        if len(name) < 2:
            return {'status':400, 'msg': '用户名不合法'}
        

        phone = request.get_json().get('phone')
        email = request.get_json().get('email')
        # 判断手机号码的合法性
        if not re.match(r'^1[3456789]\d{9}$',phone):
            return {'status':400, 'msg':'手机号不合法'}
        # 判断邮箱的合法性
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-0_-]+(\.[a-zA-Z0-9_-]+)+$',email):
            return {'status':400, 'msg':'邮箱不合法'}
        try:
            # 判断用户名是否存在
            user = models.User.query.filter(name == name).first()
            if user:
                return {'status':400, 'msg':'用户名已经存在'}
        except Exception as e:
            pass
            # return {'status':400, 'msg':'查询用户失败'}

        nick_name = request.get_json().get('nick_name')
       
        # 创建用户对象
        user = models.User(name=name, password=pwd, phone=phone, email=email, nick_name=nick_name)

        # 保存到数据库中
        db.session.add(user)
        db.session.commit()
        return {'status':200, 'msg': '注册成功'}

user_api.add_resource(Users, '/users/')

@user_bp.route('/test/')
@login_required
def test_login_required():
    return {'status': 200, 'msg': 'success'}