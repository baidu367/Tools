# -*- coding:utf-8 -*-
# Time : 2022/5/7 16:56 
# FileName : callExecjs.py
# Author : Gecko
# Description：python调用js方法
import execjs


def getParamsValue(args, filename):
    jsstr = get_js(filename)
    ctx = execjs.compile(jsstr)  # 加载JS文件
    return ctx.call('调用的函数名称', args)  # 调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数


def get_js(filename):
    htmlstr = ''
    with open(filename, 'r') as file:  # 打开JS文件
        line = file.readline()
        while line:
            htmlstr = htmlstr + line
            line = file.readline()
    return htmlstr


if __name__ == '__main__':
    print(getParamsValue('参数', 'js文件名'))
