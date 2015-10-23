# -*- coding: utf-8 -*-

# 一些关于tuple的内容
"""
tuple是不可变的list，一旦创建了tuple就不能以任何方式改变它
"""


t = ("a","b","c","d","e","f")
print t

#t.append("new")
#print t
print "a" in t


"""
| tuple没有类似list的append，remove，index等方法，但是有in这个方法

| tuple可以通过一个特殊的函数转变为list

| tuple可以用作dictionary的key，但是list不可以，实际更复杂
| dictionary的key必须是不可变的，如果tuple的元素含有可变的list的话，此时作为key就是不行的，所以作为key的要求总结如下：
  只有字符串、整数或其它对dictionary安全的tuple才可以用作dictionary key.

| tuple接收一个list，返回一个tuple
  listj接收一个tuple，返回一个list
"""