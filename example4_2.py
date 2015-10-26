# -*- coding: utf-8 -*-

import odbchelper
from example4_1_introspection import info

li=[]
print info(li)


print """
———————————————————————————————————————#4_02_可选参数和命名参数 optional and named arguments——————————————————————————————————————————————
"""

"""
spacing和collapse就是可选参数，定义了缺省值
object是必备参数，没有指定缺省值

通过使用named arguments(命名参数)，参数在写入的顺序就可以自由指定了

"""

print info(odbchelper)
print info(odbchelper,12)
print info(odbchelper,collapse=0)
print info(spacing=15,object=odbchelper)