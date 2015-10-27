# -*- coding: utf-8 -*-
#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_14_过滤列表 filtering lists——————————————————————————————————————————————
"""
"""
|前的映射列表（map list）功能配合这个过滤列表，可以有选择性的对列表中的元素进行映射
-|大致语法：[mapping−expression for element in source−list if filter−expression]
"""

li = ["a","mpligrim","foo","b","c","b","d","d"]
print [elem for elem in li if len(elem)>1]
print [elem for elem in li if elem != "b"]
print [elem for elem in li if li.count(elem) == 1]

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


#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_15_and 和 or 之 and——————————————————————————————————————————————
"""

print "a" and "b"
print '' and "b"
print "a" and "b" and "c"

"""
|使用and时候，python从左到右演算表达式的值

|0,'',[],(),{},none表示布尔中的假

|如果布尔返回的的值都为真，则and返回最后一个值

|如果布尔有一个值为假，则and返回第一个假值
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_16_and 和 or 之 or——————————————————————————————————————————————
"""

print 'a' or 'b'
print '' or 'b'
print '' or [] or {}
def sidefx():
    print "in sidefx()"
    return 1
print 'a' or sidefx()
# print sidefx() or 'a'

"""
|or，和and一样从左到右演算，如果一个值为真，则立马返回这个值，后边忽略 （and是返回最后一个真值）

|如果有真有假，例如'' or 'b' ，先演算''为假，然后演算'b'为真，则返回真

｜如果所有的值都为假，则返回最后一个假值
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_17_and和or的实际使用场景——————————————————————————————————————————————
"""
a = 'first'
b = 'second'
print 1 and a or b
print 0 and a or b
"""
|从左到右的演算就行了~

|另一中思想，类比bool?a:b的用法~(js或者c中有)
-|bool真则选a，bool假则选b

|这里只是拿这个特例来类比，比如，如果这里a为假，则得到的结果和类比表达式的结果就不同啦
"""
#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_18_and和or的实际使用场景 类比失效的例子——————————————————————————————————————————————
"""

c = ""
d = "second"
print 1 and c or d

"""
|and-or技巧（bool and a or b），类比其它语言的bool?a:b表达式,当a为假的时候，在python中得到的结果和传统其它语言表达式得到的结果会不同

|这个and-or技巧（bool and a or b）主要意义其实在于：保证a的值为真
-|通常的用法是，把a设为[a],b设为[b]，然后使用返回列表的第一个元素值，应该是a或者b中的一个
"""

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_19_安全使用and-or——————————————————————————————————————————————
"""
f = None
g = "second"
print (1 and [f] or [g])[0]
"""
|由于[f]是一个非空列表，所以它绝对不会为假。即使f是0或者""或者其它假值，列表[f]也为真，因为它有一个元素
"""

