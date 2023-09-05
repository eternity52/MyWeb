import os

class Config:
    # 设置参数（关于数据库）
    MYSQL_DIALECT = 'mysql'
    MYSQL_DRIVER = 'pymysql'
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3307
    MYSQL_DB = 'shop'
    MYSQL_CHARSET = 'utf8mb4'

    # 数据库链接字符串URI
    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DRIVER}://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'

    # 数据盐
    SECRET_KEY = os.urandom(16)
    # 设置JSON数据不使用ASCII码
    JSON_AS_ASCII = False
    RESTFUL_JSON = {'ensure_ascii': False}
    # 设置token的过期时间，以秒为单位
    JWT_EXOIRATION_DELTA = 60 * 60 * 24 * 7

    DEBUG = True


class DevelopmentConfig(Config):
    # 开发环境
    # DEBUG模式
    DEBUG = True

class ProductionConfig(Config):
    # 生产环境
    DEBUG = False

class TestingConfig(Config):
    # 测试环境
    pass


config_map = {
    'develop': DevelopmentConfig,
    'product': ProductionConfig,
    'test': TestingConfig
}