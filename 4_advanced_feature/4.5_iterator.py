#/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Ehang Zhang
@file: 4.5_iterator.py
@time: 2018/7/12 22:23
"""

# 迭代器
#
# 可以直接作用于for循环的数据类型有两种：
# 1. 集合数据类型，如list, tuple, set, dict, str等
# 2. generator，包括生成器和带yield的generation function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()来判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))

# 可以被next()函数调用不断返回下一个值的对象成为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Itereator对象：
from collections import Iterator
print(isinstance((x * x for x in range(10))), Iterator)

# generator都是Iterator对象，list、dict、str虽然是Iterable，但却不是Iterator
# 可以使用iter()函数将list、dict、str等Iterable转换成Iterator：
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))


# 小结
"""
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
"""