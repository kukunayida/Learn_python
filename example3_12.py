# -*- coding: utf-8 -*-
#用来测试list中的搜索操作

li =['a', 'b', 'c', 'dds', 'e', 'f', ['g', 'h'], 'strtype']

print li.index("b")
print "a" in li
print "le" in li
#print li.index("el")

"""
index方法返回元素在list的索引号,如果index方法中的元素没有在list中，则返回错误
in方法判断元素是否在list中，返回的是一个布尔值，注意大小写，布尔中的真假需要首字母大写

0,为False
空字符串(""),为False
空列表list([]),为False
空元祖tuple(()),为False
空字典dictionary({}),为False
"""

# ——————————————————————————————————————

#用来测试list中的删除操作
"""#3_13"""
print """
———————————————————————————————————————#3_13——————————————————————————————————————————————
"""
print li
print li.remove("a") #和extend类似，remove方法也是原地操作
print li
#li.remove("wu")
print li.pop() #pop删除list中的最后一个元素，且返回被删除的元素，所以print不会报错
print li
"""
remove也是原地操作，和extend类似
remove一个没有的元素也会直接报错，和index方法类似
pop会删除list中的最后一个元素，且！返回被删除的元素，所以print不会报错~
"""



# ——————————————————————————————————————

#用来测试list中的运算符操作
"""#3_14"""
print """
———————————————————————————————————————#3_14_list的运算符操作——————————————————————————————————————————————
"""
li1 = ["a","b"]
li2 = ["a2","b2"]
print li1;print li2
li3 = li1 + li2
print li3
li3 += ["a3"]
print li3
print li1*3
li3 += "347"
print li3
"""
+运算符和extend方法类似，也是合并两个list，不过+会返回新合成的list，extend只原地操作
+=等同于extend方法，直接print会报错，别的貌似一样
*方法可以看作是一个重复器，li*3 相当于 li+li+li
"""

litest = [22,33] #用来测试非字符作为list的元素
print litest