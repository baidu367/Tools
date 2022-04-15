# -*- coding:utf-8 -*-
# Time : 2021/12/27 17:23 
# FileName : testPort.py
# Author : Gecko
# Description：测试端口是否被占用
import socket


def net_is_used(port, ip='127.0.0.1'):
    """
    :param port: 端口号
    :param ip: 访问地址
    :return: True 或 False
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        print('%s:%d is used' % (ip, port))
        return True
    except:
        print('%s:%d is unused' % (ip, port))
        return False
