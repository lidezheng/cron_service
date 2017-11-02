#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2017/10/24 上午10:52

from __future__ import absolute_import

from celery_app import app
from script.push_script import add, hello


@app.task
def run_celery_add(x, y):
    """测试"""
    return add(x, y)


# 忽略返回值
@app.task(ignore_result=True)
def run_celery_hello():
    """测试"""
    return hello()

