# -*- coding:utf-8 -*-
# Time : 2021/9/22 9:00 
# FileName : gapCalculation.py
# Author : Gecko
# Description：验证码图片缺口计算
import cv2
import numpy as np

# def identify_gap(bg, tp, out):
#     '''
#     bg: 背景图片
#     tp: 缺口图片
#     out:输出图片
#     '''
#     # 读取背景图片和缺口图片
#     bg_img = cv2.imread(bg)  # 背景图片
#     tp_img = cv2.imread(tp)  # 缺口图片
#
#     # 识别图片边缘
#     bg_edge = cv2.Canny(bg_img, 100, 200)
#     tp_edge = cv2.Canny(tp_img, 100, 200)
#
#     # 转换图片格式
#     bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
#     tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
#
#     # 缺口匹配
#     res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
#
#     # 绘制方框
#     th, tw = tp_pic.shape[:2]
#     tl = max_loc  # 左上角点的坐标
#     br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
#     cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
#     cv2.imwrite(out, bg_img)  # 保存在本地
#
#     # 返回缺口的X坐标
#     return tl[0]
#
# if __name__ == '__main__':
#     bg = 'imageToSave2.png'
#     tp = 'imageToSave1.png'
#     out = 'imageToSave3.png'
#     result = identify_gap(bg, tp, out)
#     print(result)


import cv2
import numpy as np


def show(name):
    cv2.imshow('Show', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main(otemp, oblk):
    # otemp = 'imageToSave1.png'
    # oblk = 'imageToSave2.png'
    target = cv2.imread(otemp, 0)
    template = cv2.imread(oblk, 0)
    w, h = target.shape[::-1]
    temp = 'temp.jpg'
    targ = 'targ.jpg'
    cv2.imwrite(temp, template)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = abs(255 - target)
    cv2.imwrite(targ, target)
    target = cv2.imread(targ)
    template = cv2.imread(temp)
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    # 展示圈出来的区域
    cv2.rectangle(template, (y, x), (y + w, x + h), (7, 249, 151), 2)
    show(template)
    return x


if __name__ == '__main__':
    main()

