# -*- coding: utf-8 -*-

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_03_定义类 defining class——————————————————————————————————————————————
"""

class Loaf:
    pass

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_04_逐步讲解 定义fileinfo类——————————————————————————————————————————————
"""

from UserDict import UserDict
class FileInfo(UserDict):
    pass

"""
|Pyhton中的类继承的原型类被直接列在类名后边的小括号内
-|因此本例中FileInfo类继承自UserDict类（从UserDict模块中导入的）

|Python支持多重类继承，在类名后边的小括号内你可以用逗号隔开的方式列出多个原型类用来继承
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_05_初始化和编码类 Initianlizing and coding classes——————————————————————————————————————————————
"""
"""
以下的列子展示了使用__init__方法初始化FileInfo类
"""


class FileInfo(UserDict):
    "store file metadata"
    def __init__(self,filename=None):
        pass

"""
|类也可以（且应该）有doc strings

|每个类下面方法（包括__init__）的第一个参数总是表示当前类实例的引用，通常都命名为self。

|在__init__中，self指向新创建的对象

|在别的类方法中，它指向方法被调用的类的示例。在定义方法的时候你需要明确指定self，但是在调用方法时，不需要指定，Pyhthon会替你自动加上

|__init__可以接受任意数目的参数，和函数类似，参数可以使用缺省值定义。

|习惯上，任何Python类方法的第一个参数（对当前实例的引用）都叫做self，但是self在Python中并不是一个保留字，他只是一个命名习惯。
-|话虽如此，不过请保持好这个习惯。
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_06_编写FileInfo类 coding the FileInfo class——————————————————————————————————————————————
"""

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self,filename=None):
        UserDict.__init__(self)
        self["name"] = filename

"""
|__init__方法不返回值
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_06扩展_总结如何使用self和__init__——————————————————————————————————————————————
"""

"""
|当定义自己的类方法时，必须明确将self作为每个方法的第一个参数列出，包括__init__

|当从你的类中调用一个父类的方法时，必须包括self参数

|当你从类的外部调用你的类的方法的时候，你不必对self参数指定任何值，你可以完全将其忽略，Python会自动替你增加实例的引用

|这些特性看上去有点矛盾，实际不是！看上去这么矛盾是因为依赖一种还没有了解的区别（绑定和解绑方法）
"""

"""
|__init__方法是可选的，但是一旦你定义了，就记得必须显示的调用父类的__init__方法（如果父类定义了__init__的话）。
-|总的来说就是：子类在任何时候想扩展父类的行为，都要在适当的时机，使用适当的参数，显示的调用父类的方法
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_07类的实例化 instantiating class——————————————————————————————————————————————
"""

import example5_1_fileinfo
f = example5_1_fileinfo.FileInfo("C:/Users/Public/Music/Sample Music/sleep away.mp3")
print f.__class__
print type(f.__class__)
print f.__doc__
print f