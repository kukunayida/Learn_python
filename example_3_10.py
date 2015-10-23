# -*- coding: utf-8 -*-
# 用来测试append和insert和extend等list操作
li = ["a","b","third","z","s"]

li.append("new")
print li #尾部追加元素 append ，注意是单个

li.insert(2,"new2")
print li #定位插入insert , 也是单个元素 list中的元素可以重复，也就是说可以有两个new，

li2 = ["one","two"]
li.extend(li2) # extend合并列表
print li
print li.extend(["ff","de"])
li.extend("345")
print li
#li.extend(3.2)
#print li


"""
直接print li.extend()会返回none   还有别的一些方法也会这样例如sort()
extend方法是原地操作，但是不返回拓展后的列表
相关讨论
http://stackoverflow.com/questions/16641119/why-does-append-return-none-in-this-code

如果extend直接接一个非list类型的参数，则
字符串自动打散，每个字符作为元素
接非字符串，例如整数，等会报错，表示object is not iterable,推断出extend的参数需要是iterable(可迭代)类型的数据
python中序列是Sequence，Sequence is interable。如果一个对象是interable的，表示它可以被遍历。
相关讨论
http://www.douban.com/group/topic/23813448/
"""
