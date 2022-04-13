# -*- coding:utf-8 -*-
# Time : 2021/3/3 14:08 
# FileName : miyisenlin.py
# Author : Gecko
# Description：蚂蚁森林物理工具
import uiautomator2 as u2
import time
import random


def collectEnergy(cnt):
    print("开始第%d次偷能量！" % cnt)
    # 开始扫描点击有能力出现的区域
    for x in range(150, 1300, 150):
        for y in range(600, 1000, 150):
            drvice.long_click(x + random.randint(10, 20), y + random.randint(10, 20), 0.1)
            time.sleep(0.01)
            if cnt != 1:
                drvice.click(536, 1816)

def start_task():
    cnt = 1
    while True:
        collectEnergy(cnt)
        a = drvice.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds
        drvice.click(0.858, 0.678)  # 找能量按钮的坐标
        ## 如果页面出现了“返回我的森林”说明已经没有能量可偷了，结束
        if drvice.xpath('//*[@text="返回我的森林"]').click_exists(timeout=2.0):
            break
        cnt += 1
    print("###结束###")
    drvice.app_stop("com.eg.android.AlipayGphone")  # 退出支付宝


if __name__ == '__main__':
    # drvice = u2.connect()  # 有线连接，手机需要插电脑上
    drvice = u2.connect("192.168.12.173")  # 通过无线连接，电脑和手机需要在同一个局域网内，并且需要先用有线的方式做过初始化
    drvice.app_stop("com.eg.android.AlipayGphone")
    print("打开支付宝")
    drvice.app_start("com.eg.android.AlipayGphone")
    time.sleep(2)  ## 休眠2s等待支付宝完全启动
    print("打开蚂蚁森林，等待5s……")
    drvice(text="蚂蚁森林").click()
    time.sleep(5)
    start_task()
