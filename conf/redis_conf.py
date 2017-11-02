#!/usr/bin/python
# -*- coding: utf8 -*-

"""redis的相关配置"""
from conf import ENV


if ENV == 'online':

    RedisConfig = {
        # 课程redis
        'XX': {
            'ip': 'ip',
            'port': port,
            'db': db,
        },
        
    }

else:

    RedisConfig = {
        
    }
