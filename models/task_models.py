#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:task_models.py
@time:2022/03/15
"""

from sqlalchemy import Column, String, Integer, DateTime, func, Boolean, UniqueConstraint, Text, JSON
from .database import Base


class TaskFlow(Base):
    __tablename__ = 'task_flow'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    des = Column(String(200), nullable=True, comment='描述')
    user_id = Column(Integer, comment='创建用户ID')
    group_id = Column(Integer, comment='创建分组ID')
    steps = Column(Text, comment="执行步骤,存储格式[{key:value},{key:value}...]")
    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
