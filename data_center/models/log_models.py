#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:log_models.py
@time:2022/03/22
"""

from sqlalchemy import Column, Integer, DateTime, func, Text
from .database import Base


class HttpUnit(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    action = Column(Text, comment='用户动作描述')
    user_id = Column(Integer, comment='创建用户ID')
    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
