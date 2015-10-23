# -*- coding: utf-8 -*-
# 映射list

li = [1,9,8,4]
print [elem*2 for elem in li]
print li
li = [elem*2 for elem in li]
print li


# ——————————————————————————————————————————————————————————映射list在 ["%s=%s" % (k, v) for k, v in params.items()] 解释
"""#3_25
["%s=%s" % (k, v) for k, v in params.items()]
"""
print """
———————————————————————————————————————#3_25_映射list在之前odbchelper中buildConnectionString函数的具体解释——————————————————————————————————————————————
"""

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
paramstest = {"server":"mpilgrim", "database":"master", "uid":"sa", (1,2):{"t1","t2"}}
print params.keys()
print params.values()
print params.items()

print paramstest
print paramstest.items()
"""
|key返回一个list,list的元素是dictionary的key

|values返回一个list，list的元素是dictionary有的value

|dictionary的item函数，返回一个list，这个list的每个元素是dictionary的键值对组成的一个个tuple  (这里测试得到一个set(集合)之前没说，可能之后会说到)
"""
# params.values()[n]= params[params.keys()[n]]
"""
函数本体
def buildConnectionString(params):
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])
"""

# ——————————————————————————————————————————————————————————buildConnectionString中list解析
"""#3_26"""
print """
———————————————————————————————————————#3_26_buildConnectionString中list解析——————————————————————————————————————————————
"""

print params.items()
print [k for k,v in params.items()]
print [v for k,v in params.items()]
print k
print v
print ["%s=%s"%(k, v) for k, v in params.items()]

"""
|k,v in params.items()---多变量赋值，可写成(k,v) in params.items()--见ex3_17

|多变量赋值循环，然后通过映射得到新的list，映射规则是字符格式化
"""