# -*- coding: utf-8 -*-
"""
def info(object,spacing = 10,collapse =1):
    ""print methods and doc strings.
        Takes module,class,list,dictionary,or string.""
    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object,method).__doc__)))
                     for method in methodList])
if __name__ == "__main__":
    print info.__doc__
"""

"""
print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object,method).__doc__)))
                     for method in methodList])

  print "\n".join(["%s %s" %( method.ljust(spacing),processFunc(str(getattr(object,method).__doc__)) ) for method in methodList])
"""

"""
| for method in methoList
-|遍历列表
"""



import odbchelper
object = odbchelper
method = 'buildConnectionString'
print getattr(object, method)
print getattr(object, method).__doc__
print type(getattr(object, method).__doc__)

"""
|由于可能有的函数没有__doc__，此时就会返回none，因此需要对getattr(object, method).__doc__使用str内置函数强制转换为字符串


"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_24_ljust方法——————————————————————————————————————————————
"""

s = 'bulidConnectionString'
print s.ljust(30)
print s.ljust(20)

"""
|ljust用空格填充字符串，以达到符合指定的长度
-|若设定的字符串长度小于字符串本身长度，则返回原始字符串
"""

