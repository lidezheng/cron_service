#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lidezheng at 2017/10/24 上午10:52

from __future__ import absolute_import

from celery.schedules import crontab
from celery.schedules import timedelta

from conf import ENV
from conf.redis_conf import RedisConfig


"""celery配置"""
CELERY_TIMEZONE = 'Asia/Shanghai'    # 指定时区，不指定默认为'UTC'
CELERY_ENABLE_UTC = False

"""BROKER配置"""
BROKER_URL = 'redis://{}:{}/{}'.format(
    RedisConfig['course']['ip'], RedisConfig['course']['port'], RedisConfig['course']['db'])

"""BACKEND配置"""
CELERY_RESULT_BACKEND = 'redis://{}:{}/{}'.format(
    RedisConfig['course']['ip'], RedisConfig['course']['port'], RedisConfig['course']['db'])

"""a task-sent event will be sent for every task so tasks can be tracked before they’re consumed by a worker"""
CELERY_TASK_SEND_SENT_EVENT = True

"""worker执行的最大任务数"""
CELERYD_MAX_TASKS_PER_CHILD = 500  # 每个worker执行了多少任务就会死掉(长时间运行Celery有可能发生内存泄露)
"""并发worker数"""
# CELERYD_CONCURRENCY = 8
"""Send task-related events 发送监控信息"""
CELERYD_SEND_EVENTS = True


if ENV == 'online':
    """BEAT配置"""
    CELERYBEAT_SCHEDULE = {
        
    }

else:
    """BEAT配置"""
    CELERYBEAT_SCHEDULE = {

        # 测试
        # 'add': {
        #     'task': 'tasks.run_celery_add',
        #     'schedule': timedelta(seconds=10),
        #     'args': (16, 16),
        # },
        # 测试
        'hello': {
            'task': 'tasks.run_celery_hello',
            'schedule': timedelta(seconds=5),
        },
    }
