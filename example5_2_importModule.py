# -*- coding: utf-8 -*-

"""
python有两种导入模块的方法
1-import module
2-from module import
|-基本用法from UserDict import UserDict

区别：
-|第二种方法，UserDict被直接导入到了局部命名空间去了，所以它可以直接使用，而不需要加上模块的限定
"""

import types
print types.FunctionType

# print FunctionType 会报错

from types import FunctionType
print FunctionType #不会报错

"""
第二种导入方式，使用场景:
-|经常访问模块的属性和方法，不想重复敲入模块的名字
-|只想选择性的导入某些属性和方法，不想要模块中别的


|如果模块中的属性或者方法和别的模块中的相同，则必须使用import module(第一种方法来避免名称冲突)
"""



