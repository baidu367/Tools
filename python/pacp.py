#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Time : 2021/4/28 10:35 
# FileName : pacp.py
# Description：分析pacp包请求内容
import pyshark
import re


cap = pyshark.FileCapture('$I077GEV.pcap', use_json=True, include_raw=True)
count = 0
for pack in cap:
    pack = str(pack.get_raw_packet())
    if 'Host' in pack:
        host = re.findall(r'Host: (.*?)\\r\\n', pack)
        url = re.findall(r'[GET|POST] (.*?)\\r\\n', pack)
        host = host[0] if host else ''
        url = url[0] if url else ''
        print('[*]应用请求域名：', host)
        print('应用请求路径：', url)
cap.close()













