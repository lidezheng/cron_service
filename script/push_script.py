#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2017/10/24 上午10:50


from base_script import *
from conf import ENV
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)



def add(x, y):
    """test"""
    print '计算两个数的和：%s + %s = ...' % (x, y)
    time.sleep(5)
    return x + y


def hello():
    logger.error('hello, world')
    return True



