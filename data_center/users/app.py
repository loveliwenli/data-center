#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:app.py
@time:2022/03/22
"""
from loguru import logger
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from utils import secret
from data_center.models.database import get_db
from .user_curd import get_user_by_name, create_user
from models.user_models import User
from data_center.models.schemas.user_schemas import AddUserSchemas, ReadeUserSchemas

user_app = APIRouter()


def authenticate_user(db: Session, form_data: OAuth2PasswordRequestForm = Depends()) -> User:
    user = get_user_by_name(db, form_data.username)
    if user:
        if secret.verify_password(form_data.password, user.password):
            return user
    return False


@user_app.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logger.info(f'登录请求信息：{form_data.__dict__}')
    user = authenticate_user(db, form_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = secret.create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}


@user_app.post("/user/register", response_model=ReadeUserSchemas)
async def register(user_info: AddUserSchemas, db: Session = Depends(get_db)):
    return create_user(db, user_info)


@user_app.get("/user/me", response_model=ReadeUserSchemas)
async def register(token: str = Depends(OAuth2PasswordBearer(tokenUrl='/login')), db: Session = Depends(get_db)):
    return secret.verify_token(db, token)
