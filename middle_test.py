# -*- coding: utf-8 -*-

# 测试doc_string，所有的函数都有这个内置的属性
import odbchelper
import sys


params = {"server": "mpilgrimtest", "database": "mastertest", "uid": "satest", "pwd": "secrettest"}
print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__

# _________________________ 测试内置模块sys的路径和sys，模块可以通过append来增加到路径中

print sys.path
print sys

# _________________________ 测试模块对象的__name__属性，如果是通过import导入的模块，则__name__属性值就是模块名

print odbchelper.__name__
print __name__ # 在非import运行，则__name__属性的值就是__name__