# -*- coding: utf-8 -*-
# 有关list（列表）的例子，list有序，但是可修改

li = ["a","b","third","z","s"]
print li
print li[0]
print li[4]
print li[-1] # -1表示最后一个
print li[-3] # -表示倒数几个

print len(li) # len表示list的长度

#slice示例
print li[1:3] #表示从第一个开始到第三个终止，不包含第三个 （1，2），返回的还是一个list
print li[1:-1] #表示从第一个开始到第最后一个终止，不包含最后一个 （1，2，3）（例子中共5个），返回的还是一个list
print li[:] #包含所有的li元素的一个 新的list