# -*- coding: utf-8 -*-
def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.
Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])


if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    print buildConnectionString(myParams)
    print [
        12,
        14,51
    ]#"""在小括号，方括号或者大括号中的表达式可以不用续行符(\)分割成多行，如定义一个(dictionary)"""

"""python不允许引用一个未被赋值的变量"""

#——————————————————————————————————————————————

print """
———————————————————————————————————————#3_19_一次赋多值——————————————————————————————————————————————
"""

(x,y,z) = (1,"d",["ef",12,"ee"]) #
print x
print y
print z

#——————————————————————————————————————————————

print """
———————————————————————————————————————#3_20_range函数——————————————————————————————————————————————
"""

print range(7)
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print MONDAY
print SUNDAY
"""
| range函数返回一个元素为整数的list，如果只填入一个数字作为参数那么就表示从0开始到上限为止（不包含上限）
| 当然也可以增加别的参数，用来表示从非0初始，步长不为1的list，具体可以查看range的doc_string
——| 可以使用一次多赋值的思路创建返回多个值的函数
"""
print range.__doc__