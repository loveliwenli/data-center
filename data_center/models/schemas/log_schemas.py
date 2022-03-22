#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:log_schemas.py
@time:2022/03/22
"""
from pydantic import BaseModel


class AddLogSchemas(BaseModel):
    action: str
    user_id: int

    class Config:
        orm_mode = True
