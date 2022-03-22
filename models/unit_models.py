#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:unit_models.py
@time:2022/03/15
"""
from sqlalchemy import Column, String, Integer, DateTime, func, Boolean, UniqueConstraint, Text, JSON
from .database import Base


class HttpUnit(Base):
    __tablename__ = 'http_unit'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    des = Column(String(200), nullable=True, comment='描述')
    url = Column(Text, nullable=False, comment='访问URL地址')
    method = Column(String(20), nullable=False, comment='请求方式')
    headers = Column(JSON, nullable=True, comment='请求头')
    params = Column(String(100), nullable=True, comment='请求路径参数')
    body = Column(JSON, nullable=True, comment='请求体')
    user_id = Column(Integer, comment='创建用户ID')
    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
