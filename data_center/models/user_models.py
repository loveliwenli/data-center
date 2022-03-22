#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:user_models.py
@time:2022/03/15
"""

from sqlalchemy import Column, String, Integer, DateTime, func, Boolean, UniqueConstraint
from .database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(100), index=True, unique=True, nullable=True, comment='用户名')
    full_name = Column(String(100), nullable=True, comment='用户全称')
    password = Column(String(100), nullable=False, comment='密码')
    email = Column(String(100), nullable=True, comment='用户邮箱')
    phone = Column(String(100), nullable=True, comment='用户手机号')
    status = Column(Boolean, default=True, comment='账号状态')
    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=False, nullable=True, comment='分组名称')
    user_id = Column(Integer, comment='创建用户ID')
    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")


class GroupAndUser(Base):
    __tablename__ = 'group_user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(String(100), unique=False, nullable=True, comment='分组id')
    user_id = Column(String(100), unique=False, nullable=True, comment='用户id')
    status = Column(Boolean, nullable=False, default=False, comment="权限状态，0=无权限")
    create_time = Column(DateTime, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    __table_args__ = (UniqueConstraint('group_id', 'user_id', name="unique_group_id_and_user_id"),)


if __name__ == '__main__':
    pass
