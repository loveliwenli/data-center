#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:task_schemas.py
@time:2022/03/22
"""

from typing import Optional, List
from pydantic import BaseModel


class AddTaskSchemas(BaseModel):
    desc: str
    user_id: int
    group_id: int
    steps: List[dict]

    class Config:
        orm_mode = True


class UpdateTaskSchemas(BaseModel):
    desc: str
    steps: List[dict]

    class Config:
        orm_mode = True
