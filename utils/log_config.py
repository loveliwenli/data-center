#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:zhaoguoqing
@file:log_config.py
@time:2022/02/05
"""
from loguru import logger
import sys

# 日志设置
# 路径，每日分割时间，是否异步记录，日志是否序列化，编码格式，最长保存日志时间
logger.remove()
logger.add(sys.stderr)
logger.add('./log/log_{time:YYYY-MM-DD}_info.log', rotation='0:00', enqueue=True, serialize=False, encoding="utf-8",
           retention="10 days", level='INFO')
logger.add('./log/log_{time:YYYY-MM-DD}_error.log', rotation='0:00', enqueue=True, serialize=False, encoding="utf-8",
           retention="10 days", level='ERROR')
logger.add('./log/log_{time:YYYY-MM-DD}_debug.log', rotation='0:00', enqueue=True, serialize=False, encoding="utf-8",
           retention="10 days", level='DEBUG')
