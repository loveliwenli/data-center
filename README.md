### 项目配置
#### 数据库配置
本项目使用了SQLAlchemy来操作数据库,alembic来跟踪数据库表的变更
```python
# 安装好依赖后,进入环境执行命令:alembic init alembic
# 会在项目根目录下生成一个alembic文件夹和alembic.ini文件
```
修改项目的数据库配置,需要修改两个地方
1. 根目录下的alembic.ini,修改sqlalchemy.url="你的数据库配置"
2. 修改./config/db_config.py文件内的db_url="你的数据库配置"

数据库表迁移
1. alembic revision --autogenerate -m "你想填写的备注"  
2. alembic upgrade head

注意:
每次在models模块新增表文件,均需要在./alembic/env.py文件中导入新增的model