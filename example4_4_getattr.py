# -*- coding: utf-8 -*-
li = ['larry','curly']
# print li.pop() 会输出curly
print li.pop
print getattr(li,"pop")
print getattr(li,"append")
print getattr(li,"append")('Moe')
print li
print getattr({}, "clear")
#print getattr((), "len") #会报错，getattr理论上可以作用于元组，不过由于元组没什么方法，所以指定了属性就会产生异常

"""
|getattr返回的是方法,因此getattr(li,"append")('Moe')这种写法才可以完成
-|getattr(li,"append")('Moe')返回方法，类似于直接使用li.append("Moe")
-|getattr(li,"pop")---这条语句获取列表的pop方法的引用，需要注意的是这条语句并不是调用pop方法，调用的写法是list.pop()

"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_11_getattr 作用于模块——————————————————————————————————————————————
"""

import odbchelper
print odbchelper.buildConnectionString
print getattr(odbchelper,"buildConnectionString")
object = odbchelper
method = "buildConnectionString"
print getattr(object,method)
print type(getattr(object,method))
import types
print type(getattr(object,method))== types.FunctionType
print callable(getattr(object,method))
"""
|0x00之类的是十六进制地址(内存地址空间)，各个机器不同
-|相关阅读：http://www.cnblogs.com/liuzhendong/archive/2011/10/17/2215632.html

|如果getattr如果引用的是模块，那么参数可以使函数、类或者全局变量等
"""
