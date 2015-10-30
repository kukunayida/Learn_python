# -*- coding: utf-8 -*-

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_11 直接继承自内建数据类型 dict——————————————————————————————————————————————
"""

# class FileInfo(dict):
#     "sotre file metadata"
#     def __init__(self,filename=None):
#         self["name"] = filename
#
#
# f = FileInfo("C:/Users/Public/Music/Sample Music/sleep away.mp3")
# print f
# print f.__class__.__bases__

"""
|不需要导入UserDict模块，因为dict已经是可以使用的内建数据类型

|不是继承自UserDict.UserDict，而是直接继承自dict

|UserDict内部的工作方式要求你手工调用它的__init__方法正确初始化它的内部数据结构，不过dict不需要这样，它不是一个封装（warper）所以不需要明确的初始化
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#5_12 专有类方法之获取和设置数据项 special class method（get and set item）——————————————————————————————————————————————
special method和magic method是一个东西，魔法方法/专用方法/特殊方法
http://stackoverflow.com/questions/1090620/special-magic-methods-in-python
"""

"""
|除了普通的类方法可以定义，类海可以定义专有的方法

|专有方法是在特定条件或者特殊语法结构下，由Python替你调用的，而不像普通方法由你自己的通过代码调用

|正如之前介绍的那样，普通的方法对于在类里封装一个字典很有帮助（go a long way towards doing sth）
-|但是只有普通方法还是不够的，因为除了调用字典的方法，还有很多事字典可以做
-|例如：
  你可以使用一种语法来获取和设置数据项（item），即使这种语法并不包括明显的方法调用
  也就是-专有方法，可以将 非方法调用语法 映射到方法调用中(class[XXX] -> class.__XXX__())
"""

# def __getitem__(self, key): return self.data[key]

import example5_1_fileinfo
f = example5_1_fileinfo.FileInfo("C:/Users/Public/Music/Sample Music/sleep away.mp3")
print f
print f.__getitem__("name") #>>>1
print f["name"] #>>>2


"""
|>>>1使用专用方法很简单，就像调用普通方法一样，不过一般不这么用 而是像 >>>2 一样去用
-|2这种写法起始相当于Python替我们完成了一个语法转换（f.__getitem__("name")）。
  你不仅可以调用专用方法，而且你可以通过特殊的语法让Python来替你调用

|类似的Python还有个专用方法叫做__setitem__
"""

# def __setitem__(self, key, item): self.data[key] = item

print f.__setitem__("genre",31)
print f
f["22"] = 21
print f

"""
|一切都和__getitem__类似

|这个专用方法在UserDict中定义了，如注释所示

|__setitem__是一个专用方法，因为你可以通过特定的语法来让Python替你调用它
-|不过普遍来说，它依然是一个类方法，所以你可以在子类中重新定义它，对父方法进行覆盖（就如__init__一样）
  如此我们就可以定义属于自己的方法，让它表现出来和真实的字典类似，不过是真实字典所不具备的功能
"""




