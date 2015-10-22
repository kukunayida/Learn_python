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
# adf