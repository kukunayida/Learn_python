# -*- coding: utf-8 -*-
# 用来测试append和insert和extend等list操作
li = ["a","b","third","z","s"]

li.append("new")
print li #尾部追加元素 append ，注意是单个

li.insert(2,"new2")
print li #定位插入insert

li2 = ["one","two"]
li.extend(li2) # extend合并列表
print li