# -*- coding: utf-8 -*-
# dictionary(字典)无序，键值对 这里的值可以是任意数据类型：

d = {"server":"mpilgrim", "database":"master"}
print d
print d["server"]
print d["database"]
# print d["mpilgrim"] 报错

d["database"] = "free"
print d["database"]

d["uid"] = "sa"
print d["uid"]
print d

# del可以删除单独元素，clear清空dictionary
del d["uid"]
print d
print "——————————1"
print d.copy() #字典有copy方法
print type(d.copy())
print "——————————2"
print d.clear()
print type(d.clear())
print d
