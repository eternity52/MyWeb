from shop import create_app, db
from flask_migrate import Migrate


app = create_app('develop')

# 创建同步数据库对象
Migrate(app, db)

"""
flask db init # 初始化数据库
flask db migrate # 生成迁移文件
flask db upgrade # 执行迁移文件
"""

# 启动服务
if __name__ == "__main__":
    app.run()