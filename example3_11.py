# -*- coding: utf-8 -*-
li = ["a","b","c","d"]

li.extend(["e","f"])
print li;print len(li)

li.append(["g","h"])
print li;print len(li)

st = "stringtype"
li.append(st)
print li
print li.append(2)
"""
extend衔接的永远是一个list（列表），而append衔接的不一定是一个列表,两者都是原地操作，直接读取返回值的话的都是none.
"""