# -*- coding: utf-8 -*-
# 使用 type、str、dir 和其它内置函数
from example4_1_introspection import info
import odbchelper,types
import __builtin__
import string
print """
———————————————————————————————————————#4_05_type函数——————————————————————————————————————————————
"""

print type(1)
li =[]
print type(li)
print type([])
print type(odbchelper)
print type(types)
print type(odbchelper)==types.ModuleType

"""
|type函数返回数据类型
-|整型，字符串，列表，字典，元祖，函数，类，模块，甚至是类型对象都可以作为参数被type函数接受
"""


#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_06_str函数——————————————————————————————————————————————
"""
# str强制将数据类型转换为字符串，每种数据类型都可以强制转换为字符串

one = str(1)
print one
print type(one)

horseman = ['war', 'pestilence','famine']
horseman.append('powerbuilder')
print horseman
str(horseman)
print type(horseman)

print odbchelper
print type(odbchelper)
cc = str(odbchelper)
print cc
print type(cc)

print str(None)
print type(None)
two = str(None)
print two
print type(two)


#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_07_dir函数——————————————————————————————————————————————
"""
# dir返回任意对象的属性和方法列表，包括
"""
dir returns a list of the attributes and methods of any object:
modules, functions, strings, lists, dictionaries... pretty much anything
"""

li =[]
print dir(li)
d= {}
print dir(d)
print dir(odbchelper)

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_08_callable 函数——————————————————————————————————————————————
"""
# callable接收任何对象最为参数，如果参数对象是可调用的则返回True，否则返回False
# 可调用的对象包括：函数、类方法，甚至是类本身

print string.punctuation
print string.join
print callable(string.punctuation)
print callable(string.join)
print string.join.__doc__

"""
|string 模块中的函数现在已经不赞成使用了（尽管很多人现在仍然还在使用join函数）
-|这个模块中包含许多有用的变量，如：punctuation，这个字符串包含了所有标准的标点符号字符。

|任何可调用的对象都可能会含有一个doc srting
-|通过将callable函数作用于一个对象的每个属性，可以确定哪些属性（方法、函数、类）是你要关注的
-|哪些是你可以忽略的（例如常量等等）
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_09_内置函数 built in函数——————————————————————————————————————————————
"""
# bulit-in functions 内置函数

""" type、str、dir等其它Python内置函数都归组到__builtin__这个特殊的模块中"""

print info(__builtin__)