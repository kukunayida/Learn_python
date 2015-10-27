# -*- coding: utf-8 -*-

#——————————————————————————————————————————————————
print """
———————————————————————————————————————#4_12_getattr 作为Dispatcher(调度，分发，调度器)(常见使用情况)——————————————————————————————————————————————
"""
"""
有关作为Dispatcher，常规意义和计算机领域
https://en.wikipedia.org/wiki/Dispatcher
https://en.wikipedia.org/wiki/Scheduling_(computing)
https://zh.wikipedia.org/wiki/%E8%B0%83%E5%BA%A6_(%E8%AE%A1%E7%AE%97%E6%9C%BA)

Python single dispatch functions (PEP 443)
http://4byte.cn/question/471262/python-single-dispatch-functions-pep-443.html
"""

import statout #这里只是举个例子
def output(data, format="text"):
    output_function = getattr(statout, "output_%s" % format, statsout.output_text)
    return output_function(data)