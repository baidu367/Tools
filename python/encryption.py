# -*- coding:utf-8 -*-
# Time : 2022/4/8 17:02 
# FileName : encryption.py
# Author : Gecko
# Description：md5、base64、sha256加密
import hashlib
import base64


def string_to_md5(string, length=32, case=False):
    '''
    md5加密函数
    :param string: 需要加密的字符串
    :param length: 默认加密长度32位,也可以是16位
    :param case: 默认小写
    :return: 默认返回小写加密结果
    '''
    md5 = hashlib.md5()
    md5.update(str(string).encode('utf-8'))
    if length == 16:
        if case:
            return md5.hexdigest()[8:-8].upper()
        return md5.hexdigest()[8:-8]
    else:
        if case:
            return md5.hexdigest().upper().upper()
        return md5.hexdigest()


print(string_to_md5(123456))


def string_to_b64encode(string):
    '''
    字符串转成base64
    :param string: 需要加密的字符串
    :return: 返回加密结果
    '''
    try:
        encode_str = base64.b64encode(str(string).encode('utf-8'))
        return encode_str.decode('utf-8')
    except:
        return ''


print(string_to_b64encode(123456))


def b64decode_to_string(string):
    '''
    base64格式转成字符串
    :param string: 需要加密的字符串
    :return: 返回加密结果
    '''
    try:
        decode_str = base64.b64decode(string)
        return decode_str.decode('utf-8')
    except:
        return ''


print(b64decode_to_string('MTIzNDU2'))


def string_to_sha256(string, case=False):
    '''
    sha256加密函数
    :param string: 需要加密的字符串
    :param case: 默认小写,
    :return: 默认返回小写加密结果
    '''
    sha256 = hashlib.sha256()
    sha256.update(str(string).encode('utf-8'))
    if case:
        return sha256.hexdigest().upper()
    return sha256.hexdigest()


print(string_to_sha256('123456'))
