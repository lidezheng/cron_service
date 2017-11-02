#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2017/10/24 上午10:52

from __future__ import absolute_import

from celery import Celery

# tasks可以按照功能划分成不同的模块, 添加到include列表即可
app = Celery('cron_service', include=['tasks'])
app.config_from_object('conf.celery_config')


if __name__ == '__main__':
    app.start()
