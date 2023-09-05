from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_map
import os

# 创建SQLAlchemy 实例
db = SQLAlchemy()

def create_app(config_name):
    # 创建一个Flask实例
    app = Flask(__name__)
    
    # 根据config_map获取配置类
    Config = config_map.get(config_name)

    # 根据类来加载配置信息
    app.config.from_object(Config)

    # 初始化db
    db.init_app(app)

    # 获取user蓝图对象
    from shop.user import user_bp

    # 注册蓝图
    app.register_blueprint(user_bp)

    return app




