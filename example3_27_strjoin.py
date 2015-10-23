# -*- coding: utf-8 -*-
# join方法连接list中的字符串

# ——————————————————————————————————————————————————————————buildConnectionString中list解析
"""#3_27"""
print """
———————————————————————————————————————#3_27_连接list为字符串 之 join——————————————————————————————————————————————
"""

""" 函数原文 return ";".join(["%s=%s" % (k, v) for k, v in params.items()]) """

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print params.items()

# print [(k,v) for k, v in params.items()]

# print "%s=%s"%(k,v)
print ["%s=%s" % (k, v) for k, v in params.items()]
li0 = ";".join(["%s=%s" % (k, v) for k, v in params.items()])
print li0

"""
|Python中函数是对象，字符串是对象...每个东西都是对象，不过没说字符串值是对象，实际不是这么个意思

|这里字符串";"就是一个对象，我们调用了它的join方法
-|这里join方法将list中的元素连接成单个字符串，每个元素用一个分号隔开
-|分号可以替换成任意字符串作为分隔符
"""

li3 = ["a","b","c"]
li5 = ["a","b",1]
li4j = "+".join(li3)
# li6j = "+".join(li5) 会报错
print li4j
# print li6j 会报错

"""
join只能作用于元素是字符串的list，不能进行强制类型转换，否则会报错
"""


# ——————————————————————————————————————————————————————————buildConnectionString中list解析
"""#3_28"""
print """
———————————————————————————————————————#3_28_分割字符串为list 之 split——————————————————————————————————————————————
"""

li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print s
print s.split(";")
print s
print s.split(";",1)

"""
|split(string[,int])--第二个可选参数表示分割的次数
"""


