# -*- coding:utf-8 -*-
# Time : 2022/6/7 10:42 
# FileName : dictToClass.py
# Author : Gecko
# Description：将字典转换成类，通过类直接调用属性(元素)
from collections import namedtuple

dic = {"name": "tom", "age": 20, "sex": "男"}


# 方法一

class DictToClass:
    def __init__(self, obj):
        self.__dict__.update(obj)


test = DictToClass(dic)
print(test.name)
print(test.age)
print(test.sex)

# 方法二

test = namedtuple("obj", dic.keys())(*dic.values())
print(test.name)
print(test.age)
print(test.sex)
