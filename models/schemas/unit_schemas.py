#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:unit_schemas.py
@time:2022/03/22
"""

from typing import Optional, List
from pydantic import BaseModel


class UpdateHttpUnitSchemas(BaseModel):
    des: str
    url: str
    method: str
    headers: Optional[dict] = {'Content-Type': 'application/json;charset=UTF-8'}
    params: Optional[dict] = None
    body: dict

    class Config:
        orm_mode = True


class AddHttpUnitSchemas(UpdateHttpUnitSchemas):
    user_id: int

    class Config:
        orm_mode = True



