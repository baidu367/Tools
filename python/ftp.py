# -*- coding:utf-8 -*-
# Time : 2022/1/19 12:40 
# FileName : ftp.py
# Author : Gecko
# Description：ftp上传、下载文件
import os
import io
import sys
import time
from ftplib import FTP
from loguru import logger as log


class Ftp_file(FTP):
    def __init__(self):
        super(Ftp_file, self).__init__()
        self.encoding = 'utf-8'  # 编码格式
        self.set_debuglevel(2)  # 是否开启调试模式
        self.buffer_size = 1024 * 1000  # 根据实际带宽进行设置
        self.host = '127.0.0.1'  # 服务器IP地址
        self.port = 21  # 服务器端口号
        self.username = '*'  # 用户名
        self.password = '*'  # 用户密码
        self.basepathfile = '存放根路径'  # 文件存放根路径

    def Connect(self):
        # 连接ftp服务器跳转到指定目标
        self.connect(self.host, self.port)
        self.login(self.username, self.password)
        self.cwd(self.basepathfile)

    def pull_file(self, write_path, path, filename):
        '''
        FTP下载文件
        :param write_path: 本地保存路径
        :param path: 远程服务器路径
        :param filename: 文件名
        :return:
        '''
        start_time = time.time()
        log.info(f'拉取FTP文件:{filename}')
        with open(write_path, "wb") as f:
            if (sys.platform).count('win'):
                ftp_file = os.path.join(self.basepathfile, path).replace('\\', '/')
            else:
                ftp_file = os.path.join(self.basepathfile, path)
            log.info(f'服务器文件存放地址:{ftp_file}')
            self.retrbinary('RETR %s' % ftp_file, f.write, blocksize=self.buffer_size)
        end_time = time.time()
        log.info(f'拉取FTP文件:{filename}，耗时:{end_time - start_time}')

    def push_file(self, save_filepath, save_filename, content):
        '''
        FTP上传文件
        :param save_filename: 服务器要保存的文件名
        :param save_filepath: 服务器保存的地址
        :param content: 文件二进制流
        '''
        # 上传文件到ftp服务器
        self.cwd(self.basepathfile)
        log.info('[FTP]文件存储路径: ' + save_filepath)
        self.cwd(save_filepath)
        if save_filename not in self.nlst():
            self.storbinary('STOR  %s' % save_filename, io.BytesIO(content))

    def __del__(self):
        self.quit()


if __name__ == '__main__':
    ftp = Ftp_file()
    ftp.Connect()

    path = 'db/0d/db0d9d34a229dbe55702c75ad7177aa0.apk'
    filepath, filename = os.path.split(path)
    write_path = filename
    ftp.pull_file(write_path, path, filename)  # 下载文件

    with open('db0d9d34a229dbe55702c75ad7177aa0.apk', 'rb') as file:
        save_filename = 'db0d9d34a229dbe55702c75ad7177aa0.apk'
        save_filepath = '/home/ftp'
        ftp.push_file(save_filepath, save_filename, file.read())  # 上传文件
