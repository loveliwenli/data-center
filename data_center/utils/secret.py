#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:secret.py
@time:2022/02/04
"""
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from data_center.utils.log_config import logger
from data_center.users.user_curd import get_user_by_id
from data_center.models.user_models import User

# openssl rand -hex 32
SECRET_KEY = 'a02236baeb6a64cb5dddab02ea4808a6b2a543c367d294b70cfc6d7cc516ef8a'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
expires_delta = timedelta(days=7)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    result = pwd_context.verify(plain_password, hashed_password)
    logger.info(result)
    return result


def get_password_hash(password):
    result = pwd_context.hash(password)
    logger.info(result)
    return result


def create_access_token(user: User):
    to_encode = {
        'username': user.user_name,
        'id': user.id
    }
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logger.info(f'用户token生成成功：{encoded_jwt}')
    return encoded_jwt


def only_verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.info(f'token解析后数据：{payload}')
        username: str = payload.get("username")
        if username is None:
            return False
    except JWTError:
        return False


def verify_token(db: Session, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.info(f'token解析后数据：{payload}')
        username: str = payload.get("username")
        id: int = payload.get('id')
        if username is None:
            return False
    except JWTError:
        return False
    user = get_user_by_id(db, id=id)
    if not user:
        return False
    return user
