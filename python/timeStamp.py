# -*- coding:utf-8 -*-
# Time : 2022/4/8 16:42 
# FileName : timeStamp.py
# Author : Gecko
# Description：时间戳与格式化时间互相转换
import time


def timestamp_to_time(timestamp, format='%Y-%m-%d %H:%M:%S'):
    '''
    格式化时间转成时间戳
    :param timestamp: 时间戳
    :param format: 默认年月日时分秒
    :return: 返回指定格式时间
    '''
    if timestamp:
        time_tuple = time.localtime(timestamp)
        result = time.strftime(format, time_tuple)
        return result
    else:
        return time.strftime(format)


print(timestamp_to_time(1649407653))


def time_to_timestamp(format_time=None, format='%Y-%m-%d %X'):
    '''
    时间戳转换成格式化时间
    :param format_time: 时间戳
    :param format:默认年月日时间秒
    :return: 返回时间戳
    '''
    if format_time:
        time_tuple = time.strptime(format_time, format)
        result = time.mktime(time_tuple)
        return int(result)
    return int(time.time())


print(time_to_timestamp('2050-1-1 01:01:01'))
