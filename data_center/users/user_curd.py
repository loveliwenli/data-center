#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:user_curd.py
@time:2022/03/22
"""

from loguru import logger
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from sqlalchemy.sql import or_
from pymysql.err import IntegrityError

from data_center.models.user_models import Group, User
from data_center.models.schemas.user_schemas import UpdateUserSchemas, AddUserSchemas, GroupSchemas, ReadeUserSchemas
from data_center.utils import secret


# 新增用户信息
def create_user(db: Session, data: AddUserSchemas):
    result: ReadeUserSchemas
    try:
        data.password = secret.get_password_hash(data.password)
        db_data = User(**data.dict())
        db.add(db_data)
        db.commit()
        return get_user_by_name(db, data.user_name)
    except IntegrityError as e:
        logger.error(e)
        db.rollback()
        return get_user_by_name(db, data.user_name)


# 更新用户信息
def update_user(db: Session, data: UpdateUserSchemas):
    db_data = User(**data.dict())
    db.execute(update(User).where(User.user_name == db_data.user_name).values(data.dict()))
    db.commit()
    db.close()


# 查询所有用户信息
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.execute(select(User).offset(skip).limit(limit)).scalars().all()


# 通过用户名字查询用户信息
def get_user(db: Session, id: int = None, user_name: str = None):
    result = db.query(User).filter(or_(User.id == id, User.user_name == user_name)).first()
    # result = db.execute(select(User).where(User.id == id)).scalars().first()
    logger.info(f'通过用户ID{id}查询到的用户信息是{result.__dict__}')
    return result


# 新增或更新分组信息
def create_group(db: Session, data: GroupSchemas):
    db_data = Group(**data.dict())
    result = db.execute(select(Group).where(Group.name == db_data.name)).scalars().first()
    if not result:
        db.add(db_data)
        db.commit()
    else:
        db.execute(update(Group).where(Group.name == db_data.name, ).values(data.dict()))
        db.commit()
