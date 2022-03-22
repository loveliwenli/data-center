#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:database.py
@time:2022/03/15
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
from data_center.config import db_config

SQLALCHEMY_DATABASE_URL = db_config.db_url

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       encoding='utf-8',
                       echo=True,
                       future=True,
                       pool_size=30,  # 连接池大小
                       pool_recycle=1600,  # 连接回收时间，这个值必须要比数据库自身配置的interactive_timeout值小
                       pool_pre_ping=True,  # 预检测池中连接是否有效，并替换无效连接
                       pool_use_lifo=True,  # 使用后进先出的方式获取连接，允许多余连接保持空闲
                       echo_pool=True,  # 会打印输出连接池的异常信息，帮助排查问题
                       max_overflow=5  # 最大允许溢出连接池大小的连接数量
                       )

SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True))

# 创建基本映射类
Base = declarative_base(bind=engine, name='Base')


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
