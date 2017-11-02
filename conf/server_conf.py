#!/usr/bin/python
# -*- coding: utf8 -*-

from conf import ENV

if ENV == 'online':
    """下游服务主域配置"""
    UpstreamConfig = {
       
    }

    """http请求的超时时间"""
    HttpTimeout = 2.0      # 单位s

else:
    """下游服务主域配置"""
    UpstreamConfig = {
        
    }

    """http请求的超时时间"""
    HttpTimeout = 2.0      # 单位s
