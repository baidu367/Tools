# -*- coding:utf-8 -*-
# Time : 2021/12/28 9:36 
# FileName : scp.py
# Author : Gecko
# Description：scp上传文件
import os
import paramiko
from scp import SCPClient


def upload_scp(local_path, local_filename, remote_path):
    '''
    将指定目录的文件上传到服务器指定目录
    :param local_path: 本地文件夹路径
    :param local_filename: 本地文件夹路径下面的文件名称
    :param remote_path: 远程服务器目录
    :return:
    '''
    host = "***.***.***.***"  # 服务器ip地址
    port = 22  # 端口号
    username = "****"  # ssh 用户名
    password = "****"  # 密码

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
    local_path = os.path.join(local_path, local_filename)
    try:
        scpclient.put(local_path, remote_path)
    except FileNotFoundError as e:
        print(e)
        print("系统找不到指定文件" + local_path)
    else:
        print("文件上传成功")
    ssh_client.close()
