#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:user_schemas.py
@time:2022/03/22
"""

from typing import Optional, List
from pydantic import BaseModel


class ReadeUserSchemas(BaseModel):
    user_name: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: bool

    class Config:
        orm_mode = True


class UpdateUserSchemas(ReadeUserSchemas):
    password: str

    class Config:
        orm_mode = True


class AddUserSchemas(UpdateUserSchemas):
    status: Optional[bool] = 0

    class Config:
        orm_mode = True


class GroupSchemas(BaseModel):
    name: str
    user_id: int

    class Config:
        orm_mode = True


class GroupAndUserSchemas(BaseModel):
    group_id: int
    user_id: int
    status: Optional[bool] = False

    class Config:
        orm_mode = True
