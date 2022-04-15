# -*- coding:utf-8 -*-
# Time : 2022/4/15 15:14 
# FileName : stringJsonToDict.py
# Author : Gecko
# Description：字符串格式json转换成python字典
import json
import ast

string = '''{"name":'Tom','sex': "男",
"age": 18,"addr": "北京",
}'''


def stingJson_to_dict(string):
    """
    字符串格式json数据转换成python字典
    :param string: Json形式的不规则字符串
    :return:
    """
    try:
        dict_data = json.loads(string, strict=False)
    except json.decoder.JSONDecodeError:
        try:
            dict_data = eval(string)
        except:
            try:
                dict_data = ast.literal_eval(string)
            except:
                dict_data = ''
    return dict_data


print(stingJson_to_dict(string))  # {'name': 'tom', 'sex': '男', 'age': 18, 'addr': '北京'}
