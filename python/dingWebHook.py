# -*- coding:utf-8 -*-
# Time : 2021/9/14 15:39 
# FileName : dingWebHook.py
# Author : Gecko
# Description：钉钉群机器人消息发送
import time
import hmac
import json
import hashlib
import base64
import requests
import urllib.parse
from requests.adapters import HTTPAdapter


def timestamp_sign(secret):
    '''
    获取接口参数
    :param secret: 加签密钥
    :return: 请求参数
    '''
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


def send_message(access_token, secret, message):
    '''
    发送钉钉消息
    :param access_token: 用户token
    :param timestamp: 请求参数
    :param sign: 请求参数
    :param message: 发送消息
    :return: None
    '''
    text = '你的任务已经完成，请查看任务信息如下:'
    timestamp, sign = timestamp_sign(secret)
    for key, value in message.items():
        text += '  \n <font color=#0000FF>{}</font>：<font color=#FF0000>{}</font>  \n  '.format(key, value)
    url = 'https://oapi.dingtalk.com/robot/send'
    params = {
        'access_token': access_token,
        'timestamp': timestamp,
        'sign': sign,
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        "Content-Type": "application/json ;charset=utf-8"
    }

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "业务信息提醒",
            "text": text
        }
    }
    try:
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=3))
        response = requests.post(url, data=json.dumps(data), params=params, headers=headers, timeout=20)
        result = response.json()
        if result['errcode'] == 0:
            print('消息发送成功')
        else:
            print(result)
            print('消息发送失败：', result['errmsg'])
    except Exception as e:
        print('消息发送失败：', e)


if __name__ == '__main__':
    secret = '*'
    access_token = '*'
    content = {
        'Type': 'info',
        'Start_time': '2050-01-01',
        'End_time': '2050-01-01',
        'run_time': '',
        'Task': 'XXXX数据采集',
        'Num': 500,
        'Executor': '小钉'
    }
    send_message(access_token, secret, content)
