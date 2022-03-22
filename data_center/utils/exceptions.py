#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:exceptions.py
@time:2022/02/09
"""

from fastapi import HTTPException


class MissingDBConfigException(HTTPException):
    pass


class MissingHttpConfigException(HTTPException):
    pass


class MissingRedisConfigException(HTTPException):
    pass


class ExistedException(HTTPException):
    '''
    已存在，重复添加
    '''
    pass


class UpdateException(HTTPException):
    '''
    更新数据失败
    '''
    pass

if __name__ == '__main__':
    pass
