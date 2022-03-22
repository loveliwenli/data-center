#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:MyOAuth2PasswordBearer.py
@time:2022/02/04
"""
from typing import Optional
from fastapi import Request, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param


class MyOAuth2PasswordBearer(OAuth2PasswordBearer):
    '''
    docs文档的接口，如果需要登录后才能访问，需要添加OAuth2PasswordBearer的依赖才会展示登录入口，并且依赖了OAuth2PasswordBearer的接口
    才会带有登录信息
    全局添加OAuth2PasswordBearer依赖，则登录接口会陷入死循环，因为登录接口没有OAuth2PasswordBearer的信息
    重写OAuth2PasswordBearer，对于登录接口，或者指定的接口不读取OAuth2PasswordBearer，直接返回空字符串
    '''

    def __init__(self, tokenUrl: str):
        super().__init__(
            tokenUrl=tokenUrl,
            scheme_name=None,
            scopes=None,
            description=None,
            auto_error=True
        )

    async def __call__(self, request: Request) -> Optional[str]:
        path: str = request.get('path')
        if path.startswith('/login') | path.startswith('/docs') | path.startswith('/openapi'):
            return ""
        authorization: str = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


my_oauth2_scheme = MyOAuth2PasswordBearer(tokenUrl='login')
