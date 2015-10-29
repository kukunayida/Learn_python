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

|在__init__中，self指向当前类的实例引用

|在别的类方法中，self它指向调用这个方法的实例引用。在定义方法的时候你需要明确指定self，但是在调用方法时，不需要指定，Pyhthon会替你自动加上

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
|子类里，必须显式的调用父类中合适的方法

|__init__方法不返回值
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_06扩展_总结如何使用self和__init__——————————————————————————————————————————————
"""

"""
|当定义自己的类的方法时，必须明确将self作为每个方法的第一个参数列出，包括__init__

|当从自定义的类里边调用父类的方法的时候，必须包括明确包含self参数

|当从外部调用自定义的类的方法的时候，你不必对self参数指定任何值，你可以完全将其忽略，Python会自动替你增加实例的引用

|这些特性看上去有点矛盾，实际不是！看上去这么矛盾是因为依赖一种还没有了解的区别（绑定和解绑方法）
"""

"""
|自定义类中的__init__方法是可选的，但是一旦你定义了，就记得必须显示的调用父类的__init__方法（如果父类定义了__init__方法的话）。
-|总的来说就是：子类在任何时候想扩展父类的行为，子类的方法必须要在适当的时机，使用适当的参数，显示的调用父类的方法
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_07类的实例化 instantiating class——————————————————————————————————————————————
"""

"""
在 Python 中对类进行实例化很直接。要对类进行实例化，只要调用类 (就好像它是一个函数)，传入定义在 __init__ 方法中的参数。返回值就是新创建的对象。
"""
import example5_1_fileinfo
f = example5_1_fileinfo.FileInfo("C:/Users/Public/Music/Sample Music/sleep away.mp3")
# g = example5_1_fileinfo.FileInfo("C:/Users/Public/Music/Sample Music/Kalimba.mp3")
print f.__class__
print f.__class__.__bases__
# print g.__class__
print type(f.__class__)
print f.__doc__
print f

"""
|f = example5_1_fileinfo.FileInfo("C:/Users/Public/Music/Sample Music/sleep away.mp3") ---这就是在创建一个FileInfo的实例

|每个类的实例都有一个内置的 属性,__class__，返回得到的就是那个实例类的对象

|类下边有方法，类似java之类可以使用方法获取一个对象的属性，python也行，不过Python中有些属性可以直接通过类似class.__class__获取对象（类也是对象）的属性

|在 Python 中，创建类的实例只要调用一个类，仿佛它是一个函数就行了。不像 C++ 或 Java 有一个明确的 new 操作符。
"""
"""
补充：http://stackoverflow.com/questions/12575484/class-inheritance-in-python
|类的实例没有__bases__属性，只有class有

"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_08垃圾回收  尝试实现内存泄漏——————————————————————————————————————————————
"""

def leakmem():
    g = example5_1_fileinfo.FileInfo('C:/Users/Public/Music/Sample Music/sleep away.mp3')
    print g

for i in range(2):
    leakmem()

"""
|Python有自己的垃圾回收机制，因此不会出现内存泄漏(轻易)，技术上叫“引用计数”
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_09封装类  UserDict： A Wrapper Class——————————————————————————————————————————————
"""

"""
class UserDict:
    def __init__(self,dict=None):
        self.data = {}
        if dict is not None:self.update(dict)
"""

"""
|UserDict是一个基类，不从任何其他类继承而来

| def __init__(self,divt=None): ---这部分就是原始的UserDict类的__inti__方法，在之前的fileInfo类中用新的__init__方法覆盖了这个原始方法

|注意到，父类中的参数列表和子类不同，这没什么问题。每个子类都可以有属于自己的一组参数，只需要在调用父类的时候给定正确的参数就行了。

|Python中支持数据属性（data attributes），（在Java和Powerbuilder中叫做“实例变量”，c++中叫做数据成员）
-|数据属性是一个（特定的）类实例拥有的数据。在本例中，每个UserDict实例将拥有一个data数据属性。
-|从外部代码引用这个属性的时候需要使用实例的名字限定，instance.data。限定的方法和之前使用模块名来限定函数一样
-|如果在内部引用一个数据属性，则用self表示当前类实例引用

|在这里父类有一个定义初始值的方法（通过在dict参数中传入一个字典），FileInfo中我们没用上
"""

"""
|update是字典的一个复制器（duplicator）

|
"""


#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_10封装类  UserDict下的常规方法——————————————————————————————————————————————
"""

def clear(self): self.data.clear()
def copy(self):
    if self.__class__ is UserDict:
        return UserDict(self.data)
    import copy
    return copy.copy(self)
def keys(self): return self.data.keys()
def items(self): return self.data.items()
def values(self): return self.data.values()

