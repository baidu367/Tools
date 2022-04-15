# -*- coding:utf-8 -*-
# Time : 2022/1/19 12:40
# FileName : logInfo.py
# Author : Gecko
# Description：自定义日志
import os
import logging
import traceback
import colorlog


class logger:
    def __init__(
            self, LOG_PATH="log", LOG_FILE='', prefix_name="log", LOG_INFO='_info.log', LOG_ERROR='_error.log',
            LOG_ENCODING='utf-8', is_debug_info=True
    ):
        """
        :param LOG_PATH:    日志目录名
        :param LOG_FILE:    日志文件夹
        :param prefix_name: 日志文件前缀名
        :param LOG_INFO:    info.log日志文件
        :param LOG_ERROR:   error.log日志文件
        :param LOG_ENCODING: 日志文件编码格式
        """
        if os.path.exists(os.path.join(LOG_PATH, LOG_FILE)):
            pass
        else:
            os.mkdir(os.path.join(LOG_PATH, LOG_FILE))
        self.prefix = prefix_name
        # 文件写入格式
        self.save_file_format = logging.Formatter(
            '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' '[%(levelname)s] : %(message)s'
        )
        # 终端输出格式并带有自定义颜色
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }
        self.format = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(threadName)s:%(thread)d]  [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s] ： %(message)s',
            log_colors=log_colors_config)
        self.info_logger = logging.getLogger("info")
        self.error_logger = logging.getLogger("error")
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(self.format)  # 设置屏幕上显示的格式
        # 指定文件位置文件名以及输出格式
        info_file_handler = logging.FileHandler(
            os.path.join(LOG_PATH, LOG_FILE, prefix_name + LOG_INFO), encoding=LOG_ENCODING
        )
        info_file_handler.setFormatter(self.save_file_format)
        self.info_logger.addHandler(info_file_handler)
        if is_debug_info:
            self.info_logger.addHandler(sh)  # 屏幕打印日志不需要可以注释掉
        error_file_handler = logging.FileHandler(
            os.path.join(LOG_PATH, LOG_FILE, prefix_name + LOG_ERROR), encoding=LOG_ENCODING
        )
        error_file_handler.setFormatter(self.save_file_format)
        self.error_logger.addHandler(error_file_handler)
        if is_debug_info:
            self.error_logger.addHandler(sh)  # 屏幕打印日志不需要可以注释掉
        # 指定日志的最低输出级别
        self.info_logger.setLevel(logging.DEBUG)
        self.error_logger.setLevel(logging.ERROR)

    def debug(self, types, msg, *args, **kwargs):
        msg = ''.join([types, '>' * 5, msg.replace('\n', '').replace('\r', '')])
        self.info_logger.debug(msg, *args, **kwargs)

    def info(self, types, msg, *args, **kwargs):
        msg = ''.join([types, '>' * 5, msg.replace('\n', '').replace('\r', '')])
        self.info_logger.info(msg, *args, **kwargs)

    def warning(self, types, msg, *args, **kwargs):
        msg = ''.join([types, '>' * 5, msg.replace('\n', '').replace('\r', '')])
        self.info_logger.warning(msg, *args, **kwargs)

    def error(self, types, msg, *args, **kwargs):
        msg = ''.join([types, '>' * 5, msg.replace('\n', '').replace('\r', '')])
        self.error_logger.error(msg, *args, **kwargs)


    def critical(self, types, msg, *args, **kwargs):
        msg = ''.join([types, '>' * 5, msg.replace('\n', '').replace('\r', '')])
        self.error_logger.critical(msg, *args, **kwargs)


if __name__ == '__main__':
    project_path = os.path.dirname(os.path.abspath(__file__))
    LOG_PATH = os.path.join(project_path, 'log')
    prefix_name = 'phone'
    LOG_INFO = '_info.log'
    LOG_ERROR = '_error.log'
    log = logger(prefix_name=prefix_name, LOG_PATH=LOG_PATH, LOG_INFO=LOG_INFO, LOG_ERROR=LOG_ERROR)
    log.debug('调试信息', '调试')
    log.info('打印信息', '打印')
    log.warning('警告信息', '警告')
    log.error('错误信息', '错误')
    log.critical('危及错误', '危及')
    try:
        a = 0
        b = '1'
        c = a + b
    except Exception as e:
        log.error(str(e), traceback.format_exc())
