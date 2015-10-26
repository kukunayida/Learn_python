# -*- coding: utf-8 -*-
li = ['larry','curly']
# print li.pop() 会输出curly
print li.pop
print getattr(li,"pop")
print getattr(li,"append")
print getattr(li,"append")('Moe')
print li
print getattr({}, "clear")
# print getattr((), "pop") 会报错

"""
getattr返回的是方法
"""