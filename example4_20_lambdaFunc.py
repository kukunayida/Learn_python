# -*- coding: utf-8 -*-
#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_20_lambda函数——————————————————————————————————————————————
"""

def f(x):
    return x*2

print f(2)

g = lambda x:x*2
print g(3)

print (lambda x:x*2)(1)

"""
|lambda函数是一个内联函数（in−line function）
-|在参数列表周围没有括号--lambda x
-|忽略了return关键字---:x*2  （隐含的存在，因为整个函数只有一行）
-|函数没有函数名，但是可以将它赋值给一个变量进行调用

|lambda函数可以接受任意多个参数（包括可选参数）
-|返回一个简单表达式的值
-|lambda函数不能包含命令，包含的表达式不能超过一个。
-|如果你需要更复杂的功能，请定义一个常规的函数

|lambda函数是一种表现形式，而不是说非使用不可
-|任何使用到lambda函数的地方都可以使用常规函数来完成同样的工作
-|lambda常常被用于封装特殊的、非重用代码上，避免代码充斥着大量单行函数
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_21_lambda函数在实际场景中的运用——————————————————————————————————————————————
"""

"""
def info(object,spacing = 10,collapse =1):
    ""print methods and doc strings.
        Takes module,class,list,dictionary,or string.""
    methodList = [method for method in dir(object) if callable(getattr(object,method))]
>>>>processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object,method).__doc__)))
                     for method in methodList])
if __name__ == "__main__":
    print info.__doc__
"""

