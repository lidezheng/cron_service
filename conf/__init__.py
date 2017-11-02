#!/usr/bin/python
# -*- coding: utf8 -*-

"""设置环境配置"""
# 获取本机IP
import socket
LOCAL_IP = socket.gethostbyname(socket.gethostname())

if LOCAL_IP in ['']:
    ENV = 'online'
else:
    ENV = 'offline'
