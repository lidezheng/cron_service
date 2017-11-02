#!/usr/bin/python
# -*- coding: utf8 -*-

"""数据库的相关配置"""
from conf import ENV


if ENV == 'online':

    DbConfig = {
        # 课程数据库
        'XX': {
            'host': 'ip:port',
            'name': 'dbname',
        },
        
    }

else:

    DbConfig = {
    }
