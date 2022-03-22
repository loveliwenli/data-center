#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:run.py
@time:2022/03/14
"""
import uvicorn
import time
from utils.log_config import logger
from fastapi import FastAPI, Request, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware

from users import user_app
from utils import secret
from data_center.models.database import SessionLocal

app = FastAPI(
    title="数据构造中心",
    description="支持使用Mysql、PostgreSQL、MongoDB、ES、Redis、HTTP请求构造数据",
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/redocs',
    # dependencies=[Depends(my_oauth2_scheme)]
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"接口{request.url}响应时间：{process_time}")
    return response


# @app.middleware("http")
async def verify_token(request: Request, call_next):
    auth_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},  # OAuth2的规范，如果认证失败，请求头中返回“WWW-Authenticate”
    )
    path: str = request.get('path')
    if path.startswith('/login') | path.startswith('/docs') | path.startswith('/openapi'):
        response = await call_next(request)
        return response
    else:
        try:
            authorization: str = request.headers.get('authorization')
            if not authorization:
                response = Response(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content="Invalid authentication credentials",
                    headers={"WWW-Authenticate": "Bearer"},  # OAuth2的规范，如果认证失败，请求头中返回“WWW-Authenticate”
                )
                return response
            token = authorization.split(' ')[1]
            with SessionLocal() as db:
                if secret.verify_token(db, token):
                    logger.info("token验证通过")
                    response = await call_next(request)
                    return response
                else:
                    raise auth_error
        except Exception as e:
            logger.error(e)
            raise auth_error


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        "http://127.0.0.1:9080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_app, tags=["用户中心"])

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=9080, reload=True, debug=True, workers=4)
