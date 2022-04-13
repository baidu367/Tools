# -*- coding:utf-8 -*-
# Time : 2022/1/4 16:31 
# FileName : mongoEngine.py
# Author : Gecko
# Description：mongoengine操作方法
from mongoengine import connect, disconnect
from mongoengine.queryset.visitor import Q
from mongoengine import Document, StringField,  EmbeddedDocument, DateTimeField, ListField, EmbeddedDocumentField, IntField
import datetime


# 字段
# StringField 字符串
# URLField Url
# EmailField 邮箱地址字段
# Intfield 32位整数
# LongField 64位整数
# FloatField 浮点数字段
# DecimalField 定点十进制
# BooleanField 布尔
# DateTimeField 时间
# ComplexDateTimeField 精确毫秒级时间
# EmbeddedDocumentField 嵌入式文档，有声明的document_type
# GenericEmbeddedDocumentField 通用嵌入式文档
# DynamicField 动态字段类型
# ListField 列表字段
# EmbeddedDocumentListField 嵌入式有文件的List字段
# SortedListField 排序的列表字段，确保始终检索为已排序的列表
# DictField 字典
# MapField 名称映射到指定字段
# ReferenceField 文档引用
# LazyReferenceField
# GenericReferenceField
# BinaryField 二进制数据字段
# FileField GirdFS存储字段
# ImageField 图像文件存储字段
# SequenceField
# ObjectIdField
# UUIDField
# GridFSProxy
# ImageGridFsProxy
# ImproperlyConfigured
mongodbinfo = {
    'host': '127.0.0.1',
    'port': 27017,
    'username': '',
    'password': '',
    'db': 'xxxx',
}
class Task_project(EmbeddedDocument):  # 嵌入式文档类型
    taskId = StringField(required=True)
    shopName = StringField(required=True)
    startTime = DateTimeField(default=datetime.datetime.utcnow)
    endTime = DateTimeField(default=None)
    count = IntField(default=0)
    status = StringField(required=True)

class Shop_project(Document):  # 文档类型
    shopName = StringField(required=True)
    shopCommand = StringField(required=True)
    scriptName = StringField(default=None)
    taskTresults = ListField(EmbeddedDocumentField(Task_project))

# 连接数据库
connect(**mongodbinfo)

##################################################查询###################################################################
# 查询所有数据， 返回所有文档， 是列表由object对象组成。
Shop_project.objects.all()

# 查询第一个文档， 是一个object对象
Shop_project.objects.first()

# 查询条件，用关键字参数传进去，返回object对象组成的列表，若不存在返回空列表。
Shop_project.objects.filter(shopName='XX应用商店')

# 查询条件，用关键字参数传进去，返回object对象组成的列表，查询满足条件的第一条数据。
Shop_project.objects.filter(shopName='XX应用商店').first()

# 字符串查询 objects(字段__操作符=查询条件)
# 注意：字段后是2个下划线
# 操作符：
# exact 完全匹配
# iexact 完全匹配（忽略大小写）
# contains 包含该值
# icontains 包含该值（忽略大小写）
# startswith 以该字符串开始
# istartswith 以该字符串开始（忽略大小写）
# endswith 以该字符串结束
# iendswith 以该字符串结束（忽略大小写）
# ne 不等于
# gt(e) 大于(等于)
# lt(e) 小于(等于)
# not 对操作符取反，比如 age__not__gt=18
# in 后面是一个列表，比如 name__in=["林冲"，"令狐冲"],找出这两个人的数据，满足一条也可以，若都不存在，返回空列表。
# nin in的取反
# mod 取模，比如 age__mod=(2,0) 表示查询出age除以2，余数是0的数据。
Shop_project.objects(shopName__contains='商店')

# 多条件查询或者关系,使用Q，结合 "&" "|" 实现, 一个 Q 类，代表一个查询条件。 objects(Q() & Q())
Shop_project.objects(Q(shopName__contains='商店') | Q(scriptName__contains='xiaomi'))

# 查询的时候排序。 .order_by("+/-字段名") 正负号，代表升降序。
Shop_project.objects.all().order_by('-shopName')
##################################################修改###################################################################
# 修改写法：update(操作符__字段=设置的值)、update_one(操作符__字段=设置的值), 返回修改数量
# 注意：操作符后是2个下划线
#操作符：
# set 设置指定的值
# unset 删除指定的值,可以直接删键
# inc 自增一个指定的值
# dec 自减一个指定的值
# push 在 list 中， 添加一个值
# push_all 在 list 中， 添加多个值,多个值写成列表的形式。
# pull 与push相反。
# pull_all 与push_all相反。
# add_to_set 当要添加的值存在，则忽略，不存在，则添加。
Shop_project.objects(shopName='XX应用商店').update(set__scriptName='huawei_kw')
##################################################删除###################################################################
Shop_project.objects(shopName='XX应用商店').delete()
##################################################新增###################################################################
shopinfo = {"shopName": "XX应用商店", "shopCommand": "XXXX_cate", "scriptName": "XXXX_cate.py"}
Shop_project(**shopinfo).save()
##################################################特殊方法################################################################
# 表名.objects.count()
# 计数。
# 表名.objects.sum("字段名")
# 求和。
# 表名.objects.average("字段名")
# 求平均数。
# 表名.objects.item_frequencies("字段名")
# 返回的是一个字典，key是字段名，value是该字段出现的次数。
# 参数 normalize:若为True, value将会是小数，所有字段的value相加为1.
# 表名.objects.aggregate()
# 第一种写法：
# a = { 管道1：{ 表达式1 } }, { 管道2：{ 表达式2 } }
# 表名.objects.aggregate(*a)
# 注意 多个管道的时候， a前面要加个星号。
# 第二张写法：
# 表名.objects.aggregate({},{},{}...)
# 直接用花括号的形式写，中间用逗号分隔。
# 表名.objects.distinct("字段名")
# 返回一个列表，该字段名的值（不重复的）组成的一个列表。

# # 关闭数据库
disconnect()

